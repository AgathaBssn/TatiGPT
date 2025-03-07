import reflex as rx

from TatiGPT.components.sidebar import lateral_menu, DrawerState
from TatiGPT.components.chat.chat_thread import chat_thread
from TatiGPT.components.chat.chat_state import ChatState


@rx.page(
        route="/tatiGPT", 
        title="AI Chat", 
        description="Chat with TatiGPT",
        )
def ai_chat()-> rx.Component:
    return (
        lateral_menu(),
        rx.container(
            rx.box(
                "AI Chat",
                chat_thread(),
                padding="2em",
                margin="2em",
                background_color=rx.color("pink", 7),
            ),
            rx.form(
                rx.input(
                    placeholder="Type your message here...",
                    enter_key_submit=True,
                    on_change=ChatState.set_current_user_input(),
                    value=ChatState.current_user_input,
                    width="100%",
                ),
                on_submit=ChatState.handle_user_input(),
            ),
            padding_left=rx.cond(DrawerState.is_open, "20%", "0%"),
            on_mount=ChatState.on_load(),
        ),
    )
