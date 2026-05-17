# Monogatari Archive

Arquivo privado para organizar capítulos em HTML, manter histórico de continuidade e reduzir repetição ao usar IA como apoio de geração. Os capítulos ficam em `chapters/`, os arcos são definidos em `arcos.json` e o catálogo navegável é gerado por `build_catalog.py`. [cite:20]

## Estrutura

- `chapters/` — capítulos em HTML e `style.css`. [cite:20]
- `guia-continuidade.html` — guia de referência da continuidade. [cite:20]
- `arcos.json` — lista oficial dos arcos a partir do capítulo 236. [cite:20]
- `catalogo.json` — catálogo gerado automaticamente. [cite:20]
- `index.html` — página de navegação local do arquivo. [cite:20]
- `build_catalog.py` — script que reconstrói o catálogo. [cite:20]
- `ignored_files.json` — arquivos HTML ignorados por não seguirem o padrão esperado. [cite:20]

## Padrão dos arquivos

Os capítulos seguem preferencialmente o formato `第(número)章　(título).html`, com número em kanji ou arábico. O script já tolera espaços Unicode e também ignora HTMLs fora do padrão em vez de quebrar a execução. [cite:20]

## Como atualizar o catálogo

1. Adicione capítulos novos em `chapters/`. [cite:20]
2. Se houver um novo arco, atualize `arcos.json` antes ou junto dos novos capítulos. [cite:20]
3. Rode `python build_catalog.py`. [cite:20]
4. Abra `index.html` no navegador para conferir a organização. [cite:20]
5. Faça commit e push no repositório. [cite:20]

## Como adicionar um novo arco

Adicione um novo objeto ao final de `arcos.json` neste formato:

```json
{
  "arc": "新しい編",
  "start": 357,
  "end": 364,
  "status": "planned"
}
```

Depois que os capítulos começarem a existir, rode o script novamente para atualizar `catalogo.json`. Capítulos faltantes dentro do intervalo aparecem como `missing_or_skipped`, e capítulos de arcos futuros podem aparecer como `planned`. [cite:20]

## Organização do índice

- Capítulos 1–235 aparecem sem divisão por arco. [cite:20]
- Capítulos 236 em diante aparecem agrupados por arco conforme `arcos.json`. [cite:20]
- Capítulos pulados ou inexistentes não quebram o sistema; eles ficam registrados no catálogo. [cite:20]

## Futuro

Mais adiante, os capítulos anteriores ao 236 podem ser analisados por tema para sugerir arcos retroativos. O caminho mais seguro é extrair o texto dos HTMLs, gerar resumos ou palavras-chave e usar agrupamento temático como sugestão, com revisão manual antes de oficializar novos arcos. [cite:20]
