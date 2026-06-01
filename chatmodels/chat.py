from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_mistralai import ChatMistralAI
load_dotenv()

#model_groq = init_chat_model("groq:llama-3.1-8b-instant")
model_mistral = ChatMistralAI(model = "mistral-small-2603")

#response_groq = model_groq.invoke("List some free AI model Api's that devs can use?")
response_mistral = model_mistral.invoke("List some free AI model Api's that devs can use?")

print(response_mistral.content)