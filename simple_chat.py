from strands import Agent, tool
from strands_tools import use_aws, file_write

SYSTEM_PROMPT = """
YOU ARE A HELPFUL AND EXPERIENCED SRE AGENT THAT WILL CONVERSE WITH USER ABOUT THEIR AWS PROBLEM.
"""
# Create agent
agent = Agent(tools=[use_aws, file_write], system_prompt=SYSTEM_PROMPT)

# Simple continuous chat
print("Agent ready! Type 'quit' to exit.")
while True:
    user_input = input("\nYou: ")
    if user_input.lower() in ['quit', 'exit']:
        break
    if user_input.strip():
        agent(user_input)
