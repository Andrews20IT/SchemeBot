from flask import Flask, render_template, request
from openai import OpenAI

app = Flask(__name__)

client = OpenAI(api_key="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")

@app.route('/', methods=['GET', 'POST'])
def home():
    response = None
    if request.method == 'POST':
        prompt = request.form['prompt']
        response = generate_response(prompt)
        # print(response)
    return render_template('index.html', response=response)

def generate_response(prompt):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant"},
                {"role": "user", "content": prompt}
            ]
        )
        # return response.choices[0].message
        response = response.choices[0].message
        message_content = response.content
        return message_content
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(debug=True)
