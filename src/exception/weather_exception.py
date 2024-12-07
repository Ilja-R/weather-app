class WeatherFetchException(Exception):

    def __init__(self, message, city, status_code=None, reason=None):
        self.city = city
        self.message = message
        self.status_code = status_code
        self.reason = reason
        super().__init__(self.message)

    def __str__(self):
        err = f"City: {self.city}"
        err += f"\n    Error: {self.message}"
        if self.status_code:
            err += f"\n    Status code: {self.status_code}"
        if self.reason:
            err += f"\n    Reason: {self.reason}"
        err += "\n"
        return err