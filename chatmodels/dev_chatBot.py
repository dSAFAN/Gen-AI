from langchain_mistralai import ChatMistralAI
from dotenv import load_dotenv
load_dotenv()


model_mistral = ChatMistralAI(model = "mistral-small-2603")

print("------------- Welcome to our test AI bot, enter 0 to exit ------------------")
while True:

    prompt = input("You : ")
    if prompt == "0":
        print("You Left the chat")
        break

    response = model_mistral.invoke(prompt)
    print("Bot : ",response.content)