def get_before_after_pairs():
    return pairs

pairs = {}
pairs["bpy"] = ("context", "data", "ops", "types", "utils", "path", "app", "props")
pairs["data"] = ("actions", "armatures", "brushes", "cameras", "curves", "filepath", "fonts", "grease_pencil", "groups", "images", "is_dirty", "is_saved", "lamps", "lattices", 
    "libraries", "linestyles", "masks", "materials", "meshes", "metaballs", "movieclips", "node_groups", "objects", "particles", "scenes", "screens", "scripts", "shape_keys",
    "sounds", "speakers", "texts", "textures", "use_autopack", "window_manager", "worlds")
pairs["types"] = ("Panel", "Operator", "Menu")
pairs["context"] = ("active_object", "selected_objects", "scene", "world", "mesh", "material")