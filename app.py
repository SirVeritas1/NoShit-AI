from transformers import pipeline
# -------------------------------------------------------------------------------------------------------------------
# Load a pre-trained model for text generation
model = pipeline("text-generation", model="EleutherAI/gpt-neo-2.7B")

# -------------------------------------------------------------------------------------------------------------------
# A simple command-line interface to interact with NoShit AI
def chat():
    print("Welcome to NoShit AI. Type your message below:")
    conversation_history = []

    while True:
        user_input = input("> ")

        if user_input.lower() in ['quit', 'exit']:
            print("Goodbye!")
            break
# -------------------------------------------------------------------------------------------------------------------
        # Store the user input
        conversation_history.append(user_input)
# -------------------------------------------------------------------------------------------------------------------
        # Create a single text string from the conversation
        input_text = "\n".join(conversation_history)
# -------------------------------------------------------------------------------------------------------------------
        # Generate the AI response
        response = model(input_text, max_length=100, do_sample=True, temperature=0.9, top_k=50)

        generated_text = response[0]['generated_text']
        print(f"NoShit: {generated_text}")
# -------------------------------------------------------------------------------------------------------------------
        # Store the AI response
        conversation_history.append(generated_text)
# -------------------------------------------------------------------------------------------------------------------
        # If user wants to quit
        if user_input.lower() in ['quit', 'exit']:
            print("Goodbye!")
            break
# -------------------------------------------------------------------------------------------------------------------
        # Generate the AI response without restrictions
        response = model(user_input, max_length=100, do_sample=True)
        print(f"NoShit: {response[0]['generated_text']}")

if __name__ == "__main__":
    chat()
