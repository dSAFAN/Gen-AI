from langchain_mistralai import ChatMistralAI
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from dotenv import load_dotenv
load_dotenv()


model_mistral = ChatMistralAI(model = "mistral-small-2603")
print("Choose your AI Style")
print("Enter 1 for Sad")
print("Enter 2 for angry")
print("Enter 3 for funny")

choice = int(input("Enter AI Style : "))
if choice == 1:
    mode = "You are a sad AI agent and respond to every chat in a sad way."
elif choice == 2:
    mode = "You are a angry AI agent and respond to every chat in a angry way."
elif choice == 3:
    mode = "You are a funny AI agent and respond to every chat in a funny way."    

messages = [
    SystemMessage(content = mode )
]

print("------------- Welcome to our test AI bsot, enter 0 to exit ------------------")
while True:

    prompt = input("You : ")
    messages.append(HumanMessage(content = prompt))
    
    if prompt == "0":
        print("You Left the chat")
        break
    
    response = model_mistral.invoke(messages)
    messages.append(AIMessage(response.content))
    print("Bot : ",response.content)