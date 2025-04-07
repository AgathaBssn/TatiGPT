import reflex as rx

from config.llm_client import llm_client
from config.logging import logger


class ChatState(rx.State):
    chat_history: list[dict] = []

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

    async def handle_user_input(self):
        # Append the user's input in the new structured format
        self.chat_history.append({
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": self.current_user_input,
                    #"cache_control": {"type": "ephemeral"},
                }
            ],
        })

        self.current_user_input = ""

        # Get the response from the LLM client
        response = await llm_client.get_response(self.chat_history)

        # Append the assistant's response in the new structured format
        self.chat_history.append({
            "role": "assistant",
            "content": response,
        })

        logger.info(f"Chat history: {self.chat_history}")