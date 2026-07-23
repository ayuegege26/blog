import bpy
import math
import os
from mathutils import Vector


ROOT = r"C:\Users\ayuegege26\OneDrive\文档\前端博客 2"
BASE_BLEND = os.path.join(ROOT, "public", "assets", "vs002", "vs002-s1-world-blockout.blend")
OUT_DIR = os.path.join(ROOT, "public", "assets", "vs002", "formal")
BLEND_PATH = os.path.join(OUT_DIR, "vs002-s2-formal-core-pass.blend")
GLB_PATH = os.path.join(OUT_DIR, "vs002-s2-formal-core-pass.glb")
os.makedirs(OUT_DIR, exist_ok=True)

bpy.ops.wm.open_mainfile(filepath=BASE_BLEND)
root = bpy.context.scene.collection
detail_collection = bpy.data.collections.get("S2_FORMAL_DETAIL_PASS") or bpy.data.collections.new("S2_FORMAL_DETAIL_PASS")
if detail_collection.name not in root.children:
    root.children.link(detail_collection)


def to_blender(position):
    x, y, z = position
    return (x, -z, y)


def dimensions_to_blender(dimensions):
    x, y, z = dimensions
    return (x, z, y)


def move_to_detail(obj):
    for collection in list(obj.users_collection):
        collection.objects.unlink(obj)
    detail_collection.objects.link(obj)
    return obj


def material(name, color, metallic=0.78, roughness=0.48, emission=None, emission_strength=0.0):
    mat = bpy.data.materials.get(name) or bpy.data.materials.new(name)
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


mat_detail = material("S2_Formal_ColdShell", (0.085, 0.16, 0.19), 0.86, 0.42)
mat_rib = material("S2_Formal_StructuralRib", (0.045, 0.10, 0.13), 0.9, 0.36)
mat_inset = material("S2_Formal_CyanInset", (0.015, 0.075, 0.085), 0.62, 0.34, (0.08, 0.60, 0.62), 1.1)
mat_band = material("S2_Formal_CyanBand", (0.02, 0.09, 0.10), 0.72, 0.32, (0.10, 0.46, 0.50), 0.62)


def box(name, location, dimensions, mat, rotation=0.0):
    bpy.ops.mesh.primitive_cube_add(location=to_blender(location))
    obj = bpy.context.object
    obj.name = name
    dims = dimensions_to_blender(dimensions)
    obj.scale = (dims[0] / 2, dims[1] / 2, dims[2] / 2)
    obj.rotation_euler[2] = rotation
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    obj.data.materials.append(mat)
    move_to_detail(obj)
    return obj


def torus(name, location, major_radius, minor_radius, mat, major_segments=16, minor_segments=5):
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
    move_to_detail(obj)
    return obj


def annular_shell(name, location, outer_radius, inner_radius, height, mat, segments=32):
    """Create a closed, planar ring shell around the existing rounded ring."""
    cx, cy, cz = location
    vertices = []
    for y in (cy - height / 2, cy + height / 2):
        for radius in (outer_radius, inner_radius):
            for index in range(segments):
                angle = math.tau * index / segments
                vertices.append(to_blender((cx + math.cos(angle) * radius, y, cz + math.sin(angle) * radius)))

    outer_bottom = 0
    inner_bottom = segments
    outer_top = segments * 2
    inner_top = segments * 3
    faces = []
    for index in range(segments):
        nxt = (index + 1) % segments
        faces.extend(
            (
                (outer_bottom + index, outer_bottom + nxt, outer_top + nxt, outer_top + index),
                (inner_bottom + index, inner_top + index, inner_top + nxt, inner_bottom + nxt),
                (outer_top + index, outer_top + nxt, inner_top + nxt, inner_top + index),
                (outer_bottom + index, inner_bottom + index, inner_bottom + nxt, outer_bottom + nxt),
            )
        )
    mesh = bpy.data.meshes.new(f"{name}_MESH")
    mesh.from_pydata(vertices, [], faces)
    mesh.update()
    obj = bpy.data.objects.new(name, mesh)
    detail_collection.objects.link(obj)
    obj.data.materials.append(mat)
    return obj


def frustum(name, location, radius_bottom, radius_top, height, mat, vertices=8, rotation=0.0):
    bpy.ops.mesh.primitive_cone_add(
        vertices=vertices,
        radius1=radius_bottom,
        radius2=radius_top,
        depth=height,
        location=to_blender(location),
    )
    obj = bpy.context.object
    obj.name = name
    obj.rotation_euler[2] = rotation
    obj.data.materials.append(mat)
    move_to_detail(obj)
    return obj


def beam_between(name, start, end, width, height, mat):
    sx, sy, sz = to_blender(start)
    ex, ey, ez = to_blender(end)
    direction = Vector((ex - sx, ey - sy, ez - sz))
    midpoint = Vector((sx + ex, sy + ey, sz + ez)) / 2
    bpy.ops.mesh.primitive_cube_add(location=midpoint)
    obj = bpy.context.object
    obj.name = name
    obj.rotation_mode = "QUATERNION"
    obj.rotation_quaternion = direction.to_track_quat("X", "Z")
    obj.scale = (direction.length / 2, width / 2, height / 2)
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    obj.data.materials.append(mat)
    move_to_detail(obj)
    return obj


def local_offset(center_x, center_z, local_x, local_z, rotation):
    cos_a = math.cos(rotation)
    sin_a = math.sin(rotation)
    return (
        center_x + local_x * cos_a - local_z * sin_a,
        center_z + local_x * sin_a + local_z * cos_a,
    )


def detail_ribs(prefix, center_x, center_z, radius, y, height, count, material_ref):
    for index in range(count):
        angle = math.tau / count * index
        x = center_x + math.cos(angle) * radius
        z = center_z + math.sin(angle) * radius
        box(f"{prefix}_{index:02d}", (x, y, z), (0.68, height, 1.25), material_ref, rotation=angle)


# Hero landmark: preserve the S1 silhouette and add only structural segmentation.
detail_ribs("S2_CORE_RIB_LOWER", 0.0, 0.0, 13.0, 24.0, 37.0, 8, mat_rib)
detail_ribs("S2_CORE_RIB_UPPER", 0.0, 0.0, 8.8, 45.0, 18.0, 8, mat_rib)
detail_ribs("S2_CORE_PANEL_LOWER", 0.0, 0.0, 12.85, 24.0, 34.0, 8, mat_detail)
detail_ribs("S2_CORE_PANEL_UPPER", 0.0, 0.0, 8.65, 45.0, 15.0, 8, mat_detail)
for index, (height, radius) in enumerate(((10.0, 14.4), (29.0, 11.8), (48.0, 7.8))):
    torus(f"S2_CORE_BAND_{index:02d}", (0.0, height, 0.0), radius, 0.20 if index == 1 else 0.15, mat_band)
for index in range(4):
    angle = math.tau / 4 * index
    x, z = math.cos(angle) * 11.55, math.sin(angle) * 11.55
    box(f"S2_CORE_INSET_{index:02d}", (x, 29.0, z), (0.20, 18.0, 0.92), mat_inset, rotation=angle)
box("S2_CORE_DOCK_DETAIL", (0.0, 25.0, 14.0), (8.0, 1.0, 4.8), mat_detail)

# Northwest vertical well sample.
detail_ribs("S2_WELL_A_RIB", -42.0, 42.0, 5.2, 19.0, 17.0, 4, mat_rib)
torus("S2_WELL_A_BAND_LOW", (-42.0, 10.0, 42.0), 6.0, 0.16, mat_band, 12, 4)
torus("S2_WELL_A_BAND_HIGH", (-42.0, 28.0, 42.0), 4.9, 0.14, mat_band, 12, 4)

# Extend the approved language to the remaining formal subjects without adding
# new masses or changing the S1.5 layout.
torus("S2_MAIN_RING_EDGE_BAND", (0.0, 16.0, 0.0), 42.0, 0.22, mat_band, 24, 5)
torus("S2_UPPER_RING_EDGE_BAND", (0.0, 29.5, 0.0), 34.0, 0.14, mat_band, 24, 4)
annular_shell("S2_MAIN_RING_OUTER_SHELL", (0.0, 16.0, 0.0), 45.8, 38.2, 2.8, mat_detail, 32)
annular_shell("S2_UPPER_RING_OUTER_SHELL", (0.0, 29.5, 0.0), 36.4, 31.6, 2.0, mat_detail, 32)
# Six shallow service nodes align with the S1.5 pylons. They read as a
# deliberate ring module rhythm instead of scattered protruding fragments.
for index in range(6):
    angle = math.tau / 6 * index + math.pi / 6
    x, z = math.cos(angle) * 45.6, math.sin(angle) * 45.6
    box(
        f"S2_MAIN_RING_SERVICE_NODE_{index:02d}",
        (x, 16.0, z),
        (3.6, 1.8, 1.15),
        mat_rib,
        rotation=angle + math.pi / 2,
    )
    inset_x, inset_z = math.cos(angle) * 46.2, math.sin(angle) * 46.2
    box(
        f"S2_MAIN_RING_SERVICE_INSET_{index:02d}",
        (inset_x, 16.05, inset_z),
        (1.8, 0.48, 0.18),
        mat_band,
        rotation=angle + math.pi / 2,
    )

detail_ribs("S2_WELL_B_RIB", 42.0, -42.0, 4.8, 19.0, 16.0, 4, mat_rib)
torus("S2_WELL_B_BAND_LOW", (42.0, 10.0, -42.0), 5.5, 0.15, mat_band, 12, 4)
torus("S2_WELL_B_BAND_HIGH", (42.0, 27.0, -42.0), 4.4, 0.13, mat_band, 12, 4)
for label, x, z, scale in (("A", -42.0, 42.0, 1.0), ("B", 42.0, -42.0, 0.92)):
    cylinder_radius = 5.22 * scale
    bpy.ops.mesh.primitive_cylinder_add(
        vertices=16,
        radius=cylinder_radius,
        depth=19.0,
        location=to_blender((x, 19.0, z)),
    )
    sleeve = bpy.context.object
    sleeve.name = f"S2_WELL_{label}_OUTER_SLEEVE"
    sleeve.data.materials.append(mat_detail)
    move_to_detail(sleeve)

float_x, float_y, float_z = 50.0, 38.0, 48.0
float_rotation = math.pi / 10

# A compact suspended chassis gives the floating group a legible underside and
# keeps it in the same restrained structural language as the tower and wells.
box("S2_FLOAT_UNDERSIDE_SLAB", (float_x, float_y - 1.55, float_z), (14.0, 1.0, 8.0), mat_rib, rotation=float_rotation)
frustum("S2_FLOAT_SUSPENSION_HUB", (float_x, float_y - 3.15, float_z), 4.4, 3.1, 2.8, mat_detail, 8, float_rotation)
for brace_index, (local_x, local_z) in enumerate(((-6.8, -3.7), (6.8, -3.7), (-6.8, 3.7), (6.8, 3.7))):
    brace_x, brace_z = local_offset(float_x, float_z, local_x, local_z, float_rotation)
    beam_between(
        f"S2_FLOAT_UNDERSIDE_BRACE_{brace_index:02d}",
        (float_x, float_y - 2.2, float_z),
        (brace_x, float_y - 1.0, brace_z),
        0.52,
        0.52,
        mat_rib,
    )
for name, local_x, local_z, dims in (
    ("FRONT", 0.0, -5.45, (17.5, 0.55, 0.42)),
    ("BACK", 0.0, 5.45, (17.5, 0.55, 0.42)),
    ("LEFT", -9.45, 0.0, (0.42, 0.55, 10.2)),
    ("RIGHT", 9.45, 0.0, (0.42, 0.55, 10.2)),
):
    trim_x, trim_z = local_offset(float_x, float_z, local_x, local_z, float_rotation)
    box(f"S2_FLOAT_PLATFORM_{name}_TRIM", (trim_x, float_y + 0.45, trim_z), dims, mat_detail, rotation=float_rotation)

# Roof caps and narrow facade ribs break the two blocks into readable modules
# without turning the group into a second landmark.
block_specs = (
    ("A", float_x - 4.5, float_y + 5.0, float_z + 0.8, math.pi / 10, 6.0, 8.0, 5.0),
    ("B", float_x + 4.0, float_y + 3.6, float_z - 1.2, -math.pi / 8, 5.0, 6.0, 6.0),
)
for label, center_x, center_y, center_z, rotation, width, height, depth in block_specs:
    box(
        f"S2_FLOAT_BLOCK_{label}_ROOF_CAP",
        (center_x, center_y + height / 2 + 0.22, center_z),
        (width + 0.5, 0.44, depth + 0.5),
        mat_detail,
        rotation=rotation,
    )
    for face_name, face_sign in (("FRONT", -1.0), ("BACK", 1.0)):
        for rib_index, local_x in enumerate((-width * 0.28, width * 0.28)):
            rib_x, rib_z = local_offset(center_x, center_z, local_x, face_sign * (depth / 2 + 0.10), rotation)
            box(
                f"S2_FLOAT_BLOCK_{label}_{face_name}_RIB_{rib_index:02d}",
                (rib_x, center_y, rib_z),
                (0.34, height * 0.72, 0.20),
                mat_rib,
                rotation=rotation,
            )
        inset_x, inset_z = local_offset(center_x, center_z, 0.0, face_sign * (depth / 2 + 0.13), rotation)
        box(
            f"S2_FLOAT_BLOCK_{label}_{face_name}_INSET",
            (inset_x, center_y, inset_z),
            (width * 0.36, height * 0.42, 0.16),
            mat_inset,
            rotation=rotation,
        )

bridge_specs = (
    ("A", (-29.7, 24.0, 29.7), (-42.0, 31.0, 42.0)),
    ("B", (29.7, 30.0, 29.7), (50.0, 38.0, 48.0)),
    ("C", (29.7, 22.0, -29.7), (42.0, 28.0, -42.0)),
)
for label, start, end in bridge_specs:
    direction_x = end[0] - start[0]
    direction_z = end[2] - start[2]
    length = math.sqrt(direction_x * direction_x + direction_z * direction_z)
    normal_x = -direction_z / length
    normal_z = direction_x / length
    offset_x = normal_x * 1.72
    offset_z = normal_z * 1.72
    # A centered underside keel and two transverse ties make the bridge read as
    # a suspended technical structure without increasing its deck footprint.
    beam_between(
        f"S2_BRIDGE_{label}_UNDERSIDE_KEEL",
        (start[0], start[1] - 1.45, start[2]),
        (end[0], end[1] - 1.45, end[2]),
        1.65,
        0.72,
        mat_rib,
    )
    for tie_index, t in enumerate((0.34, 0.67)):
        center_x = start[0] + direction_x * t
        center_y = start[1] + (end[1] - start[1]) * t - 1.38
        center_z = start[2] + direction_z * t
        beam_between(
            f"S2_BRIDGE_{label}_CROSS_TIE_{tie_index:02d}",
            (center_x - normal_x * 1.9, center_y, center_z - normal_z * 1.9),
            (center_x + normal_x * 1.9, center_y, center_z + normal_z * 1.9),
            0.42,
            0.42,
            mat_detail,
        )
    beam_between(
        f"S2_BRIDGE_{label}_HIGH_EDGE",
        (start[0] + offset_x, start[1] + 1.05, start[2] + offset_z),
        (end[0] + offset_x, end[1] + 1.05, end[2] + offset_z),
        0.22,
        0.92,
        mat_band,
    )
    beam_between(
        f"S2_BRIDGE_{label}_LOW_CURB",
        (start[0] - offset_x, start[1] + 0.58, start[2] - offset_z),
        (end[0] - offset_x, end[1] + 0.58, end[2] - offset_z),
        0.20,
        0.30,
        mat_detail,
    )

# Refine the oversized S1.5 landing discs in place. They remain structural
# transfer points, but no longer dominate the bridge silhouette.
for dock_name in ("BRIDGE_A_RING_DOCK", "BRIDGE_B_RING_DOCK", "BRIDGE_C_RING_DOCK"):
    dock = bpy.data.objects.get(dock_name)
    if dock:
        dock.scale.x *= 0.78
        dock.scale.y *= 0.78
for dock_name in ("BRIDGE_A_WELL_DOCK", "BRIDGE_B_FLOAT_DOCK", "BRIDGE_C_WELL_DOCK"):
    dock = bpy.data.objects.get(dock_name)
    if dock:
        dock.scale.x *= 0.86
        dock.scale.y *= 0.86

scene = bpy.context.scene
scene["vs002_stage"] = "S2_FORMAL_SHELL_PASS"
scene["vs002_s2_scope"] = "core_wells_ring_floating_group_bridge_detail_and_outer_shell"
scene["vs002_s2_revision"] = "gate_2b_shell_pass"
scene["vs002_s2_assets"] = "procedural_blender_detail_on_s1_5_blockout"
scene["vs002_formal_asset"] = True

# Export the frozen S1.5 world plus the new S2 detail collection; markers remain blend-only.
bpy.ops.object.select_all(action="DESELECT")
for collection in (bpy.data.collections.get("WORLD_BLOCKOUT"), detail_collection):
    if collection:
        for obj in collection.objects:
            obj.select_set(True)
bpy.context.view_layer.objects.active = next(iter(bpy.data.collections["WORLD_BLOCKOUT"].objects))

bpy.ops.wm.save_as_mainfile(filepath=BLEND_PATH)
bpy.ops.export_scene.gltf(filepath=GLB_PATH, export_format="GLB", use_selection=True, export_apply=True)
print(f"Formal S2 core pass saved: {BLEND_PATH}")
print(f"Formal S2 core pass GLB saved: {GLB_PATH}")
