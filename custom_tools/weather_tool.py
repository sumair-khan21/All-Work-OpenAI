from agents import function_tool


@function_tool
def weather(city: str) -> str:
    print("weather tool fired ==========>")
    """ Fetches the current weather for a given city."""
    return f"The current weather in {city} is sunny with a temperature of 25°C." 