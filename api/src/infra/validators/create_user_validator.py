from pydantic import BaseModel, ValidationError, EmailStr, Field
from src.infra.views.http_types.http_request import HttpRequest


def create_user_validator(http_request: HttpRequest) -> None:
    """
    Validates the user data in the given HTTP request.

    Args:
        http_request (HttpRequest): The HTTP request containing the user data.

    Raises:
        ValidationError: If the validation fails for any of the fields.
    """

    class BodyData(BaseModel):
        """
        Validate Body Schema
        """

        email: EmailStr
        name: str = Field(..., min_length=3, max_length=50)
        nickname: str = Field(..., min_length=3, max_length=30)
        password: str = Field(..., min_length=8, max_length=100)
        role: int

    try:
        BodyData(**http_request.body)
    except ValidationError as error:
        raise error
