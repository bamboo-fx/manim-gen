from compiler.scenes.array_scene import ArrayScene

def compile_scene(scene_ir):
    if scene_ir.type == "array":
        return ArrayScene(scene_ir.values)
    else:
        raise ValueError(f"Unknown scene type: {scene_ir.type}")
