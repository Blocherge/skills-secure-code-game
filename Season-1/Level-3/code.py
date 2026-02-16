# Welcome to Secure Code Game Season-1/Level-3!

# You know how to play by now, good luck!

import os
from flask import Flask, request

### Unrelated to the exercise -- Starts here -- Please ignore
app = Flask(__name__)
@app.route("/")
def source():
    TaxPayer('foo', 'bar').get_tax_form_attachment(request.args["input"])
    TaxPayer('foo', 'bar').get_prof_picture(request.args["input"])
### Unrelated to the exercise -- Ends here -- Please ignore

class TaxPayer:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.prof_picture = None
        self.tax_form_attachment = None

    # returns the path of an optional profile picture that users can set
    def get_prof_picture(self, path=None):
        # setting a profile picture is optional
        if not path:
            return None

        # reject absolute paths immediately
        if os.path.isabs(path):
            return None

        # builds path and normalizes it
        base_dir = os.path.dirname(os.path.abspath(__file__))
        prof_picture_path = os.path.normpath(os.path.join(base_dir, path))

        # ensure the resulting path is still under our base directory
        try:
            if os.path.commonpath([base_dir, prof_picture_path]) != base_dir:
                return None
        except ValueError:
            # commonpath can raise if paths are on different drives
            return None

        with open(prof_picture_path, 'rb') as pic:
            picture = bytearray(pic.read())

        # assume that image is returned on screen after this
        return prof_picture_path

    # returns the path of an attached tax form that every user should submit
    def get_tax_form_attachment(self, path=None):
        tax_data = None

        if not path:
            raise Exception("Error: Tax form is required for all users")

        # reject absolute paths and traversal attempts
        if os.path.isabs(path):
            raise Exception("Invalid path")

        base_dir = os.path.dirname(os.path.abspath(__file__))
        attachment_path = os.path.normpath(os.path.join(base_dir, path))

        try:
            if os.path.commonpath([base_dir, attachment_path]) != base_dir:
                raise Exception("Invalid path")
        except ValueError:
            raise Exception("Invalid path")

        with open(attachment_path, 'rb') as form:
            tax_data = bytearray(form.read())

        # assume that tax data is returned on screen after this
        return attachment_path

