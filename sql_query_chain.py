from database_connector import db
from llm_handler import generate_explanation, llm
from utils import extract_sql

# Attempt to import appropriate SQL chain
try:
    from langchain.chains.sql_database import SQLDatabaseChain
    db_chain = SQLDatabaseChain.from_llm(llm, db, verbose=True)
except ImportError:
    from langchain.chains import create_sql_query_chain
    db_chain = create_sql_query_chain(llm, db)

def chat_with_db(user_query):
    """
    Process the user's natural language query, convert it to SQL, execute it, and return results.
    """
    try:
        response = db_chain.invoke({"question": user_query})
        cleaned_query = extract_sql(response)

        result = db.run(cleaned_query)

        # Generate explanation
        final_explanation = generate_explanation(user_query, cleaned_query, result)

        return {
            "query": cleaned_query,
            "result": final_explanation.content
        }
    except Exception as e:
        print("Error:", e)
        return None
