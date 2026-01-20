from manim import *

def compare(scene, i, j):
    box_i = scene.boxes[i]
    box_j = scene.boxes[j]

    scene.play(
        box_i.animate.set_stroke(YELLOW, width=4),
        box_j.animate.set_stroke(YELLOW, width=4),
        run_time=0.6
    )

    scene.wait(0.3)

    scene.play(
        box_i.animate.set_stroke(WHITE, width=2),
        box_j.animate.set_stroke(WHITE, width=2),
        run_time=0.6
    )
