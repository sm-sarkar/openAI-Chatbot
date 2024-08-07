import groq
import streamlit as st

with st.sidebar:
    st.title('🤖💬 Groq Chatbot')
    if 'GROQ_API_KEY' in st.secrets:
        st.success('API key already provided!', icon='✅')
        groq.api_key = st.secrets['GROQ_API_KEY']
    else:
        groq.api_key = st.text_input('Enter Groq API token:', type='password')
        if not groq.api_key:
            st.warning('Please enter your credentials!', icon='⚠️')
        else:
            st.success('Proceed to entering your prompt message!', icon='👉')

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""

        # Use Groq API for chat completion
        response = groq.ChatCompletion.create(
            model="llama3-8b-8192",  # Adjust this if Groq uses different model identifiers
            messages=[{"role": m["role"], "content": m["content"]} for m in st.session_state.messages]
        )

        full_response = response['choices'][0]['message']['content']
        message_placeholder.markdown(full_response)
    st.session_state.messages.append({"role": "assistant", "content": full_response})
