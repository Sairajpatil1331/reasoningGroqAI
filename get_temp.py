import os
import json
import requests
from dotenv import load_dotenv
from groq import Groq


load_dotenv()
client = Groq()


def fetch_local_weather(location):
    """Fetches real-time, live weather data from the open internet."""
    print(f"\n⚙️  PYTHON EXECUTING: Reaching out to live satellites for {location}...")
    try:
        geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={location}&count=1&language=en&format=json"
        geo_response = requests.get(geo_url).json()

        if "results" not in geo_response:
            return json.dumps({"error": "City not found on Earth."})

        lat = geo_response["results"][0]["latitude"]
        lon = geo_response["results"][0]["longitude"]

        weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
        weather_response = requests.get(weather_url).json()

        current_temp = weather_response["current_weather"]["temperature"]

        real_data = {
            "location": location,
            "temperature_celsius": current_temp,
            "data_source": "Live Open-Meteo Satellite",
        }
        print(f"📡 DATA SECURED: {current_temp}°C")
        return json.dumps(real_data)

    except Exception as e:
        print(f"❌ API ERROR: {e}")
        return json.dumps({"error": "Failed to connect to weather database."})


tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get current temperature for a given location.",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {"type": "string", "description": "City and country"}
                },
                "required": ["location"],
            },
        },
    }
]

print("==================================================")
print("🌤️  LIVE WEATHER AI AGENT ONLINE")
print("Type 'quit' or 'exit' to shut down the agent.")
print("==================================================\n")

conversation_history = []

while True:
    # This is what pauses the script and waits for you to type!
    user_input = input("You: ")

    if user_input.lower() in ["quit", "exit"]:
        print("Shutting down Agent. Goodbye!")
        break

    conversation_history.append({"role": "user", "content": user_input})

    response1 = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=conversation_history,
        tools=tools,
        tool_choice="auto",
    )

    ai_message = response1.choices[0].message

    if ai_message.tool_calls:
        tool_request = ai_message.tool_calls[0]
        conversation_history.append(ai_message)

        arguments = json.loads(tool_request.function.arguments)

        real_weather_data = fetch_local_weather(arguments["location"])

        # Send data back to the AI
        conversation_history.append(
            {
                "tool_call_id": tool_request.id,
                "role": "tool",
                "name": tool_request.function.name,
                "content": real_weather_data,
            }
        )

        response2 = client.chat.completions.create(
            model="llama-3.3-70b-versatile", messages=conversation_history
        )
        final_answer = response2.choices[0].message.content
        print(f"\n🤖 AI: {final_answer}\n")

        conversation_history.append({"role": "assistant", "content": final_answer})

    else:
        # If the AI didn't need a tool (like if you just said "Hello")
        print(f"\n🤖 AI: {ai_message.content}\n")
        conversation_history.append(
            {"role": "assistant", "content": ai_message.content}
        )
