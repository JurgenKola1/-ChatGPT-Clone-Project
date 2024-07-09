from flask import Flask, request, render_template
import openai
import config

# Initialize the OpenAI API key
openai.api_key = config.API_KEY
print("HI")

# Initialize the Flask app
app = Flask(__name__)

# Initialize the conversation history
conversation_history = []

@app.route("/")
def index():
    """Render the main page of the chatbot."""
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    """Handle user messages and return AI responses."""
    user_text = request.args.get('msg')
    model_engine = "gpt-3.5-turbo"

    # Append user message to conversation history
    conversation_history.append({"role": "user", "content": user_text})

    # Generate response using OpenAI API
    response = openai.ChatCompletion.create(
        model=model_engine,
        messages=conversation_history
    )

    # Extract AI response from the API response
    ai_response = response["choices"][0]["message"]["content"]

    # Append AI response to conversation history
    conversation_history.append({"role": "assistant", "content": ai_response})

    # Return the AI response to the user
    return ai_response

if __name__ == "__main__":
    app.run(debug=True)
