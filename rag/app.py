from src.data_loader import load_all_documents
from src.vectorestore import FaissVectorStore
from src.search import RAGSearch


if __name__ == "__main__":
     # search the current directory so files directly under rag/ are found

     ## RUN ONLY ONCE
     # data_path = "."
     # documents = load_all_documents(data_path)
     # print(f"Total documents loaded: {len(documents)}")
     # print("\n\n", documents)
     # chunks = EmbeddingPipeline().chunk_documents(documents)
     # chunkvectors = EmbeddingPipeline().embed_chunks(chunks)
     # print(chunkvectors)


     store = FaissVectorStore("faiss_store")

     ### RUN ONLY ONCE
     # store.build_from_documents(documents)


     store.load()
     # print(store.query("What is the attention mechanism?"))

     rag_search = RAGSearch() 

     query = "What is attention mechanism?"
     summary = rag_search.search_and_summarize(query, top_k=3)
     print("Summary:", summary)
     






