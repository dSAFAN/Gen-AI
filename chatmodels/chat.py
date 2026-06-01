from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

load_dotenv()

model = init_chat_model("groq:llama-3.1-8b-instant")
response = model.invoke("List some free AI model Api's that devs can use?")

print(response.content)