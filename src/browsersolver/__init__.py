"""Official Python SDK for the BrowserSolver API."""

from ._endpoints import ENDPOINTS
from ._version import __version__
from .client import (
    DEFAULT_BASE_URL,
    DEFAULT_CONCURRENCY,
    DEFAULT_RETRY_DELAY,
    DEFAULT_TIMEOUT,
    MAX_RETRIES,
    RETRY_BACKOFF_FACTOR,
    AsyncBrowserSolverClient,
    BrowserSolverClient,
)
from .errors import (
    BrowserSolverAPIError,
    BrowserSolverConfigurationError,
    BrowserSolverError,
    BrowserSolverJobTimeoutError,
    BrowserSolverResponseDecodingError,
    BrowserSolverSerializationError,
    BrowserSolverTransportError,
)
from .models import (
    APIResponse,
    BatchResult,
    BinaryResponse,
    EndpointDefinition,
    HTTPMethod,
    JsonResponse,
    RawResponse,
    RequestOptions,
)

__all__ = [
    "APIResponse",
    "AsyncBrowserSolverClient",
    "BatchResult",
    "BinaryResponse",
    "DEFAULT_BASE_URL",
    "DEFAULT_CONCURRENCY",
    "DEFAULT_RETRY_DELAY",
    "DEFAULT_TIMEOUT",
    "MAX_RETRIES",
    "RETRY_BACKOFF_FACTOR",
    "ENDPOINTS",
    "EndpointDefinition",
    "HTTPMethod",
    "JsonResponse",
    "RawResponse",
    "RequestOptions",
    "BrowserSolverAPIError",
    "BrowserSolverClient",
    "BrowserSolverConfigurationError",
    "BrowserSolverError",
    "BrowserSolverJobTimeoutError",
    "BrowserSolverResponseDecodingError",
    "BrowserSolverSerializationError",
    "BrowserSolverTransportError",
    "__version__",
]
