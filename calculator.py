_operations = {
    "+": (lambda x, y: x + y),
    "-": (lambda x, y: x - y)
}

def perform_operation(operation: str):
    first, operator, second = operation.split(" ")
    return _operations[operator](int(first), int(second))
