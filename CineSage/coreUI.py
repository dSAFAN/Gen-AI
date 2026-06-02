import streamlit as st
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

# 1. Load environment variables
load_dotenv()

# 2. Set up the Streamlit Page Layout
st.set_page_config(page_title="Data Extractor", page_icon="🎬")
st.title("🎬 Movie Review Information Extractor")
st.write("Paste a movie review paragraph below to parse out essential structured details.")

# 3. Initialize the Mistral Model
model = ChatMistralAI(model="mistral-small-2603")

# 4. Define the ChatPromptTemplate (Exactly matching your core rules)
prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
You are an expert data extraction assistant. Your task is to analyze the provided movie review and extract specific attributes about the film.

Strictly adhere to the following rules:

Extract information accurately based ONLY on the provided text.

Do not assume details if they are completely absent from the text (output "Not mentioned" instead).

Please extract the following fields:

Movie Name: The title of the movie.

Director: The director of the film.

Cast: A list of all actors mentioned.

Awards: Any specific awards, nominations, or wins mentioned.

Key Praises: Specific elements the reviewer liked (e.g., acting, directing).

Rating : If rating is mentioned in the review then add but that is individual rating from a single user highlight that, if not mentioned then get it from Ibdm and mention.

Short Summary: A brief, 2-3 sentence objective summary of the review.
"""
    ),
    (
        "human",
        """
Extract information from this paragraph:

{paragraph}

"""
    )
])

# 5. Streamlit Interactive UI Components
para = st.text_area(
    label="Provide your paragraph:", 
    height=250, 
    placeholder="Paste your movie review text here..."
)

# 6. Execution Trigger Button
if st.button("Extract Information", type="primary"):
    if not para.strip():
        st.error("Please paste a paragraph first before extracting.")
    else:
        # Visual loading indicator while the API handles the request
        with st.spinner("Processing text with Mistral AI..."):
            try:
                # Format the prompt using the text area value
                final_prompt = prompt.invoke({"paragraph": para})
                
                # Fetch the completion from the model
                response = model.invoke(final_prompt)
                
                # Render the clean text response to the web UI
                st.success("Extraction Complete!")
                st.subheader("📌 Extracted Details")
                st.markdown(response.content)
                
            except Exception as e:
                st.error(f"An error occurred during extraction: {e}")