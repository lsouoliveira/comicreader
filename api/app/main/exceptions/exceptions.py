class ApiError(Exception):
    def __init__(self, title, details, code, status_code, source=None):
        super().__init__()

        self.title = title
        self.details = details
        self.code = code
        self.status_code = status_code
        self.source = source

    def to_dict(self):
        rv = dict(())
        rv['code'] = self.code
        rv['title'] = self.title
        rv['details'] = self.details

        if self.source:
            rv['source'] = self.source

        return rv

class InternalError(ApiError):
    def __init__(self):
        super().__init__("Internal Error", "A internal error ocurred.", 0, 500)

class PageNotFoundError(ApiError):
    def __init__(self):
        super().__init__("Page not found", "The page requested was not found.", 1, 404)
