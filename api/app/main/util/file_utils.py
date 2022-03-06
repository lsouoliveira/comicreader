from werkzeug.utils import secure_filename
from os.path import splitext

def extract_extension(filename):
    return splitext(filename)

def extract_extension_and_secure(filename):
    return splitext(secure_filename(filename))
