import reflex as rx

from TatiGPT.components.chat.chat_state import ChatState
from TatiGPT.components.chat.chat_thread import chat_thread
from TatiGPT.components.sidebar import DrawerState, lateral_menu


@rx.page(
    route="/tatiGPT",
    title="AI Chat",
    description="Chat with TatiGPT",
)

def ai_chat() -> rx.Component:
    return (
        lateral_menu(),
        rx.container(
            rx.box(
                chat_thread(),
                padding="2em",
                margin="2em",
                overflow_y="auto",  
                height="calc(100vh - 100px)", 
            ),
            rx.box(
                rx.form(
                    rx.input(
                        placeholder="Type your message here...",
                        enter_key_submit=True,
                        on_change=ChatState.set_current_user_input,
                        value=ChatState.current_user_input,
                        width="100%",
                    ),
                    on_submit= ChatState.add_user_input,
                ),
                position="fixed", 
                bottom="0",
                left=rx.cond(DrawerState.is_open, "20%", "10%"),
                width=rx.cond(DrawerState.is_open, "80%", "80%"), 
                padding="1em",
                background_color="white", 
                box_shadow="0 -2px 5px rgba(0, 0, 0, 0.1)",
            
            ),
            size="4",
            padding="0",
            padding_left=rx.cond(DrawerState.is_open, "20%", "0%"),
            transition="padding-left 0.3s ease",
            on_mount=ChatState.on_load,
        ),
    )
