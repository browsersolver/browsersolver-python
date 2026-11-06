"""Start an async job and wait for its result."""

from browsersolver import BrowserSolverClient

with BrowserSolverClient() as client:  # reads BROWSERSOLVER_API_KEY
    submitted = client.website_webunlocker(query="https://example.com", is_async=True)
    job = client.wait_for_job(
        submitted.data["job_id"],
        on_progress=lambda j: print(j["status"], j.get("progress")),
    )
    print(job.data)
