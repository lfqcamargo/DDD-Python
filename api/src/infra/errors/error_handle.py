from pydantic import ValidationError
from src.infra.views.http_types.http_response import HttpResponse
from src.infra.errors.error_types.http_bad_request import HttpBadRequestError
from src.infra.errors.error_types.http_not_found import HttpNotFoundError
from src.infra.errors.error_types.http_unprocessable_entity import (
    HttpUnprocessableEntityError,
)


def handle_errors(error: Exception) -> HttpResponse:
    """
    Handles exceptions and maps them to appropriate HTTP responses.

    Args:
        error (Exception): The exception to handle.

    Returns:
        HttpResponse: The HTTP response corresponding to the handled exception.
    """
    if isinstance(error, ValidationError):
        return HttpResponse(
            status_code=422,
            body={
                "errors": [
                    {
                        "title": "Validation Error",
                        "detail": e["msg"],
                        "field": e.get("loc"),
                    }
                    for e in error.errors()
                ]
            },
        )

    if isinstance(
        error, (HttpBadRequestError, HttpNotFoundError, HttpUnprocessableEntityError)
    ):
        return HttpResponse(
            status_code=error.status_code,
            body={"errors": [{"title": error.name, "detail": error.message}]},
        )

    return HttpResponse(
        status_code=500,
        body={"errors": [{"title": "Server Error", "detail": str(error)}]},
    )
