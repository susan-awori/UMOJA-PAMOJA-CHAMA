import vertexai
from vertexai.preview import reasoning_engines

PROJECT_ID = "190783044556"
LOCATION = "us-central1"

vertexai.init(project=PROJECT_ID, location=LOCATION)

# Connect to the live resource endpoint that just built
agent_resource = "projects/190783044556/locations/us-central1/reasoningEngines/6897329349771395072"
remote_agent = reasoning_engines.ReasoningEngine(agent_resource)

print("--- Sending Sheng Dispute Query to Mzee Arbitrator ---")
query = "Mzee! Caleb Lema anadai alituma chapaa ya April 2025 on the 5th exact, lakini Treasurer anasema haijaletwa. Nani muongo?"

response = remote_agent.query(input=query)
print("\nMzee's Decision:")
print(response)