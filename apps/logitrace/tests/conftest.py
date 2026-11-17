"""
Test isolation for LogiTrace.

Runs before any backend module is imported:
- points the app at a throwaway SQLite file (tests never touch logitrace.db);
- blanks the 9router key so tests never call the network (LLM path -> fallback).
load_dotenv() does not override variables that are already set, so these win over .env.
"""

import os
import tempfile

_tmpdir = tempfile.mkdtemp(prefix="logitrace_test_")
_db_path = os.path.join(_tmpdir, "test.db").replace("\\", "/")

os.environ["DATABASE_URL"] = f"sqlite+aiosqlite:///{_db_path}"
os.environ["LOGITRACE_DB_URL"] = os.environ["DATABASE_URL"]
os.environ["NINEROUTER_API_KEY"] = ""
os.environ["NINEROUTER_API_URL"] = "http://127.0.0.1:9/v1/chat/completions"
