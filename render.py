import json
from compiler.ir_schema import VideoIR
from compiler.compiler import compile_scene

def main():
    with open("examples/bubble_sort.json") as f:
        ir = VideoIR(**json.load(f))

    scene = compile_scene(ir.scenes[0])
    scene.render()

if __name__ == "__main__":
    main()