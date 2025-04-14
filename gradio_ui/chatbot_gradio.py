import gradio as gr
import requests
import json

# URL của Rasa API (thường là http://localhost:5005)
rasa_url = "http://rasa_core:5005/webhooks/rest/webhook"


def send_message(message):
    """Gửi message đến Rasa và nhận phản hồi"""
    payload = {
        "sender": "user",
        "message": message
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(rasa_url, data=json.dumps(payload), headers=headers)

    # Trả về câu trả lời từ bot
    if response.status_code == 200:
        return response.json()[0]["text"]
    else:
        return "Error: Unable to get a response from the bot."


# Tạo giao diện chatbot với Gradio
chatbot = gr.Interface(fn=send_message, inputs="text", outputs="text", live=True, title="Rasa Chatbot")

# Chạy ứng dụng Gradio
if __name__ == "__main__":
    chatbot.launch(server_name="0.0.0.0", server_port=7860, favicon_path=None)

