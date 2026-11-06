"""Call the featured endpoint and print the JSON result."""

import json
import os

from browsersolver import BrowserSolverClient

with BrowserSolverClient(os.environ["BROWSERSOLVER_API_KEY"]) as client:
    response = client.website_webunlocker(query="https://example.com")
    print(json.dumps(response.data, indent=2))
