# run a simple interaction with memgpt
# based on https://memgpt.readme.io/docs/python_client
from memgpt import Admin, create_client

token = "4PpZP-hqJZRWeGGw7Kd1sQ" # replace with your token you get after doing 'memgpt server'
admin = Admin(base_url="http://localhost:8283", token=token)
client = create_client(base_url="http://localhost:8283", token=token)
agent_name = "test-assistant"
human_name = "chris"

agents = client.list_agents().agents

# create agent if not exists
if agent_name not in [agent['name'] for agent in agents]:
    agent = client.create_agent(name = agent_name, persona = "You are a personal assistant and mental health coach that helps the user achieve their goals and live a fulfilled life.",human = human_name) 
    print(f"Created agent {agent_name}")
else:
    agent_id = [agent['id'] for agent in agents if agent['name'] == agent_name][0]
    agent = client.get_agent(agent_id=agent_id)
    print(f"Continuing with {agent_name}")


# Send a message to the agent
messages = client.user_message(agent_id=agent.id, message="Hello, agent!")
# Create a helper that sends a message and prints the assistant response only
def send_message(message: str):
    """
    sends a message and prints the assistant output only.
    :param message: the message to send
    """
    response = client.user_message(agent_id=agent.id, message=message)
    for r in response:
        for m in r[1]:
            if "assistant_message" in m:
                print("ASSISTANT:", m["assistant_message"])
            elif "internal_monologue" in m:
                print("THOUGHTS:", m["internal_monologue"])

# Send a message and see the response
send_message("Please introduce yourself and tell me about your abilities!")