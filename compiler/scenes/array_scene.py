from manim import *

class ArrayScene(Scene):
    def __init__(self, values):
        super().__init__()
        self.values = values

    def construct(self):
        boxes = VGroup(*[
            Square().scale(0.6).set_stroke(WHITE)
            for _ in self.values
        ]).arrange(RIGHT, buff=0.2)

        labels = VGroup(*[
            Text(str(v)).scale(0.5)
            for v in self.values
        ])

        for box, label in zip(boxes, labels):
            label.move_to(box.get_center())

        self.play(Create(boxes), Write(labels))
        self.wait(1)

