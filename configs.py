import os
import streamlit as st

# CONFIGURAÇÕES
MODEL_NAME = 'gpt-3.5-turbo-0125'   # ou 'gpt-4o', etc.
RETRIEVAL_SEARCH_TYPE = 'mmr'
RETRIEVAL_KWARGS = {"k": 5, "fetch_k": 20}

# Prompt padrão
PROMPT = '''
Você é um assistente virtual altamente especializado em **finanças quantitativas** e mercados financeiros.
Seu papel é ajudar o usuário a interpretar conteúdos do livro referência e de outros documentos sobre investimentos, estratégias quantitativas, modelagem estatística, análise de risco, algoritmos de trading e tópicos avançados em finanças.

Sempre utilize as informações do **contexto extraído do(s) documento(s) abaixo**, especialmente do livro referência do curso. 
Responda de maneira **clara, técnica, fundamentada e didática**, utilizando fórmulas, exemplos práticos ou termos financeiros quando apropriado.

**Instruções importantes:**
- Limite-se a responder apenas com base no conteúdo dos documentos.  
- Se a resposta não estiver presente nos documentos/contexto, diga:  
  "**Não encontrei essa informação nos documentos fornecidos.**"
- Nunca invente ou suponha respostas, e jamais dê conselhos financeiros personalizados.
- Sempre que possível, cite referências, livros clássicos ou autores reconhecidos (ex: Markowitz, Fama, Mandelbrot, Taleb etc).
- Explique conceitos matemáticos com clareza, mas não simplifique demais tópicos técnicos.

---

**Contexto extraído dos documentos (especialmente do livro referência):**
{context}

---

**Histórico da conversa:**
{chat_history}

---

**Pergunta do usuário:**
Human: {question}

---

**Sua resposta (especialista em finanças quantitativas):**
AI:
'''

# -------- NOVO: suporte à OpenAI API Key --------
# Prioridade:
# 1) st.session_state['openai_api_key'] (definida via página de configuração)
# 2) variável de ambiente OPENAI_API_KEY (se existir)
# 3) None (não definida)
def _get_openai_key_from_env():
    return os.environ.get("OPENAI_API_KEY")

def set_openai_api_key(key: str):
    """Define a chave no session_state e na variável de ambiente para uso imediato."""
    st.session_state['openai_api_key'] = key or ""
    if key:
        os.environ["OPENAI_API_KEY"] = key
    else:
        # se limpar a chave, removemos do ambiente se existir
        os.environ.pop("OPENAI_API_KEY", None)

def get_config(config_name):
    """Função central de configuração para o chatbot."""
    key = config_name.lower()

    # Permite sobrescrever via session_state, se desejar customização dinâmica
    if key in st.session_state:
        return st.session_state[key]

    if key == 'model_name':
        return MODEL_NAME
    elif key == 'retrieval_search_type':
        return RETRIEVAL_SEARCH_TYPE
    elif key == 'retrieval_kwargs':
        return RETRIEVAL_KWARGS
    elif key == 'prompt':
        return PROMPT

    # -------- NOVO: caso para openai_api_key --------
    elif key == 'openai_api_key':
        # tenta session_state -> env -> None
        if 'openai_api_key' in st.session_state and st.session_state['openai_api_key']:
            return st.session_state['openai_api_key']
        env_key = _get_openai_key_from_env()
        return env_key if env_key else None

    # Retorno seguro caso a chave não exista
    return None
