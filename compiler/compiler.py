from compiler.algorithms.bubble_sort import bubble_sort_steps
from compiler.scenes.bubble_sort_scene import BubbleSortScene

def compile_video(ir):
    if ir.topic == "bubble_sort":
        steps = bubble_sort_steps(ir.input)
        return BubbleSortScene(
            steps=steps,
            values=ir.input
        )

    else:
        raise ValueError(f"Unknown topic: {ir.topic}")

