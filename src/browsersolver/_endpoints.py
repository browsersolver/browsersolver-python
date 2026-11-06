"""Generated from the BrowserSolver OpenAPI document. Do not edit by hand."""

from __future__ import annotations

from .models import EndpointDefinition

ENDPOINTS: dict[str, EndpointDefinition] = {
    "jobs": EndpointDefinition(
        path="/v1/jobs/{id}",
        methods=("GET",),
        response="json",
        required=("id",),
    ),
    "stats": EndpointDefinition(
        path="/v1/stats",
        methods=("GET",),
        response="json",
        required=(),
    ),
    "usage": EndpointDefinition(
        path="/v1/usage",
        methods=("GET",),
        response="json",
        required=(),
    ),
    "website_antibot": EndpointDefinition(
        path="/v1/website/antibot",
        methods=("GET",),
        response="json",
        required=("query",),
    ),
    "website_crawler": EndpointDefinition(
        path="/v1/website/crawler",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "website_rendering": EndpointDefinition(
        path="/v1/website/rendering",
        methods=("GET",),
        response="json",
        required=("query",),
    ),
    "website_screenshot": EndpointDefinition(
        path="/v1/website/screenshot",
        methods=(
            "GET",
            "POST",
        ),
        response="any",
        required=("url",),
    ),
    "website_technology": EndpointDefinition(
        path="/v1/website/technology",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "website_webunlocker": EndpointDefinition(
        path="/v1/website/webunlocker",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
}
