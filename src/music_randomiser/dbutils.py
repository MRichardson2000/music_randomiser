from dotenv import load_dotenv
from pathlib import Path
import os
import sqlalchemy as sa
from typing import Any
from .utils import CREATES_DBO, ANALYTICS_DBO
from music_randomiser.logger import get_logger
from music_randomiser.exceptions import DatabaseError


logger = get_logger(__name__)
load_dotenv()


def get_engine() -> sa.Engine:
    """Forms the URL from details in the .env file and then creates the engine"""
    url = (
        f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}"
        f"@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
    )
    return sa.create_engine(url, echo=False, future=True)


def fetch_result(
    query: str, params: dict[str, Any] | None = None
) -> list[dict[str, Any]]:
    """If the Query executed returns a value then this returns it as a dictionary"""
    engine = get_engine()
    try:
        with engine.begin() as conn:
            result = conn.execute(sa.text(query), params or {})
            logger.debug("Successfully fetched results from the database")
            return [dict(r) for r in result.mappings()]
    except Exception as e:
        logger.error("Failed to fetch results from the database: %s", e, exc_info=True)
        raise DatabaseError(f"Failed to fetch results due to: {e}")


def execute_query(query: str, params: dict[str, Any] | None = None) -> None:
    """If you're only executing a query but not expecting a result back the you can run this and it won't return anything"""
    engine = get_engine()
    try:
        with engine.begin() as conn:
            conn.execute(sa.text(query), params or {})
            logger.debug("Successfully executed query against the database")
    except Exception as e:
        logger.error("Failed to execute query: %s", e, exc_info=True)
        raise DatabaseError(f"Failed to execute query due to: {e}")


def load_sql_as_text(path: Path, file_name: str) -> str:
    """My SQL files in the DBO fold can be read in as text by using this function"""
    full_path = str(path) + "/" + file_name
    with open(full_path, "r") as f:
        return f.read()


def create_schemas() -> None:
    table = load_sql_as_text(CREATES_DBO, "*_table.sql")
    print("# --- Creating Walk Table --- #")
    execute_query(table)


def view_sql_as_text() -> None:
    print(fetch_result(""))


def main() -> None:
    create_schemas()
    # view_sql_as_text()


if __name__ == "__main__":
    main()
