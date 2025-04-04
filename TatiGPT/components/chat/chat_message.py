import reflex as rx


# Class that represent a pair of question and answer
class QA(rx.Base):
    question: str
    answer: str


# A component that display a QA object
def message(qa: QA):
    return rx.box(
        rx.markdown(
            qa.question,
            background_color=rx.color("pink", 7),
        ),
        rx.markdown(
            qa.answer,
            background_color=rx.color("lime", 7),
        ),
        padding="1em",
        margin="1em",
    )
