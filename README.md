# Manim-Gen

A compiler-based system for generating Manim animations from algorithm descriptions. Define algorithms using JSON input and automatically generate educational visualization videos.

## Features

- **Declarative Input**: Describe algorithms using simple JSON schemas
- **Modular Architecture**: Extensible compiler system for adding new algorithms
- **Manim Integration**: Leverages Manim for high-quality mathematical animations
- **Type-Safe**: Uses Pydantic for input validation and type checking

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd manim-gen
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Ensure Manim is properly configured (see [Manim documentation](https://docs.manim.community/) for system-specific setup).

## Usage

### Basic Example

Create a JSON file describing your algorithm visualization:

```json
{
  "topic": "bubble_sort",
  "input": [5, 1, 4, 2]
}
```

Run the render script:

```bash
python render.py
```

This will generate a Manim animation visualizing the bubble sort algorithm on the input array `[5, 1, 4, 2]`.

### Example Files

See `examples/bubble_sort.json` for a complete example.

## Project Structure

```
manim-gen/
├── compiler/
│   ├── algorithms/          # Algorithm implementations
│   │   ├── bubble_sort.py   # Bubble sort step generator
│   │   └── __init__.py
│   ├── scenes/              # Manim scene definitions
│   │   ├── base_algo.py     # Base algorithm scene class
│   │   ├── bubble_sort_scene.py
│   │   ├── compare_scene.py
│   │   └── swap_scene.py
│   ├── compiler.py          # Main compiler logic
│   └── ir_schema.py         # Input schema definitions
├── examples/                # Example JSON inputs
│   └── bubble_sort.json
├── render.py                # Main entry point
└── requirements.txt         # Python dependencies
```

## Architecture

### Compiler Pipeline

1. **Input**: JSON file describing algorithm and input data
2. **IR Schema**: Pydantic model validates and structures the input
3. **Algorithm Module**: Generates step-by-step operations (e.g., compare, swap)
4. **Scene Compiler**: Converts steps into Manim scene objects
5. **Output**: Rendered Manim animation

### Adding New Algorithms

To add support for a new algorithm:

1. **Define the IR schema** in `compiler/ir_schema.py`:
```python
class VideoIR(BaseModel):
    topic: Literal["bubble_sort", "your_algorithm"]
    input: List[int]
```

2. **Implement the algorithm** in `compiler/algorithms/your_algorithm.py`:
```python
def your_algorithm_steps(arr):
    # Generate list of step dictionaries
    # Each step should have a "type" field
    return steps
```

3. **Create scene components** in `compiler/scenes/`:
   - Base scene class or extend `AlgorithmScene`
   - Scene-specific operations (e.g., compare, swap, insert)

4. **Update the compiler** in `compiler/compiler.py`:
```python
def compile_video(ir):
    if ir.topic == "your_algorithm":
        steps = your_algorithm_steps(ir.input)
        return YourAlgorithmScene(steps=steps, values=ir.input)
    # ...
```

## Development

### Code Style

- Files should end with a newline (POSIX compliance)
- Type hints are encouraged
- Follow PEP 8 style guidelines

### Testing

Run the render script with example inputs to verify functionality:

```bash
python render.py
```

## Dependencies

- `manim`: Mathematical animation engine
- `pydantic`: Data validation and settings management

## License

[Add your license here]

## Contributing

[Add contribution guidelines here]


