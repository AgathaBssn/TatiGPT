import reflex as rx
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
        self.chat_history.append({"question": self.current_user_input, "answer": "I don't know"})
        self.current_user_input = ""