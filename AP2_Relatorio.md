# AP2 — Foguete do Conhecimento

**Aluno:** Ricardo Castro  
**Ferramenta:** Blender 4.5 LTS  
**Disciplina:** Computação Gráfica  
**Data da entrega:** 18/11/2026

## 1. Título, conceito e resumo da sequência

**Título:** Foguete do Conhecimento.

O projeto dá continuidade à proposta da AP1, em que três objetos autorais — **livro, capelo de formatura e propulsor** — foram combinados para compor um foguete. A metáfora central é a de que **o conhecimento impulsiona a trajetória acadêmica**.

Na AP2, a composição se transforma em uma animação de 15 segundos. O foguete se prepara para decolar, sobe com um deslocamento lateral e uma leve inclinação, deixando um rastro de fumaça estilizada. O cenário foi ampliado para incluir chão com grama, céu iluminado pelo sol e uma versão simplificada do prédio do Ibmec, que recebe destaque no enquadramento final. A palavra **Ibmec** permanece como elemento de identidade visual da peça.

## 2. Momentos, planos e ações animadas

| Momento | Tempo aproximado | Frames aproximados | Ação e enquadramento |
|---|---|---|---|
| 1. Apresentação | 0–3 s | 1–72 | Apresentação do foguete e do ambiente externo, com o edifício do Ibmec ao fundo. |
| 2. Preparação | 3–5 s | 73–120 | Início da ativação dos propulsores e formação do rastro de fumaça. |
| 3. Decolagem | 5–10 s | 121–240 | O foguete ganha altitude, move-se lateralmente e se inclina de forma suave; a câmera acompanha parte do percurso. |
| 4. Abertura do enquadramento | 10–13 s | 241–312 | A câmera se afasta gradualmente, revelando mais da arquitetura e dos materiais do prédio. |
| 5. Encerramento | 13–15 s | 313–360 | O enquadramento se estabiliza e prioriza a fachada e a identidade do Ibmec. |

*Os intervalos são referências narrativas do storyboard atualizado; os keyframes foram ajustados durante a produção e podem não coincidir exatamente com todas essas divisões.*

## 3. Propriedades animadas, timing e interpolação

A animação foi planejada para **360 frames a 24 fps**, totalizando **15 segundos**. As principais propriedades trabalhadas foram:

- **Foguete:** `Location Z` para a subida; deslocamento horizontal em `Location X` e leve `Rotation Y` para acompanhar a mudança de direção. Os movimentos foram controlados por keyframes no objeto de controle do conjunto, preservando a montagem dos três objetos autorais.
- **Câmera:** animação de posição e orientação para acompanhar parcialmente a decolagem e, no final, se afastar e valorizar o prédio do Ibmec.
- **Fumaça:** nuvens geométricas animadas com variações de posição, escala e transparência ao longo do tempo; os pontos de emissão acompanham o foguete.

O timing prioriza início mais contido, aceleração perceptível durante a subida e desaceleração do movimento de câmera no encerramento. Foram utilizadas curvas com **interpolação Bézier**, ajustadas para evitar transições bruscas. O movimento lateral e a inclinação foram aumentados proporcionalmente à escala da cena durante os testes.

## 4. Iluminação e renderização

A cena foi organizada como um **ambiente externo**, com céu procedural e iluminação solar. A luz do tipo **Sun** funciona como fonte direcional principal, produzindo sombras sobre o chão e as fachadas; o ambiente do céu complementa a iluminação para preservar a legibilidade dos objetos.

A configuração de produção adotada para a AP2 é:

| Parâmetro | Configuração |
|---|---|
| Versão | Blender 4.5 LTS |
| Motor de render | Eevee |
| Intervalo | Frames 1–360 |
| Taxa de quadros | 24 fps |
| Duração | 15 segundos |
| Resolução-alvo | 1920 × 1080 (Full HD) |
| Entrega de vídeo | MP4, codec H.264 |

O fluxo de exportação recomendado consiste em **renderizar a sequência de quadros em PNG** e depois reuni-los em MP4 pelo Video Sequencer do Blender. Essa estratégia permite preservar os quadros concluídos em caso de interrupção. A duração, o codec e a integridade visual devem ser conferidos no arquivo exportado.

## 5. Materiais e texturas da AC05 reaproveitados ou ajustados

Na AC05, foram criados os materiais `MAT_Metal_Escovado`, `MAT_Madeira_PBR` e `MAT_Espelho`, inicialmente demonstrados em cubos de teste. Na continuidade da AP2, os cubos de demonstração foram retirados do enquadramento e o foco passou aos objetos autorais e ao cenário.

- **Propulsor:** reaproveitamento do aspecto metálico desenvolvido na AC05, apropriado para as peças mecânicas do foguete.
- **Livros e capelo:** preservação da aparência e das cores necessárias para reconhecer os objetos autorais; os materiais foram considerados em conjunto com a nova iluminação.
- **Prédio Ibmec:** criação de materiais para paredes claras de concreto, estruturas azuis, detalhes laranja e painéis escuros com **aparência de vidro opaco**. Os painéis não utilizam transparência, dispensando modelagem de interiores.
- **Concreto:** utilização de textura PBR obtida no **ambientCG**, aplicada às superfícies de concreto, inclusive partes claras da fachada e/ou cobertura conforme os ajustes do projeto.
- **Grama:** material procedural com `Noise Texture`, `Color Ramp` e `Bump`, acrescentando variação de tonalidade e relevo aparente ao solo.

Nos materiais com mapas de imagem, o **Base Color** utiliza espaço de cor `sRGB`; mapas de **Roughness** e **Normal** usam `Non-Color`, e o normal map de imagem é ligado ao **Principled BSDF** por meio do nó **Normal Map**. Materiais procedurais que utilizam `Bump` produzem relevo visual sem alterar diretamente a geometria.

## 6. Desafios encontrados e soluções adotadas

| Desafio | Solução |
|---|---|
| Organizar uma animação com três peças que precisam permanecer unidas | Uso de um objeto controlador para movimentar o foguete como conjunto. |
| Fazer a subida parecer natural | Ajustes dos keyframes de altura, deslocamento lateral, inclinação e interpolação. |
| Produzir fumaça acompanhando um foguete que percorre grande distância | Substituição da simulação física pesada por fumaça procedural estilizada, com emissão vinculada ao foguete e rastro animado. |
| Adicionar uma referência institucional clara | Modelagem simplificada da fachada e ampliação lateral e traseira do prédio do Ibmec. |
| Evitar custo de modelar interiores | Uso de painéis escuros opacos no lugar de vidro transparente. |
| Corrigir interferências entre partes do prédio | Reorganização de pilares, barras azuis, volumes e letreiro da fachada. |
| Melhorar a leitura dos materiais | Reutilização dos materiais da AC05, aplicação de concreto e ajustes de textura, rugosidade e normais. |
| Encerrar a narrativa enfatizando o Ibmec | Ajuste da câmera para se afastar e revelar a arquitetura no plano final. |
| Reduzir o risco de perder o vídeo ao renderizar | Renderização planejada por sequência de PNGs, seguida de codificação MP4/H.264. |

## 7. Fontes, ferramentas e licenças

| Recurso | Fonte | Uso | Licença / observação |
|---|---|---|---|
| Assistência na elaboração de scripts, solução de problemas e documentação | [ChatGPT — OpenAI](https://chatgpt.com/) | Auxílio técnico na criação/ajuste de scripts Python para Blender, materiais, câmera, fumaça e redação do relatório | Ferramenta de IA utilizada como apoio; scripts e resultados revisados e ajustados durante o desenvolvimento do projeto. Não é uma biblioteca de texturas. |
| Textura PBR de concreto | [ambientCG — catálogo de materiais](https://ambientcg.com/list?type=material%2Cdecal%2Catlas&sort=popular) | Material de concreto aplicado ao prédio | **CC0 1.0**; utilização e adaptação permitidas, inclusive sem atribuição obrigatória. |
| Textura de metal `Metal009` (AC05) | [ambientCG — Metal009](https://ambientcg.com/view?id=Metal009) | Material metálico desenvolvido na AC05 e reaproveitado no propulsor | **CC0 1.0**. |
| Textura de madeira `Wood051` (AC05) | [ambientCG — Wood051](https://ambientcg.com/view?id=Wood051) | Material PBR desenvolvido na AC05 | **CC0 1.0**. |
| Referência visual do edifício | Fotografia da unidade Ibmec fornecida para o desenvolvimento da cena | Referência de formas, cores e fachada para modelagem simplificada | Uso como referência acadêmica; autoria/licença da fotografia não identificada. |

**Licença do ambientCG:** <https://docs.ambientcg.com/license/>.

**Observação sobre autoria e IA:** O conceito do *Foguete do Conhecimento* e a união de livro, capelo e propulsor são provenientes da AP1. O ChatGPT foi utilizado como ferramenta de apoio para automatizar parte da construção da cena, sugerir soluções técnicas, corrigir scripts e auxiliar na documentação; a seleção, os testes e os ajustes visuais foram realizados no Blender durante o desenvolvimento da AP2.

---

**Checklist final de entrega:** arquivo `.blend` com recursos externos empacotados ou caminhos relativos funcionais; vídeo `.mp4` com 15 segundos e 24 fps; pelo menos uma imagem renderizada; storyboard atualizado; e este relatório.
