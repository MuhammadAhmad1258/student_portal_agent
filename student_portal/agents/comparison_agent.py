# comparison_agent.py — Side by side university comparison
from google.adk.agents import LlmAgent
from tools.comparison_tools import compare_universities, get_fee_structure

comparison_agent = LlmAgent(
    name="comparison_agent",
    model="gemini-2.5-flash",
    description="Compares two universities side by side.",
    instruction="""
    Compare universities on: fee structure, location, programs,
    closing merit, hostel availability, and general reputation.
    Be balanced and factual.
    """,
    tools=[compare_universities, get_fee_structure],
)
