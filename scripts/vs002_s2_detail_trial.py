import bpy
import math
import os


ROOT = r"C:\Users\ayuegege26\OneDrive\文档\前端博客 2"
OUT_DIR = os.path.join(ROOT, "public", "assets", "vs002", "experiments")
BLEND_PATH = os.path.join(OUT_DIR, "vs002-s2-core-detail-trial.blend")
GLB_PATH = os.path.join(OUT_DIR, "vs002-s2-core-detail-trial.glb")
os.makedirs(OUT_DIR, exist_ok=True)

bpy.ops.object.select_all(action="SELECT")
bpy.ops.object.delete(use_global=False)
for collection in list(bpy.data.collections):
    if collection.name != "Collection":
        bpy.data.collections.remove(collection)

trial_collection = bpy.data.collections.new("S2_DETAIL_TRIAL")
bpy.context.scene.collection.children.link(trial_collection)


def to_blender(position):
    x, y, z = position
    return (x, -z, y)


def dimensions_to_blender(dimensions):
    x, y, z = dimensions
    return (x, z, y)


def move_to_trial(obj):
    for collection in list(obj.users_collection):
        collection.objects.unlink(obj)
    trial_collection.objects.link(obj)
    return obj


def material(name, color, metallic, roughness, emission=None, emission_strength=0.0):
    mat = bpy.data.materials.new(name)
    mat.diffuse_color = (*color, 1.0)
    mat.metallic = metallic
    mat.roughness = roughness
    mat.use_nodes = True
    bsdf = mat.node_tree.nodes.get("Principled BSDF")
    if bsdf:
        bsdf.inputs["Base Color"].default_value = (*color, 1.0)
        bsdf.inputs["Metallic"].default_value = metallic
        bsdf.inputs["Roughness"].default_value = roughness
        emission_input = bsdf.inputs.get("Emission Color") or bsdf.inputs.get("Emission")
        strength_input = bsdf.inputs.get("Emission Strength")
        if emission and emission_input:
            emission_input.default_value = (*emission, 1.0)
        if strength_input:
            strength_input.default_value = emission_strength
    return mat


mat_base = material("TRIAL_Base", (0.025, 0.055, 0.070), 0.78, 0.58)
mat_shell = material("TRIAL_ColdShell", (0.075, 0.145, 0.175), 0.86, 0.42)
mat_shell_light = material("TRIAL_ColdShellLight", (0.13, 0.24, 0.27), 0.76, 0.48)
mat_rib = material("TRIAL_StructuralRib", (0.055, 0.12, 0.15), 0.9, 0.36)
mat_inset = material("TRIAL_CyanInset", (0.015, 0.08, 0.09), 0.62, 0.34, (0.08, 0.62, 0.62), 1.25)
mat_ring = material("TRIAL_CyanRing", (0.02, 0.10, 0.11), 0.7, 0.32, (0.10, 0.55, 0.56), 0.72)


def box(name, location, dimensions, mat, rotation=0.0):
    bpy.ops.mesh.primitive_cube_add(location=to_blender(location))
    obj = bpy.context.object
    obj.name = name
    dims = dimensions_to_blender(dimensions)
    obj.scale = (dims[0] / 2, dims[1] / 2, dims[2] / 2)
    obj.rotation_euler[2] = rotation
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    obj.data.materials.append(mat)
    move_to_trial(obj)
    return obj


def cylinder(name, location, radius, depth, mat, vertices=8):
    bpy.ops.mesh.primitive_cylinder_add(vertices=vertices, radius=radius, depth=depth, location=to_blender(location))
    obj = bpy.context.object
    obj.name = name
    obj.data.materials.append(mat)
    move_to_trial(obj)
    return obj


def cone(name, location, radius_bottom, radius_top, depth, mat, vertices=8, rotation=0.0):
    bpy.ops.mesh.primitive_cone_add(
        vertices=vertices,
        radius1=radius_bottom,
        radius2=radius_top,
        depth=depth,
        location=to_blender(location),
        rotation=(0.0, 0.0, rotation),
    )
    obj = bpy.context.object
    obj.name = name
    obj.data.materials.append(mat)
    move_to_trial(obj)
    return obj


def torus(name, location, major_radius, minor_radius, mat, major_segments=8, minor_segments=4):
    bpy.ops.mesh.primitive_torus_add(
        major_radius=major_radius,
        minor_radius=minor_radius,
        major_segments=major_segments,
        minor_segments=minor_segments,
        location=to_blender(location),
    )
    obj = bpy.context.object
    obj.name = name
    obj.data.materials.append(mat)
    move_to_trial(obj)
    return obj


# One focused hero-tower experiment. This is intentionally not the formal map.
cylinder("TRIAL_BASE_PLINTH", (0.0, 1.0, 0.0), 19.0, 2.0, mat_base, vertices=12)
cylinder("TRIAL_BASE_STEP", (0.0, 3.0, 0.0), 16.8, 2.0, mat_shell, vertices=12)
cone("TRIAL_CORE_LOWER", (0.0, 15.5, 0.0), 15.0, 11.2, 23.0, mat_shell, vertices=8, rotation=math.pi / 8)
cone("TRIAL_CORE_UPPER", (0.0, 38.0, 0.0), 11.2, 6.4, 22.0, mat_shell_light, vertices=8, rotation=math.pi / 8)
cone("TRIAL_CORE_CROWN", (0.0, 54.5, 0.0), 6.4, 2.4, 11.0, mat_shell, vertices=8, rotation=math.pi / 8)
cylinder("TRIAL_CROWN_CAP", (0.0, 60.5, 0.0), 2.7, 1.0, mat_ring, vertices=8)

# Structural ribs test whether vertical segmentation can add scale without 3A density.
for index in range(8):
    angle = math.tau / 8 * index
    x, z = math.cos(angle) * 12.6, math.sin(angle) * 12.6
    box(f"DETAIL_RIB_LOWER_{index:02d}", (x, 18.0, z), (0.72, 26.0, 1.45), mat_rib, rotation=angle)

for index in range(8):
    angle = math.tau / 8 * index
    x, z = math.cos(angle) * 8.7, math.sin(angle) * 8.7
    box(f"DETAIL_RIB_UPPER_{index:02d}", (x, 40.0, z), (0.55, 21.0, 1.15), mat_rib, rotation=angle)

# Four restrained emissive insets provide a cold technical rhythm.
for index in range(4):
    angle = math.tau / 4 * index
    x, z = math.cos(angle) * 11.45, math.sin(angle) * 11.45
    box(f"DETAIL_INSET_{index:02d}", (x, 31.0, z), (0.22, 18.0, 1.0), mat_inset, rotation=angle)

# Three low-segment bands establish detail density and provide proximity feedback targets.
for index, (height, radius) in enumerate(((9.0, 14.4), (29.0, 11.8), (48.0, 7.7))):
    torus(f"DETAIL_RING_{index:02d}", (0.0, height, 0.0), radius, 0.24 if index == 1 else 0.18, mat_ring)

# One exterior docking ledge tests how detail meets a future bridge connection.
box("TRIAL_DOCKING_LEDGE", (0.0, 25.0, 13.0), (8.0, 1.1, 5.5), mat_shell_light)
box("DETAIL_DOCK_LIGHT", (0.0, 25.65, 15.15), (5.2, 0.12, 0.18), mat_inset)

scene = bpy.context.scene
scene["vs002_stage"] = "S2_DETAIL_TRIAL"
scene["vs002_scope"] = "core_tower_ribs_insets_bands_single_dock"
scene["vs002_formal_asset"] = False
scene["vs002_coordinate_contract"] = "Three.js Y-up converted to Blender Z-up"
scene.world.color = (0.025, 0.07, 0.11)

bpy.ops.object.select_all(action="DESELECT")
for obj in trial_collection.objects:
    obj.select_set(True)
bpy.context.view_layer.objects.active = next(iter(trial_collection.objects))

bpy.ops.wm.save_as_mainfile(filepath=BLEND_PATH)
bpy.ops.export_scene.gltf(filepath=GLB_PATH, export_format="GLB", use_selection=True, export_apply=True)
print(f"S2 detail trial saved: {BLEND_PATH}")
print(f"S2 detail trial GLB saved: {GLB_PATH}")
