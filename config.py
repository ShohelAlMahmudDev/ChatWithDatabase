import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Database credentials
DB_USER = os.getenv("MYSQL_USER")
DB_PASSWORD = os.getenv("MYSQL_PASSWORD")
DB_HOST = os.getenv("MYSQL_HOST")
DB_NAME = os.getenv("MYSQL_DB")

# DeepSeek API Key
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")
os.environ["DEEPSEEK_API_KEY"] = DEEPSEEK_API_KEY
