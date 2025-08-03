from agents import RunContextWrapper


def dynamic_instruction(ctx:RunContextWrapper,agent):
    print("dynamic instruction fired =============>")
    return f"User name is {ctx.context["name"]}, you are helpful assistant"



async def en(ctx:RunContextWrapper,agent):
    print("enable tool =========>")
    if ctx.context["age"] > 18:
        return False
    return True