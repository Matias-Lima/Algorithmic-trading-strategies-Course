# utils.py (ou o arquivo equivalente onde ficam essas funções)

from typing import List, Optional
import streamlit as st

from langchain.chains.conversational_retrieval.base import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate
from langchain_community.vectorstores.faiss import FAISS
from langchain_openai.embeddings import OpenAIEmbeddings
from langchain_openai.chat_models import ChatOpenAI
from langchain.schema import Document as LC_Document

from pydantic import Field
try:
    # LangChain >= 0.2
    from langchain_core.retrievers import BaseRetriever
except ImportError:
    # fallback para versões < 0.2
    from langchain.schema import BaseRetriever

from configs import get_config

# ===== Configurações locais =====
INDEX_DIR = "Algorithmic_Trading"


# ===== Helpers =====
def _get_api_key_or_fail() -> str:
    """Obtém a OpenAI API Key da página de config. Erra com mensagem amigável se ausente."""
    api_key = get_config('openai_api_key')
    if not api_key:
        st.error(
            "OpenAI API Key não configurada. Vá em **Página de configuração → "
            "Configurar OpenAI API Key** e salve a sua chave."
        )
        raise ValueError("OPENAI_API_KEY ausente")
    return api_key


def _sanitize_vector_store_docs(vector_store) -> None:
    """
    Garante que todos os Documents do docstore tenham metadata=dict.
    Evita erros do tipo: 'NoneType' object has no attribute 'get'.
    """
    try:
        store = getattr(vector_store, "docstore", None)
        backing = getattr(store, "_dict", None)  # InMemoryDocstore
        if isinstance(backing, dict):
            for key, doc in list(backing.items()):
                # doc pode ser LC_Document ou dict serializado
                if isinstance(doc, LC_Document):
                    if doc.metadata is None:
                        doc.metadata = {}
                elif isinstance(doc, dict):
                    page_content = doc.get("page_content", "") or ""
                    metadata = doc.get("metadata") or {}
                    backing[key] = LC_Document(page_content=page_content, metadata=metadata)
    except Exception as e:
        st.warning(f"Não foi possível sanitizar todos os documentos do índice: {e}")


class SafeRetriever(BaseRetriever):
    """Retriever que garante metadata=dict nos docs retornados (compatível com Pydantic)."""
    base: BaseRetriever = Field(..., description="Retriever base a ser encapsulado")

    # Métodos internos esperados por BaseRetriever (não use as versões públicas aqui)
    def _get_relevant_documents(self, query: str, *, run_manager: Optional[object] = None) -> List[LC_Document]:
        docs = self.base.get_relevant_documents(query)
        for d in docs:
            if getattr(d, "metadata", None) is None:
                d.metadata = {}
        return docs

    async def _aget_relevant_documents(self, query: str, *, run_manager: Optional[object] = None) -> List[LC_Document]:
        docs = await self.base.aget_relevant_documents(query)
        for d in docs:
            if getattr(d, "metadata", None) is None:
                d.metadata = {}
        return docs


# ===== Pipeline =====
def carrega_vector_store():
    """Carrega o vetor FAISS do disco e sanitiza os documentos."""
    try:
        api_key = _get_api_key_or_fail()
        embedding_model = OpenAIEmbeddings(openai_api_key=api_key)

        vector_store = FAISS.load_local(
            INDEX_DIR,
            embedding_model,
            allow_dangerous_deserialization=True,
        )

        # Sanitiza para evitar metadata=None
        _sanitize_vector_store_docs(vector_store)
        return vector_store

    except Exception as e:
        st.error(f'Erro ao carregar o vetor FAISS: {e}')
        raise


def safe_get_config(key, default=None, required=True):
    """Busca uma configuração; lança erro se requerida e ausente."""
    value = get_config(key)
    if value is None and required:
        msg = f'Configuração "{key}" não encontrada.'
        st.error(msg)
        raise ValueError(msg)
    return value if value is not None else default


def cria_chain_conversa():
    """Cria e salva no session_state a ConversationalRetrievalChain do LangChain."""
    try:
        # Pega a chave diretamente da página de config
        api_key = _get_api_key_or_fail()

        # Vector store + retriever seguro
        vector_store = carrega_vector_store()
        retriever_base = vector_store.as_retriever(
            search_type=safe_get_config('retrieval_search_type'),
            search_kwargs=safe_get_config('retrieval_kwargs')
        )
        retriever = SafeRetriever(base=retriever_base)  # agora é um BaseRetriever válido

        # LLM com a chave explícita
        chat = ChatOpenAI(
            model=safe_get_config('model_name'),
            openai_api_key=api_key,
        )

        # Memória e prompt
        memory = ConversationBufferMemory(
            return_messages=True,
            memory_key='chat_history',
            output_key='answer'
        )
        prompt = PromptTemplate.from_template(safe_get_config('prompt'))

        # Chain conversacional com retrieval
        chat_chain = ConversationalRetrievalChain.from_llm(
            llm=chat,
            memory=memory,
            retriever=retriever,
            return_source_documents=True,
            verbose=True,
            combine_docs_chain_kwargs={'prompt': prompt}
        )

        # Guarda no estado
        st.session_state['chain'] = chat_chain
        st.session_state['memory'] = memory  # opcional

    except Exception as e:
        st.error(f'Erro ao inicializar o ChatBot: {e}')
        raise
