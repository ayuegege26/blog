import bpy
import math
import os
from mathutils import Vector


ROOT = r"C:\Users\ayuegege26\OneDrive\文档\前端博客 2"
OUT_DIR = os.path.join(ROOT, "public", "assets", "vs002")
BLEND_PATH = os.path.join(OUT_DIR, "vs002-s1-world-blockout.blend")
GLB_PATH = os.path.join(OUT_DIR, "vs002-s1-world-blockout.glb")

os.makedirs(OUT_DIR, exist_ok=True)

# S1 is a spatial blockout: continuous masses and navigation relationships only.
bpy.ops.object.select_all(action="SELECT")
bpy.ops.object.delete(use_global=False)
for collection in list(bpy.data.collections):
    if collection.name != "Collection":
        bpy.data.collections.remove(collection)

root = bpy.context.scene.collection
world_collection = bpy.data.collections.new("WORLD_BLOCKOUT")
root.children.link(world_collection)
marker_collection = bpy.data.collections.new("NAV_MARKERS")
root.children.link(marker_collection)


def material(name, color, metallic=0.25, roughness=0.78):
    mat = bpy.data.materials.new(name)
    mat.diffuse_color = (*color, 1.0)
    mat.metallic = metallic
    mat.roughness = roughness
    return mat


mat_ground = material("S1_Ground", (0.035, 0.095, 0.13), 0.15, 0.92)
mat_core = material("S1_CoreLandmark", (0.18, 0.30, 0.35), 0.55, 0.68)
mat_ring = material("S1_MainRing", (0.10, 0.20, 0.24), 0.48, 0.72)
mat_support = material("S1_Support", (0.16, 0.28, 0.32), 0.42, 0.74)
mat_bridge = material("S1_FloatingBridge", (0.12, 0.29, 0.32), 0.5, 0.62)
mat_float = material("S1_FloatingGroup", (0.12, 0.23, 0.30), 0.44, 0.7)
mat_marker_low = material("S1_MarkerLow", (0.12, 0.52, 0.58), 0.1, 0.5)
mat_marker_mid = material("S1_MarkerMid", (0.23, 0.68, 0.68), 0.1, 0.5)
mat_marker_high = material("S1_MarkerHigh", (0.44, 0.78, 0.74), 0.1, 0.5)


def to_blender(position):
    """Convert desired Three.js Y-up coordinates to Blender Z-up coordinates."""
    x, y, z = position
    return (x, -z, y)


def dimensions_to_blender(dimensions):
    """Convert desired Three.js dimensions to Blender axis order."""
    x, y, z = dimensions
    return (x, z, y)


def move_to_collection(obj, collection):
    for current in list(obj.users_collection):
        current.objects.unlink(obj)
    collection.objects.link(obj)
    return obj


def box(name, location, dimensions, mat, rotation=0.0, collection=world_collection):
    bpy.ops.mesh.primitive_cube_add(location=to_blender(location))
    obj = bpy.context.object
    obj.name = name
    blender_dimensions = dimensions_to_blender(dimensions)
    obj.scale = (blender_dimensions[0] / 2, blender_dimensions[1] / 2, blender_dimensions[2] / 2)
    obj.rotation_euler[2] = rotation
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    obj.data.materials.append(mat)
    move_to_collection(obj, collection)
    return obj


def beam_between(name, start, end, width, height, mat, collection=world_collection):
    start_vec = Vector(to_blender(start))
    end_vec = Vector(to_blender(end))
    direction = end_vec - start_vec
    length = direction.length
    midpoint = (start_vec + end_vec) / 2
    bpy.ops.mesh.primitive_cube_add(location=midpoint)
    obj = bpy.context.object
    obj.name = name
    obj.rotation_mode = "QUATERNION"
    obj.rotation_quaternion = direction.to_track_quat("X", "Z")
    obj.scale = (length / 2, width / 2, height / 2)
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    obj.data.materials.append(mat)
    move_to_collection(obj, collection)
    return obj


def cylinder(name, location, radius, depth, mat, vertices=16, collection=world_collection):
    bpy.ops.mesh.primitive_cylinder_add(vertices=vertices, radius=radius, depth=depth, location=to_blender(location))
    obj = bpy.context.object
    obj.name = name
    obj.data.materials.append(mat)
    move_to_collection(obj, collection)
    return obj


def cone(name, location, radius_bottom, radius_top, depth, mat, vertices=8, rotation=0.0):
    bpy.ops.mesh.primitive_cone_add(vertices=vertices, radius1=radius_bottom, radius2=radius_top, depth=depth, location=to_blender(location), rotation=(0.0, 0.0, rotation))
    obj = bpy.context.object
    obj.name = name
    obj.data.materials.append(mat)
    move_to_collection(obj, world_collection)
    return obj


def torus(name, location, major_radius, minor_radius, mat, major_segments=32, minor_segments=8):
    bpy.ops.mesh.primitive_torus_add(
        major_radius=major_radius,
        minor_radius=minor_radius,
        major_segments=major_segments,
        minor_segments=minor_segments,
        location=to_blender(location),
        # Blender XY exports to the Three.js XZ ground plane.
        rotation=(0.0, 0.0, 0.0),
    )
    obj = bpy.context.object
    obj.name = name
    obj.data.materials.append(mat)
    move_to_collection(obj, world_collection)
    return obj


def empty_marker(name, location, mat, radius=0.5):
    marker = cylinder(name, location, radius, 0.08, mat, vertices=8, collection=marker_collection)
    marker.hide_render = True
    marker["navigation_layer"] = name.split("_")[1].lower()
    return marker


# Ground plane and one continuous main ring footprint.
cylinder("MAP_EXTERNAL_SURFACE", (0.0, -0.45, 0.0), 70.0, 0.8, mat_ground, vertices=64)
cylinder("MAIN_RING_FOUNDATION", (0.0, 1.5, 0.0), 47.0, 2.4, mat_ring, vertices=32)
torus("MAIN_RING_CONTINUOUS", (0.0, 16.0, 0.0), 42.0, 4.5, mat_ring, 32, 8)
torus("MAIN_RING_UPPER_TIER", (0.0, 29.5, 0.0), 34.0, 2.4, mat_support, 32, 6)

# S1.5 structural completion: anchor the main ring to the base and suspend the
# upper tier with a small number of legible load-bearing members.
for index in range(6):
    angle = math.tau / 6 * index + math.pi / 6
    x, z = math.cos(angle) * 42.0, math.sin(angle) * 42.0
    cylinder(f"MAIN_RING_BASE_PYLON_{index:02d}", (x, 8.6, z), 1.8, 13.2, mat_support, vertices=8)

for index in range(6):
    angle = math.tau / 6 * index
    lower = (math.cos(angle) * 42.0, 18.0, math.sin(angle) * 42.0)
    upper = (math.cos(angle) * 34.0, 28.8, math.sin(angle) * 34.0)
    beam_between(f"MAIN_RING_TIER_STRUT_{index:02d}", lower, upper, 3.4, 2.4, mat_support)

# Four short radial spines keep the ring connected to the central landmark.
for index, end in enumerate(((0.0, 16.0, 27.0), (27.0, 16.0, 0.0), (0.0, 16.0, -27.0), (-27.0, 16.0, 0.0))):
    beam_between(f"CORE_RADIAL_SPINE_{index:02d}", (0.0, 16.0, 0.0), end, 3.2, 2.4, mat_support)

# The only primary landmark: a tall, readable server-tower mass.
cylinder("CORE_BASE_COLLAR", (0.0, 3.0, 0.0), 17.5, 3.0, mat_support, vertices=24)
cone("CORE_BASE_SHROUD", (0.0, 6.0, 0.0), 18.0, 14.0, 5.0, mat_ring, vertices=8, rotation=math.pi / 8)
cone("MAIN_SERVER_CORE", (0.0, 25.0, 0.0), 14.0, 7.0, 48.0, mat_core, vertices=8, rotation=math.pi / 8)
cone("MAIN_SERVER_CROWN", (0.0, 53.5, 0.0), 7.0, 3.0, 9.0, mat_support, vertices=8, rotation=math.pi / 8)


def vertical_well(prefix, x, z, scale=1.0):
    cylinder(f"{prefix}_BASE", (x, 5.0, z), 7.0 * scale, 8.0, mat_support, vertices=12)
    cylinder(f"{prefix}_SHAFT", (x, 19.0, z), 4.8 * scale, 20.0, mat_support, vertices=12)
    cone(f"{prefix}_CROWN", (x, 32.0, z), 4.8 * scale, 2.6 * scale, 7.0, mat_ring, vertices=8, rotation=math.pi / 8)


# Secondary regions from the approved top-view layout.
vertical_well("VERTICAL_WELL_A", -42.0, 42.0, 1.0)
vertical_well("VERTICAL_WELL_B", 42.0, -42.0, 0.92)

# Three elevated bridges: every secondary region returns to the main ring.
beam_between("FLOATING_BRIDGE_A", (-29.7, 24.0, 29.7), (-42.0, 31.0, 42.0), 4.0, 2.2, mat_bridge)
beam_between("FLOATING_BRIDGE_B", (29.7, 30.0, 29.7), (50.0, 38.0, 48.0), 4.0, 2.2, mat_bridge)
beam_between("FLOATING_BRIDGE_C", (29.7, 22.0, -29.7), (42.0, 28.0, -42.0), 4.0, 2.2, mat_bridge)

# Bridge landing nodes make each connection read as a structural transfer,
# not as an isolated floating beam.
for name, location, radius in (
    ("BRIDGE_A_RING_DOCK", (-29.7, 24.0, 29.7), 5.2),
    ("BRIDGE_A_WELL_DOCK", (-42.0, 31.0, 42.0), 5.8),
    ("BRIDGE_B_RING_DOCK", (29.7, 30.0, 29.7), 5.0),
    ("BRIDGE_B_FLOAT_DOCK", (50.0, 38.0, 48.0), 6.2),
    ("BRIDGE_C_RING_DOCK", (29.7, 22.0, -29.7), 5.2),
    ("BRIDGE_C_WELL_DOCK", (42.0, 28.0, -42.0), 5.6),
):
    cylinder(name, location, radius, 2.0, mat_bridge, vertices=12)

# One compact floating group in the northeast; it is not a second city.
float_x, float_y, float_z = 50.0, 38.0, 48.0
box("FLOATING_GROUP_PLATFORM", (float_x, float_y, float_z), (20.0, 2.2, 12.0), mat_float, rotation=math.pi / 10)
box("FLOATING_GROUP_BLOCK_A", (float_x - 4.5, float_y + 5.0, float_z + 0.8), (6.0, 8.0, 5.0), mat_float, rotation=math.pi / 10)
box("FLOATING_GROUP_BLOCK_B", (float_x + 4.0, float_y + 3.6, float_z - 1.2), (5.0, 6.0, 6.0), mat_float, rotation=-math.pi / 8)

# Editable navigation markers remain in the .blend but are excluded from GLB.
empty_marker("LAYER_LOW", (0.0, 3.0, 34.0), mat_marker_low, 1.4)
empty_marker("LAYER_MID", (0.0, 24.0, 34.0), mat_marker_mid, 1.1)
empty_marker("LAYER_HIGH", (0.0, 48.0, 34.0), mat_marker_high, 0.8)
empty_marker("PLAYER_START", (-55.0, 4.0, -47.0), mat_marker_low, 1.0)

scene = bpy.context.scene
scene["vs002_stage"] = "S1_STRUCTURE_COMPLETION"
scene["vs002_layout"] = "single_continuous_ring_core_two_wells_floating_group_three_bridges"
scene["vs002_bounds"] = "x/z +-70; y 0.8-61.5"
scene["vs002_assets"] = "procedural_primitives_only; no_external_assets"
scene["vs002_bridge_network"] = "all_secondary_regions_connected_to_main_ring"
scene["vs002_structural_pass"] = "base_pylons_upper_tier_struts_core_collar_bridge_docks"
scene.world.color = (0.04, 0.10, 0.16)

# Export only runtime world geometry; navigation markers stay editable in Blender.
bpy.ops.object.select_all(action="DESELECT")
for obj in world_collection.objects:
    obj.select_set(True)
bpy.context.view_layer.objects.active = next(iter(world_collection.objects))

bpy.ops.wm.save_as_mainfile(filepath=BLEND_PATH)
bpy.ops.export_scene.gltf(filepath=GLB_PATH, export_format="GLB", use_selection=True, export_apply=True)
print(f"S1 blockout saved: {BLEND_PATH}")
print(f"S1 runtime GLB saved: {GLB_PATH}")
