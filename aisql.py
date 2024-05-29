import os
import logging
from sqlalchemy import create_engine, MetaData
from llama_index.core import SQLDatabase
from llama_index.llms.openai import OpenAI
from llama_index.core.query_engine import NLSQLTableQueryEngine

# Set up basic logging
logging.basicConfig(level=logging.INFO)

# Environment configuration (set these values as environment variables in your deployment)
os.environ["OPENAI_API_KEY"] = "sk-proj-hIklpwXCcMYPAEJS29OqT3BlbkFJF9mnHVyiAiJUPvTf62oB"
os.environ["DB_NAME"] = "mod_sec1"
os.environ["DB_USER"] = "rohithbalasubramani"
os.environ["DB_PASSWORD"] = "rohithabc123"
os.environ["DB_HOST"] = "165.232.185.79"
os.environ["DB_PORT"] = "5432"

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")

# Database connection setup
DATABASE_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}?options=-c%20search_path%3Ddbo"
engine = create_engine(DATABASE_URL, future=True)
metadata = MetaData()
metadata.reflect(bind=engine)

# LlamaIndex Setup
sql_database = SQLDatabase(engine, include_tables=metadata.tables.keys())
llm = OpenAI(temperature=0.1, model="gpt-3.5-turbo", api_key=OPENAI_API_KEY)
sql_query_engine = NLSQLTableQueryEngine(sql_database=sql_database, tables=metadata.tables.keys(), llm=llm)

# Function to execute natural language queries
def execute_query(query):
    try:
        result = sql_query_engine.query(query)
        return result
    except Exception as e:
        logging.error(f"Failed to execute query: {e}")
        return None

# Example usage
if __name__ == "__main__":
    query = input("Enter your query: ")
    result = execute_query(query)
    print(result)