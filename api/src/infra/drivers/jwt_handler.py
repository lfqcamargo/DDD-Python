from typing import Dict, Optional
from datetime import datetime, timedelta, timezone
import jwt
from src.configs.jwt_configs import jwt_infos


class JwtHandler:
    def create_jwt_token(self, body: Optional[Dict] = None) -> str:
        """
        Creates a JWT token.

        Args:
            body (Optional[Dict]): Additional payload to include in the token.

        Returns:
            str: The generated JWT token.
        """
        if body is None:
            body = {}

        token = jwt.encode(
            payload={
                "exp": datetime.now(timezone.utc)
                + timedelta(hours=jwt_infos["JWT_HOURS"]),
                **body,
            },
            key=jwt_infos["KEY"],
            algorithm=jwt_infos["ALGORITHM"],
        )
        return token

    def decode_jwt_token(self, token: str) -> Dict:
        """
        Decodes a JWT token.

        Args:
            token (str): The JWT token to decode.

        Returns:
            Dict: The decoded payload of the token.
        """
        token_information = jwt.decode(token, key="minhaChave", algorithms="HS256")
        return token_information
