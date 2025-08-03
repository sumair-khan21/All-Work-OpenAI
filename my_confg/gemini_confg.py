from decouple import config
from agents import AsyncOpenAI,OpenAIChatCompletionsModel


my_key = config('GEMINI_API_KEY')
base_url = config('BASE_URL')

# asynchronous banane k liye use hota hay AsyncOpenAI
# ye ek client banata hay jo gemini api ke liye use hota hay
client = AsyncOpenAI(api_key=my_key, base_url=base_url)


# Ye ek model wrapper class hai jo gpt-3.5, gpt-4, ya kisi OpenAI chat model ko agent ke liye enable karta hai.
MODEL_ONE = OpenAIChatCompletionsModel(model="gemini-2.0-flash",openai_client=client)
MODEL_TWO = OpenAIChatCompletionsModel(model="gemini-2.5-flash",openai_client=client)







