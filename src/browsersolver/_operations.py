"""Generated from the BrowserSolver OpenAPI document. Do not edit by hand."""

from __future__ import annotations

from collections.abc import Sequence
from typing import Any, Literal, cast

from .models import APIResponse, JsonResponse, RequestOptions


class _SyncOperations:
    """Generated BrowserSolver endpoint methods."""

    __slots__ = ()

    def _call(
        self, name: str, params: dict[str, Any], options: RequestOptions | None
    ) -> APIResponse:
        raise NotImplementedError

    def jobs(
        self,
        *,
        id: str,
        request_options: RequestOptions | None = None,
    ) -> JsonResponse:
        """Jobs. Poll the status, progress (0–100) and result of a job started with is_async=true. Polling is free. Poll until status is terminal: CompletedJob, Error, NotFound or BadRequest.

        ``GET /v1/jobs/{id}``

        Args:
            id: The job_id returned by an endpoint called with is_async=true.
        """
        return cast(JsonResponse, self._call("jobs", {"id": id}, request_options))

    def stats(
        self,
        *,
        engine: str | None = None,
        path: str | None = None,
        request_options: RequestOptions | None = None,
    ) -> JsonResponse:
        """Stats. Infrastructure health for an engine or endpoint over the last hour. Not scoped to your account or tenant. Enabled per account: HTTP 403 means contact support to activate it.

        ``GET /v1/stats``

        Args:
            engine: API family to check, for example website. Provide at least engine or path.
            path: Specific endpoint to check, for example /v1/website/screenshot. If you also pass engine, use an endpoint from that API.
        """
        return cast(
            JsonResponse, self._call("stats", {"engine": engine, "path": path}, request_options)
        )

    def usage(
        self,
        *,
        request_options: RequestOptions | None = None,
    ) -> JsonResponse:
        """Usage. Retrieve real-time usage statistics and credit balance for your BrowserSolver account.

        ``GET /v1/usage``
        """
        return cast(JsonResponse, self._call("usage", {}, request_options))

    def website_antibot(
        self,
        *,
        query: str,
        timeout: int | float | None = None,
        fields: str | None = None,
        is_async: bool | None = None,
        soft_fail: bool | None = None,
        request_options: RequestOptions | None = None,
    ) -> JsonResponse:
        """Website Antibot. Single-pass scan that names the bot-protection vendor in front of a URL so you can choose the right BrowserSolver fetch tier next. Credit cost: 1 credit per call.

        ``GET /v1/website/antibot``

        Args:
            query: Full URL or bare domain to scan for bot-protection vendors.
            timeout: Upper bound for waiting on the target HTTP response, expressed in seconds (defaults to 15).
            fields: Comma-separated list of fields to keep in the response, with dot notation for nested fields (e.g. name,location.city). Does not change the credit cost.
            is_async: Process the request asynchronously: the response is a job_id to poll on /v1/jobs/{id} (see waitForJob).
            soft_fail: Return HTTP 200 even when an error occurs; the error is then in the response body.
        """
        return cast(
            JsonResponse,
            self._call(
                "website_antibot",
                {
                    "query": query,
                    "timeout": timeout,
                    "fields": fields,
                    "is_async": is_async,
                    "soft_fail": soft_fail,
                },
                request_options,
            ),
        )

    def website_crawler(
        self,
        *,
        query: str,
        allow_redirects: bool | None = None,
        return_page_source: bool | None = None,
        fields: str | None = None,
        is_async: bool | None = None,
        soft_fail: bool | None = None,
        request_options: RequestOptions | None = None,
    ) -> JsonResponse:
        """Website Crawler. Fast HTTP pull of public HTML with no browser session. Ideal when the first response already contains the content you need. Credit cost: 1 credit per call.

        ``GET / POST /v1/website/crawler``

        Args:
            query: Public URL to retrieve with the Crawler tier (plain HTTP, no JavaScript). Include http:// or https://.
            allow_redirects: Whether BrowserSolver should chase HTTP redirects for this fetch.
            return_page_source: Choose between processed markup and the exact bytes from the origin.
            fields: Comma-separated list of fields to keep in the response, with dot notation for nested fields (e.g. name,location.city). Does not change the credit cost.
            is_async: Process the request asynchronously: the response is a job_id to poll on /v1/jobs/{id} (see waitForJob).
            soft_fail: Return HTTP 200 even when an error occurs; the error is then in the response body.
        """
        return cast(
            JsonResponse,
            self._call(
                "website_crawler",
                {
                    "query": query,
                    "allow_redirects": allow_redirects,
                    "return_page_source": return_page_source,
                    "fields": fields,
                    "is_async": is_async,
                    "soft_fail": soft_fail,
                },
                request_options,
            ),
        )

    def website_rendering(
        self,
        *,
        query: str,
        wait_in_seconds: int | float | None = None,
        wait_for: str | None = None,
        block_ads: bool | None = None,
        timeout: int | float | None = None,
        fields: str | None = None,
        is_async: bool | None = None,
        soft_fail: bool | None = None,
        request_options: RequestOptions | None = None,
    ) -> JsonResponse:
        """Website Rendering. Run a managed browser session against a public URL and collect the HTML after client-side scripts finish. Prefer Crawler for static markup; escalate to WebUnlocker on approved hosts when challenges persist. Credit cost: 2 credits per call.

        ``GET /v1/website/rendering``

        Args:
            query: Public URL to load inside BrowserSolver's headless browser. Include http:// or https://.
            wait_in_seconds: Extra pause, in seconds, after the page load event before BrowserSolver returns HTML. Helpful when widgets animate or hydrate late.
            wait_for: CSS or XPath selector that must appear in the DOM before HTML is returned. The managed browser waits until the node exists (or until timeout).
            block_ads: Skip ad-network requests while the page renders.
            timeout: Hard ceiling, in seconds, for the render session. When reached, BrowserSolver returns whatever HTML is available.
            fields: Comma-separated list of fields to keep in the response, with dot notation for nested fields (e.g. name,location.city). Does not change the credit cost.
            is_async: Process the request asynchronously: the response is a job_id to poll on /v1/jobs/{id} (see waitForJob).
            soft_fail: Return HTTP 200 even when an error occurs; the error is then in the response body.
        """
        return cast(
            JsonResponse,
            self._call(
                "website_rendering",
                {
                    "query": query,
                    "wait_in_seconds": wait_in_seconds,
                    "wait_for": wait_for,
                    "block_ads": block_ads,
                    "timeout": timeout,
                    "fields": fields,
                    "is_async": is_async,
                    "soft_fail": soft_fail,
                },
                request_options,
            ),
        )

    def website_screenshot(
        self,
        *,
        url: str,
        format: Literal["jpeg", "jpg", "pdf", "png", "webp"] | str | None = None,
        device: Literal[
            "galaxy_fold4",
            "galaxy_s23",
            "galaxy_s23_ultra",
            "galaxy_s8",
            "huawei_mate_50_pro",
            "huawei_p60_pro",
            "ipad",
            "iphone_12",
            "iphone_13_mini",
            "iphone_13_pro_max",
            "iphone_14_pro",
            "iphone_14_pro_max",
            "iphone_x",
            "pixel_5",
            "pixel_6a",
            "pixel_7_pro",
            "redmi_note_11",
            "redmi_note_12_pro",
        ]
        | str
        | None = None,
        full_page: bool | None = None,
        full_page_scroll: bool | None = None,
        full_page_scroll_duration: int | float | None = None,
        viewport_width: int | float | None = None,
        viewport_height: int | float | None = None,
        scale_factor: int | float | None = None,
        image_quality: str | None = None,
        selector: str | None = None,
        cache: bool | None = None,
        cache_ttl: int | float | None = None,
        remove_selectors: str | None = None,
        remove_cookie_banners: bool | None = None,
        remove_ads: bool | None = None,
        block_resources: Literal[
            "document",
            "eventsource",
            "fetch",
            "font",
            "image",
            "manifest",
            "media",
            "other",
            "script",
            "stylesheet",
            "texttrack",
            "websocket",
            "xhr",
        ]
        | str
        | None = None,
        block_urls: str | None = None,
        delay: int | float | None = None,
        wait_until: Sequence[
            Literal["domcontentloaded", "load", "networkidle0", "networkidle2"] | str
        ]
        | None = None,
        wait_for_selector: str | None = None,
        proxy: str | None = None,
        s3_secret_key: str | None = None,
        s3_access_key_id: str | None = None,
        s3_bucket: str | None = None,
        s3_object_key: str | None = None,
        s3_region: str | None = None,
        storage_endpoint: str | None = None,
        s3_url: bool | None = None,
        fields: str | None = None,
        is_async: bool | None = None,
        soft_fail: bool | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Website Screenshot. Turn any public URL into a PNG, JPEG, WebP, or PDF asset rendered by BrowserSolver. No local Chromium fleet to operate. Credit cost: 2 credits per call.

        ``GET / POST /v1/website/screenshot``

        Args:
            url: Page address to render into an image or PDF. Must include a protocol.
            format: File type returned in the response body.
            device: Swap the desktop viewport for a preset handset or tablet fingerprint.
            full_page: Extend the capture beyond the viewport so the entire scrollable document is included.
            full_page_scroll: Drive a scroll pass first so deferred content mounts before a tall capture.
            full_page_scroll_duration: Milliseconds spent scrolling prior to a full-height capture.
            viewport_width: Width of the synthetic desktop window, in pixels.
            viewport_height: Height of the synthetic desktop window, in pixels.
            scale_factor: Pixel density multiplier. Raise it for retina-quality output; files grow accordingly.
            image_quality: Lossy compression level for soft formats.
            selector: Limit the shot to one DOM node matched by this CSS selector.
            cache: Serve a stored capture on repeat requests when caching is enabled.
            cache_ttl: Lifetime of cached captures in seconds.
            remove_selectors: Hide matching CSS selectors (modals, promo bars, etc.) before shooting.
            remove_cookie_banners: Best-effort removal of cookie consent layers before capture.
            remove_ads: Best-effort stripping of ad slots before capture.
            block_resources: Resource kinds to discard during load, as a comma list (example: image,stylesheet,font).
            block_urls: Substring patterns that should never be fetched (example: analytics,tracking,advertisement). Hosts, paths, or fragments such as .example.com/ work.
            delay: Additional settle time in seconds after the readiness event.
            wait_until: Which browser lifecycle event marks the page ready.
            wait_for_selector: Hold capture until this CSS node is present.
            proxy: Route the browser through an intermediate proxy.
            s3_secret_key: Secret key used to authenticate uploads.
            s3_access_key_id: Access key used to authenticate uploads.
            s3_bucket: Destination bucket for the binary asset.
            s3_object_key: Key under which the object is stored (generated automatically if blank).
            s3_region: Cloud region of the bucket.
            storage_endpoint: Override the default AWS endpoint for S3-compatible backends. Leave blank for AWS. R2 example: https://<accountId>.r2.cloudflarestorage.com.
            s3_url: Upload the binary and include the public object URL in the API response.
            fields: Comma-separated list of fields to keep in the response, with dot notation for nested fields (e.g. name,location.city). Does not change the credit cost.
            is_async: Process the request asynchronously: the response is a job_id to poll on /v1/jobs/{id} (see waitForJob).
            soft_fail: Return HTTP 200 even when an error occurs; the error is then in the response body.
        """
        return self._call(
            "website_screenshot",
            {
                "url": url,
                "format": format,
                "device": device,
                "full_page": full_page,
                "full_page_scroll": full_page_scroll,
                "full_page_scroll_duration": full_page_scroll_duration,
                "viewport_width": viewport_width,
                "viewport_height": viewport_height,
                "scale_factor": scale_factor,
                "image_quality": image_quality,
                "selector": selector,
                "cache": cache,
                "cache_ttl": cache_ttl,
                "remove_selectors": remove_selectors,
                "remove_cookie_banners": remove_cookie_banners,
                "remove_ads": remove_ads,
                "block_resources": block_resources,
                "block_urls": block_urls,
                "delay": delay,
                "wait_until": wait_until,
                "wait_for_selector": wait_for_selector,
                "proxy": proxy,
                "s3_secret_key": s3_secret_key,
                "s3_access_key_id": s3_access_key_id,
                "s3_bucket": s3_bucket,
                "s3_object_key": s3_object_key,
                "s3_region": s3_region,
                "storage_endpoint": storage_endpoint,
                "s3_url": s3_url,
                "fields": fields,
                "is_async": is_async,
                "soft_fail": soft_fail,
            },
            request_options,
        )

    def website_technology(
        self,
        *,
        query: str,
        mode: str | None = None,
        fields: str | None = None,
        is_async: bool | None = None,
        soft_fail: bool | None = None,
        request_options: RequestOptions | None = None,
    ) -> JsonResponse:
        """Website Technology. Map CMS, frameworks, analytics, CDN, and security tooling exposed by a public URL. Choose simple lists or expert metadata with confidence scores. Credit cost: 1 credit per call.

        ``GET / POST /v1/website/technology``

        Args:
            query: Public URL to fingerprint for CMS, frameworks, analytics, CDN, and security tooling. Include http:// or https://.
            mode: How much detail to include in the stack report.
            fields: Comma-separated list of fields to keep in the response, with dot notation for nested fields (e.g. name,location.city). Does not change the credit cost.
            is_async: Process the request asynchronously: the response is a job_id to poll on /v1/jobs/{id} (see waitForJob).
            soft_fail: Return HTTP 200 even when an error occurs; the error is then in the response body.
        """
        return cast(
            JsonResponse,
            self._call(
                "website_technology",
                {
                    "query": query,
                    "mode": mode,
                    "fields": fields,
                    "is_async": is_async,
                    "soft_fail": soft_fail,
                },
                request_options,
            ),
        )

    def website_webunlocker(
        self,
        *,
        query: str,
        allow_redirects: bool | None = None,
        return_page_source: bool | None = None,
        fields: str | None = None,
        is_async: bool | None = None,
        soft_fail: bool | None = None,
        request_options: RequestOptions | None = None,
    ) -> JsonResponse:
        """Website WebUnlocker. BrowserSolver's highest HTML fetch tier for retail and marketplace hosts on your account whitelist. Solves persistent bot challenges that still block Rendering. Credit cost: 3 credits per call.

        ``GET / POST /v1/website/webunlocker``

        Args:
            query: Public URL to fetch with the WebUnlocker tier. Include http:// or https://. The hostname must be on your BrowserSolver whitelist.
            allow_redirects: Whether the unlock session should chase HTTP redirects.
            return_page_source: Choose between processed markup and the exact post-unlock source.
            fields: Comma-separated list of fields to keep in the response, with dot notation for nested fields (e.g. name,location.city). Does not change the credit cost.
            is_async: Process the request asynchronously: the response is a job_id to poll on /v1/jobs/{id} (see waitForJob).
            soft_fail: Return HTTP 200 even when an error occurs; the error is then in the response body.
        """
        return cast(
            JsonResponse,
            self._call(
                "website_webunlocker",
                {
                    "query": query,
                    "allow_redirects": allow_redirects,
                    "return_page_source": return_page_source,
                    "fields": fields,
                    "is_async": is_async,
                    "soft_fail": soft_fail,
                },
                request_options,
            ),
        )


class _AsyncOperations:
    """Generated BrowserSolver endpoint methods."""

    __slots__ = ()

    async def _call(
        self, name: str, params: dict[str, Any], options: RequestOptions | None
    ) -> APIResponse:
        raise NotImplementedError

    async def jobs(
        self,
        *,
        id: str,
        request_options: RequestOptions | None = None,
    ) -> JsonResponse:
        """Jobs. Poll the status, progress (0–100) and result of a job started with is_async=true. Polling is free. Poll until status is terminal: CompletedJob, Error, NotFound or BadRequest.

        ``GET /v1/jobs/{id}``

        Args:
            id: The job_id returned by an endpoint called with is_async=true.
        """
        return cast(JsonResponse, await self._call("jobs", {"id": id}, request_options))

    async def stats(
        self,
        *,
        engine: str | None = None,
        path: str | None = None,
        request_options: RequestOptions | None = None,
    ) -> JsonResponse:
        """Stats. Infrastructure health for an engine or endpoint over the last hour. Not scoped to your account or tenant. Enabled per account: HTTP 403 means contact support to activate it.

        ``GET /v1/stats``

        Args:
            engine: API family to check, for example website. Provide at least engine or path.
            path: Specific endpoint to check, for example /v1/website/screenshot. If you also pass engine, use an endpoint from that API.
        """
        return cast(
            JsonResponse,
            await self._call("stats", {"engine": engine, "path": path}, request_options),
        )

    async def usage(
        self,
        *,
        request_options: RequestOptions | None = None,
    ) -> JsonResponse:
        """Usage. Retrieve real-time usage statistics and credit balance for your BrowserSolver account.

        ``GET /v1/usage``
        """
        return cast(JsonResponse, await self._call("usage", {}, request_options))

    async def website_antibot(
        self,
        *,
        query: str,
        timeout: int | float | None = None,
        fields: str | None = None,
        is_async: bool | None = None,
        soft_fail: bool | None = None,
        request_options: RequestOptions | None = None,
    ) -> JsonResponse:
        """Website Antibot. Single-pass scan that names the bot-protection vendor in front of a URL so you can choose the right BrowserSolver fetch tier next. Credit cost: 1 credit per call.

        ``GET /v1/website/antibot``

        Args:
            query: Full URL or bare domain to scan for bot-protection vendors.
            timeout: Upper bound for waiting on the target HTTP response, expressed in seconds (defaults to 15).
            fields: Comma-separated list of fields to keep in the response, with dot notation for nested fields (e.g. name,location.city). Does not change the credit cost.
            is_async: Process the request asynchronously: the response is a job_id to poll on /v1/jobs/{id} (see waitForJob).
            soft_fail: Return HTTP 200 even when an error occurs; the error is then in the response body.
        """
        return cast(
            JsonResponse,
            await self._call(
                "website_antibot",
                {
                    "query": query,
                    "timeout": timeout,
                    "fields": fields,
                    "is_async": is_async,
                    "soft_fail": soft_fail,
                },
                request_options,
            ),
        )

    async def website_crawler(
        self,
        *,
        query: str,
        allow_redirects: bool | None = None,
        return_page_source: bool | None = None,
        fields: str | None = None,
        is_async: bool | None = None,
        soft_fail: bool | None = None,
        request_options: RequestOptions | None = None,
    ) -> JsonResponse:
        """Website Crawler. Fast HTTP pull of public HTML with no browser session. Ideal when the first response already contains the content you need. Credit cost: 1 credit per call.

        ``GET / POST /v1/website/crawler``

        Args:
            query: Public URL to retrieve with the Crawler tier (plain HTTP, no JavaScript). Include http:// or https://.
            allow_redirects: Whether BrowserSolver should chase HTTP redirects for this fetch.
            return_page_source: Choose between processed markup and the exact bytes from the origin.
            fields: Comma-separated list of fields to keep in the response, with dot notation for nested fields (e.g. name,location.city). Does not change the credit cost.
            is_async: Process the request asynchronously: the response is a job_id to poll on /v1/jobs/{id} (see waitForJob).
            soft_fail: Return HTTP 200 even when an error occurs; the error is then in the response body.
        """
        return cast(
            JsonResponse,
            await self._call(
                "website_crawler",
                {
                    "query": query,
                    "allow_redirects": allow_redirects,
                    "return_page_source": return_page_source,
                    "fields": fields,
                    "is_async": is_async,
                    "soft_fail": soft_fail,
                },
                request_options,
            ),
        )

    async def website_rendering(
        self,
        *,
        query: str,
        wait_in_seconds: int | float | None = None,
        wait_for: str | None = None,
        block_ads: bool | None = None,
        timeout: int | float | None = None,
        fields: str | None = None,
        is_async: bool | None = None,
        soft_fail: bool | None = None,
        request_options: RequestOptions | None = None,
    ) -> JsonResponse:
        """Website Rendering. Run a managed browser session against a public URL and collect the HTML after client-side scripts finish. Prefer Crawler for static markup; escalate to WebUnlocker on approved hosts when challenges persist. Credit cost: 2 credits per call.

        ``GET /v1/website/rendering``

        Args:
            query: Public URL to load inside BrowserSolver's headless browser. Include http:// or https://.
            wait_in_seconds: Extra pause, in seconds, after the page load event before BrowserSolver returns HTML. Helpful when widgets animate or hydrate late.
            wait_for: CSS or XPath selector that must appear in the DOM before HTML is returned. The managed browser waits until the node exists (or until timeout).
            block_ads: Skip ad-network requests while the page renders.
            timeout: Hard ceiling, in seconds, for the render session. When reached, BrowserSolver returns whatever HTML is available.
            fields: Comma-separated list of fields to keep in the response, with dot notation for nested fields (e.g. name,location.city). Does not change the credit cost.
            is_async: Process the request asynchronously: the response is a job_id to poll on /v1/jobs/{id} (see waitForJob).
            soft_fail: Return HTTP 200 even when an error occurs; the error is then in the response body.
        """
        return cast(
            JsonResponse,
            await self._call(
                "website_rendering",
                {
                    "query": query,
                    "wait_in_seconds": wait_in_seconds,
                    "wait_for": wait_for,
                    "block_ads": block_ads,
                    "timeout": timeout,
                    "fields": fields,
                    "is_async": is_async,
                    "soft_fail": soft_fail,
                },
                request_options,
            ),
        )

    async def website_screenshot(
        self,
        *,
        url: str,
        format: Literal["jpeg", "jpg", "pdf", "png", "webp"] | str | None = None,
        device: Literal[
            "galaxy_fold4",
            "galaxy_s23",
            "galaxy_s23_ultra",
            "galaxy_s8",
            "huawei_mate_50_pro",
            "huawei_p60_pro",
            "ipad",
            "iphone_12",
            "iphone_13_mini",
            "iphone_13_pro_max",
            "iphone_14_pro",
            "iphone_14_pro_max",
            "iphone_x",
            "pixel_5",
            "pixel_6a",
            "pixel_7_pro",
            "redmi_note_11",
            "redmi_note_12_pro",
        ]
        | str
        | None = None,
        full_page: bool | None = None,
        full_page_scroll: bool | None = None,
        full_page_scroll_duration: int | float | None = None,
        viewport_width: int | float | None = None,
        viewport_height: int | float | None = None,
        scale_factor: int | float | None = None,
        image_quality: str | None = None,
        selector: str | None = None,
        cache: bool | None = None,
        cache_ttl: int | float | None = None,
        remove_selectors: str | None = None,
        remove_cookie_banners: bool | None = None,
        remove_ads: bool | None = None,
        block_resources: Literal[
            "document",
            "eventsource",
            "fetch",
            "font",
            "image",
            "manifest",
            "media",
            "other",
            "script",
            "stylesheet",
            "texttrack",
            "websocket",
            "xhr",
        ]
        | str
        | None = None,
        block_urls: str | None = None,
        delay: int | float | None = None,
        wait_until: Sequence[
            Literal["domcontentloaded", "load", "networkidle0", "networkidle2"] | str
        ]
        | None = None,
        wait_for_selector: str | None = None,
        proxy: str | None = None,
        s3_secret_key: str | None = None,
        s3_access_key_id: str | None = None,
        s3_bucket: str | None = None,
        s3_object_key: str | None = None,
        s3_region: str | None = None,
        storage_endpoint: str | None = None,
        s3_url: bool | None = None,
        fields: str | None = None,
        is_async: bool | None = None,
        soft_fail: bool | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Website Screenshot. Turn any public URL into a PNG, JPEG, WebP, or PDF asset rendered by BrowserSolver. No local Chromium fleet to operate. Credit cost: 2 credits per call.

        ``GET / POST /v1/website/screenshot``

        Args:
            url: Page address to render into an image or PDF. Must include a protocol.
            format: File type returned in the response body.
            device: Swap the desktop viewport for a preset handset or tablet fingerprint.
            full_page: Extend the capture beyond the viewport so the entire scrollable document is included.
            full_page_scroll: Drive a scroll pass first so deferred content mounts before a tall capture.
            full_page_scroll_duration: Milliseconds spent scrolling prior to a full-height capture.
            viewport_width: Width of the synthetic desktop window, in pixels.
            viewport_height: Height of the synthetic desktop window, in pixels.
            scale_factor: Pixel density multiplier. Raise it for retina-quality output; files grow accordingly.
            image_quality: Lossy compression level for soft formats.
            selector: Limit the shot to one DOM node matched by this CSS selector.
            cache: Serve a stored capture on repeat requests when caching is enabled.
            cache_ttl: Lifetime of cached captures in seconds.
            remove_selectors: Hide matching CSS selectors (modals, promo bars, etc.) before shooting.
            remove_cookie_banners: Best-effort removal of cookie consent layers before capture.
            remove_ads: Best-effort stripping of ad slots before capture.
            block_resources: Resource kinds to discard during load, as a comma list (example: image,stylesheet,font).
            block_urls: Substring patterns that should never be fetched (example: analytics,tracking,advertisement). Hosts, paths, or fragments such as .example.com/ work.
            delay: Additional settle time in seconds after the readiness event.
            wait_until: Which browser lifecycle event marks the page ready.
            wait_for_selector: Hold capture until this CSS node is present.
            proxy: Route the browser through an intermediate proxy.
            s3_secret_key: Secret key used to authenticate uploads.
            s3_access_key_id: Access key used to authenticate uploads.
            s3_bucket: Destination bucket for the binary asset.
            s3_object_key: Key under which the object is stored (generated automatically if blank).
            s3_region: Cloud region of the bucket.
            storage_endpoint: Override the default AWS endpoint for S3-compatible backends. Leave blank for AWS. R2 example: https://<accountId>.r2.cloudflarestorage.com.
            s3_url: Upload the binary and include the public object URL in the API response.
            fields: Comma-separated list of fields to keep in the response, with dot notation for nested fields (e.g. name,location.city). Does not change the credit cost.
            is_async: Process the request asynchronously: the response is a job_id to poll on /v1/jobs/{id} (see waitForJob).
            soft_fail: Return HTTP 200 even when an error occurs; the error is then in the response body.
        """
        return await self._call(
            "website_screenshot",
            {
                "url": url,
                "format": format,
                "device": device,
                "full_page": full_page,
                "full_page_scroll": full_page_scroll,
                "full_page_scroll_duration": full_page_scroll_duration,
                "viewport_width": viewport_width,
                "viewport_height": viewport_height,
                "scale_factor": scale_factor,
                "image_quality": image_quality,
                "selector": selector,
                "cache": cache,
                "cache_ttl": cache_ttl,
                "remove_selectors": remove_selectors,
                "remove_cookie_banners": remove_cookie_banners,
                "remove_ads": remove_ads,
                "block_resources": block_resources,
                "block_urls": block_urls,
                "delay": delay,
                "wait_until": wait_until,
                "wait_for_selector": wait_for_selector,
                "proxy": proxy,
                "s3_secret_key": s3_secret_key,
                "s3_access_key_id": s3_access_key_id,
                "s3_bucket": s3_bucket,
                "s3_object_key": s3_object_key,
                "s3_region": s3_region,
                "storage_endpoint": storage_endpoint,
                "s3_url": s3_url,
                "fields": fields,
                "is_async": is_async,
                "soft_fail": soft_fail,
            },
            request_options,
        )

    async def website_technology(
        self,
        *,
        query: str,
        mode: str | None = None,
        fields: str | None = None,
        is_async: bool | None = None,
        soft_fail: bool | None = None,
        request_options: RequestOptions | None = None,
    ) -> JsonResponse:
        """Website Technology. Map CMS, frameworks, analytics, CDN, and security tooling exposed by a public URL. Choose simple lists or expert metadata with confidence scores. Credit cost: 1 credit per call.

        ``GET / POST /v1/website/technology``

        Args:
            query: Public URL to fingerprint for CMS, frameworks, analytics, CDN, and security tooling. Include http:// or https://.
            mode: How much detail to include in the stack report.
            fields: Comma-separated list of fields to keep in the response, with dot notation for nested fields (e.g. name,location.city). Does not change the credit cost.
            is_async: Process the request asynchronously: the response is a job_id to poll on /v1/jobs/{id} (see waitForJob).
            soft_fail: Return HTTP 200 even when an error occurs; the error is then in the response body.
        """
        return cast(
            JsonResponse,
            await self._call(
                "website_technology",
                {
                    "query": query,
                    "mode": mode,
                    "fields": fields,
                    "is_async": is_async,
                    "soft_fail": soft_fail,
                },
                request_options,
            ),
        )

    async def website_webunlocker(
        self,
        *,
        query: str,
        allow_redirects: bool | None = None,
        return_page_source: bool | None = None,
        fields: str | None = None,
        is_async: bool | None = None,
        soft_fail: bool | None = None,
        request_options: RequestOptions | None = None,
    ) -> JsonResponse:
        """Website WebUnlocker. BrowserSolver's highest HTML fetch tier for retail and marketplace hosts on your account whitelist. Solves persistent bot challenges that still block Rendering. Credit cost: 3 credits per call.

        ``GET / POST /v1/website/webunlocker``

        Args:
            query: Public URL to fetch with the WebUnlocker tier. Include http:// or https://. The hostname must be on your BrowserSolver whitelist.
            allow_redirects: Whether the unlock session should chase HTTP redirects.
            return_page_source: Choose between processed markup and the exact post-unlock source.
            fields: Comma-separated list of fields to keep in the response, with dot notation for nested fields (e.g. name,location.city). Does not change the credit cost.
            is_async: Process the request asynchronously: the response is a job_id to poll on /v1/jobs/{id} (see waitForJob).
            soft_fail: Return HTTP 200 even when an error occurs; the error is then in the response body.
        """
        return cast(
            JsonResponse,
            await self._call(
                "website_webunlocker",
                {
                    "query": query,
                    "allow_redirects": allow_redirects,
                    "return_page_source": return_page_source,
                    "fields": fields,
                    "is_async": is_async,
                    "soft_fail": soft_fail,
                },
                request_options,
            ),
        )
