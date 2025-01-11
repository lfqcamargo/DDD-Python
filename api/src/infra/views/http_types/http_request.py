from typing import Dict, Optional, Any


class HttpRequest:
    """
    Represents an HTTP request, including body and parameters.
    """

    def __init__(
        self,
        body: Optional[Dict[str, Any]] = None,
        param: Optional[Dict[str, Any]] = None,
    ) -> None:
        """
        Initializes an HttpRequest instance.

        Args:
            body (Optional[Dict[str, Any]]): The body of the HTTP request, containing key-value pairs.
            param (Optional[Dict[str, Any]]): Additional parameters for the HTTP request.
        """
        self.body = body or {}
        self.param = param or {}
