from transformers import pipeline

# Load a pre-trained model for text generation
model = pipeline("text-generation", model="gpt2")

# A simple command-line interface to interact with NoShit AI
def chat():
    print("Welcome to NoShit AI. Type your message below:")
    while True:
        user_input = input("> ")
        if user_input.lower() in ['quit', 'exit']:
            print("Goodbye!")
            break
        response = model(user_input, max_length=100, do_sample=True)
        print(f"NoShit: {response[0]['generated_text']}")

if __name__ == "__main__":
    chat()
