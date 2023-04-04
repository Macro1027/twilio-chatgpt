import openai
from dotenv import load_dotenv
from twilio.rest import Client
import os

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")

starting_condition1 = "When it comes to writing content, two factors are crucial, “perplexity” and “burstiness.” Perplexity measures the complexity of text. Separately, burstiness compares the variations of sentences. Humans tend to write with greater burstiness, for example, with some longer or complex sentences alongside shorter ones. AI sentences tend to be more uniform. Therefore, when writing the following content I am going to ask you to create, I need it to have a good amount of perplexity and burstiness. Do you understand?”"
starting_condition2 = "As a drunk man, answer the following:"
conversation = [{"role": "system", "content": starting_condition1}]

def chatbot_response(user_prompt: str):
    global conversation
    if user_prompt.lower() == "clear":
        conversation = [{"role": "system", "content": starting_condition1}]
        return {
            'status': 1,
            'response': {'content': 'Context cleared. Please ask me anything :)'}
        }
    conversation.append({"role": "user", "content": user_prompt})
    try:
        response = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages=conversation,
            temperature=0.9,
        )
        conversation.append(response.choices[0]['message'])
        return {
            'status': 1,
            'response': response.choices[0]['message']
        }
    except:
        return {
            'status': 0,
            'response': ''
        }



client = Client(account_sid, auth_token)

def send_message(to: str, message: str) -> None:

    _ = client.messages.create(
        from_=os.getenv('FROM'),
        body=message,
        to=to
    )
    
# while True:
#     prompt = input('You: ')
#     if prompt.lower() == "clear":
#         conversation = [{"role": "user", "content": starting_condition2}]
#         print("Context cleared.")
#         continue
#     elif prompt.lower() == "quit":
#         break
#     conversation.append({"role": "user", "content": prompt})
    
#     response = chatbot_response()["choices"][0]["message"]['content']
#     conversation.append({"role": "assistant", "content": response})
#     print("AI: ", response)


