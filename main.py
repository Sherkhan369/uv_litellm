import os
from dotenv import load_dotenv
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel
load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")

provider = AsyncOpenAI(
    api_key = gemini_api_key,
    base_url = "https://generativelanguage.googleapis.com/v1beta/openai",
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client= provider
)

agent = Agent(
    name= "Greetig Agent",
    instructions = """
You are a greeting agent. Your task is to greet users based on their input:
- If the user says 'hi', 'hello', or any greeting, reply with: 'Salam from Sher Khan!'
- If the user says anything else (but not a greeting), reply with: 'How can I assist you?'
- If the user asks a question not related to greetings, reply with: 'I am just a greeting agent.'
"""
,
    model= model
)

input_value = input("How Can I Assist You Today? ")
result = Runner.run_sync(
    agent, input_value
)

print(result.final_output)


