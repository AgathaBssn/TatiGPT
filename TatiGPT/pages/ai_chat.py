import reflex as rx

from TatiGPT.components.sidebar import lateral_menu


@rx.page(route="/tatiGPT", title="AI Chat", description="Chat with TatiGPT")
def ai_chat():
    return (
        lateral_menu(),
        rx.container(
            rx.box(
                "AI Chat",
                padding="2em",
                margin="2em",
                background_color=rx.color("pink", 7),
            ),
            padding_left="20%",
        ),
    )
