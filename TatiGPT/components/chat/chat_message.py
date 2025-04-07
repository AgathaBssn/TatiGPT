import reflex as rx


# Class that represent a pair of question and answer
class QA(rx.Base):
    question: str
    answer: str


# A component that display a QA object
def message(qa: dict):
    role = qa["role"]
    content = qa["content"]

    # Use rx.cond to determine the background color based on the role
    background_color = rx.cond(
        role == "user",
        rx.color("pink", 7),
        rx.color("lime", 7),
    )

    return rx.box(
        rx.markdown(
            content,
            background_color=background_color,
        ),
        padding="1em",
        margin="1em",
    )