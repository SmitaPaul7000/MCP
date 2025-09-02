
import streamlit as st
import asyncio
from router import route_query
from utils import stream_text

st.set_page_config(page_title="LangGraph Router Chat")

if "chat" not in st.session_state:
    st.session_state.chat = []

st.title("LangGraph Router Chat with Memory & Streaming")

for role, msg in st.session_state.chat:
    with st.chat_message(role):
        st.markdown(msg)

if user_input := st.chat_input("Ask about RISK, RAS, or ICAP"):
    st.session_state.chat.append(("user", user_input))
    with st.chat_message("assistant"):
        placeholder = st.empty()
        async def run():
            resp = await route_query(user_input)
            text = resp["answer"]
            out = ""
            async for chunk in stream_text(text):
                out += chunk
                placeholder.markdown(out)
        asyncio.run(run())
    st.session_state.chat.append(("assistant", resp["answer"]))