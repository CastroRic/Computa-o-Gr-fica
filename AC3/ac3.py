import bpy
import math


NOME_COLECAO = "AC03_transformacoes"


def obter_colecao():
    colecao = bpy.data.collections.get(NOME_COLECAO)

    if colecao is None:
        colecao = bpy.data.collections.new(NOME_COLECAO)
        bpy.context.scene.collection.children.link(colecao)

    return colecao


def remover_objeto(nome):
    objeto = bpy.data.objects.get(nome)

    if objeto is not None:
        bpy.data.objects.remove(objeto, do_unlink=True)


def mover_para_colecao(objeto, colecao):
    for colecao_atual in list(objeto.users_collection):
        colecao_atual.objects.unlink(objeto)

    colecao.objects.link(objeto)


def criar_material(nome, cor, metalico=0.0, rugosidade=0.4):
    material = bpy.data.materials.get(nome)

    if material is None:
        material = bpy.data.materials.new(nome)

    material.use_nodes = True
    material.diffuse_color = (*cor, 1.0)

    principled = material.node_tree.nodes.get("Principled BSDF")

    if principled is not None:
        principled.inputs["Base Color"].default_value = (*cor, 1.0)
        principled.inputs["Metallic"].default_value = metalico
        principled.inputs["Roughness"].default_value = rugosidade

    return material


def atribuir_material(objeto, material):
    objeto.data.materials.clear()
    objeto.data.materials.append(material)


colecao = obter_colecao()

remover_objeto("obj3d_cubo_script")
remover_objeto("obj3d_esfera_script")
remover_objeto("controle_orbita_esfera")

cena = bpy.context.scene
cena.frame_start = 1
cena.frame_end = 120
cena.render.fps = 24

# Cubo

bpy.ops.mesh.primitive_cube_add(location=(3, 2, 1))
cubo = bpy.context.active_object
cubo.name = "obj3d_cubo_script"
mover_para_colecao(cubo, colecao)

material_cubo = criar_material(
    "material_cubo_vermelho",
    (0.75, 0.08, 0.05),
    metalico=0.15,
    rugosidade=0.3,
)

atribuir_material(cubo, material_cubo)

cubo.location = (3, 2, 1)
cubo.rotation_euler = (
    math.radians(0),
    math.radians(0),
    math.radians(0),
)
cubo.scale = (1, 1, 1)

cubo.keyframe_insert(data_path="location", frame=1)
cubo.keyframe_insert(data_path="rotation_euler", frame=1)
cubo.keyframe_insert(data_path="scale", frame=1)

cubo.location = (3, 2, 1.3)
cubo.rotation_euler = (
    math.radians(20),
    math.radians(35),
    math.radians(15),
)
cubo.scale = (1.2, 0.8, 1.5)

cubo.keyframe_insert(data_path="location", frame=60)
cubo.keyframe_insert(data_path="rotation_euler", frame=60)
cubo.keyframe_insert(data_path="scale", frame=60)

cubo.location = (3, 2, 1)
cubo.rotation_euler = (
    math.radians(45),
    math.radians(60),
    math.radians(90),
)
cubo.scale = (0.8, 1.3, 1.7)

cubo.keyframe_insert(data_path="location", frame=120)
cubo.keyframe_insert(data_path="rotation_euler", frame=120)
cubo.keyframe_insert(data_path="scale", frame=120)

controle = bpy.data.objects.new(
    "controle_orbita_esfera",
    None,
)

colecao.objects.link(controle)
controle.empty_display_type = "CIRCLE"
controle.empty_display_size = 1.0
controle.location = (-3, 2, 1.2)

# Esfera

bpy.ops.mesh.primitive_uv_sphere_add(location=(1.8, 0, 0))
esfera = bpy.context.active_object
esfera.name = "obj3d_esfera_script"
mover_para_colecao(esfera, colecao)

esfera.parent = controle

esfera.rotation_euler = (
    math.radians(15),
    math.radians(25),
    math.radians(10),
)
esfera.scale = (0.8, 0.8, 0.8)

material_esfera = criar_material(
    "material_esfera_amarela",
    (0.95, 0.55, 0.05),
    metalico=0.05,
    rugosidade=0.25,
)

atribuir_material(esfera, material_esfera)

for poligono in esfera.data.polygons:
    poligono.use_smooth = True

controle.rotation_euler = (0, 0, math.radians(0))
controle.keyframe_insert(data_path="rotation_euler", frame=1)

controle.rotation_euler = (0, 0, math.radians(180))
controle.keyframe_insert(data_path="rotation_euler", frame=60)

controle.rotation_euler = (0, 0, math.radians(360))
controle.keyframe_insert(data_path="rotation_euler", frame=120)

cena.frame_set(1)

print("AC03: cubo e esfera, animações e hierarquia criados.")




from mathutils import Vector


def apontar_para(objeto, alvo):
    """Orienta câmera ou luz para um ponto da cena."""
    direcao = Vector(alvo) - objeto.location
    objeto.rotation_euler = direcao.to_track_quat("-Z", "Y").to_euler()


# Remove elementos de apresentação antigos ao executar novamente
for nome in (
    "base_parque",
    "Camera_AC03",
    "Luz_Area_AC03",
    "Luz_Sol_AC03",
):
    remover_objeto(nome)


# Base do parque
bpy.ops.mesh.primitive_plane_add(
    size=20,
    location=(0, 0, -0.15),
)

base = bpy.context.active_object
base.name = "base_parque"
mover_para_colecao(base, colecao)

material_base = criar_material(
    "material_base_parque",
    (0.08, 0.18, 0.12),
    metalico=0.0,
    rugosidade=0.75,
)

atribuir_material(base, material_base)


# Câmera
bpy.ops.object.camera_add(
    location=(11, -15, 13),
)

camera = bpy.context.active_object
camera.name = "Camera_AC03"
camera.data.lens = 50
mover_para_colecao(camera, colecao)

apontar_para(camera, (0, 0, 1))
cena.camera = camera


# Luz principal
bpy.ops.object.light_add(
    type="AREA",
    location=(1, -4, 10),
)

luz_area = bpy.context.active_object
luz_area.name = "Luz_Area_AC03"
luz_area.data.energy = 1300
luz_area.data.shape = "DISK"
luz_area.data.size = 7
mover_para_colecao(luz_area, colecao)

apontar_para(luz_area, (0, 0, 0))


# Luz complementar
bpy.ops.object.light_add(
    type="SUN",
    location=(0, 0, 8),
)

luz_sol = bpy.context.active_object
luz_sol.name = "Luz_Sol_AC03"
luz_sol.data.energy = 1.5
luz_sol.rotation_euler = (
    math.radians(25),
    math.radians(-20),
    math.radians(30),
)

mover_para_colecao(luz_sol, colecao)


# Fundo da cena
cena.world.use_nodes = True
fundo = cena.world.node_tree.nodes.get("Background")

if fundo is not None:
    fundo.inputs["Color"].default_value = (0.025, 0.04, 0.07, 1.0)
    fundo.inputs["Strength"].default_value = 0.35


# Configurações do render
cena.render.engine = "BLENDER_EEVEE_NEXT"
cena.render.resolution_x = 1280
cena.render.resolution_y = 720
cena.render.resolution_percentage = 100
cena.render.image_settings.file_format = "PNG"
cena.render.filepath = "//AC03_JoãoVictorBathomarco.png"

cena.frame_set(120)

print("Câmera, iluminação e base configuradas com sucesso.")