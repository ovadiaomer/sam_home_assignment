import json

class ApiResponse:
    def __init__(self, domain, status, duration, response):
        self.domain = domain
        self.status = status
        self.duration = duration
        self.response = response

    @classmethod
    def from_success(cls, domain, duration, response):
        return cls(domain, "success", duration, response.json())

    @classmethod
    def from_failure(cls, domain, duration, error_message):
        return cls(domain, "failed", duration, {"error": error_message})

    def to_dict(self):
        return {
            "domain": self.domain,
            "status": self.status,
            "duration": self.duration,
            "response": str(self.response)
        }
