# helper.py — call_agent_async helper function
from google.genai import types
from runner.session import runner, USER_ID, SESSION_ID

async def call_agent_async(query: str):
    """Wrap query, run agent, extract and return final response."""
    content = types.Content(role="user", parts=[types.Part(text=query)])
    events = runner.run_async(
        user_id=USER_ID,
        session_id=SESSION_ID,
        new_message=content,
    )
    async for event in events:
        if event.is_final_response():
            response = event.content.parts[0].text
            print(f"Agent: {response}")
            return response
