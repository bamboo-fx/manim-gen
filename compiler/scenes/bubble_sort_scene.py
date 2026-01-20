from compiler.scenes.base_algo import AlgorithmScene
from compiler.scenes.compare_scene import compare
from compiler.scenes.swap_scene import swap

class BubbleSortScene(AlgorithmScene):
    def __init__(self, steps, values):
        super().__init__()
        self.steps = steps
        self.initial_values = values

    def construct(self):
        self.setup_array(self.initial_values)

        for step in self.steps:
            if step["type"] == "compare":
                compare(self, step["i"], step["j"])
            elif step["type"] == "swap":
                swap(self, step["i"], step["j"])
