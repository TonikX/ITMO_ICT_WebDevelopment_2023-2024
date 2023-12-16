class LocationException(Exception):
    """
    Exception is raised for invalid location inputs

    e.g. latitude not in range [-90, 90]
    """
    
    def __init__(self, message: str):
        super().__init__(message)
