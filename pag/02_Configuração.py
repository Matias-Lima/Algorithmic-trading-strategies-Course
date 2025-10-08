import json
import streamlit as st
from configs import get_config, set_openai_api_key
from utils import cria_chain_conversa

def config_page():
    st.header('Página de configuração', divider=True)

    # ------------------ NOVO: Seção para OpenAI API Key ------------------
    with st.expander('🔑 Configurar OpenAI API Key', expanded=True):
        # tenta preencher com o que já estiver no session_state/env (mas sem exibir)
        existing_key = get_config('openai_api_key') or ""
        placeholder = "Cole sua chave aqui (sk-...)"
        api_key_input = st.text_input(
            'OpenAI API Key',
            value="",
            type="password",
            placeholder=placeholder,
            help="A chave ficará disponível apenas nesta sessão. "
                 "Opcionalmente será exportada para a variável de ambiente OPENAI_API_KEY enquanto o app estiver rodando."
        )

        cols = st.columns([1,1,1])
        with cols[0]:
            if st.button('Salvar chave', use_container_width=True):
                set_openai_api_key(api_key_input.strip())
                st.success('Chave definida para esta sessão.')
        with cols[1]:
            if st.button('Limpar chave', use_container_width=True):
                set_openai_api_key("")
                st.info('Chave removida desta sessão e do ambiente.')
        with cols[2]:
            if existing_key:
                st.caption('✅ Uma chave já está configurada nesta sessão/ambiente.')
            else:
                st.caption('⚠️ Nenhuma chave configurada no momento.')

    # ------------------ Configurações já existentes ------------------
    model_name = st.text_input('Modifique o modelo', value=get_config('model_name'))
    retrieval_search_type = st.text_input('Modifique o tipo de retrieval', value=get_config('retrieval_search_type'))
    retrieval_kwargs = st.text_input('Modifique os parâmetros de retrieval', value=json.dumps(get_config('retrieval_kwargs')))
    prompt = st.text_area('Modifique o prompt padrão', height=350, value=get_config('prompt'))

    if st.button('Salvar parâmetros', use_container_width=True):
        retrieval_kwargs = json.loads(retrieval_kwargs.replace("'", '"'))
        st.session_state['model_name'] = model_name
        st.session_state['retrieval_search_type'] = retrieval_search_type
        st.session_state['retrieval_kwargs'] = retrieval_kwargs
        st.session_state['prompt'] = prompt
        st.rerun()
    
    if st.button('Atualizar ChatBot', use_container_width=True):
        st.success('Inicializando o ChatBot...')
        cria_chain_conversa()
        st.rerun()

config_page()
