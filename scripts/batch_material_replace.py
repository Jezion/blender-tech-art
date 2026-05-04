import bpy
import logging
from material_utils import apply_material


def batch_material_replace(base_color, metallic, roughness, material_name="Material", alpha=1.0):
    """Replaces material on all selected mesh objects with a new one. All material slots are deleted and a new one is
    created. If a mesh has no material slots, a new one is created. Objects are taken from 
    bpy.context.selected_objects (if none are selected function returns (0, 0) and prints a warning).
    Non-mesh objects are skipped
    
    Args:
        base_color (tuple): (r, g, b) material RGB color
        metallic (float): material surface metallic value
        roughness (float): material surface roughness value
        material_name (str): material name. If not provided name is "Material". If "MAT_Stone",
            name is "MAT_Stone". Blender appends .001, .002 etc. on subsequent calls
        alpha (float): alpha of material base color. Defaults to 1.0
        
    Returns:
        tuple[int, int]: (objects_updated, slots_replaced) - number of updated meshes and total material 
            slots removed before replacement
    """
    objects = bpy.context.selected_objects
    objects_updated = 0
    slots_replaced = 0
    if not objects:
        logging.warning("No objects selected")
        return (objects_updated, slots_replaced)
    for obj in objects:
        if obj.type != "MESH":
            logging.info(f"Skipping non-mesh object: {obj.name} (type={obj.type})")
            continue
        material_slots_num = len(obj.material_slots)
        obj.data.materials.clear()
        obj = apply_material(obj, base_color, metallic, roughness, alpha=alpha, name=material_name)
        objects_updated += 1
        slots_replaced += material_slots_num

    logging.info(f"objects updated: {objects_updated}, slots replaced: {slots_replaced}")
    return (objects_updated, slots_replaced)

if __name__ == '__main__':
    batch_material_replace((0.2,0.2,0.2), 0, 0, "MAT_Stone")