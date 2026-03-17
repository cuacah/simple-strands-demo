from strands import Agent, tool
from strands_tools import calculator, current_time, python_repl, file_read, http_request, use_aws

# Create agent
agent = Agent(tools=[calculator, current_time, file_read, http_request, use_aws])

# Simple continuous chat
print("Agent ready! Type 'quit' to exit.")
while True:
    user_input = input("\nYou: ")
    if user_input.lower() in ['quit', 'exit']:
        break
    if user_input.strip():
        agent(user_input)
