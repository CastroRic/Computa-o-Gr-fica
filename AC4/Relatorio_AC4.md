# AC4 – Modelos de iluminação: Lambert, Phong e Blinn-Phong

**Aluno:** Ricardo Castro  
**Arquivo:** `AC4_RicardoCastro.blend` (Blender 4.5, EEVEE Next, 1920×1080, view transform AgX)

> Os dados abaixo foram lidos diretamente do arquivo `.blend`. A seção 4 foi
> derivada dos parâmetros dos materiais e da luz, não de um render feito por mim.
> Confira-a contra o seu render final.

---

## 1. Objetos e materiais

| Objeto | Material | Modelo representado |
|---|---|---|
| `obj_livro` | `MAT_Lambert` | Lambert (difuso) |
| `obj_propulsor` | `MAT_Phong` | Phong |
| `obj_capela` | `MAT_BlinnPhong` | Blinn-Phong |

Observações:

- Cada um desses objetos tem vários *material slots*. Os materiais acima ocupam um slot em cada objeto, e os demais slots usam materiais genéricos (`Material.0xx`).
- Há ainda `obj_foguete` (54 slots, nenhum dos três materiais), dois objetos de texto (`obj_txt_ibmec`, `obj_txt_ibmec.001`), a câmera e a luz.

## 2. Iluminação

**Luz principal** (`Area`, única luz da cena):

| Parâmetro | Valor |
|---|---|
| Tipo / forma | Area / Disk |
| Tamanho | 4,0 m |
| Potência | 1500 W |
| Cor | Branca (1, 1, 1) |
| Posição (x, y, z) | (−9,92; 5,59; 6,34) m |
| Rotação | (0°, 0°, 0°), apontando para −Z (para baixo) |
| Spread | 180° |
| Fatores difuso / especular | 1,0 / 1,0 |

**Luz de preenchimento:** não há. O que preenche as sombras é apenas o *World*, com cor cinza escuro (linear 0,051, ≈ `#404040` em sRGB) e Strength 1,0. Isso é luz ambiente, e não uma segunda luz.

## 3. Valores principais dos materiais

Todos usam `Principled BSDF` (distribuição Multiscatter GGX, IOR 1,5).  
Cores em linear, como armazenadas no Blender, com o hex sRGB aproximado entre parênteses.

| Material | Base Color (RGB linear) | Roughness | Specular IOR Level | Metallic |
|---|---|---|---|---|
| `MAT_Lambert` | (0,007; 0,800; 0,000), verde (`#15E700`) | **1,0** | **0,1** | 0,0 |
| `MAT_Phong` | (0,000; 0,572; 0,801), ciano (`#00C7E7`) | **0,2** | **0,5** | 0,5 |
| `MAT_BlinnPhong` | (0,000; 0,035; 0,800), azul (`#0034E7`) | **0,1** | **1,0** | 0,0 |

Os demais parâmetros (Coat, Sheen, Transmission, Subsurface, Emission) estão zerados ou no padrão.

## 4. Comparação das aparências

- **Lambert:** com roughness 1,0 e IOR Level 0,1, quase não há brilho especular. A superfície fica mate e o sombreamento depende só do ângulo entre normal e luz (Lei de Lambert). É a aparência mais "de giz" ou "de papel".
- **Phong:** roughness 0,2 e IOR Level 0,5 dão um brilho visível, mas relativamente espalhado. O `Metallic = 0,5` faz o reflexo ser parcialmente tingido pela cor-base, o que dá um aspecto semimetálico e menos "plástico".
- **Blinn-Phong:** roughness 0,1 e IOR Level 1,0 (máximo) dão o brilho mais concentrado e intenso dos três, com cara de plástico ou verniz polido. Como `Metallic = 0`, o reflexo é branco, sem tingimento.

Ou seja, a progressão Lambert → Phong → Blinn-Phong vai de **sem highlight** a **highlight moderado** e a **highlight pequeno e forte**. Parte da diferença entre Phong e Blinn-Phong vem dos valores escolhidos (rugosidade e metallic diferentes), não só do modelo de sombreamento.

## 5. Por que são aproximações

O `Principled BSDF` do Blender (EEVEE e Cycles) **não implementa** as equações clássicas:

- **Lambert** é literal: `I = kd · max(0, N·L)`. O lobo difuso do Principled é equivalente a isso, e o ajuste `Roughness = 1` e especular baixo apenas faz o termo especular desaparecer, sem ser exatamente zero (IOR Level 0,1 ainda reflete cerca de 0,8 % de luz em incidência normal).
- **Phong** (`ks · (R·V)ⁿ`) e **Blinn-Phong** (`ks · (N·H)ⁿ`) usam um expoente `n` e um coeficiente `ks` livres. No Principled o brilho vem de um modelo *microfacet* (Multiscatter GGX), com distribuição de normais, termo de sombreamento/mascaramento e Fresnel, baseado em física. Não há expoente de Phong nem vetor halfway ajustável.
- Os parâmetros são diferentes: `Roughness` controla a largura do lobo, `Specular IOR Level` (junto com o IOR) controla a intensidade, e `Metallic` muda como o reflexo é colorido. Uma correspondência comum é `n ≈ 2/α² − 2`, com `α = roughness²`, mas ela é só uma heurística visual.
- O Fresnel também muda o brilho em ângulos rasantes, o que Phong e Blinn-Phong clássicos não têm. O "Phong" e o "Blinn-Phong" do arquivo são, portanto, **aproximações visuais** do comportamento dos modelos, obtidas calibrando `Roughness` e `Specular IOR Level`, e não implementações literais.
