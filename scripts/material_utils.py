import bpy

def apply_material(obj, base_color, metallic, roughness, alpha=1.0, name="Material"):
    """ Applies material to provided object
    
    Args:
        obj (bpy.types.Object): object to which material apply to
        base_color (tuple): (r, g, b) RGB color, float values
        metallic (float): material metallic surface value
        roughness (float): material roughness surface value
        alpha (float): Alpha of base color
        name (str): material name. Defaults to "Material"
        
    Returns:
        bpy.types.Object: The object with applied material
    """
    material = bpy.data.materials.new(name)
    material.use_nodes = True
    bsdf = material.node_tree.nodes["Principled BSDF"]
    bsdf.inputs["Base Color"].default_value = base_color + (alpha, )
    bsdf.inputs["Metallic"].default_value = metallic
    bsdf.inputs["Roughness"].default_value = roughness

    obj.data.materials.append(material)
    
    return obj