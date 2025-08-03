from agents import Agent, ModelSettings
from my_confg.gemini_confg import MODEL_ONE, MODEL_TWO
from custom_tools.weather_tool import weather

weather_agent = Agent(
    name= "weather agent",
    instructions= "you are a weather agent, you are designed to provide current weather information for any city.",
    model=MODEL_ONE,
    tools=[weather],
    tool_use_behavior="run_llm_again"
    # tool_use_behavior="stop_on_first_tool"
    # model_settings=ModelSettings(tool_choice="none"),
)