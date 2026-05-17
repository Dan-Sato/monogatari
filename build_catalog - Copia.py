import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CHAPTERS_DIR = ROOT / 'chapters'
ARCOS_FILE = ROOT / 'arcos.json'
CATALOGO_FILE = ROOT / 'catalogo.json'
IGNORED_FILE = ROOT / 'ignored_files.json'

KANJI_DIGITS = {
    '零': 0, '〇': 0,
    '一': 1, '二': 2, '三': 3, '四': 4, '五': 5,
    '六': 6, '七': 7, '八': 8, '九': 9
}
KANJI_UNITS = {'十': 10, '百': 100, '千': 1000}

FILENAME_RE = re.compile(r'^第(?P<number>.+?)章[\u3000 ]+(?P<title>.+)\.html$', re.IGNORECASE)


def normalize_whitespace(text: str) -> str:
    return re.sub(r'\s+', '', text).strip()


def parse_chapter_number(text: str) -> int:
    text = normalize_whitespace(text)
    if not text:
        raise ValueError('Empty chapter number')
    if text.isdigit():
        return int(text)

    total = 0
    current = 0
    for ch in text:
        if ch in KANJI_DIGITS:
            current = KANJI_DIGITS[ch]
        elif ch in KANJI_UNITS:
            unit = KANJI_UNITS[ch]
            if current == 0:
                current = 1
            total += current * unit
            current = 0
        else:
            raise ValueError(f'Unsupported numeral: {text}')
    return total + current


def chapter_to_kanji(n: int) -> str:
    digits = ['', '一', '二', '三', '四', '五', '六', '七', '八', '九']
    if n == 0:
        return '零'
    parts = []
    thousands = n // 1000
    hundreds = (n % 1000) // 100
    tens = (n % 100) // 10
    ones = n % 10
    if thousands:
        parts.append(('' if thousands == 1 else digits[thousands]) + '千')
    if hundreds:
        parts.append(('' if hundreds == 1 else digits[hundreds]) + '百')
    if tens:
        parts.append(('' if tens == 1 else digits[tens]) + '十')
    if ones:
        parts.append(digits[ones])
    return ''.join(parts)


def load_arcs():
    with ARCOS_FILE.open('r', encoding='utf-8') as f:
        return json.load(f)


def parse_existing_files():
    existing = {}
    ignored = []

    for path in sorted(CHAPTERS_DIR.glob('*.html')):
        match = FILENAME_RE.match(path.name)
        if not match:
            ignored.append({
                'file': str(path.relative_to(ROOT)).replace('\\', '/'),
                'reason': 'filename_does_not_match_expected_pattern'
            })
            continue

        number_raw = match.group('number')
        title = match.group('title').strip()

        try:
            chapter_num = parse_chapter_number(number_raw)
        except ValueError as e:
            ignored.append({
                'file': str(path.relative_to(ROOT)).replace('\\', '/'),
                'reason': f'invalid_chapter_number: {str(e)}'
            })
            continue

        existing[chapter_num] = {
            'chapter': chapter_num,
            'chapter_kanji': f'第{chapter_to_kanji(chapter_num)}章',
            'title': title,
            'file': str(path.relative_to(ROOT)).replace('\\', '/'),
            'status': 'existing'
        }

    return existing, ignored


def build_catalog():
    arcs = load_arcs()
    existing, ignored = parse_existing_files()
    chapters = []

    for arc in arcs:
        planned = arc.get('status') == 'planned'
        for chapter_num in range(arc['start'], arc['end'] + 1):
            base = {
                'chapter': chapter_num,
                'chapter_kanji': f'第{chapter_to_kanji(chapter_num)}章',
                'arc': arc['arc']
            }
            if chapter_num in existing:
                row = {**base, **existing[chapter_num], 'arc': arc['arc']}
            else:
                row = {
                    **base,
                    'title': None,
                    'file': None,
                    'status': 'planned' if planned else 'missing_or_skipped'
                }
            chapters.append(row)

    catalog = {
        'chapters_source': 'chapters/*.html',
        'css_path': 'chapters/style.css',
        'guide_path': 'guia-continuidade.html',
        'generated_by': 'build_catalog.py',
        'chapters': chapters
    }

    with CATALOGO_FILE.open('w', encoding='utf-8') as f:
        json.dump(catalog, f, ensure_ascii=False, indent=2)

    with IGNORED_FILE.open('w', encoding='utf-8') as f:
        json.dump(ignored, f, ensure_ascii=False, indent=2)

    existing_count = sum(1 for c in chapters if c['status'] == 'existing')
    missing_count = sum(1 for c in chapters if c['status'] == 'missing_or_skipped')
    planned_count = sum(1 for c in chapters if c['status'] == 'planned')
    print(f'catalogo.json atualizado: {existing_count} existing, {missing_count} missing_or_skipped, {planned_count} planned, {len(ignored)} ignored')


if __name__ == '__main__':
    build_catalog()
