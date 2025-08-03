import chainlit as cl
from my_agents.helper_agent import agent, math_agent
from my_agents.weather_agent import weather_agent
from agents import Runner, set_tracing_disabled





# Disable tracing for cleaner output
set_tracing_disabled(True)


@cl.on_chat_start
async def on_chat_start():
    await cl.Message(content="Welcome to the AI Assistant! You can ask about weather, math problems, or general queries.").send()


@cl.on_message
async def on_message(message: cl.Message):
    query = message.content.lower()

    if "weather" in query:
       result = await Runner.run(weather_agent, message.content)
    elif "math" in query:
        result = await Runner.run(math_agent, message.content)
    else:
        result = await Runner.run(agent, message.content)
    
    
    await cl.Message(content=result.final_output).send()

















