from agents import Runner, set_tracing_disabled,SQLiteSession
from my_agents.helper_agent import agent
from my_agents.weather_agent import weather_agent
from my_agents.handoff_agent import triage_agent
import asyncio
from openai.types.responses import ResponseTextDeltaEvent

# from agents.helpers import ItemHelpers
# 
set_tracing_disabled(True)
# enable_verbose_stdout_logging()

# ===============================================================================================
# SIMPLE HELPER AGENT RUNNER
# res = Runner.run_sync(agent, "What is the capital of France?")
# print(res.final_output)

# ===============================================================================================
# SIMPLE MATH AGENT RUNNER
# result = Runner.run_sync(math_agent, "What is 10 + 10?")
# result = Runner.run_sync(math_agent, "What is 20 * 20? give me detailed answer.")
# print(result.final_output)

# ===============================================================================================
# SIMLPE WEATHER AGENT RUNNER
# result = Runner.run_sync(weather_agent, "What is the current weather in Karachi?")
# print(result.final_output)

# ===============================================================================================
# SIMPLE PYDANTIC AGENT RUNNER
# result = Runner.run_sync(agent, "My name is Ali, I am 22 years old and my email is ali@gmail.com")
# print(result.final_output)

# result = Runner.run_sync(math_agent, "plus karo 200 ko 100 se")
# print(result.final_output)


# ===============================================================================================
# SIMPLE HANDOFF AGENT RUNNER

# result = Runner.run_sync(triage_agent, "Mujhe Python mein loop banana hai, help karo or get me the weather in karachi")
# print(result.final_output)
# print("last agent=============>",result.last_agent)

# ===============================================================================================
# STREAMING AGENT RUNNER WITH DETAILS OUTPUT

# async def run_streaming_agent():
#     result = await Runner.streamed(triage_agent, input="I need help with a python problem and also get me the weather in karachi and also need with javascript problem")
 
#     async for event in result.stream_events():
#      if event.type == "raw_response_event" and isinstance(event.data, ResponseTextDeltaEvent):
#         # print("output",event.data.delta)

#         continue
#      elif event.type == "agent_updated_stream_event":
#         print(event)
#         continue
#             #  jb koi pora action perform hoga ya events
#      elif event.type == "run_item_stream_event":
#         # print(event)
#         if event.item.type == "message_output_item":
#                 print(ItemHelpers.text_message_output(event.item))

     


#     asyncio.run(run_streaming_agent())
#     print("last_agent ===========>",result.last_agent)
#     print("result.final_output ===========>",result.final_output)


# =====================================================================================
# STREAMING AGENT RUNNER WITH SIMPLE OUTPUT
# res = Runner.run_sync(triage_agent, "mujhe python mai nested if k baray mai bta do or javascript mai nested if k baray mai bta do")
# print(res.final_output)



# async def main():
#     res= Runner.run_streamed(
#         starting_agent=triage_agent, 
#         input="javascript mein nested if k baray mai bta do")
#     async for event in res.stream_events():
#         if event.type == "raw_response_event" and isinstance(event.data,ResponseTextDeltaEvent ):
#             print("output=============>",event.data.delta)

#     print("Last Agent>>>>>",res.last_agent)
#     print("Final Output>>>>>",res.final_output)


# asyncio.run(main())


# ===========================================================================================
# SIMPLE CUSTOM TOOL CALL


# res =  Runner.run_sync(
#     starting_agent=agent,
#     input="200-100=?",
#     context={"name":"atma raam", "age":2, "role":"teacher"}

# )



# print(res.final_output)


# ===========================================================================================
# simple last agent , to_input_list practice
# res = Runner.run_sync(agent, "what is the weather of karachi?")
# print("Final Output:", res.final_output)
# # print("Last Agent:", res.last_agent)
# print("To Input List:", res.to_input_list())


# ============================================================================================
# simple to input list practice

# async def main():
#     prompt = input("Enter your prompt: ")
#     res = await Runner.run(agent,prompt)
#     print("Final Output:", res.final_output)
    
#     prompt = input("Enter your next prompt: ")
#     new_prompt = res.to_input_list() + [{"role": "user", "content": prompt}]
#     res = await Runner.run(agent, new_prompt)
#     print("Final Output:", res.final_output)
    
    
# if __name__ == "__main__":
#     asyncio.run(main())
    
    
    
async def main():
    my_session = SQLiteSession("mysession.1234", "my_conversation.db")
    prompt = input("Enter your prompt: ")
    res = await Runner.run(agent, prompt, session=my_session)
    print("Final Output:", res.final_output)
    
    prompt = input("Enter your next prompt: ")
    res = await Runner.run(agent, prompt, session=my_session)
    print("Final Output:", res.final_output)
    print("last agent======>", res.last_agent)
    
    
if __name__ == "__main__":
    asyncio.run(main())

