import streamlit as st
from langchain_mistralai import ChatMistralAI
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from dotenv import load_dotenv

# 1. Load environment variables
load_dotenv()

# 2. Set up the Streamlit Page
st.title("Mistral AI Persona Chat")
st.sidebar.header("Choose your AI Style")

# 3. Handle Persona Selection
style_choice = st.sidebar.radio(
    "Select a persona:",
    ("Sad", "Angry", "Funny")
)

# Map the choice to the system prompt
if style_choice == "Sad":
    mode = "You are a sad AI agent and respond to every chat in a sad way."
elif style_choice == "Angry":
    mode = "You are an angry AI agent and respond to every chat in an angry way."
elif style_choice == "Funny":
    mode = "You are a funny AI agent and respond to every chat in a funny way."

# 4. Initialize the Model
model_mistral = ChatMistralAI(model="mistral-small-2603")

# 5. Handle Memory (Session State)
# If the messages list doesn't exist yet, OR if the user changes the persona in the sidebar, reset the chat.
if "messages" not in st.session_state or st.session_state.get("current_style") != style_choice:
    st.session_state.current_style = style_choice
    st.session_state.messages = [SystemMessage(content=mode)]

# 6. Display Chat History
# We loop through session_state.messages (skipping the first item, which is the hidden SystemMessage)
for msg in st.session_state.messages[1:]:
    if isinstance(msg, HumanMessage):
        with st.chat_message("user"):
            st.markdown(msg.content)
    elif isinstance(msg, AIMessage):
        with st.chat_message("assistant"):
            st.markdown(msg.content)

# 7. Handle New User Input
if prompt := st.chat_input("Type your message here..."):
    # Immediately display the user's message
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Add user message to our memory
    st.session_state.messages.append(HumanMessage(content=prompt))
    
    # Get the AI response
    with st.chat_message("assistant"):
        # A quick spinner so the user knows it is thinking
        with st.spinner("Thinking..."):
            response = model_mistral.invoke(st.session_state.messages)
            st.markdown(response.content)
            
    # Add AI response to our memory
    st.session_state.messages.append(AIMessage(content=response.content))