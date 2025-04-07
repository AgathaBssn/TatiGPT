import reflex as rx

from TatiGPT.components.chat.chat_message import message
from TatiGPT.components.chat.chat_state import ChatState


# Component that represent a hole chat
def chat_thread() -> rx.Component:
    return rx.auto_scroll(
        rx.vstack(
            rx.foreach(
            ChatState.chat_history,
            lambda m: message(m[1])  # m[1] is the value, m[0] is the key
        ),
            align_items="start",  # Align messages to the start
            spacing="1",  # Add spacing between messages
        )
    )
