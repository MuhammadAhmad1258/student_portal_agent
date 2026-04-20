# session.py — Session and runner setup
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from agents.coordinator import coordinator_agent

APP_NAME   = "student_portal"
USER_ID    = "student_1"
SESSION_ID = "session_1"

session_service = InMemorySessionService()
runner = None  # Initialized in create_session_and_runner()

async def create_session_and_runner():
    global runner
    await session_service.create_session(
        app_name=APP_NAME,
        user_id=USER_ID,
        session_id=SESSION_ID,
    )
    runner = Runner(
        agent=coordinator_agent,
        app_name=APP_NAME,
        session_service=session_service,
    )
