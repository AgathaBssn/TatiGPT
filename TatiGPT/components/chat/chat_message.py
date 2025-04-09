import reflex as rx


# Class that represent a pair of question and answer
class QA(rx.Base):
    question: str
    answer: str


# A component that display a QA object
def message(qa: dict) -> rx.Component:
    role = qa["role"]
    content = qa["content"]

    # Skip the system prompt
    return rx.cond(
        role == "system",
        rx.box(),
        rx.box(
        rx.markdown(
            content,
            padding="2px 8px",
            border_radius="4px",
            width="fit-content",
            background_color=rx.cond(
                role == "user", 
                rx.color("red", 2),
                rx.color("ruby", 7),
            ),
        ),
        display="flex",
        justify_content=rx.cond(role == "user", "end", "start"),
        width="100%",
        margin_bottom="8px",
        )
    )
