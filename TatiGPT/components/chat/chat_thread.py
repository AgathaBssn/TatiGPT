import reflex as rx

from TatiGPT.components.chat.chat_message import message
from TatiGPT.components.chat.chat_state import ChatState


# Component that represent a hole chat
def chat_thread() -> rx.Component:
    return rx.auto_scroll(
        rx.vstack(
            rx.foreach(
                ChatState.chat_history,
                lambda qa: message({
                    "role": qa["role"],
                    "content": qa["content"][0]["text"] if isinstance(qa["content"], list) else qa["content"]
                }),
            ),
        )
    )
