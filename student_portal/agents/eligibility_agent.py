# eligibility_agent.py — Tells student where they can get in
from google.adk.agents import LlmAgent
from tools.eligibility_tools import get_eligible_universities, get_realistic_chances

eligibility_agent = LlmAgent(
    name="eligibility_agent",
    model="gemini-2.5-flash",
    description="Tells student which universities they are eligible for.",
    instruction="""
    Based on student's aggregate scores, tell them which universities
    they are likely, possibly, or unlikely to get into.
    Compare against last year's closing merits from data/.
    """,
    tools=[get_eligible_universities, get_realistic_chances],
)
