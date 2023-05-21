from chatbot.app import app
import os

PORT = os.getenv('PORT')

if __name__ == "__main__":
    app.run(port=int(os.environ.get("PORT", PORT)),host='0.0.0.0',debug=True)