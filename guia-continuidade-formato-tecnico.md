# GUIA DE CONTINUIDADE — Light Novel HTML

_Projeto de leitura em japonês._

## ⚠️ FORMATO TÉCNICO OBRIGATÓRIO

> Narrativa Light Novel
>
> HTML puro — SEM `<style>` blocks ou inline styles
>
> Apenas: `<link rel="stylesheet" href="style.css">`
>
> Ruby: `<ruby>漢字<rt>ふりがな</rt><span class="mean">tradução</span></ruby>`
>
> **FURIGANA SEMPRE EM HIRAGANA/KATAKANA — NUNCA ROMAJI**
>
> Dupla verificação de todas as tags
>
> Em torno de 25k a 30k caracteres no HTML
>
> Nome dos arquivos: 第000章　タイトル.html
>
> Nível em torno de N4, com conversas geralmente na forma casual
>
> Vocabulários e kanji usados devem ser os comuns em mídias
>
> Não deve ser utilizado grafias raramente usadas (ateji), como 有難う, 素敵, por exemplo
>
> 3 notas de rodapé por capítulo
>
> Narrativa: 3ª pessoa, parágrafos contínuos, diálogo em 「」
>
> Os capítulos seguem o roteiro planejado, sem antecipar elementos dos capítulos seguintes
>
> Tom sugestivo/sensual/explícito permitido

## CAPÍTULO EXEMPLO

<!doctype html>
<html lang="ja">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>第五百七十六章 目覚めの朝、そして誕生日</title>
    <link rel="stylesheet" href="style.css" />
  </head>
  <body>
    <div class="page">
      <h1>
        第五百七十六章
        <ruby>目覚<rt>めざ</rt><span class="mean">despertar</span></ruby
        >めの<ruby>朝<rt>あさ</rt><span class="mean">manha</span></ruby
        >、そして<ruby>誕生日<rt>たんじょうび</rt><span class="mean">aniversario</span></ruby>
      </h1>

      <p>
        <ruby>朝<rt>あさ</rt><span class="mean">manha</span></ruby
        >の<ruby>光<rt>ひかり</rt><span class="mean">luz</span></ruby
        >が<ruby>カーテン<rt>カーテン</rt><span class="mean">cortina</span></ruby
        >の<ruby>隙間<rt>すきま</rt><span class="mean">fresta</span></ruby
        >から<ruby>柔<rt>やわ</rt><span class="mean">suave</span></ruby
        >らかく<ruby>差<rt>さ</rt><span class="mean">entrar</span></ruby
        >し<ruby>込<rt>こ</rt><span class="mean">entrar</span></ruby
        >んでいた。<ruby>ダン<rt>ダン</rt><span class="mean">Dan</span></ruby
        >は<ruby>先<rt>さき</rt><span class="mean">primeiro</span></ruby
        >に<ruby>目<rt>め</rt><span class="mean">olhos</span></ruby
        >を<ruby>覚<rt>さ</rt><span class="mean">despertar</span></ruby
        >まし、<ruby>隣<rt>となり</rt><span class="mean">ao lado</span></ruby
        >で<ruby>眠<rt>ねむ</rt><span class="mean">dormir</span></ruby
        >っている<ruby>舞<rt>まい</rt><span class="mean">Mai</span></ruby
        >の<ruby>顔<rt>かお</rt><span class="mean">rosto</span></ruby
        >をぼんやりと<ruby>見<rt>み</rt><span class="mean">olhar</span></ruby
        >つめた。<ruby>何<rt>なに</rt><span class="mean">nada</span></ruby
        >も<ruby>纏<rt>まと</rt><span class="mean">vestir</span></ruby
        >わない<ruby>二人<rt>ふたり</rt><span class="mean">os dois</span></ruby
        >の<ruby>体<rt>からだ</rt><span class="mean">corpo</span></ruby
        >が、<ruby>薄<rt>うす</rt><span class="mean">fino</span></ruby
        >い<ruby>布団<rt>ふとん</rt><span class="mean">futon</span></ruby
        >の<ruby>下<rt>した</rt><span class="mean">embaixo</span></ruby
        >で<ruby>寄<rt>よ</rt><span class="mean">encostar-se</span></ruby
        >り<ruby>添<rt>そ</rt><span class="mean">encostar-se</span></ruby
        >っていた。
      </p>

      <p>
        <ruby>舞<rt>まい</rt><span class="mean">Mai</span></ruby
        >の<ruby>睫毛<rt>まつげ</rt><span class="mean">cilios</span></ruby
        >が<ruby>微<rt>かす</rt><span class="mean">levemente</span></ruby
        >かに<ruby>震<rt>ふる</rt><span class="mean">tremer</span></ruby
        >え、それから<ruby>ゆっくり<rt>ゆっくり</rt><span class="mean">lentamente</span></ruby
        >と<ruby>目<rt>め</rt><span class="mean">olhos</span></ruby
        >が<ruby>開<rt>ひら</rt><span class="mean">abrir</span></ruby
        >いた。<ruby>視線<rt>しせん</rt><span class="mean">olhar</span></ruby
        >の<ruby>先<rt>さき</rt><span class="mean">adiante</span></ruby
        >に、<ruby>じっと<rt>じっと</rt><span class="mean">fixamente</span></ruby
        >こちらを<ruby>見<rt>み</rt><span class="mean">olhar</span></ruby
        >つめる<ruby>ダン<rt>ダン</rt><span class="mean">Dan</span></ruby
        >の<ruby>顔<rt>かお</rt><span class="mean">rosto</span></ruby
        >があった。「……おはよう」<ruby>舞<rt>まい</rt><span class="mean">Mai</span></ruby
        >が<ruby>眠<rt>ねむ</rt><span class="mean">sonolento</span></ruby
        >そうな<ruby>声<rt>こえ</rt><span class="mean">voz</span></ruby
        >で<ruby>言<rt>い</rt><span class="mean">dizer</span></ruby
        >った。「<ruby>何<rt>なに</rt><span class="mean">o que</span></ruby
        >？<ruby>何<rt>なに</rt><span class="mean">algo</span></ruby
        >かあった？」
      </p>

      <p>
        <ruby>ダン<rt>ダン</rt><span class="mean">Dan</span></ruby
        >が<ruby>小<rt>ちい</rt><span class="mean">pequeno</span></ruby
        >さく<ruby>笑<rt>わら</rt><span class="mean">sorrir</span></ruby
        >った。「<ruby>何<rt>なに</rt><span class="mean">nada</span></ruby
        >もない。ただ<ruby>お前<rt>おまえ</rt><span class="mean">voce</span></ruby
        >を<ruby>見<rt>み</rt><span class="mean">olhar</span></ruby
        >てただけだ」<ruby>そう<rt>そう</rt><span class="mean">assim</span></ruby
        >言<ruby>い<rt>い</rt><span class="mean">dizer</span></ruby
        >ながら、<ruby>ダン<rt>ダン</rt><span class="mean">Dan</span></ruby
        >は<ruby>手<rt>て</rt><span class="mean">mao</span></ruby
        >を<ruby>伸<rt>の</rt><span class="mean">estender</span></ruby
        >ばして<ruby>舞<rt>まい</rt><span class="mean">Mai</span></ruby
        >の<ruby>頬<rt>ほお</rt><span class="mean">bochecha</span></ruby
        >に<ruby>触<rt>ふ</rt><span class="mean">tocar</span></ruby
        >れ、それから<ruby>乱<rt>みだ</rt><span class="mean">desarrumado</span></ruby
        >れた<ruby>髪<rt>かみ</rt><span class="mean">cabelo</span></ruby
        >を<ruby>そっと<rt>そっと</rt><span class="mean">suavemente</span></ruby
        >撫でた。「<ruby>綺麗<rt>きれい</rt><span class="mean">bonito</span></ruby
        >だな、お<ruby>前<rt>まえ</rt><span class="mean">voce</span></ruby
        >」
      </p>

      <p>
        <ruby>舞<rt>まい</rt><span class="mean">Mai</span></ruby
        >が<ruby>目<rt>め</rt><span class="mean">olhos</span></ruby
        >を<ruby>丸<rt>まる</rt><span class="mean">arregalar</span></ruby
        >くしてから、<ruby>慌<rt>あわ</rt><span class="mean">apressado</span></ruby
        >てて<ruby>顔<rt>かお</rt><span class="mean">rosto</span></ruby
        >の<ruby>前<rt>まえ</rt><span class="mean">frente</span></ruby
        >で<ruby>手<rt>て</rt><span class="mean">mao</span></ruby
        >を<ruby>振<rt>ふ</rt><span class="mean">balancar</span></ruby
        >った。「そんなわけないでしょ。<ruby>絶対<rt>ぜったい</rt><span class="mean">absolutamente</span></ruby
        >、<ruby>髪<rt>かみ</rt><span class="mean">cabelo</span></ruby
        >も<ruby>ぼさぼさ<rt>ぼさぼさ</rt><span class="mean">desarrumado</span></ruby
        >で、<ruby>変<rt>へん</rt><span class="mean">estranho</span></ruby
        >な<ruby>顔<rt>かお</rt><span class="mean">rosto</span></ruby
        >してるはずだよ」<ruby>ダン<rt>ダン</rt><span class="mean">Dan</span></ruby
        >が<ruby>首<rt>くび</rt><span class="mean">pescoco</span></ruby
        >を<ruby>横<rt>よこ</rt><span class="mean">de lado</span></ruby
        >に<ruby>振<rt>ふ</rt><span class="mean">balancar</span></ruby
        >った。「<ruby>寧<rt>むし</rt><span class="mean">pelo contrario</span></ruby
        >ろ、そういう<ruby>崩<rt>くず</rt><span class="mean">descontraido</span></ruby
        >れた<ruby>感<rt>かん</rt><span class="mean">sensacao</span></ruby
        >じ、すごく<ruby>色<rt>いろ</rt><span class="mean">sensual</span></ruby
        >っぽいと<ruby>思<rt>おも</rt><span class="mean">achar</span></ruby
        >うぞ」
      </p>

      <p>
        <ruby>舞<rt>まい</rt><span class="mean">Mai</span></ruby
        >の<ruby>頬<rt>ほお</rt><span class="mean">bochecha</span></ruby
        >が<ruby>赤<rt>あか</rt><span class="mean">vermelho</span></ruby
        >らんだ。「もう……そういうこと、<ruby>朝<rt>あさ</rt><span class="mean">manha</span></ruby
        >から<ruby>言<rt>い</rt><span class="mean">dizer</span></ruby
        >わないでよ」<ruby>ダン<rt>ダン</rt><span class="mean">Dan</span></ruby
        >が<ruby>笑<rt>わら</rt><span class="mean">rir</span></ruby
        >いながら<ruby>彼女<rt>かのじょ</rt><span class="mean">ela</span></ruby
        >を<ruby>もう<rt>もう</rt><span class="mean">mais</span></ruby
        ><ruby>少<rt>すこ</rt><span class="mean">um pouco</span></ruby
        >し<ruby>近<rt>ちか</rt><span class="mean">aproximar</span></ruby
        >づけた。「なあ、<ruby>知<rt>し</rt><span class="mean">saber</span></ruby
        >ってるか。お<ruby>前<rt>まえ</rt><span class="mean">voce</span></ruby
        >、<ruby>寝<rt>ね</rt><span class="mean">dormir</span></ruby
        >てる<ruby>時<rt>とき</rt><span class="mean">momento</span></ruby
        >、たまに<ruby>変<rt>へん</rt><span class="mean">estranho</span></ruby
        >な<ruby>寝言<rt>ねごと</rt><span class="mean">fala durante o sono</span></ruby
        >を<ruby>言<rt>い</rt><span class="mean">dizer</span></ruby
        >うんだぞ」<ruby>舞<rt>まい</rt><span class="mean">Mai</span></ruby
        >が<ruby>驚<rt>おどろ</rt><span class="mean">surpreender</span></ruby
        >いた<ruby>顔<rt>かお</rt><span class="mean">rosto</span></ruby
        >をした。「え、<ruby>本当<rt>ほんとう</rt><span class="mean">realmente</span></ruby
        >？<ruby>何<rt>なに</rt><span class="mean">o que</span></ruby
        >て<ruby>言<rt>い</rt><span class="mean">dizer</span></ruby
        >ってた？」
      </p>

      <p>
        <ruby>ダン<rt>ダン</rt><span class="mean">Dan</span></ruby
        >が<ruby>悪戯<rt>いたずら</rt><span class="mean">travesso</span></ruby
        >っぽく<ruby>笑<rt>わら</rt><span class="mean">sorrir</span></ruby
        >った。「<ruby>秘密<rt>ひみつ</rt><span class="mean">segredo</span></ruby
        >」<ruby>舞<rt>まい</rt><span class="mean">Mai</span></ruby
        >が<ruby>拳<rt>こぶし</rt><span class="mean">punho</span></ruby
        >で<ruby>軽<rt>かる</rt><span class="mean">leve</span></ruby
        >く<ruby>ダン<rt>ダン</rt><span class="mean">Dan</span></ruby
        >の<ruby>胸<rt>むね</rt><span class="mean">peito</span></ruby
        >を<ruby>叩<rt>たた</rt><span class="mean">bater</span></ruby
        >いた。「ずるい！<ruby>教<rt>おし</rt><span class="mean">ensinar</span></ruby
        >えなさいよ」それでもその<ruby>声<rt>こえ</rt><span class="mean">voz</span></ruby
        >には<ruby>笑<rt>わら</rt><span class="mean">rir</span></ruby
        >いが<ruby>混<rt>ま</rt><span class="mean">misturar</span></ruby
        >じっていた。
      </p>

      <p>
        <ruby>ダン<rt>ダン</rt><span class="mean">Dan</span></ruby
        >が<ruby>不意<rt>ふい</rt><span class="mean">de repente</span></ruby
        >に<ruby>真剣<rt>しんけん</rt><span class="mean">serio</span></ruby
        >な<ruby>顔<rt>かお</rt><span class="mean">rosto</span></ruby
        >になった。「<ruby>舞<rt>まい</rt><span class="mean">Mai</span></ruby
        >、<ruby>愛<rt>あい</rt><span class="mean">amor</span></ruby
        >してる」<ruby>舞<rt>まい</rt><span class="mean">Mai</span></ruby
        >が<ruby>一瞬<rt>いっしゅん</rt><span class="mean">por um instante</span></ruby
        >、<ruby>目<rt>め</rt><span class="mean">olhos</span></ruby
        >を<ruby>見開<rt>みひら</rt><span class="mean">arregalar</span></ruby
        >いてから、<ruby>柔<rt>やわ</rt><span class="mean">suave</span></ruby
        >らかく<ruby>微笑<rt>ほほえ</rt><span class="mean">sorrir</span></ruby
        >んだ。<ruby>両手<rt>りょうて</rt><span class="mean">ambas as maos</span></ruby
        >を<ruby>伸<rt>の</rt><span class="mean">estender</span></ruby
        >ばし、<ruby>ダン<rt>ダン</rt><span class="mean">Dan</span></ruby
        >を<ruby>ぎゅっと<rt>ぎゅっと</rt><span class="mean">bem apertado</span></ruby
        ><ruby>抱<rt>だ</rt><span class="mean">abracar</span></ruby
        >き<ruby>寄<rt>よ</rt><span class="mean">puxar</span></ruby
        >せた。「<ruby>私<rt>わたし</rt><span class="mean">eu</span></ruby
        >も<ruby>愛<rt>あい</rt><span class="mean">amor</span></ruby
        >してる。<ruby>誰<rt>だれ</rt><span class="mean">ninguem</span></ruby
        >よりも」
      </p>

      <p>
        <ruby>ダン<rt>ダン</rt><span class="mean">Dan</span></ruby
        >の<ruby>頭<rt>あたま</rt><span class="mean">cabeca</span></ruby
        >が<ruby>舞<rt>まい</rt><span class="mean">Mai</span></ruby
        >の<ruby>胸<rt>むね</rt><span class="mean">peito</span></ruby
        >に<ruby>埋<rt>うず</rt><span class="mean">enterrar</span></ruby
        >もれ、<ruby>二人<rt>ふたり</rt><span class="mean">os dois</span></ruby
        >の<ruby>脚<rt>あし</rt><span class="mean">pernas</span></ruby
        >が<ruby>自然<rt>しぜん</rt><span class="mean">naturalmente</span></ruby
        >と<ruby>絡<rt>から</rt><span class="mean">entrelacar</span></ruby
        >み<ruby>合<rt>あ</rt><span class="mean">entrelacar-se</span></ruby
        >った。<ruby>舞<rt>まい</rt><span class="mean">Mai</span></ruby
        >が<ruby>ダン<rt>ダン</rt><span class="mean">Dan</span></ruby
        >の<ruby>髪<rt>かみ</rt><span class="mean">cabelo</span></ruby
        >を<ruby>優<rt>やさ</rt><span class="mean">gentilmente</span></ruby
        >しく<ruby>撫<rt>な</rt><span class="mean">acariciar</span></ruby
        >でながら、<ruby>静<rt>しず</rt><span class="mean">silencioso</span></ruby
        >かに<ruby>時間<rt>じかん</rt><span class="mean">tempo</span></ruby
        >が<ruby>流<rt>なが</rt><span class="mean">fluir</span></ruby
        >れていくのを<ruby>感<rt>かん</rt><span class="mean">sentir</span></ruby
        >じていた。
      </p>

      <p>
        <ruby>少<rt>すこ</rt><span class="mean">um pouco</span></ruby
        >し<ruby>経<rt>た</rt><span class="mean">passar</span></ruby
        >って、<ruby>ダン<rt>ダン</rt><span class="mean">Dan</span></ruby
        >がぼそりと<ruby>呟<rt>つぶや</rt><span class="mean">murmurar</span></ruby
        >いた。「……<ruby>天国<rt>てんごく</rt><span class="mean">ceu</span></ruby
        >にいる<ruby>気分<rt>きぶん</rt><span class="mean">sensacao</span></ruby
        >だ」<ruby>舞<rt>まい</rt><span class="mean">Mai</span></ruby
        >が<ruby>小<rt>ちい</rt><span class="mean">pequeno</span></ruby
        >さく<ruby>笑<rt>わら</rt><span class="mean">rir</span></ruby
        >い<ruby>声<rt>ごえ</rt><span class="mean">voz</span></ruby
        >を<ruby>漏<rt>も</rt><span class="mean">deixar escapar</span></ruby
        >らした。「<ruby>大袈裟<rt>おおげさ</rt><span class="mean">exagerado</span></ruby
        >だなあ」でも、その<ruby>声<rt>こえ</rt><span class="mean">voz</span></ruby
        >には<ruby>嬉<rt>うれ</rt><span class="mean">feliz</span></ruby
        >しさが<ruby>隠<rt>かく</rt><span class="mean">esconder</span></ruby
        >せていなかった。
      </p>

      <p>
        <ruby>やがて<rt>やがて</rt><span class="mean">eventualmente</span></ruby
        >、<ruby>二人<rt>ふたり</rt><span class="mean">os dois</span></ruby
        >は<ruby>身<rt>み</rt><span class="mean">corpo</span></ruby
        >を<ruby>起<rt>お</rt><span class="mean">levantar</span></ruby
        >こし、<ruby>身支度<rt>みじたく</rt><span class="mean">preparativos</span></ruby
        >を<ruby>整<rt>ととの</rt><span class="mean">arrumar</span></ruby
        >えて<ruby>部屋<rt>へや</rt><span class="mean">quarto</span></ruby
        >を<ruby>出<rt>で</rt><span class="mean">sair</span></ruby
        >た。<ruby>ホテル<rt>ホテル</rt><span class="mean">hotel</span></ruby
        >の<ruby>玄関<rt>げんかん</rt><span class="mean">entrada</span></ruby
        >を<ruby>出<rt>で</rt><span class="mean">sair</span></ruby
        >ると、<ruby>朝<rt>あさ</rt><span class="mean">manha</span></ruby
        >の<ruby>光<rt>ひかり</rt><span class="mean">luz</span></ruby
        >が<ruby>眩<rt>まぶ</rt><span class="mean">deslumbrante</span></ruby
        >しかった。<ruby>舞<rt>まい</rt><span class="mean">Mai</span></ruby
        >が<ruby>昨夜<rt>ゆうべ</rt><span class="mean">ontem a noite</span></ruby
        >の<ruby>ワンピース<rt>ワンピース</rt><span class="mean">vestido</span></ruby
        >のまま、<ruby>気<rt>き</rt><span class="mean">preocupacao</span></ruby
        >まずそうに<ruby>周囲<rt>しゅうい</rt><span class="mean">arredores</span></ruby
        >を<ruby>見<rt>み</rt><span class="mean">olhar</span></ruby
        >回した。「なんか、こういう<ruby>格好<rt>かっこう</rt><span class="mean">roupa</span></ruby
        >で<ruby>朝<rt>あさ</rt><span class="mean">manha</span></ruby
        >からラブホから<ruby>出<rt>で</rt><span class="mean">sair</span></ruby
        >てくるの、<ruby>すごく<rt>すごく</rt><span class="mean">muito</span></ruby
        ><ruby>恥<rt>は</rt><span class="mean">vergonha</span></ruby
        >ずかしいんだけど」
      </p>

      <p>
        <ruby>ダン<rt>ダン</rt><span class="mean">Dan</span></ruby
        >が<ruby>肩<rt>かた</rt><span class="mean">ombro</span></ruby
        >をすくめた。「<ruby>誰<rt>だれ</rt><span class="mean">ninguem</span></ruby
        >も<ruby>気<rt>き</rt><span class="mean">notar</span></ruby
        >にしてないよ」<ruby>舞<rt>まい</rt><span class="mean">Mai</span></ruby
        >が<ruby>頬<rt>ほお</rt><span class="mean">bochecha</span></ruby
        >を<ruby>膨<rt>ふく</rt><span class="mean">inflar</span></ruby
        >らませた。「<ruby>私<rt>わたし</rt><span class="mean">eu</span></ruby
        >が<ruby>気<rt>き</rt><span class="mean">preocupacao</span></ruby
        >にしてるの！」<ruby>二人<rt>ふたり</rt><span class="mean">os dois</span></ruby
        >は<ruby>笑<rt>わら</rt><span class="mean">rir</span></ruby
        >い<ruby>合<rt>あ</rt><span class="mean">reciprocamente</span></ruby
        >いながら、<ruby>手<rt>て</rt><span class="mean">mao</span></ruby
        >を<ruby>繋<rt>つな</rt><span class="mean">segurar</span></ruby
        >いで<ruby>家<rt>いえ</rt><span class="mean">casa</span></ruby
        >へと<ruby>向<rt>む</rt><span class="mean">direcionar-se</span></ruby
        >かった。
      </p>

      <p>
        <ruby>扉<rt>とびら</rt><span class="mean">porta</span></ruby
        >を<ruby>開<rt>あ</rt><span class="mean">abrir</span></ruby
        >けると、<ruby>ティファ<rt>ティファ</rt><span class="mean">Tifa</span></ruby
        >が<ruby>腕<rt>うで</rt><span class="mean">braco</span></ruby
        >を<ruby>組<rt>く</rt><span class="mean">cruzar</span></ruby
        >んで<ruby>待<rt>ま</rt><span class="mean">esperar</span></ruby
        >っていた。「もう、<ruby>二人<rt>ふたり</rt><span class="mean">os dois</span></ruby
        >とも、こんな<ruby>時間<rt>じかん</rt><span class="mean">horario</span></ruby
        >まで<ruby>帰<rt>かえ</rt><span class="mean">voltar</span></ruby
        >ってこないんだから。<ruby>心配<rt>しんぱい</rt><span class="mean">preocupacao</span></ruby
        >したんだよ」<ruby>キャミィ<rt>キャミィ</rt><span class="mean">Cammy</span></ruby
        >が<ruby>台所<rt>だいどころ</rt><span class="mean">cozinha</span></ruby
        >から<ruby>顔<rt>かお</rt><span class="mean">rosto</span></ruby
        >を<ruby>出<rt>だ</rt><span class="mean">aparecer</span></ruby
        >した。「まあ、<ruby>戻<rt>もど</rt><span class="mean">voltar</span></ruby
        >ってきたなら<ruby>良<rt>よ</rt><span class="mean">bom</span></ruby
        >い」
      </p>

      <p>
        <ruby>舞<rt>まい</rt><span class="mean">Mai</span></ruby
        >が<ruby>両手<rt>りょうて</rt><span class="mean">ambas as maos</span></ruby
        >を<ruby>合<rt>あ</rt><span class="mean">juntar</span></ruby
        >わせて<ruby>謝<rt>あやま</rt><span class="mean">desculpar-se</span></ruby
        >った。「ごめん、<ruby>ごめん<rt>ごめん</rt><span class="mean">desculpe</span></ruby
        >！ちょっと<ruby>朝<rt>あさ</rt><span class="mean">manha</span></ruby
        >まで<ruby>ゆっくり<rt>ゆっくり</rt><span class="mean">lentamente</span></ruby
        >しちゃって」<ruby>ティファ<rt>ティファ</rt><span class="mean">Tifa</span></ruby
        >が<ruby>溜息<rt>ためいき</rt><span class="mean">suspiro</span></ruby
        >をついた。「そのせいで、<ruby>ケーキ<rt>ケーキ</rt><span class="mean">bolo</span></ruby
        >を<ruby>切<rt>き</rt><span class="mean">cortar</span></ruby
        >るのが<ruby>誕生日<rt>たんじょうび</rt><span class="mean">aniversario</span></ruby
        >の<ruby>翌日<rt>よくじつ</rt><span class="mean">dia seguinte</span></ruby
        >になっちゃったよ」
      </p>

      <p>
        <ruby>舞<rt>まい</rt><span class="mean">Mai</span></ruby
        >の<ruby>頬<rt>ほお</rt><span class="mean">bochecha</span></ruby
        >が<ruby>真<rt>ま</rt><span class="mean">totalmente</span></ruby
        >っ<ruby>赤<rt>あか</rt><span class="mean">vermelho</span></ruby
        >になった。「そ、それは……あれだから……ラブホに<ruby>朝<rt>あさ</rt><span class="mean">manha</span></ruby
        >まで<ruby>いた<rt>いた</rt><span class="mean">ficar</span></ruby
        >から……」<ruby>言葉<rt>ことば</rt><span class="mean">palavras</span></ruby
        >を<ruby>濁<rt>にご</rt><span class="mean">deixar vago</span></ruby
        >らせながら<ruby>視線<rt>しせん</rt><span class="mean">olhar</span></ruby
        >を<ruby>逸<rt>そ</rt><span class="mean">desviar</span></ruby
        >らした。<ruby>キャミィ<rt>キャミィ</rt><span class="mean">Cammy</span></ruby
        >が<ruby>淡々<rt>たんたん</rt><span class="mean">calmamente</span></ruby
        >と<ruby>言<rt>い</rt><span class="mean">dizer</span></ruby
        >った。「<ruby>説明<rt>せつめい</rt><span class="mean">explicacao</span></ruby
        >は<ruby>不要<rt>ふよう</rt><span class="mean">desnecessario</span></ruby
        >だ。<ruby>大体<rt>だいたい</rt><span class="mean">mais ou menos</span></ruby
        >の<ruby>想像<rt>そうぞう</rt><span class="mean">imaginacao</span></ruby
        >はつく」
      </p>

      <p>
        <ruby>四人<rt>よにん</rt><span class="mean">os quatro</span></ruby
        >は<ruby>顔<rt>かお</rt><span class="mean">rosto</span></ruby
        >を見<ruby>合<rt>あ</rt><span class="mean">entreolhar</span></ruby
        >わせて<ruby>笑<rt>わら</rt><span class="mean">rir</span></ruby
        >い<ruby>始<rt>はじ</rt><span class="mean">comecar</span></ruby
        >めた。<ruby>ティファ<rt>ティファ</rt><span class="mean">Tifa</span></ruby
        >が<ruby>台所<rt>だいどころ</rt><span class="mean">cozinha</span></ruby
        >から<ruby>箱<rt>はこ</rt><span class="mean">caixa</span></ruby
        >を<ruby>取<rt>と</rt><span class="mean">pegar</span></ruby
        >り<ruby>出<rt>だ</rt><span class="mean">tirar</span></ruby
        >した。「よし、<ruby>遅<rt>おく</rt><span class="mean">atrasado</span></ruby
        >れちゃったけど、ケーキの<ruby>時間<rt>じかん</rt><span class="mean">hora</span></ruby
        >にしよう」<ruby>箱<rt>はこ</rt><span class="mean">caixa</span></ruby
        >の<ruby>中<rt>なか</rt><span class="mean">dentro</span></ruby
        >には、<ruby>三人<rt>さんにん</rt><span class="mean">as tres</span></ruby
        >で<ruby>協力<rt>きょうりょく</rt><span class="mean">cooperar</span></ruby
        >して<ruby>作<rt>つく</rt><span class="mean">fazer</span></ruby
        >った、<ruby>生<rt>なま</rt><span class="mean">fresco</span></ruby
        >クリームと<ruby>果物<rt>くだもの</rt><span class="mean">fruta</span></ruby
        >たっぷりのケーキが<ruby>入<rt>はい</rt><span class="mean">estar dentro</span></ruby
        >っていた。
      </p>

      <p>
        <ruby>蝋燭<rt>ろうそく</rt><span class="mean">vela</span></ruby
        >に<ruby>火<rt>ひ</rt><span class="mean">fogo</span></ruby
        >が<ruby>灯<rt>とも</rt><span class="mean">acender</span></ruby
        >され、<ruby>四人<rt>よにん</rt><span class="mean">os quatro</span></ruby
        >が<ruby>声<rt>こえ</rt><span class="mean">voz</span></ruby
        >を<ruby>揃<rt>そろ</rt><span class="mean">juntos</span></ruby
        >えて<ruby>誕生日<rt>たんじょうび</rt><span class="mean">aniversario</span></ruby
        >の<ruby>歌<rt>うた</rt><span class="mean">musica</span></ruby
        >を<ruby>歌<rt>うた</rt><span class="mean">cantar</span></ruby
        >った。<ruby>ダン<rt>ダン</rt><span class="mean">Dan</span></ruby
        >が<ruby>照<rt>て</rt><span class="mean">envergonhar-se</span></ruby
        >れくさそうに<ruby>笑<rt>わら</rt><span class="mean">sorrir</span></ruby
        >いながら<ruby>蝋燭<rt>ろうそく</rt><span class="mean">vela</span></ruby
        >を<ruby>吹<rt>ふ</rt><span class="mean">soprar</span></ruby
        >き<ruby>消<rt>け</rt><span class="mean">apagar</span></ruby
        >した。<ruby>皆<rt>みんな</rt><span class="mean">todos</span></ruby
        >が<ruby>拍手<rt>はくしゅ</rt><span class="mean">aplauso</span></ruby
        >をし、<ruby>ケーキ<rt>ケーキ</rt><span class="mean">bolo</span></ruby
        >を<ruby>切<rt>き</rt><span class="mean">cortar</span></ruby
        >り<ruby>分<rt>わ</rt><span class="mean">dividir</span></ruby
        >けて<ruby>食<rt>た</rt><span class="mean">comer</span></ruby
        >べ<ruby>始<rt>はじ</rt><span class="mean">comecar</span></ruby
        >めた。
      </p>

      <p>
        <ruby>ソファ<rt>ソファ</rt><span class="mean">sofa</span></ruby
        >に<ruby>座<rt>すわ</rt><span class="mean">sentar</span></ruby
        >り、ケーキを<ruby>頬張<rt>ほおば</rt><span class="mean">comer com a boca cheia</span></ruby
        >りながら、<ruby>ティファ<rt>ティファ</rt><span class="mean">Tifa</span></ruby
        >が<ruby>興味深<rt>きょうみぶか</rt><span class="mean">com interesse</span></ruby
        >そうに<ruby>聞<rt>き</rt><span class="mean">perguntar</span></ruby
        >いた。「それで、<ruby>結局<rt>けっきょく</rt><span class="mean">no final</span></ruby
        >、<ruby>昨日<rt>きのう</rt><span class="mean">ontem</span></ruby
        ><ruby>一日<rt>いちにち</rt><span class="mean">um dia</span></ruby
        >、どんな<ruby>感<rt>かん</rt><span class="mean">sensacao</span></ruby
        >じだった？」<ruby>ダン<rt>ダン</rt><span class="mean">Dan</span></ruby
        >が<ruby>満足<rt>まんぞく</rt><span class="mean">satisfeito</span></ruby
        >そうな<ruby>笑顔<rt>えがお</rt><span class="mean">sorriso</span></ruby
        >を<ruby>浮<rt>う</rt><span class="mean">exibir</span></ruby
        >かべた。「<ruby>最高<rt>さいこう</rt><span class="mean">o melhor</span></ruby
        >だったよ。<ruby>全部<rt>ぜんぶ</rt><span class="mean">tudo</span></ruby
        >、<ruby>一<rt>ひと</rt><span class="mean">um</span></ruby
        >つ<ruby>一<rt>ひと</rt><span class="mean">um</span></ruby
        >つ<ruby>話<rt>はな</rt><span class="mean">contar</span></ruby
        >していいか？」
      </p>

      <p>
        <ruby>キャミィ<rt>キャミィ</rt><span class="mean">Cammy</span></ruby
        >が<ruby>眉<rt>まゆ</rt><span class="mean">sobrancelha</span></ruby
        >を<ruby>上<rt>あ</rt><span class="mean">levantar</span></ruby
        >げた。「<ruby>詳細<rt>しょうさい</rt><span class="mean">detalhes</span></ruby
        >まで<ruby>話<rt>はな</rt><span class="mean">contar</span></ruby
        >す<ruby>必要<rt>ひつよう</rt><span class="mean">necessario</span></ruby
        >はないぞ」<ruby>ダン<rt>ダン</rt><span class="mean">Dan</span></ruby
        >が<ruby>笑<rt>わら</rt><span class="mean">rir</span></ruby
        >いながら<ruby>手<rt>て</rt><span class="mean">mao</span></ruby
        >を<ruby>振<rt>ふ</rt><span class="mean">balancar</span></ruby
        >った。「そういう<ruby>意味<rt>いみ</rt><span class="mean">significado</span></ruby
        >じゃないよ。<ruby>朝<rt>あさ</rt><span class="mean">manha</span></ruby
        >のキャミィの<ruby>特訓<rt>とっくん</rt><span class="mean">treino intensivo</span></ruby
        >、<ruby>本当<rt>ほんとう</rt><span class="mean">realmente</span></ruby
        >に<ruby>死<rt>し</rt><span class="mean">morrer</span></ruby
        >ぬかと<ruby>思<rt>おも</rt><span class="mean">pensar</span></ruby
        >ったぞ。<ruby>公園<rt>こうえん</rt><span class="mean">parque</span></ruby
        >でのサンドイッチも、<ruby>本当<rt>ほんとう</rt><span class="mean">realmente</span></ruby
        >にうまかったし」
      </p>

      <p>
        <ruby>キャミィ<rt>キャミィ</rt><span class="mean">Cammy</span></ruby
        >が<ruby>少<rt>すこ</rt><span class="mean">um pouco</span></ruby
        >し<ruby>誇<rt>ほこ</rt><span class="mean">orgulhoso</span></ruby
        >らしげに<ruby>頷<rt>うなず</rt><span class="mean">acenar</span></ruby
        >いた。<ruby>ダン<rt>ダン</rt><span class="mean">Dan</span></ruby
        >が<ruby>続<rt>つづ</rt><span class="mean">continuar</span></ruby
        >けた。「それから、<ruby>芝生<rt>しばふ</rt><span class="mean">gramado</span></ruby
        >で<ruby>休<rt>やす</rt><span class="mean">descansar</span></ruby
        >んでる<ruby>時<rt>とき</rt><span class="mean">momento</span></ruby
        >、キャミィがキスしてくれたんだ。<ruby>誕生日<rt>たんじょうび</rt><span class="mean">aniversario</span></ruby
        >おめでとうって」<ruby>舞<rt>まい</rt><span class="mean">Mai</span></ruby
        >が<ruby>目<rt>め</rt><span class="mean">olhos</span></ruby
        >を<ruby>丸<rt>まる</rt><span class="mean">arregalar</span></ruby
        >くしてから、<ruby>頬<rt>ほお</rt><span class="mean">bochecha</span></ruby
        >を<ruby>膨<rt>ふく</rt><span class="mean">inflar</span></ruby
        >らませた。「なにそれ、<ruby>羨<rt>うらや</rt><span class="mean">invejar</span></ruby
        >ましい」
      </p>

      <p>
        <ruby>ダン<rt>ダン</rt><span class="mean">Dan</span></ruby
        >が<ruby>笑<rt>わら</rt><span class="mean">rir</span></ruby
        >いながら<ruby>続<rt>つづ</rt><span class="mean">continuar</span></ruby
        >けた。「<ruby>午後<rt>ごご</rt><span class="mean">tarde</span></ruby
        >は<ruby>ティファ<rt>ティファ</rt><span class="mean">Tifa</span></ruby
        >と<ruby>街<rt>まち</rt><span class="mean">cidade</span></ruby
        >を<ruby>歩<rt>ある</rt><span class="mean">andar</span></ruby
        >き<ruby>回<rt>まわ</rt><span class="mean">passear</span></ruby
        >って、バーでカクテル<ruby>飲<rt>の</rt><span class="mean">beber</span></ruby
        >んで、<ruby>観覧車<rt>かんらんしゃ</rt><span class="mean">roda gigante</span></ruby
        >にも<ruby>乗<rt>の</rt><span class="mean">andar</span></ruby
        >ったんだ」<ruby>舞<rt>まい</rt><span class="mean">Mai</span></ruby
        >が<ruby>頬<rt>ほお</rt><span class="mean">bochecha</span></ruby
        >を<ruby>膨<rt>ふく</rt><span class="mean">inflar</span></ruby
        >らませたまま<ruby>ティファ<rt>ティファ</rt><span class="mean">Tifa</span></ruby
        >を<ruby>見<rt>み</rt><span class="mean">olhar</span></ruby
        >た。「ティファもキスしたんでしょ、<ruby>顔<rt>かお</rt><span class="mean">rosto</span></ruby
        >に<ruby>書<rt>か</rt><span class="mean">escrever</span></ruby
        >いてある」<ruby>ティファ<rt>ティファ</rt><span class="mean">Tifa</span></ruby
        >が<ruby>頬<rt>ほお</rt><span class="mean">bochecha</span></ruby
        >を<ruby>赤<rt>あか</rt><span class="mean">vermelho</span></ruby
        >らめながら<ruby>笑<rt>わら</rt><span class="mean">sorrir</span></ruby
        >った。「うん、<ruby>観覧車<rt>かんらんしゃ</rt><span class="mean">roda gigante</span></ruby
        >の<ruby>上<rt>うえ</rt><span class="mean">em cima</span></ruby
        >で」
      </p>

      <p>
        <ruby>舞<rt>まい</rt><span class="mean">Mai</span></ruby
        >が<ruby>唇<rt>くちびる</rt><span class="mean">labios</span></ruby
        >を<ruby>尖<rt>とが</rt><span class="mean">fazer bico</span></ruby
        >らせた。「もう、<ruby>二人<rt>ふたり</rt><span class="mean">as duas</span></ruby
        >とも<ruby>抜<rt>ぬ</rt><span class="mean">adiantar-se</span></ruby
        >け<ruby>目<rt>め</rt><span class="mean">adiantar-se</span></ruby
        >ないんだから」でも、その<ruby>口調<rt>くちょう</rt><span class="mean">tom de voz</span></ruby
        >には<ruby>本気<rt>ほんき</rt><span class="mean">seriedade</span></ruby
        >の<ruby>怒<rt>いか</rt><span class="mean">raiva</span></ruby
        >りは<ruby>感<rt>かん</rt><span class="mean">sentir</span></ruby
        >じられなかった。<ruby>キャミィ<rt>キャミィ</rt><span class="mean">Cammy</span></ruby
        >が<ruby>肩<rt>かた</rt><span class="mean">ombro</span></ruby
        >をすくめた。「<ruby>気<rt>き</rt><span class="mean">se importar</span></ruby
        >にしてないみたいだが」<ruby>舞<rt>まい</rt><span class="mean">Mai</span></ruby
        >が<ruby>笑<rt>わら</rt><span class="mean">rir</span></ruby
        >いながら<ruby>認<rt>みと</rt><span class="mean">admitir</span></ruby
        >めた。「うん、<ruby>気<rt>き</rt><span class="mean">se importar</span></ruby
        >にしてない。<ruby>私<rt>わたし</rt><span class="mean">eu</span></ruby
        >たち、みんな<ruby>選<rt>えら</rt><span class="mean">escolher</span></ruby
        >んだ<ruby>家族<rt>かぞく</rt><span class="mean">familia</span></ruby
        >なんだから」
      </p>

      <p>
        <ruby>ダン<rt>ダン</rt><span class="mean">Dan</span></ruby
        >が<ruby>頷<rt>うなず</rt><span class="mean">acenar</span></ruby
        >いてから、<ruby>いよいよ<rt>いよいよ</rt><span class="mean">finalmente</span></ruby
        ><ruby>夜<rt>よる</rt><span class="mean">noite</span></ruby
        >の<ruby>話<rt>はなし</rt><span class="mean">historia</span></ruby
        >に<ruby>入<rt>はい</rt><span class="mean">entrar</span></ruby
        >った。「それで、<ruby>夜<rt>よる</rt><span class="mean">noite</span></ruby
        >は<ruby>舞<rt>まい</rt><span class="mean">Mai</span></ruby
        >が<ruby>レストラン<rt>レストラン</rt><span class="mean">restaurante</span></ruby
        >に<ruby>連<rt>つ</rt><span class="mean">levar</span></ruby
        >れてってくれて、それからホテルの<ruby>部屋<rt>へや</rt><span class="mean">quarto</span></ruby
        >で……」<ruby>舞<rt>まい</rt><span class="mean">Mai</span></ruby
        >が<ruby>慌<rt>あわ</rt><span class="mean">apressado</span></ruby
        >てて<ruby>口<rt>くち</rt><span class="mean">boca</span></ruby
        >を<ruby>塞<rt>ふさ</rt><span class="mean">tapar</span></ruby
        >いだ。「ちょっと、それ<ruby>以上<rt>いじょう</rt><span class="mean">mais que isso</span></ruby
        >は<ruby>言<rt>い</rt><span class="mean">dizer</span></ruby
        >わないで！」
      </p>

      <p>
        <ruby>ダン<rt>ダン</rt><span class="mean">Dan</span></ruby
        >が<ruby>笑<rt>わら</rt><span class="mean">rir</span></ruby
        >いながら<ruby>続<rt>つづ</rt><span class="mean">continuar</span></ruby
        >けた。「<ruby>大丈夫<rt>だいじょうぶ</rt><span class="mean">tudo bem</span></ruby
        >、そこは<ruby>話<rt>はな</rt><span class="mean">contar</span></ruby
        >さないよ。でも、ポールダンスのことは<ruby>話<rt>はな</rt><span class="mean">contar</span></ruby
        >していいだろ？」<ruby>舞<rt>まい</rt><span class="mean">Mai</span></ruby
        >が<ruby>顔<rt>かお</rt><span class="mean">rosto</span></ruby
        >を<ruby>覆<rt>おお</rt><span class="mean">cobrir</span></ruby
        >った。「やめて、それは<ruby>恥<rt>は</rt><span class="mean">vergonha</span></ruby
        >ずかしすぎる」<ruby>ティファ<rt>ティファ</rt><span class="mean">Tifa</span></ruby
        >と<ruby>キャミィ<rt>キャミィ</rt><span class="mean">Cammy</span></ruby
        >が<ruby>同時<rt>どうじ</rt><span class="mean">ao mesmo tempo</span></ruby
        >に<ruby>身<rt>み</rt><span class="mean">corpo</span></ruby
        >を<ruby>乗<rt>の</rt><span class="mean">inclinar</span></ruby
        >り<ruby>出<rt>だ</rt><span class="mean">para frente</span></ruby
        >した。「ポールダンス！？」
      </p>

      <p>
        <ruby>ダン<rt>ダン</rt><span class="mean">Dan</span></ruby
        >が<ruby>楽<rt>たの</rt><span class="mean">divertido</span></ruby
        >しそうに<ruby>話<rt>はな</rt><span class="mean">contar</span></ruby
        >し<ruby>始<rt>はじ</rt><span class="mean">comecar</span></ruby
        >めた。「<ruby>舞<rt>まい</rt><span class="mean">Mai</span></ruby
        >、ホテルの<ruby>部屋<rt>へや</rt><span class="mean">quarto</span></ruby
        >にあったポールで、<ruby>動画<rt>どうが</rt><span class="mean">video</span></ruby
        >で<ruby>練習<rt>れんしゅう</rt><span class="mean">praticar</span></ruby
        >したダンスを<ruby>披露<rt>ひろう</rt><span class="mean">apresentar</span></ruby
        >しようとしたんだけど……<ruby>見事<rt>みごと</rt><span class="mean">de forma admiravel</span></ruby
        >に<ruby>滑<rt>すべ</rt><span class="mean">escorregar</span></ruby
        >って<ruby>落<rt>お</rt><span class="mean">cair</span></ruby
        >ちたんだ」<ruby>舞<rt>まい</rt><span class="mean">Mai</span></ruby
        >が<ruby>クッション<rt>クッション</rt><span class="mean">almofada</span></ruby
        >を<ruby>掴<rt>つか</rt><span class="mean">agarrar</span></ruby
        >んでダンに<ruby>投<rt>な</rt><span class="mean">arremessar</span></ruby
        >げた。「もう、<ruby>言<rt>い</rt><span class="mean">dizer</span></ruby
        >わないでって<ruby>言<rt>い</rt><span class="mean">dizer</span></ruby
        >ったのに！」
      </p>

      <p>
        <ruby>ティファ<rt>ティファ</rt><span class="mean">Tifa</span></ruby
        >が<ruby>声<rt>こえ</rt><span class="mean">voz</span></ruby
        >を<ruby>上<rt>あ</rt><span class="mean">soltar</span></ruby
        >げて<ruby>笑<rt>わら</rt><span class="mean">rir</span></ruby
        >った。「<ruby>舞<rt>まい</rt><span class="mean">Mai</span></ruby
        >らしいね、それ！」<ruby>キャミィ<rt>キャミィ</rt><span class="mean">Cammy</span></ruby
        >も<ruby>珍<rt>めずら</rt><span class="mean">raramente</span></ruby
        >しく<ruby>口元<rt>くちもと</rt><span class="mean">canto da boca</span></ruby
        >を<ruby>緩<rt>ゆる</rt><span class="mean">relaxar</span></ruby
        >めた。<ruby>ダン<rt>ダン</rt><span class="mean">Dan</span></ruby
        >が<ruby>笑<rt>わら</rt><span class="mean">rir</span></ruby
        >いながらもクッションを<ruby>避<rt>さ</rt><span class="mean">evitar</span></ruby
        >けた。「それでも<ruby>舞<rt>まい</rt><span class="mean">Mai</span></ruby
        >、ちゃんと<ruby>普通<rt>ふつう</rt><span class="mean">normal</span></ruby
        >に<ruby>踊<rt>おど</rt><span class="mean">dancar</span></ruby
        >るダンスも<ruby>見<rt>み</rt><span class="mean">mostrar</span></ruby
        >せてくれたんだ。あれは<ruby>本当<rt>ほんとう</rt><span class="mean">realmente</span></ruby
        >に<ruby>綺麗<rt>きれい</rt><span class="mean">bonito</span></ruby
        >だった」
      </p>

      <p>
        <ruby>舞<rt>まい</rt><span class="mean">Mai</span></ruby
        >の<ruby>顔<rt>かお</rt><span class="mean">rosto</span></ruby
        >が<ruby>少<rt>すこ</rt><span class="mean">um pouco</span></ruby
        >し<ruby>照<rt>て</rt><span class="mean">envergonhar-se</span></ruby
        >れたように<ruby>緩<rt>ゆる</rt><span class="mean">relaxar</span></ruby
        >んだ。<ruby>ダン<rt>ダン</rt><span class="mean">Dan</span></ruby
        >が<ruby>構<rt>かま</rt><span class="mean">nao se importar</span></ruby
        >わず<ruby>続<rt>つづ</rt><span class="mean">continuar</span></ruby
        >けた。「<ruby>俺<rt>おれ</rt><span class="mean">eu</span></ruby
        >の<ruby>膝<rt>ひざ</rt><span class="mean">joelho</span></ruby
        >の<ruby>上<rt>うえ</rt><span class="mean">em cima</span></ruby
        >に<ruby>座<rt>すわ</rt><span class="mean">sentar</span></ruby
        >って<ruby>踊<rt>おど</rt><span class="mean">dancar</span></ruby
        >ったやつもあったんだけど、あれは……」<ruby>舞<rt>まい</rt><span class="mean">Mai</span></ruby
        >が<ruby>今度<rt>こんど</rt><span class="mean">desta vez</span></ruby
        >は<ruby>本気<rt>ほんき</rt><span class="mean">seriedade</span></ruby
        >で<ruby>ダン<rt>ダン</rt><span class="mean">Dan</span></ruby
        >の<ruby>口<rt>くち</rt><span class="mean">boca</span></ruby
        >を<ruby>手<rt>て</rt><span class="mean">mao</span></ruby
        >で<ruby>塞<rt>ふさ</rt><span class="mean">tapar</span></ruby
        >いだ。「それ<ruby>以上<rt>いじょう</rt><span class="mean">mais que isso</span></ruby
        >は、<ruby>本当<rt>ほんとう</rt><span class="mean">realmente</span></ruby
        >に、<ruby>絶対<rt>ぜったい</rt><span class="mean">absolutamente</span></ruby
        >に<ruby>言<rt>い</rt><span class="mean">dizer</span></ruby
        >わせない」
      </p>

      <p>
        <ruby>ダン<rt>ダン</rt><span class="mean">Dan</span></ruby
        >が<ruby>舞<rt>まい</rt><span class="mean">Mai</span></ruby
        >の<ruby>手<rt>て</rt><span class="mean">mao</span></ruby
        >を<ruby>優<rt>やさ</rt><span class="mean">gentilmente</span></ruby
        >しく<ruby>外<rt>はず</rt><span class="mean">remover</span></ruby
        >した。「わかったよ、<ruby>そこ<rt>そこ</rt><span class="mean">isso</span></ruby
        >は<ruby>言<rt>い</rt><span class="mean">dizer</span></ruby
        >わない。でも、<ruby>最後<rt>さいご</rt><span class="mean">por ultimo</span></ruby
        >に<ruby>二人<rt>ふたり</rt><span class="mean">os dois</span></ruby
        >で<ruby>一緒<rt>いっしょ</rt><span class="mean">junto</span></ruby
        >に<ruby>踊<rt>おど</rt><span class="mean">dancar</span></ruby
        >った<ruby>時<rt>とき</rt><span class="mean">momento</span></ruby
        >は、<ruby>俺<rt>おれ</rt><span class="mean">eu</span></ruby
        >が<ruby>舞<rt>まい</rt><span class="mean">Mai</span></ruby
        >の<ruby>足<rt>あし</rt><span class="mean">pe</span></ruby
        >を<ruby>何度<rt>なんど</rt><span class="mean">varias vezes</span></ruby
        >も<ruby>踏<rt>ふ</rt><span class="mean">pisar</span></ruby
        >んじゃって」<ruby>舞<rt>まい</rt><span class="mean">Mai</span></ruby
        >が<ruby>頷<rt>うなず</rt><span class="mean">acenar</span></ruby
        >いた。「<ruby>本当<rt>ほんとう</rt><span class="mean">realmente</span></ruby
        >に<ruby>下手<rt>へた</rt><span class="mean">sem jeito</span></ruby
        >なダンサーだったよね」
      </p>

      <p>
        <ruby>ダン<rt>ダン</rt><span class="mean">Dan</span></ruby
        >が<ruby>苦笑<rt>くしょう</rt><span class="mean">sorriso amargo</span></ruby
        >いした。「<ruby>否定<rt>ひてい</rt><span class="mean">negar</span></ruby
        >できないな。それでも、あの<ruby>時間<rt>じかん</rt><span class="mean">tempo</span></ruby
        >、すごく<ruby>楽<rt>たの</rt><span class="mean">divertido</span></ruby
        >しかった」<ruby>皆<rt>みんな</rt><span class="mean">todos</span></ruby
        >が<ruby>笑<rt>わら</rt><span class="mean">rir</span></ruby
        >い<ruby>合<rt>あ</rt><span class="mean">reciprocamente</span></ruby
        >う<ruby>中<rt>なか</rt><span class="mean">meio de</span></ruby
        >、<ruby>ダン<rt>ダン</rt><span class="mean">Dan</span></ruby
        >が<ruby>不意<rt>ふい</rt><span class="mean">de repente</span></ruby
        >に<ruby>真剣<rt>しんけん</rt><span class="mean">serio</span></ruby
        >な<ruby>顔<rt>かお</rt><span class="mean">rosto</span></ruby
        >になった。
      </p>

      <p>
        「なあ、<ruby>三人<rt>さんにん</rt><span class="mean">as tres</span></ruby
        >とも、<ruby>本当<rt>ほんとう</rt><span class="mean">realmente</span></ruby
        >にありがとう」<ruby>ダン<rt>ダン</rt><span class="mean">Dan</span></ruby
        >が<ruby>一人一人<rt>ひとりひとり</rt><span class="mean">cada uma</span></ruby
        >の<ruby>顔<rt>かお</rt><span class="mean">rosto</span></ruby
        >を<ruby>見<rt>み</rt><span class="mean">olhar</span></ruby
        >つめた。「<ruby>愛<rt>あい</rt><span class="mean">amor</span></ruby
        >してる、<ruby>三人<rt>さんにん</rt><span class="mean">as tres</span></ruby
        >とも。お<ruby>前<rt>まえ</rt><span class="mean">voces</span></ruby
        >らは<ruby>俺<rt>おれ</rt><span class="mean">eu</span></ruby
        >にとって、<ruby>最高<rt>さいこう</rt><span class="mean">o melhor</span></ruby
        >の<ruby>相棒<rt>あいぼう</rt><span class="mean">companheira</span></ruby
        >で、<ruby>最高<rt>さいこう</rt><span class="mean">o melhor</span></ruby
        >の<ruby>友達<rt>ともだち</rt><span class="mean">amiga</span></ruby
        >で――それ<ruby>以上<rt>いじょう</rt><span class="mean">mais que isso</span></ruby
        >の<ruby>存在<rt>そんざい</rt><span class="mean">existencia</span></ruby
        >だ」
      </p>

      <p>
        <ruby>一瞬<rt>いっしゅん</rt><span class="mean">por um instante</span></ruby
        >、<ruby>部屋<rt>へや</rt><span class="mean">quarto</span></ruby
        >が<ruby>静<rt>しず</rt><span class="mean">silencioso</span></ruby
        >まった。<ruby>舞<rt>まい</rt><span class="mean">Mai</span></ruby
        >、<ruby>ティファ<rt>ティファ</rt><span class="mean">Tifa</span></ruby
        >、<ruby>キャミィ<rt>キャミィ</rt><span class="mean">Cammy</span></ruby
        >が<ruby>顔<rt>かお</rt><span class="mean">rosto</span></ruby
        >を見<ruby>合<rt>あ</rt><span class="mean">entreolhar</span></ruby
        >わせ、それから<ruby>三人<rt>さんにん</rt><span class="mean">as tres</span></ruby
        >が<ruby>同時<rt>どうじ</rt><span class="mean">ao mesmo tempo</span></ruby
        >に<ruby>ダン<rt>ダン</rt><span class="mean">Dan</span></ruby
        >に<ruby>飛<rt>と</rt><span class="mean">saltar</span></ruby
        >びついた。<ruby>四人<rt>よにん</rt><span class="mean">os quatro</span></ruby
        >はソファの<ruby>上<rt>うえ</rt><span class="mean">em cima</span></ruby
        >で<ruby>ぎゅっと<rt>ぎゅっと</rt><span class="mean">bem apertado</span></ruby
        ><ruby>抱<rt>だ</rt><span class="mean">abracar</span></ruby
        >き<ruby>合<rt>あ</rt><span class="mean">reciprocamente</span></ruby
        >い、<ruby>笑<rt>わら</rt><span class="mean">rir</span></ruby
        >い<ruby>声<rt>ごえ</rt><span class="mean">voz</span></ruby
        >が<ruby>部屋<rt>へや</rt><span class="mean">quarto</span></ruby
        >いっぱいに<ruby>響<rt>ひび</rt><span class="mean">ressoar</span></ruby
        >いた。
      </p>

      <p>
        <ruby>窓<rt>まど</rt><span class="mean">janela</span></ruby
        >から<ruby>差<rt>さ</rt><span class="mean">entrar</span></ruby
        >し<ruby>込<rt>こ</rt><span class="mean">entrar</span></ruby
        >む<ruby>柔<rt>やわ</rt><span class="mean">suave</span></ruby
        >らかな<ruby>陽<rt>ひ</rt><span class="mean">sol</span></ruby
        >の<ruby>光<rt>ひかり</rt><span class="mean">luz</span></ruby
        >が、<ruby>四人<rt>よにん</rt><span class="mean">os quatro</span></ruby
        >を<ruby>優<rt>やさ</rt><span class="mean">gentilmente</span></ruby
        >しく<ruby>照<rt>て</rt><span class="mean">iluminar</span></ruby
        >らしていた。<ruby>誕生日<rt>たんじょうび</rt><span class="mean">aniversario</span></ruby
        >の<ruby>三<rt>み</rt><span class="mean">tres</span></ruby
        >つの<ruby>部<rt>ぶ</rt><span class="mean">parte</span></ruby
        >が<ruby>全<rt>すべ</rt><span class="mean">todos</span></ruby
        >て<ruby>終<rt>お</rt><span class="mean">terminar</span></ruby
        >わり、それぞれの<ruby>思<rt>おも</rt><span class="mean">pensamento</span></ruby
        >いが<ruby>込<rt>こ</rt><span class="mean">colocar</span></ruby
        >められた<ruby>特別<rt>とくべつ</rt><span class="mean">especial</span></ruby
        >な<ruby>一日<rt>いちにち</rt><span class="mean">um dia</span></ruby
        >が、<ruby>笑<rt>わら</rt><span class="mean">rir</span></ruby
        >い<ruby>声<rt>ごえ</rt><span class="mean">voz</span></ruby
        >とともに<ruby>幕<rt>まく</rt><span class="mean">cortina</span></ruby
        >を<ruby>閉<rt>と</rt><span class="mean">fechar</span></ruby
        >じようとしていた。
      </p>

      <div class="notes">
        <p><i>※ ダンは三人それぞれの贈り物の詳細を全て語り、四人の絆はより一層深まった。</i></p>
        <p><i>※ ケーキは誕生日の翌朝に食べることになったが、誰も気にしていなかった。</i></p>
        <p><i>※ 誕生日編はこれで幕を閉じる。</i></p>
      </div>
    </div>

  </body>
</html>
