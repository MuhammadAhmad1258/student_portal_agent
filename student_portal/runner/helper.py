# helper.py — call_agent_async helper function
from google.genai import types
from runner.session import USER_ID, SESSION_ID, session_service
from agents.coordinator import coordinator_agent
from google.adk.runners import Runner

runner = None

async def call_agent_async(query: str):
    global runner
    if runner is None:
        runner = Runner(
            agent=coordinator_agent,
            app_name="student_portal",
            session_service=session_service,
        )
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
