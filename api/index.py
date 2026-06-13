import os
import shutil
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "backend", "src"))

_BUNDLED_DB = os.path.join(os.path.dirname(__file__), "genesnap.db")
_TMP_DB = "/tmp/genesnap.db"

if not os.path.exists(_TMP_DB):
    if not os.path.exists(_BUNDLED_DB):
        raise RuntimeError(
            f"Bundled database not found at {_BUNDLED_DB}. "
            "Ensure the Vercel build step ran successfully."
        )
    shutil.copy2(_BUNDLED_DB, _TMP_DB)

os.environ.setdefault("DB_PATH", _TMP_DB)

from mangum import Mangum  # noqa: E402

from genesnap.main import app  # noqa: E402

handler = Mangum(app, lifespan="auto")
