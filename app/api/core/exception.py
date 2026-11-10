class AppError(Exception):
    details='Bad request'
    status=400
    def __init__(self,details:str|None=None):
        if details:
            self.details=details

class NotFoundError(AppError):
    status=404
    details="Not found"

class ConflictError(AppError):
    status=409
    details="Conflict"        