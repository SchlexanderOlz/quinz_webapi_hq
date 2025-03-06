import requests

class APIClient:
    def __init__(self, base_url, auth_token=None):
        """
        Initialize the API client.

        :param base_url: Base URL of the API.
        :param auth_token: Authentication token for APIs requiring X-Auth-Token.
        """
        self.base_url = base_url.rstrip("/")
        self.headers = {"Content-Type": "application/json"}
        if auth_token:
            self.set_auth_token(auth_token)
    
    def set_auth_token(self, auth_token):
        """
        Set the authentication token.

        :param auth_token: Authentication token.
        """
        self.headers["X-Auth-Token"] = auth_token

    def post(self, path, payload, headers=None):
        """
        Send a POST request to the API.
        :param path: API endpoint path.
        :param payload: Request body as a dictionary.
        :param headers: Additional headers for the request.
        :return: Response as a dictionary.
        """
        url = f"{self.base_url}/{path.lstrip('/')}"
        request_headers = self.headers.copy()
        if headers:
            request_headers.update(headers)
        response = requests.post(url, json=payload, headers=request_headers, verify=False)
        response.raise_for_status()
        return response.json()
