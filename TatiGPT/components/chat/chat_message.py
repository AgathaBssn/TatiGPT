import reflex as rx


# Class that represent a pair of question and answer
class QA(rx.Base):
    question: str
    answer: str


# A component that display a QA object
def message(qa: dict) -> rx.Component:
    role = qa["role"]
    content = qa["content"]

    return rx.box(
        rx.markdown(
            content,
            background_color=rx.cond(
                role == "user",
                rx.color("pink", 7),
                rx.color("lime", 7),
            ),
        ),
        padding="8px",
    )
