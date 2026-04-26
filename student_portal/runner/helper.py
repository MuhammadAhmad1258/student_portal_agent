# helper.py — call_agent_async helper function
from google.genai import types
import runner.session as session # Import the session module

async def call_agent_async(query: str):
    # Access the shared runner from the session module
    if session.runner is None:
        raise RuntimeError("Runner not initialized. Call create_session_and_runner() first.")
        
    content = types.Content(role="user", parts=[types.Part(text=query)])
    events = session.runner.run_async(
        user_id=session.USER_ID,
        session_id=session.SESSION_ID,
        new_message=content,
    )
    async for event in events:
        if event.is_final_response():
            response = event.content.parts[0].text
            print(f"Agent: {response}")
            return response
