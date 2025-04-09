import reflex as rx
from TatiGPT.components.chat.chat_state import ChatState

def chat_input_form() -> rx.Component:
    return rx.form(
        rx.input(
            placeholder="Type your message here...",
            enter_key_submit=True,
            on_change=ChatState.set_current_user_input,
            value=ChatState.current_user_input,
            flex=1,
        ),
        rx.button(
            rx.icon(
                "send-horizontal", 
                box_size="1.5em",
                color="crimson"),
            type="submit",
            variant="ghost",
            background_color="none",
        ),
        on_submit=ChatState.add_user_input,
        display="flex",
        gap="7px",
        align_items="center",
    )