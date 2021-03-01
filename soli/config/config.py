import os
from configparser import ConfigParser

DIRNAME = os.path.dirname(__file__)
FILENAME = "/soliConfig.ini"


def config(filename=DIRNAME + FILENAME, section='soliConfig'):
    parser = ConfigParser()
    parser.read(filename)
    db = {}

    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]

    else:
        raise Exception(f'Section {section} not found in {filename}')

    return db
