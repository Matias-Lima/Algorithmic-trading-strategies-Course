import streamlit as st
from utils import cria_chain_conversa

def sidebar():
    """Renderiza a sidebar para inicializar ou atualizar o ChatBot."""
    if 'chain' in st.session_state:
        label_botao = 'Atualizar ChatBot'
    else:
        label_botao = 'Inicializar ChatBot'

    if st.button(label_botao, use_container_width=True):
        try:
            with st.spinner('Inicializando o ChatBot...'):
                cria_chain_conversa()
            st.success('ChatBot pronto!')
            # Mantemos o rerun APENAS aqui (na inicialização/atualização do bot),
            # pois recria toda a chain/memória e precisa re-renderizar a página.
            st.rerun()
        except Exception as e:
            st.error(f'Erro ao inicializar o ChatBot: {e}')

def _render_historico(chain):
    """Renderiza histórico armazenado na memória do chain."""
    memory = getattr(chain, 'memory', None)
    if memory is None:
        st.error('Erro: Memória do chatbot não encontrada.')
        st.stop()

    try:
        mensagens = memory.load_memory_variables({}).get('chat_history', [])
    except Exception as e:
        st.error(f'Erro ao carregar o histórico do chat: {e}')
        st.stop()

    container = st.container()
    for mensagem in mensagens:
        # Compatibilidade: mensagem pode ser LangChain Message ou dict
        tipo = getattr(mensagem, 'type', None)
        conteudo = getattr(mensagem, 'content', None)
        if isinstance(mensagem, dict):
            tipo = mensagem.get('type', tipo)
            conteudo = mensagem.get('content', conteudo)

        # Normaliza tipo
        if tipo not in ['ai', 'human']:
            # Em versões recentes, o tipo costuma ser 'human'/'ai'.
            # Se vier vazio ou outro, tratamos como 'ai' por padrão.
            tipo = 'ai'

        if conteudo:
            container.chat_message(tipo).markdown(conteudo)

    return container

def chat_window():
    """Renderiza a janela de chat principal."""
    st.header('🤖 Bem-vindo ao Chat', divider=True)

    if 'chain' not in st.session_state:
        st.error('O chatbot não foi inicializado corretamente! Clique no botão ao lado para começar.')
        st.stop()

    chain = st.session_state['chain']

    # 1) Renderiza histórico já salvo
    container = _render_historico(chain)

    # 2) Campo de entrada do usuário (FORA do loop de histórico)
    nova_mensagem = st.chat_input('Converse com seus documentos...')

    if nova_mensagem:
        # Mostra imediatamente a mensagem do usuário
        container.chat_message('human').markdown(nova_mensagem)

        with st.spinner('Gerando resposta...'):
            try:
                # Para ConversationalRetrievalChain, a chave padrão é "question"
                resposta = chain.invoke({'question': nova_mensagem})

                # Resposta costuma vir em resposta['answer']; em alguns casos pode ser 'result'
                if isinstance(resposta, dict):
                    resposta_txt = (
                        resposta.get('answer')
                        or resposta.get('result')
                        or str(resposta)
                    )
                else:
                    resposta_txt = str(resposta)

                st.session_state['ultima_resposta'] = resposta

                # Renderiza resposta do assistente
                container.chat_message('ai').markdown(resposta_txt)

                # ⚠️ Importante: NÃO chamar st.rerun() aqui.
                # Deixe a página como está para que a mensagem permaneça visível.
            except Exception as e:
                st.session_state['ultima_resposta'] = None
                container.chat_message('ai').markdown(f'❌ Erro ao gerar resposta: {e}')
        # Sem rerun aqui!

def main():
    with st.sidebar:
        sidebar()
    chat_window()

if __name__ == '__main__':
    main()
