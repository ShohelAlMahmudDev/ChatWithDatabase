from langchain.sql_database import SQLDatabase

# Import credentials from config
from config import DB_USER, DB_PASSWORD, DB_HOST, DB_NAME

def get_database_connection():
    """Create and return a database connection."""
    connection_uri = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
    return SQLDatabase.from_uri(connection_uri)

db = get_database_connection()
