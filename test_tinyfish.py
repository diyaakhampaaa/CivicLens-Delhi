
import os
from dotenv import load_dotenv
from tinyfish import TinyFish

load_dotenv()

api_key = os.getenv("TINYFISH_API_KEY")

if not api_key:
    raise RuntimeError(
        "API key missing. Add TINYFISH_API_KEY to your .env file."
    )

client = TinyFish()

print("Starting TinyFish investigation...")

response = client.agent.run(
    url="https://mcdonline.nic.in/",
    goal=(
        "Find official information about how citizens can report "
        "potholes, damaged roads, garbage or sanitation issues in "
        "Delhi. Return the relevant complaint channels, instructions "
        "and source URLs. Do not submit a complaint. If information "
        "cannot be verified, clearly say so."
    ),
)

print("\nStatus:", response.status)
print("\nResult:")
print(response.result)
