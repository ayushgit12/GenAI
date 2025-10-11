from pathlib import Path
from typing import List, Any
from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain_community.document_loaders import Docx2txtLoader
from langchain_community.document_loaders.excel import UnstructuredExcelLoader
from langchain_community.document_loaders import JSONLoader

def load_all_documents(data_dir: str) -> List[Any]:
    
     data_path = Path(data_dir).resolve()
     print(f"[DEBUG] Data Path: {data_path}")
     documents = []

     pdf_files = list(data_path.glob("**/*.pdf"))
     print(f"[DEBUG] Found {len(pdf_files)} PDF files.")

     for pdf_file in pdf_files:
          print(f"[DEBUG] Loading PDF file: {pdf_file}")

          try:
               loader = PyPDFLoader(str(pdf_file))
               docs = loader.load()
               print(f"[DEBUG] Loaded {len(docs)} documents from {pdf_file}")
               documents.extend(docs)
          except Exception as e:
               print(f"[ERROR] Failed to load PDF file {pdf_file}: {e}")

     # TEXT FILES
     text_files = list(data_path.glob("**/*.txt"))
     print(f"[DEBUG] Found {len(text_files)} text files.")

     for text_file in text_files:
          print(f"[DEBUG] Loading text file: {text_file}")

          try:
               loader = TextLoader(str(text_file))
               docs = loader.load()
               print(f"[DEBUG] Loaded {len(docs)} documents from {text_file}")
               documents.extend(docs)
          except Exception as e:
               print(f"[ERROR] Failed to load text file {text_file}: {e}")

     # CSV FILES

     csv_files = list(data_path.glob("**/*.csv"))
     print(f"[DEBUG] Found {len(csv_files)} CSV files.")
     for csv_file in csv_files:
          print(f"[DEBUG] Loading CSV file: {csv_file}")

          try:
               loader = UnstructuredExcelLoader(str(csv_file))
               docs = loader.load()
               print(f"[DEBUG] Loaded {len(docs)} documents from {csv_file}")
               documents.extend(docs)
          except Exception as e:
               print(f"[ERROR] Failed to load CSV file {csv_file}: {e}")

     # SQL FILES
     sql_files = list(data_path.glob("**/*.sql"))

     print(f"[DEBUG] Found {len(sql_files)} sql files.")

     for sql_file in sql_files:
          print(f"[DEBUG] Loading SQL file: {sql_file}")

          try:
               loader = Docx2txtLoader(str(sql_file))
               docs = loader.load()
               print(f"[DEBUG] Loaded {len(docs)} documents from {sql_file}")
               documents.extend(docs)
          except Exception as e:
               print(f"[ERROR] Failed to load docx file {sql_file}: {e}")
     
     # JSON FILES
     json_files = list(data_path.glob("**/*.json"))
     print(f"[DEBUG] Found {len(json_files)} JSON files.")

     for json_file in json_files:
          print(f"[DEBUG] Loading JSON file: {json_file}")

          try:
               # JSONLoader requires a jq schema. Use '.' to select the root
               # (the file is a JSON array) and set text_content=False since
               # each item is an object (dict) not plain text.
               loader = JSONLoader(str(json_file), jq_schema='.', text_content=False)
               docs = loader.load()
               print(f"[DEBUG] Loaded {len(docs)} documents from {json_file}")
               documents.extend(docs)
          except Exception as e:
               print(f"[ERROR] Failed to load JSON file {json_file}: {e}")

     print(f"[DEBUG] Total documents loaded: {len(documents)}")
     return documents
          
     

     
