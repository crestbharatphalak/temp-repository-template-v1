from strands import Agent
from strands_tools import calculator

# Create agent with specific configuration
agent = Agent(
    model="us.anthropic.claude-sonnet-4-20250514-v1:0",
    system_prompt="You are a helpful assistant specialized in data analysis.",
    tools=[calculator]
)

# Test with specific queries
response = agent("Analyze this data and create a summary: [Item, Cost 2023, Cost 2024, Cost 2025\n Apple, $0.46, $0.47, $0.55, Banna, $0.40, $0.13, $0.47\n]")
print(str(response))