class APIError(Exception):
    """Generic API error."""
    pass


class AuthenticationError(APIError):
    """Authentication failed."""
    pass


class PermissionError(APIError):
    """Permission denied."""
    pass
