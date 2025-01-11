from pydantic import BaseModel, constr, ValidationError
from src.infra.views.http_types.http_request import HttpRequest

def create_user_validator(htpp_request: HttpRequest) -> None:
    class BodyData(BaseModel):
        email: constr(min_length=1)