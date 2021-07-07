class ConnexionError(Exception):
    def __init__(self, url):
        self.message = "Unnable to connect to this url : " + url

class UnknownWebsiteError(Exception):
    def __init__(self, sitename):
        self.message = sitename + "isn\'t known nowadays."

class InputError(Exception):
    def __init__(self, message = ""):
        self.message = "The format of the input is incorrect. " + message

class OSError(Exception):
    def __init__(self, message):
        self.message = message