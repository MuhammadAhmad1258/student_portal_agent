# coordinator.py — Root agent, routes all queries to sub-agents
from google.adk.agents import LlmAgent

coordinator_agent = LlmAgent(
    name="coordinator",
    model="gemini-2.0-flash",
    description="Main coordinator for the Student Admission Portal.",
    instruction="""
    You are the main agent for a Pakistani university admission portal.
    Route the user query to the correct sub-agent:
    - Profile questions → profile_agent
    - Merit/aggregate calculation → merit_agent
    - Eligibility (where can I get in) → eligibility_agent
    - Deadlines and dates → deadline_agent
    - University comparison → comparison_agent
    - Live/current info → search_agent
    Only handle admissions-related queries. Politely decline anything else.
    """,
    sub_agents=[],  # Import and add sub-agents here
)
