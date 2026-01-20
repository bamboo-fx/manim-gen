from manim import *

def swap(scene, i, j):
    box_i, box_j = scene.boxes[i], scene.boxes[j]
    label_i, label_j = scene.labels[i], scene.labels[j]

    scene.play(
        box_i.animate.shift(RIGHT * 0.8),
        box_j.animate.shift(LEFT * 0.8),
        label_i.animate.shift(RIGHT * 0.8),
        label_j.animate.shift(LEFT * 0.8),
        run_time=0.8
    )

    scene.boxes[i], scene.boxes[j] = scene.boxes[j], scene.boxes[i]
    scene.labels[i], scene.labels[j] = scene.labels[j], scene.labels[i]
