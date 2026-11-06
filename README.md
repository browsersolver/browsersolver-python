# BrowserSolver Python SDK

The official Python SDK for the [BrowserSolver](https://www.browsersolver.com) web unlocker API.

Unlock, render, crawl and screenshot any website — anti-bot bypass and technology detection through one API.

The SDK exposes **9 typed methods**, one per documented endpoint, with blocking and `asyncio` clients built on [HTTPX](https://www.python-httpx.org/), plus a generic `request()`.

## Requirements

- Python 3.11 or newer

## Installation

```sh
pip install browsersolver
```

## Get your API key

[Sign up for BrowserSolver](https://app.browsersolver.com/register) or sign in, then copy your API key from the [dashboard](https://app.browsersolver.com). The client reads the `BROWSERSOLVER_API_KEY` environment variable when no key is passed.

## Quick start

```python
import os

from browsersolver import BrowserSolverClient

with BrowserSolverClient(os.environ["BROWSERSOLVER_API_KEY"]) as client:
    response = client.website_webunlocker(query="https://example.com")
    print(response.data)
```

Keyword arguments mirror the [API reference](https://app.browsersolver.com/openapi). Python keywords get a trailing underscore (`from_=`), and the wire name is used on the request.

## Binary responses

Endpoints that can return a file (image, PDF…) return a `JsonResponse` or a `BinaryResponse`:

```python
from browsersolver import BinaryResponse

response = client.website_screenshot(url="https://example.com", format="png")
if isinstance(response, BinaryResponse):
    with open("screenshot.png", "wb") as file:
        file.write(response.bytes)
```

## Async jobs

Any call accepts `is_async: true` (useful past the 60-second server limit): the response is then a `job_id`. `wait_for_job()` polls `GET /v1/jobs/{id}` until the job reaches a terminal status (`CompletedJob`, `Error`, `NotFound`, `BadRequest`):

```python
submitted = client.website_webunlocker(query="https://example.com", is_async=True)
job = client.wait_for_job(
    submitted.data["job_id"],
    on_progress=lambda j: print(j["status"], j.get("progress")),
)
print(job.data)
```

## Async I/O

```python
import asyncio

from browsersolver import AsyncBrowserSolverClient


async def main() -> None:
    async with AsyncBrowserSolverClient() as client:
        response = await client.website_webunlocker(query="https://example.com")
        print(response.data)


asyncio.run(main())
```

## GET or POST

Methods use GET when the endpoint supports it (parameters in the query string). POST sends the same parameters as a JSON body:

```python
from browsersolver import RequestOptions

client.website_crawler(query="https://books.toscrape.com/", request_options=RequestOptions(method="POST"))
```

`None` values are omitted, `False` and `0` are sent, and sequences repeat the parameter name.

## Any endpoint

```python
response = client.request("GET", "/v1/usage")
```

## Errors

```python
from browsersolver import BrowserSolverAPIError

try:
    client.website_webunlocker(query="https://example.com")
except BrowserSolverAPIError as error:
    print(error.status, error, error.response_body)
```

| Error | When |
| --- | --- |
| `BrowserSolverConfigurationError` | Missing API key, invalid options, unsupported method, closed client. |
| `BrowserSolverSerializationError` | A required parameter is missing or a value can't be sent. |
| `BrowserSolverTransportError` | Network failure or timeout. |
| `BrowserSolverAPIError` | Non-2xx status (`status`, `error_message`, `response_body`, `raw_response`). |
| `BrowserSolverResponseDecodingError` | A success response could not be decoded. |

All of them extend `BrowserSolverError`.

## Retries

Requests are retried up to 3 times after a network error, a `408`, `500`, `502`, `503` or `504`, or a rate limit — which the API returns as `401` (or `429`) with a `Rate limit exceeded` message. Per-key quota errors (`…: quota daily`) are not retried, nor are `400`, `402`, `404` or client-side timeouts. The delay starts at 1 second and grows 1.5× per retry (capped at 30 seconds); a `Retry-After` header wins.

```python
client = BrowserSolverClient(max_retries=5, retry_delay=0.5)

# or for one request
client.website_webunlocker(query="https://example.com", request_options=RequestOptions(max_retries=0))
```

## Batch requests

`batch()` runs a function per item on 10 threads (`concurrency`) and returns one `BatchResult` per item, in input order. A failing item never stops the others. `AsyncBrowserSolverClient.batch()` does the same with `asyncio`.

```python
inputs = ["https://example.com", "https://www.browsersolver.com"]
results = client.batch(inputs, lambda query: client.website_webunlocker(query=query), concurrency=5)

for result in results:
    if result.ok:
        print(result.value.data)
    else:
        print(inputs[result.index], result.error)
```

| Constant | Default | Description |
| --- | --- | --- |
| `DEFAULT_CONCURRENCY` | `10` | Tasks run at the same time by batch |
| `DEFAULT_TIMEOUT` | `120.0` | Request timeout (seconds) |
| `MAX_RETRIES` | `3` | Retry attempts after a network error, a 408/5xx or a rate limit |
| `RETRY_BACKOFF_FACTOR` | `1.5` | Exponential backoff multiplier |
| `DEFAULT_RETRY_DELAY` | `1.0` | Delay before the first retry (seconds) |

## Timeouts and custom HTTPX clients

```python
import httpx

from browsersolver import BrowserSolverClient, RequestOptions

client = BrowserSolverClient(timeout=60)  # seconds, default 120, None disables
client.website_webunlocker(query="https://example.com", request_options=RequestOptions(timeout=30))

# Bring your own HTTPX client (proxies, limits, event hooks…). You keep ownership of it.
http_client = httpx.Client(proxy="http://localhost:8080")
client = BrowserSolverClient(http_client=http_client)
```

## Endpoints

9 methods, generated from the [OpenAPI document](https://app.browsersolver.com/openapi).

| Method | HTTP | Description |
| --- | --- | --- |
| `jobs()` | GET `/v1/jobs/{id}` | Poll the status, progress (0–100) and result of a job started with is_async=true. Polling is free. Poll until status is terminal: Completed… |
| `stats()` | GET `/v1/stats` | Infrastructure health for an engine or endpoint over the last hour. Not scoped to your account or tenant. Enabled per account: HTTP 403 mea… |
| `usage()` | GET `/v1/usage` | Retrieve real-time usage statistics and credit balance for your BrowserSolver account. |
| `website_antibot()` | GET `/v1/website/antibot` | Single-pass scan that names the bot-protection vendor in front of a URL so you can choose the right BrowserSolver fetch tier next. |
| `website_crawler()` | GET / POST `/v1/website/crawler` | Fast HTTP pull of public HTML with no browser session. Ideal when the first response already contains the content you need. |
| `website_rendering()` | GET `/v1/website/rendering` | Run a managed browser session against a public URL and collect the HTML after client-side scripts finish. Prefer Crawler for static markup;… |
| `website_screenshot()` | GET / POST `/v1/website/screenshot` | Turn any public URL into a PNG, JPEG, WebP, or PDF asset rendered by BrowserSolver. No local Chromium fleet to operate. |
| `website_technology()` | GET / POST `/v1/website/technology` | Map CMS, frameworks, analytics, CDN, and security tooling exposed by a public URL. Choose simple lists or expert metadata with confidence s… |
| `website_webunlocker()` | GET / POST `/v1/website/webunlocker` | BrowserSolver's highest HTML fetch tier for retail and marketplace hosts on your account whitelist. Solves persistent bot challenges that s… |

## All BrowserSolver SDKs

| SDK | Package | Install |
| --- | --- | --- |
| Node.js | [`@browsersolver/sdk`](https://www.npmjs.com/package/@browsersolver/sdk) | `npm install @browsersolver/sdk` |
| Python | [`browsersolver`](https://pypi.org/project/browsersolver/) | `pip install browsersolver` |
| Go | [`browsersolver-go`](https://pkg.go.dev/github.com/browsersolver/browsersolver-go) | `go get github.com/browsersolver/browsersolver-go` |
| .NET | [`BrowserSolver`](https://www.nuget.org/packages/BrowserSolver) | `dotnet add package BrowserSolver` |
| Ruby | [`browsersolver`](https://rubygems.org/gems/browsersolver) | `gem install browsersolver` |
| PHP | [`browsersolver/sdk`](https://packagist.org/packages/browsersolver/sdk) | `composer require browsersolver/sdk` |
| Java | [`browsersolver-java`](https://github.com/browsersolver/browsersolver-java) | build from source, see its README |
| CLI | [`@browsersolver/cli`](https://www.npmjs.com/package/@browsersolver/cli) | `npm install -g @browsersolver/cli` |
| MCP server | [`@browsersolver/mcp`](https://www.npmjs.com/package/@browsersolver/mcp) | `npx -y @browsersolver/mcp` |

## License

MIT — see [LICENSE](LICENSE).
