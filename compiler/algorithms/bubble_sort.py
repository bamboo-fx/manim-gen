def bubble_sort_steps(arr):
    arr = arr.copy()
    steps = []

    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            steps.append({
                "type": "compare",
                "i": j,
                "j": j + 1
            })

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                steps.append({
                    "type": "swap",
                    "i": j,
                    "j": j + 1
                })

    return steps
