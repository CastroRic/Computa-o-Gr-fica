# AC05 – Materiais PBR e Texturas
**Aluno:** Ricardo Castro

## 1. Objetos e materiais

| Objeto | Material | Descrição |
|---|---|---|
| Cubo 1 | MAT_Metal_Escovado | Metal escovado escuro, textura de imagem PBR |
| Cubo 2 | MAT_Madeira_PBR | Madeira escura com veios, textura de imagem PBR |
| Cubo 3 | MAT_Espelho | Superfície espelhada, cor sólida |

Os três objetos foram modelados como cubos e posicionados ao lado dos
objetos da AP1 (livros, capelo, etc.), na coleção AC05_Materiais_Texturas.

## 2. Propriedades principais

| Material | Base Color | Metallic | Roughness | Outros |
|---|---|---|---|---|
| MAT_Metal_Escovado | textura _Color | 1.0 | textura _Roughness | IOR 1.5, Normal Map |
| MAT_Madeira_PBR | textura _Color | 0.0 | textura _Roughness | IOR 1.5, Normal Map |
| MAT_Espelho | (cor clara) | 1.0 | 0.0–0.05 | IOR 1.5 |

## 3. Mapas utilizados e conexões

- **Metal:** Color (sRGB) → Base Color; Roughness (Non-Color) → Roughness;
  NormalGL (Non-Color) → nó Normal Map → Normal do Principled BSDF.
- **Madeira:** Color (sRGB) → Base Color; Roughness (Non-Color) → Roughness;
  NormalGL (Non-Color) → nó Normal Map → Normal do Principled BSDF.
- **Espelho:** sem mapas; apenas valores numéricos.

Mapas de dados (Roughness, Normal) foram configurados como Non-Color.
O mapa de cor foi mantido em sRGB. Foi usado o NormalGL, formato esperado pelo Blender.

## 4. UV

Método: Smart UV Project (Angle Limit 66°, Island Margin __).
Por serem cubos, o método gerou ilhas retangulares sem distorção relevante.
Inspeção: ilhas conferidas no UV Editor, dentro do espaço 0–1 e sem sobreposição.

## 5. Origem e licença das texturas

| Textura | Fonte | Link | Licença |
|---|---|---|---|
| Metal009 (1K-PNG) | ambientCG | https://ambientcg.com/view?id=Metal009 | CC0 |
| Wood051 (1K-PNG) | ambientCG | https://ambientcg.com/view?id=Wood051 | CC0 |