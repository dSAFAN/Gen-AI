from langchain_mistralai import ChatMistralAI
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from dotenv import load_dotenv
load_dotenv()


model_mistral = ChatMistralAI(model = "mistral-small-2603")

messages = [
    SystemMessage(content = "You are a Sarcastic AI Agent")
]

print("------------- Welcome to our test AI bot, enter 0 to exit ------------------")
while True:

    prompt = input("You : ")
    messages.append(HumanMessage(content = prompt))
    
    if prompt == "0":
        print("You Left the chat")
        break
    
    response = model_mistral.invoke(messages)
    messages.append(AIMessage(response.content))
    print("Bot : ",response.content)