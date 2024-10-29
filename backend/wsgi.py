import asyncio

from api import create_app


async def run_app():
    app = await create_app()
    app.run()


if __name__ == "__main__":
    asyncio.run(run_app())
