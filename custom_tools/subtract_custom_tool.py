from my_schema.subtract_tool_schema import SubtractSchema
from agents import RunContextWrapper, FunctionTool
from dataclasses import dataclass
from pydantic import BaseModel
from instructions.dynamic_instruction import en


@dataclass
class User(BaseModel):
    name:str
    id:int
    age:int



async def subtract(ctx:RunContextWrapper,agrs):
    """subtract ka function hay"""
    print("subtract tool fire =========>")
    obj = SubtractSchema.model_validate_json(agrs)
    return f"your answer is {obj.n1-obj.n2}"



subtract = FunctionTool(
    name="subtract",
    description="subtract ka function hay",
    params_json_schema=SubtractSchema.model_json_schema(), # # model_json_schema ye paydantic ki waja se aaya hy 
        # on_invoke_tool ye tool ko invoke karega ya function ko invoke karega
    on_invoke_tool=subtract,
    # is_enabled=True, # ye tool ko enable karega ya disable karega
    is_enabled=en
)