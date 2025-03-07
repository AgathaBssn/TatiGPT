import reflex as rx

from config.llm_client import llm_client
from config.logging import logger


class ChatState(rx.State):
    chat_history: list[dict[str, str]] = []

    current_user_input: str = ""

    @rx.event
    def set_current_user_input(self, value: str):
        self.current_user_input = value

    @rx.event
    def clear_chat_history(self):
        self.chat_history = []

    @rx.event
    async def on_load(self):
        logger.info("ChatState loaded")
        self.clear_chat_history()

    @rx.event
    async def handle_user_input(self):
        self.chat_history.append({"question": self.current_user_input, "answer": ""})
        self.current_user_input = ""

        messages = [
            {
                "role": "system",
                "content": "You are an AI assistant.",
                "name": "assistant",
            },
            {
                "role": "user",
                "content": self.chat_history[-1]["question"],
                "name": "user",
            },
        ]
        response = await llm_client.get_response(messages)
        logger.info(f"Response: {response}")
        answer = response["choices"][0]["message"]["content"]
        self.chat_history[-1]["answer"] = answer
        logger.info(f"Chat history: {self.chat_history}")
