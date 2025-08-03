from agents import Agent, ModelSettings
from my_confg.gemini_confg import MODEL_ONE,MODEL_TWO
from custom_tools.basic_tool import add, multiply
from custom_tools.weather_tool import weather
from custom_tools.subtract_custom_tool import subtract
# from my_schema.agent_output import MyDataOutput, MathOutput
from instructions.dynamic_instruction import dynamic_instruction


# ===============================================================================================
# SIMPLE HELPER AGENT
# Agent ek AI assistant bananay wali class hai jo tumhare diye hue rules aur model ke sath kaam karta hai.
# agentka paramter 
# name – Agent ka unique naam.

# instructions – Agent ko diya gaya system prompt ya behavior guide.

# model – AI model ka naam (e.g., "gpt-4o", "o3-mini").

# model_settings – Model ke settings jaise temperature, max_tokens.

# tools – Functions ya tools jo agent use kar sakta hai.

# handoffs – Doosre agents jinko yeh agent kaam de sakta hai.

# output_type – Expected structured output ka type (e.g., dataclass).

# prompt – Custom ya dynamic prompt template.

# input_guardrails – Input validate karne wale rules/functions.

# output_guardrails – Output validate karne wale rules/functions.

# hooks – Custom event handlers (e.g., on_start, on_finish).

# metadata – Optional custom metadata for debugging or tracking.

# description – Agent ka short description (mostly for docs/UI).



# agent = Agent(
#     name= "helper_agent", 
#     instructions="This agent is designed to assist with various tasks and provide helpful information.", 
#     model=MODEL_ONE,
#     # output_type=MyDataOutput
#     )

# ===============================================================================================
# SIMPLE MATH AGENT

# math_agent = Agent(
#     name="math agent", 
#     instructions= "you are a math agent, you are designed to solve math problems and provide the answer in a concise and easy to understand way.", 
#     model=MODEL_ONE,
#     # output_type=MathOutput,
#     tools=[add, multiply],
#     # model_settings=ModelSettings(tool_choice="none"),
#     # tool_use_behavior="required",  # some time model ki waja se errors ata hai
#     tool_use_behavior="run_llm_again"
    
#     )



# ===============================================================================================
# custom tool agent 


# agent = Agent(
#     name="helper agent",
#     instructions=dynamic_instruction,
#     model=MODEL_ONE,
#     tools=[subtract]
#     )

# print(agent.tools)


# ===============================================================================================

agent = Agent(
    name = "helper agent",
    instructions="you are the heplful agent.",
    model=MODEL_TWO,
    tools=[weather],
    tool_use_behavior="run_llm_again",
    # context = {"name":"atma raam"}
)






















