from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
load_dotenv()

model = ChatMistralAI(model = "mistral-small-2603")
prompt = ChatPromptTemplate.from_messages([(
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

Rating : If rating is mentioned by user then add but that is individual rating from a single user, if not mentioned then get it from Ibdm and mention.

Short Summary: A brief, 2-3 sentence objective summary of the review.
"""
),
("human",
"""
Extract information from this paragraph:

{paragraph}

""")
])

para = input("Provide your paragrapgh : ")
final_prompt = prompt.invoke({"paragraph" : para})

response = model.invoke(final_prompt)
print(response.content)