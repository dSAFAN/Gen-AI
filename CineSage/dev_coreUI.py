import streamlit as st
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel
from typing import List, Optional
from langchain_core.output_parsers import PydanticOutputParser 
from dotenv import load_dotenv

# 1. Load environment variables
load_dotenv()

# 2. Configure Streamlit Web Page layout
st.set_page_config(page_title="Pydantic Extractor", page_icon="🤖")
st.title("🤖 Structured Pydantic Extraction UI")
st.write("Extract strongly-typed data structures from unstructured text blocks.")

# 3. Initialize Model
model = ChatMistralAI(model="mistral-small-2603")

# 4. Create Schema (Exactly matching your core structure)
class Movie(BaseModel):
    title: str
    release_year: Optional[int]
    genre: List[str]
    director: Optional[str]
    cast: List[str]
    rating: Optional[float]
    summary: str

# 5. Create Parser
parser = PydanticOutputParser(pydantic_object=Movie)

# 6. Set Up Prompt Template
prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
    Extract movie information from the paragrapgh
    {format_instructions}
"""
    ),
    ("human", "{paragraph}")
])

# 7. Streamlit Input Area
para = st.text_area(
    label="Provide your paragraph:", 
    height=200, 
    placeholder="Paste your unstructured movie review here..."
)

# 8. Execution Logic Trigger
if st.button("Extract & Parse Structure", type="primary"):
    if not para.strip():
        st.error("The paragraph input field cannot be empty.")
    else:
        with st.spinner("Invoking model and running Pydantic parser..."):
            try:
                # Format final prompt strings
                final_prompt = prompt.invoke({
                    "paragraph": para, 
                    "format_instructions": parser.get_format_instructions()
                })
                
                # Fetch output string from Mistral
                response = model.invoke(final_prompt)
                
                # Convert the raw JSON string into the typed Pydantic object
                movie_data = parser.parse(response.content)
                
                st.success("Extraction and parsing successful!")
                
                # UI Display matching your two terminal print targets
                st.subheader("1. Raw LLM Content (JSON String Output)")
                st.code(response.content, language="json")
                
                st.subheader("2. Instantiated Pydantic Object Representation")
                st.write(movie_data)
                
            except Exception as e:
                st.error(f"An error occurred: {e}")