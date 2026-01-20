from manim import *

class AlgorithmScene(Scene):
    def setup_array(self, values):
        self.values = values

        self.boxes = VGroup(*[
            Square().scale(0.6).set_stroke(WHITE)
            for _ in values
        ]).arrange(RIGHT, buff=0.2)

        self.labels = VGroup(*[
            Text(str(v)).scale(0.5)
            for v in values
        ])

        for box, label in zip(self.boxes, self.labels):
            label.move_to(box.get_center())

        self.play(Create(self.boxes), Write(self.labels))
        self.wait(0.5)
