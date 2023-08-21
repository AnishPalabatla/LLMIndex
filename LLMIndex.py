import os
from llama_index import TreeIndex, SimpleDirectoryReader
import openai
openai.api_key = "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"
pdf_directory = r"c:\Users\anish\TempPDF"
resume = SimpleDirectoryReader(pdf_directory).load_data()
new_index = TreeIndex.from_documents(resume)
query_engine = new_index.as_query_engine()
query = "What will shut the sheep in the pen after sunset"
response = query_engine.query(query)
print("Response:", response)
