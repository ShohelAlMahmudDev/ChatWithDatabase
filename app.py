import streamlit as st
from sql_query_chain import chat_with_db

def show_ui():
    """ Streamlit UI for interacting with the database. """
    st.title("Chat with Database App")
    question = st.text_area("Enter your question:")

    if st.button("Execute"):
        if question:
            md_result = chat_with_db(question)
            if md_result:
                st.write("Generated SQL Query:")
                st.code(md_result["query"], language="sql")
                st.write("Query Result:")
                st.markdown(md_result["result"])
            else:
                st.error("No result returned due to an error.")
        else:
            st.warning("Please enter a question.")

if __name__ == "__main__":
    show_ui()
