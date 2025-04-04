import reflex as rx


class DrawerState(rx.State):
    is_open: bool = True

    @rx.event
    def toggle_drawer(self):
        self.is_open = not self.is_open


# drawer content
def drawer_content():
    return rx.drawer.content(
        rx.flex(
            rx.drawer.close(
                rx.box(
                    rx.icon(
                        "arrow-left-from-line",
                        color=rx.color("white", 7),
                    ),
                    on_click=DrawerState.toggle_drawer,
                )
            ),
            rx.link(
                "Link 1",
                href="#test1",
                on_click=DrawerState.toggle_drawer,
            ),
            align_items="start",
            direction="column",
        ),
        height="100%",
        width="20%",
        padding="2em",
        background_color=rx.color("pink", 7),
    )


# component to open drawer
def lateral_menu():
    return rx.drawer.root(
        rx.drawer.trigger(
            rx.box(
                rx.icon(
                    "arrow-right-from-line",
                    color=rx.color("crimson", 7),
                ),
                on_click=DrawerState.toggle_drawer,
            )
        ),
        rx.drawer.overlay(),
        rx.drawer.portal(drawer_content()),
        open=DrawerState.is_open,
        direction="left",
        modal=False,
    )
