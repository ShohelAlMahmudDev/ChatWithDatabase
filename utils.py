import re

def extract_sql(query_str: str) -> str:
    """
    Extracts SQL query from a markdown formatted output.
    """
    query_str = query_str.replace("SQLQuery:", "").strip()
    pattern = r"```(?:sql)?\s*(.*?)\s*```"
    match = re.search(pattern, query_str, re.DOTALL)

    if match:
        return match.group(1).strip()
    
    return query_str.split("### Explanation:")[0].strip()
