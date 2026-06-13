import os
import shutil
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "backend", "src"))

_BUNDLED_DB = os.path.join(os.path.dirname(__file__), "genesnap.db")
_TMP_DB = "/tmp/genesnap.db"

if not os.path.exists(_TMP_DB):
    shutil.copy2(_BUNDLED_DB, _TMP_DB)

from genesnap.main import app  # noqa: E402
from mangum import Mangum  # noqa: E402

handler = Mangum(app, lifespan="auto")
