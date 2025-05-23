import reflex as rx

from config.llm_client import llm_client
from config.logging import logger


class ChatState(rx.State):
    chat_history: dict[str, dict] = {}

    def init_chat_history(self):
        """Initialize the chat history with a context message."""
        self.chat_history["0"] = {
            "role": "system",
            "content": "You are a helpful assistant.\n"
                       "Sometimes you are asked in french or in english, please respond in the same language as the user.\n"
                       "Please respond in markdown format, and if the user asks for code, please use the code block format.\n",
        }

    current_user_input: str = ""

    @rx.event
    def set_current_user_input(self, value: str):
        self.current_user_input = value

    @rx.event
    def clear_chat_history(self):
        self.chat_history = {}

    @rx.event
    async def on_load(self):
        logger.info("ChatState loaded")
        self.clear_chat_history()
        self.init_chat_history()

    @rx.event
    async def add_user_input(self):
        """Add the user message and trigger assistant reply in background."""
        message_id = f"{len(self.chat_history) + 1}"
        self.chat_history[message_id] = {
            "role": "user",
            "content": self.current_user_input,
        }
        self.current_user_input = ""

        # Lancement du traitement en background
        yield ChatState.fetch_response()

    @rx.event(background=True)
    async def fetch_response(self):
        # Do long work outside async with
        chat_history_list = list(self.chat_history.values())
        response = await llm_client.get_response(chat_history_list)

        # Then safely update state
        async with self:
            message_id = f"{len(self.chat_history) + 1}"
            self.chat_history[message_id] = {
                "role": "assistant",
                "content": response,
            }
