"""Call any path with request() and handle API errors."""

from browsersolver import BrowserSolverAPIError, BrowserSolverClient, JsonResponse

with BrowserSolverClient() as client:  # reads BROWSERSOLVER_API_KEY
    try:
        response = client.request("GET", "/v1/usage")
        if isinstance(response, JsonResponse):
            print(response.data)
    except BrowserSolverAPIError as error:
        print(f"HTTP {error.status}: {error}")
