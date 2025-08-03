from agents import function_tool


@function_tool
def add(a: int, b:int) -> int:
    print("tool fire ==========>")
    """add two numbes."""
    return a + b



@function_tool
def multiply(a: int, b:int) -> int:
    print("multiplay tool ========>")
    """multtiply two numbers."""
    return a * b
