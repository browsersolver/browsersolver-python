"""Use the asyncio client."""

import asyncio

from browsersolver import AsyncBrowserSolverClient


async def main() -> None:
    async with AsyncBrowserSolverClient() as client:  # reads BROWSERSOLVER_API_KEY
        response = await client.website_webunlocker(query="https://example.com")
        print(response.data)


asyncio.run(main())
