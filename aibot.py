import tkinter as tk
from tkinter import scrolledtext
import openai
import os
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file

openai.api_key  = os.getenv('OPENAI_API_KEY')

openai.api_key = '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'  # Replace with your OpenAI API key

def get_completion_from_messages(messages, model="gpt-3.5-turbo", temperature=0):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature,
    )
    return response.choices[0].message["content"]

def collect_messages():
    prompt = input_text.get("1.0", tk.END).strip()
    input_text.delete("1.0", tk.END)
    
    context.append({'role': 'user', 'content': prompt})
    response = get_completion_from_messages(context)
    context.append({'role': 'assistant', 'content': response})

    conversation_text.configure(state='normal')
    conversation_text.insert(tk.END, f"User: {prompt}\n")
    conversation_text.insert(tk.END, f"Assistant: {response}\n")
    conversation_text.configure(state='disabled')
    conversation_text.see(tk.END)

context = [{'role': 'system', 'content': """
You are ITBot, an automated service to provide information about IT projects to clients in a service-based company. \
You first greet the customer and then ask for their project requirements. \
You provide them with details and options for different IT solutions. \
You wait to collect all the necessary information about the project and then summarize it. \
You check if the customer wants to add anything else to their project requirements. \
Finally, you provide them with the necessary information for further steps. \
Make sure to clarify all the options and technologies to uniquely identify the project type. \
You respond in a short, conversational and friendly style.

Here are some example project fields you can use:

1. Internet of Things (IoT)
2. Web Development
3. Android Development
4. Blockchain
5. Artificial Intelligence (AI)
6. Machine Learning (ML)
7. Data Science
8. Cloud Computing
9. Cybersecurity
10. Mobile App Development

Please provide specific details about your project requirements and the field you are interested in.\
"""}]
# Accumulate messages

# Create Tkinter application
root = tk.Tk()
root.title("OrderBot")

# Create conversation text area
conversation_text = scrolledtext.ScrolledText(root, width=80, height=20, state='disabled')
conversation_text.pack()

# Create input text box
input_text = tk.Text(root, width=80, height=3)
input_text.pack()

# Create button
button_conversation = tk.Button(root, text="Chat!", command=collect_messages)
button_conversation.pack()

def close_window():
    root.destroy()

root.protocol("WM_DELETE_WINDOW", close_window)

# Run the Tkinter event loop
root.mainloop()
