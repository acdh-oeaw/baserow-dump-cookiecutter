import os
from acdh_baserow_pyutils import BaseRowClient


BASEROW_DB_ID = {{ cookiecutter.db_id }}
BASEROW_URL = "https://baserow.acdh-dev.oeaw.ac.at/api/"
BASEROW_USER = os.environ.get("BASEROW_USER")
BASEROW_PW = os.environ.get("BASEROW_PW")
BASEROW_TOKEN = os.environ.get("BASEROW_TOKEN")
JSON_FOLDER = "json_dumps"
TEI_FOLDER = "tei"


try:
    br_client = BaseRowClient(
        BASEROW_USER, BASEROW_PW, BASEROW_TOKEN, br_base_url=BASEROW_URL
    )
except KeyError:
    br_client = None
