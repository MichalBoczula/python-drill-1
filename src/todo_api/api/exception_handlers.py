"""Shared Problem Details response for request validation failures."""

from fastapi import FastAPI, Request
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse


def register_exception_handlers(app: FastAPI) -> None:
    @app.exception_handler(RequestValidationError)
    async def validation_error(request: Request, exc: RequestValidationError) -> JSONResponse:
        return JSONResponse(
            status_code=422,
            media_type="application/problem+json",
            content={
                "type": "https://httpstatuses.io/422",
                "title": "Validation failed",
                "status": 422,
                "detail": "The request contains invalid data.",
                "instance": request.url.path,
                "code": "request_validation_failed",
                "errors": jsonable_encoder(exc.errors()),
            },
        )
