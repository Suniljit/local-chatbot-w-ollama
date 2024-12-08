from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

template = """
Answer the question below.

Here is the conversion history: {context}

Question: {question}

Answer:
"""

model = OllamaLLM(model="llama3") 
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model # Chain the prompt and model operations


def main():
    # Initialize the context and start the conversation
    context = ""
    print("Welcome! Type 'exit' to end the conversation.")
    
    # Manage the conversation, context and exit condition
    while True:
        user_input = input("User: ")
        if user_input.lower() == "exit": # Exit condition
            break
        
        result = chain.invoke({
            "context": context,
            "question": user_input
        }) # Generate response
        print("Bot: ", result) 
        
        context += f"\nUser: {user_input}\nBot: {result}" # Update the context
        
        
if __name__ == "__main__":
    main()