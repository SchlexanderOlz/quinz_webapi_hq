class APIEndpoints:
    def __init__(self, client):
        """
        Initialize endpoints with the given client.

        :param client: Instance of `APIClient`.
        """
        self.client = client

    def login(self, username, password):
        """
        Login to the system.

        :param username: Username.
        :param password: Password.
        :return: Login response.
        """
        payload = [{
            "id": 0,
            "jsonrpc": "2.0",
            "method": "Api.Login",
            "params": {"user": username, "password": password}
        }]
        return self.client.post("/api/jsonrpc", payload)

    def get_permissions(self, headers):
        """
        Get permissions for the current user.

        :param headers: Request headers.
        :return: Permissions response.
        """
        payload = [{
            "jsonrpc": "2.0",
            "method": "Api.GetPermissions",
            "id": 1
        }]
        return self.client.post("/api/jsonrpc", payload, headers)

    def browse(self, var, mode, headers):
        """
        Browse PLC program variables.

        :param var: Variable path.
        :param mode: Browse mode ('children' or 'var').
        :param headers: Request headers.
        :return: Browse response.
        """
        payload = [{
            "jsonrpc": "2.0",
            "id": 4,
            "method": "PlcProgram.Browse",
            "params": {"var": var, "mode": mode}
        }]
        return self.client.post("/api/jsonrpc", payload, headers)

    def read(self, var, headers):
        """
        Read a PLC program variable.

        :param var: Variable path.
        :param headers: Request headers.
        :return: Read response.
        """
        payload = [{
            "id": 1,
            "jsonrpc": "2.0",
            "method": "PlcProgram.Read",
            "params": {"var": var}
        }]
        return self.client.post("/api/jsonrpc", payload, headers)

    def write(self, var, value, headers):
        """
        Write to a PLC program variable.

        :param var: Variable path.
        :param value: Value to write.
        :param headers: Request headers.
        :return: Write response.
        """
        payload = [{
            "jsonrpc": "2.0",
            "method": "PlcProgram.Write",
            "id": 1,
            "params": {"var": var, "value": value}
        }]
        return self.client.post("/api/jsonrpc", payload, headers)

    def ping(self, headers):
        """
        Ping the API server to check availability.

        :param headers: Request headers.
        :return: Ping response.
        """
        payload = [{
            "jsonrpc": "2.0",
            "method": "Api.Ping",
            "id": 1
        }]
        return self.client.post("/api/jsonrpc", payload, headers)

    def logout(self, headers):
        """
        Logout from the system.

        :param headers: Request headers.
        :return: Logout response.
        """
        payload = [{
            "jsonrpc": "2.0",
            "method": "Api.Logout",
            "id": 0
        }]
        return self.client.post("/api/jsonrpc", payload, headers)

    def write_speed(self, var, value, headers):
        """
        Write the speed variable to a PLC program.

        :param var: Variable name (e.g., "Motor.Sollgeschwindigkeit").
        :param value: Speed value to write.
        :param headers: Request headers.
        :return: Write speed response.
        """
        payload = [{
            "jsonrpc": "2.0",
            "method": "PlcProgram.Write",
            "id": 1,
            "params": {"var": var, "value": value}
        }]
        return self.client.post("/api/jsonrpc", payload, headers)

    def turn_on(self, headers):
        payload = [{
            "jsonrpc": "2.0",
            "method": "PlcProgram.Write",
            "id": 1,
            "params": {"var": "\"Motor\".ein", "value": True}
        }]
        return self.client.post("/api/jsonrpc", payload, headers)

    def turn_off(self, headers):
        payload = [{
            "jsonrpc": "2.0",
            "method": "PlcProgram.Write",
            "id": 1,
            "params": {"var": "\"Motor\".ein", "value": False}
        }]
        return self.client.post("/api/jsonrpc", payload, headers)

