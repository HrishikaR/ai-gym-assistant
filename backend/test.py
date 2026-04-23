from services.rag_module import create_vector_db, get_rag_context

create_vector_db()

print(get_rag_context("Suggest a diet for weight loss"))