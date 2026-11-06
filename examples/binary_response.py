"""Save a binary response to a file."""

import os

from browsersolver import BinaryResponse, BrowserSolverClient

with BrowserSolverClient(os.environ["BROWSERSOLVER_API_KEY"]) as client:
    response = client.website_screenshot(url="https://example.com", format="png")
    if isinstance(response, BinaryResponse):
        with open("screenshot.png", "wb") as file:
            file.write(response.bytes)
        print(f"Saved screenshot.png ({response.content_type}, {len(response.bytes)} bytes)")
    else:
        print(response.data)
