import google.generativeai as genai

# Configure Gemini API
genai.configure(api_key="API KEY")
model = genai.GenerativeModel("gemini-1.5-flash")

def get_user_input():
    print("Choose prompting type:")
    print("1. Zero-Shot Prompting")
    print("2. Few-Shot Prompting")
    print("3. Chain-of-Thought (CoT) Prompting")

    choice = input("Enter the number (1/2/3): ").strip()

    if choice == "1":
        prompt = input("\nEnter your zero-shot prompt: ").strip()

    elif choice == "2":
        prompt = input("\nEnter the main prompt: ").strip()
        examples = []
        print("\nEnter a few examples (Type 'done' when finished):")
        while True:
            example = input("Example: ").strip()
            if example.lower() == "done":
                break
            examples.append(example)
        
        example_text = "\n".join(examples)
        prompt = f"Examples:\n{example_text}\n\nNow, {prompt}"

    elif choice == "3":
        print("\nChoose CoT prompting approach:")
        print("a. Provide an example of reasoning")
        print("b. Automatically add 'Describe your reasoning in steps'")
        cot_choice = input("Enter the alphabet (a/b): ").strip()

        prompt = input("\nEnter your CoT prompt: ").strip()

        if cot_choice == "a":
            reasoning_example = input("\nEnter an example of complex reasoning: ").strip()
            prompt = f"Example:\n{reasoning_example}\n\nNow, {prompt}"
        else:
            prompt += "\n\nDescribe your reasoning in steps."

    else:
        print("Invalid choice. Please try again.")
        return get_user_input()

    return prompt

# Generate response using Gemini API
def generate_response(prompt):
    response = model.generate_content(prompt)
    print("\nResponse:\n", response.text)

# Main function
def main():
    prompt = get_user_input()
    generate_response(prompt)

if __name__ == "__main__":
    main()
