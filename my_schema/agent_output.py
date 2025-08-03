# from pydantic import BaseModel

# class MyDataOutput(BaseModel):
#     name: str
#     age: int
#     email: str
    
#     response: str = "Thank you for your input!"



# class MathOutput(BaseModel):
#     n1: int
#     n2: int
#     response: str = "Thank you"


# structure + validate

# ==================================================================================================
# from dataclasses import dataclass

# @dataclass
# class MyDataOutput:
#     name: str
#     age: int
#     email: str
    
#     response: str = "Thank you for your input!"
    
# @dataclass
# class MathOutput:
#     n1: int
#     n2: int
#     response: str = "Thank you for your input!"

# just structured

# ==================================================================================================
# custom class


# class MyDataOutput:
#     def __init__(self, name:str, age: int, email:str):
#        self.name = name
#        self.age = age
#        self.email = str
    
    
#     response: str = "Thanks"