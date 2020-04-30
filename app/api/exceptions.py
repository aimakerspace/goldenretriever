class InvalidUsage(Exception):
    """
    Raises exception
    https://flask.palletsprojects.com/en/1.1.x/patterns/apierrors/
    """
    status_code = 400

    def __init__(self, message="query endpoint requires arguments: query, kb_name", 
                 status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv