import importlib
import os

import reflex as rx

from TatiGPT.pages.ai_chat import ai_chat

app = rx.App(
    theme=rx.theme(
        appearance="light",
        has_background=True,
        radius="large",
        accent_color="crimson",
    )
)

### SECTION adding pages

# default page for route /
app.add_page(ai_chat, route="/", title="Tati GPT")

pages_dir = "TatiGPT/pages"

for filename in os.listdir(pages_dir):
    if filename.endswith(".py"):
        module_name = f"TatiGPT.pages.{filename[:-3]}"
        module = importlib.import_module(module_name)

        # check if there is a rx.page decorator
        if hasattr(module, "page"):
            app.add_page(getattr(module, "page"))
