
class ApiServiceError(Exception):
    def __init__(self, message='API service error!'):
        super(ApiServiceError, self).__init__(message)

