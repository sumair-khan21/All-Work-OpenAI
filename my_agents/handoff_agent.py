from my_confg.gemini_confg import MODEL_ONE
from agents import Agent,handoff,function_tool
from agents.extensions import handoff_filters


@function_tool
def get_weather(city:str):
    print("weather tool===================> ")
    return f"The weather in {city} is sunny and the temperature is 30 degree celsius"



javascript_agent = Agent(
    name= "javascript agent",
    instructions= "you are a javascript agent, you are designed to assist with javascript programming tasks and provide solutions.",
    model=MODEL_ONE,
)

# def custom_description(tool_name:str):
#     return f"This is a custom description for the {tool_name} tool"


def on_handoff_function(context):
    print("on_handoff_function===================> ")
    print(context)

python_agent = Agent(
    name= "python agent",
    instructions= "you are a python agent, you are designed to assist with python programming tasks and provide solutions.",
    model=MODEL_ONE,
)

python_handoff = handoff(
    agent=python_agent,
    tool_name_override="handoff_to_python_agent",
    input_filter=handoff_filters.remove_all_tools,
    # tool_description_override=custom_description,
    on_handoff=on_handoff_function
)


triage_agent = Agent(
    name= "triage agent",
    instructions = "you are a triage agent, you are designed to triage the user's request and determine which agent to hand off to.",
    model=MODEL_ONE,
    handoffs=[javascript_agent, 
    # python_agent
    python_handoff
    ],
    tools=[get_weather]
)




