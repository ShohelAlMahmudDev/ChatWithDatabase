from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate

# Import API Key
from config import DEEPSEEK_API_KEY

# Initialize DeepSeek LLM
llm = ChatOpenAI(temperature=0, api_key=DEEPSEEK_API_KEY, model="deepseek-chat", base_url="https://api.deepseek.com")

# Explanation prompt template
EXPLANATION_PROMPT_TEMPLATE = """ 
You are a data analyst. Given the following details:
Original Question: {question}
Generated SQL Query: {generated_sql}
Query Result: {query_result}
Please provide a concise and short answer that explains the meaning of the query result in context.
"""

# Explanation prompt function
def generate_explanation(question, generated_sql, query_result):
    """Generate a natural language explanation of the SQL query result."""
    explanation_prompt = PromptTemplate(
        input_variables=["question", "generated_sql", "query_result"],
        template=EXPLANATION_PROMPT_TEMPLATE.strip()
    )
    chain = explanation_prompt | llm
    return chain.invoke({"question": question, "generated_sql": generated_sql, "query_result": query_result})
