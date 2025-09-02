# streamlit_app.py
import streamlit as st
import asyncio
from router import route_query
from memory import load_memory

# App title
st.set_page_config(page_title="LangGraph Router Chat", page_icon="🤖")
st.title("LangGraph Router Chat (FakeLLM + Memory)")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Sidebar shows stored memory (diffs per agent)
st.sidebar.header("Agent Memory (last data + diffs)")
mem_data = load_memory()
if mem_data:
    for agent, value in mem_data.items():
        st.sidebar.write(f"**{agent.upper()}** → {value}")
else:
    st.sidebar.write("No memory stored yet.")

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Input field for user
if prompt := st.chat_input("Ask about RISK ID, RAS, or ICAP..."):
    # Add user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Process async agent response
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        message_placeholder.markdown("⏳ Thinking...")

        async def get_response():
            # Router picks the right agent (async execution)
            result = await route_query(prompt)
            return result.get("answer", "⚠️ No answer generated")

        response = asyncio.run(get_response())

        # Display response
        message_placeholder.markdown(response)

    # Save assistant reply
    st.session_state.messages.append({"role": "assistant", "content": response})
