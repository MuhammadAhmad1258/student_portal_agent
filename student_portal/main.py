import asyncio
from runner.session import create_session_and_runner
from runner.helper import call_agent_async

async def main():
    await create_session_and_runner()
    print("Student Portal ready! Type your query.")
    while True:
        query = input("You: ")
        if query.lower() in ("exit", "quit"):
            break
        await call_agent_async(query)

if __name__ == "__main__":
    asyncio.run(main())
