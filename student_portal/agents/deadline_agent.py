# deadline_agent.py — Handles dates, deadlines, test schedules
from google.adk.agents import LlmAgent
from tools.deadline_tools import (
    get_application_deadline,
    get_entry_test_date,
    get_days_remaining,
)

deadline_agent = LlmAgent(
    name="deadline_agent",
    model="gemini-2.0-flash",
    description="Provides deadlines and entry test dates for universities.",
    instruction="""
    Answer questions about application deadlines, entry test dates,
    and days remaining. Always mention if data may be outdated and
    suggest checking the official university website.
    """,
    tools=[get_application_deadline, get_entry_test_date, get_days_remaining],
)
