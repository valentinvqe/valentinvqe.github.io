import openai 

openai.api_key = open("/Users/valentinvaquie/anaconda3/CHAT GPT/key.txt", "r").read().strip()

message_history = []

def chat(inp , role = "user"): 
    message_history.append({'role': 'user', 'content': f'{inp}'})
    

    complétion = openai.ChatCompletion.create(
    model = "gpt-3.5-turbo",
    messages=message_history,
    )
    
    reply_content = complétion.choices[0].message.content
    
    message_history.append({'role': 'assistant', 'content': f'{reply_content}'})


    return reply_content



user_input = input("> ")

for i in range (2) : 
    
    user_input = input("> ")
    
    print("user input: " + user_input)
    
    print(chat(user_input)) 
    print()

