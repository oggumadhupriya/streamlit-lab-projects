import streamlit as st
import time

st.set_page_config(page_title="Simple Chatbot",layout="centered")

st.title("💬 Simple Chatbot")
st.write("Ask me something about Python or Streamlit!")

if "messages" not in st.session_state:
    st.session_state.messages=[]

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

prompt=st.chat_input("Type your message...")

if prompt:
    st.session_state.messages.append(
        {"role":"user","content":prompt}
    )

    with st.chat_message("user"):
        st.write(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Assistant is typing..."):
            time.sleep(1)

            if "python" in prompt.lower():
                reply=(
                    "Python is a popular programming language "
                    "for AI and data science."
                )
            elif "streamlit" in prompt.lower():
                reply=(
                    "Streamlit is a Python framework for "
                    "building interactive web applications."
                )
            else:
                reply=(
                    f"You said:'{prompt}'. "
                    "I'm a demo chatbot!"
                )

        st.write(reply)

    st.session_state.messages.append(
        {"role":"assistant","content":reply}
    )

if st.session_state.messages:
    chat_text="\n".join(
        f"{msg['role']}:{msg['content']}"
        for msg in st.session_state.messages
    )

    st.download_button(
        label="Download Chat History",
        data=chat_text,
        file_name="chat_history.txt",
        mime="text/plain"
    )

if st.button("Clear Chat"):
    st.session_state.messages=[]
    st.rerun()