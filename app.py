from flask import Flask, render_template, request, jsonify
import ollama


# modelName = 'tinyllama'
modelName = 'llama3.1'

app = Flask(__name__)

@app.route('/')
def index():
    # return render_template('index.html')
    return render_template('graph.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')

    prompt = f"""System: Respond only with a Python array with at least items, following these guidelines:
Your answer should be a Python list in this format: ["item1", "item2", "item3"]
Do not add any extra words or explanations outside the array.
Only list items that directly answer the question\nUser:{user_message}"""


    print(f"User:{user_message}")

    response = ollama.chat(model=modelName, messages=[
    {
        'role': 'user',
        'content': prompt
    }
    ])
    # print(response['message']['content'])
    chatbot_message = response['message']['content']#f"I got:{user_message}. I give: " + response['message']['content']
    # remove [ and ] and split by comma
    # remove char [
    print(f"Chatbot Message:{chatbot_message}")
    chatbot_message = chatbot_message.replace('"','').replace('[','').replace(']','')
    items = chatbot_message.split(',')
    print(f"Items:{items}")
    return jsonify({'response':items})

if __name__ == '__main__':
    # app.run(debug=True,host='0.0.0.0')#
    app.run(debug=True,port=5002)#


