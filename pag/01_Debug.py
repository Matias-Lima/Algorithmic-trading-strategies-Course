import streamlit as st
from langchain.prompts import PromptTemplate
from configs import get_config

def debug_page():
    st.header('Página de debug', divider=True)

    # Tenta obter e construir o prompt template
    try:
        prompt_template_str = get_config('prompt')
        if not prompt_template_str:
            st.error("Prompt de configuração não encontrado.")
            st.stop()
        prompt_template = PromptTemplate.from_template(prompt_template_str)
    except Exception as e:
        st.error(f"Erro ao criar PromptTemplate: {e}")
        st.stop()

    # Checa se existe resposta anterior
    if 'ultima_resposta' not in st.session_state:
        st.error('Realize uma pergunta para o modelo para visualizar o debug.')
        st.stop()

    ultima_resposta = st.session_state['ultima_resposta']

    # Coleta contexto dos documentos fonte
    try:
        contexto_docs = ultima_resposta.get('source_documents', [])
        if not contexto_docs:
            st.warning('Nenhum documento de contexto retornado para esta resposta.')
            contexto_str = ''
        else:
            contexto_list = [getattr(doc, "page_content", str(doc)) for doc in contexto_docs]
            contexto_str = '\n\n'.join(contexto_list)
    except Exception as e:
        st.error(f'Erro ao processar documentos de contexto: {e}')
        contexto_str = ''

    # Recupera o histórico de conversa
    try:
        if 'chain' not in st.session_state:
            st.error('Objeto da chain não encontrado.')
            st.stop()
        chain = st.session_state['chain']
        memory = getattr(chain, 'memory', None)
        if not memory:
            st.error('Memória não encontrada na chain.')
            st.stop()
        chat_history = getattr(memory, 'buffer_as_str', '')
    except Exception as e:
        st.error(f'Erro ao recuperar o histórico de conversa: {e}')
        chat_history = ''

    with st.container(border=True):
        try:
            prompt = prompt_template.format(
                chat_history=chat_history,
                context=contexto_str,
                question=''
            )
            st.code(prompt)
        except Exception as e:
            st.error(f'Erro ao formatar o prompt: {e}')
            st.write("Variáveis disponíveis:")
            st.write(f"chat_history: {chat_history[:100]}...")  # Trunca para não poluir
            st.write(f"context (len): {len(contexto_str)}")

debug_page()
