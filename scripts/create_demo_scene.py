import bpy
import random
    

def create_sphere(location, radius=1.0, name="Sphere"):
    """Create a UV sphere at given location
    
    Args:
        location (tuple): (x, y, z) world coordinates.
        radius (float): Sphere radius. Defaults to 1.0
        name (str): Sphere name. Defaults to "Sphere"
    
    Returns:
        bpy.types.Object: The created sphere object.
    """
    bpy.ops.mesh.primitive_uv_sphere_add(location=location, radius=radius)
    obj = bpy.context.active_object
    obj.name = name
    
    return obj

def apply_material(obj, base_color_rgb, metallic, roughness, alpha=1.0, name="Material"):
    """ Apply material to provided object
    
    Args:
        obj (bpy.types.Object): mesh to which material apply to
        base_color_rgb (tuple): (r, g, b , a) RGB color
        metallic (float): metallic surface strength of material
        roughness (float): roughness surface strength of material
        alpha (float): Alpha of base color
        name (string): material name. Defaults to "Material"
        
    Returns:
        bpy.types.Object: The object with applied material
    """
    material = bpy.data.materials.new(name)
    material.use_nodes = True
    bsdf = material.node_tree.nodes["Principled BSDF"]
    bsdf.inputs["Base Color"].default_value = base_color_rgb + (alpha, )
    bsdf.inputs["Metallic"].default_value = metallic
    bsdf.inputs["Roughness"].default_value = roughness

    obj.data.materials.append(material)
    
    return obj
            
    
def create_demo_scene(sphere_count=6, spacing=2.0, clear_scene=True):
    """Create a demo scene with spheres.
    
    Args:
        sphere_count (int): number of spheres to create. Defaults to 6
        spacing (float): distance between spheres. Defaults to 2.0
        clear_scene (bool): indicates if the scene will be cleared before creation of spheres. Defaults to True
    
    Returns:
        None
    """
    if clear_scene:
        bpy.ops.object.select_all(action='SELECT')
        bpy.ops.object.delete()
    for i in range(0, sphere_count):
        cord_xyz = spacing * i
        location = (cord_xyz, cord_xyz, cord_xyz)
        sphere = create_sphere(location)
        
        base_color = (random.random(),random.random(),random.random())
        metallic = random.random()
        roughness = random.random()
        apply_material(sphere, base_color, metallic, roughness)
        
    
if __name__ == "__main__":
    create_demo_scene()
    