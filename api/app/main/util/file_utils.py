from werkzeug.utils import secure_filename

def extract_extension(filename):
    if '.' in filename:
        return filename.rsplit('.', 1)

    return None, None

def extract_extension_and_secure(filename):
    if '.' in filename:
        return secure_filename(filename).rsplit('.', 1)

    return None, None
