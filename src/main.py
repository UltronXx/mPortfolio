import flet as ft
from flet import (
    Page, app,
    Container,
    Column, Row,
    Image,
    Text, TextStyle,
    FontWeight,
    MainAxisAlignment,
    CrossAxisAlignment,
)

from pathlib import Path
from assets.shared.colors import *

assets = f"{Path(__file__).parent}/src/assets"


class NavBar(Column):
    def __init__(self):
        super().__init__()

        self.nav_bar_links: list[str] = ["Home", "Projects", "Ideas", "About"]
        self.nav_bar = Row(
            controls=[],
            alignment=MainAxisAlignment.CENTER,
            spacing=50,
        )

        for nav_bar_link in self.nav_bar_links:
            self.nav_bar.controls.append(
                Text(
                    value=f"{nav_bar_link}",
                    color=black,
                    size=14,
                    weight=FontWeight.W_500,
                    style=TextStyle(
                        letter_spacing=-0.3
                    )
                )
            )

        self.background: Container = Container(
            height=65,
            bgcolor=white_mid,
            content=self.nav_bar
        )

        self.controls = [
            self.background
        ]


class ContentBody(Column):
    def __init__(self):
        super().__init__()

        #self.horizontal_alignment = CrossAxisAlignment.CENTER
        self.width = 780

        self.controls = [
            Container(
                bgcolor="green",
                content=Column(
                    expand=True,
                    controls=[
                        Column(height=50),
                        # Hero Section
                        Container(
                            bgcolor="blue",
                            height=480,
                            alignment=ft.alignment.center,
                            content=Column(
                                alignment=MainAxisAlignment.CENTER,
                                horizontal_alignment=CrossAxisAlignment.CENTER,
                                controls=[
                                    Text(
                                        value="Site Under\nConstruction",
                                        weight=FontWeight.W_800,
                                        size=70, text_align=ft.TextAlign.CENTER,
                                        style=TextStyle(letter_spacing=-3, height=1),
                                    ),
                                    Column(height=10),
                                    Text(
                                        value="Your patience,\nis everything we need.",
                                        color=black,
                                        weight=FontWeight.W_500,
                                        size=15,
                                        style=TextStyle(letter_spacing=-0.3, height=1.2),
                                        text_align=ft.TextAlign.CENTER
                                    ),
                                ]
                            )
                        ),
                        # Section Two
                        Column(
                            horizontal_alignment=CrossAxisAlignment.CENTER,
                            controls=[
                                # Space
                                Column(height=80),
                                Text(value="Header here"),
                                Row(
                                    vertical_alignment=CrossAxisAlignment.START,
                                    height=300,
                                    controls=[
                                        Container(
                                            expand=True,
                                            bgcolor="pink",
                                            content=Column(
                                                alignment=MainAxisAlignment.SPACE_BETWEEN,
                                                controls=[
                                                    Container(
                                                        bgcolor="blue",
                                                        alignment=ft.alignment.center,
                                                        expand=True,
                                                        content=Column(
                                                            alignment=MainAxisAlignment.CENTER,
                                                            horizontal_alignment=CrossAxisAlignment.CENTER,
                                                            controls=[
                                                                Text(
                                                                    value="Less Is More",
                                                                    text_align=ft.TextAlign.CENTER,
                                                                    weight=FontWeight.W_700,
                                                                    size=30,
                                                                    style=TextStyle(letter_spacing=-1)
                                                                ),
                                                                Text(
                                                                    value="A minimalist approach to\n"
                                                                     "everything you do.",
                                                                    text_align=ft.TextAlign.CENTER,
                                                                    weight=FontWeight.W_500,
                                                                    style=TextStyle(letter_spacing=-0.4)
                                                                ),
                                                            ]
                                                        )
                                                    ),
                                                    Container(
                                                        alignment=ft.alignment.center,
                                                        bgcolor="brown",
                                                        padding=ft.padding.only(top=40, bottom=40),
                                                        content=Text(
                                                            value="Just for you"
                                                        )
                                                    )
                                                ]
                                            )
                                        ),
                                        Container(
                                            expand=True,
                                            gradient=ft.LinearGradient(
                                                begin=ft.alignment.top_left,
                                                end=ft.alignment.bottom_right,
                                                colors=["blue", "green"]
                                            ),
                                            content=Image(src="imgs/phone.png")
                                        )
                                    ]
                                )
                            ]
                        ),
                        # Section Three
                        Column(
                            horizontal_alignment=CrossAxisAlignment.CENTER,
                            controls=[
                                # Space
                                Column(height=80),
                                Text(value="See Our next moves"),
                                Container(
                                    height=400,
                                    bgcolor="blue",
                                    #alignment=ft.alignment.center,
                                    content=Row(
                                        alignment=MainAxisAlignment.CENTER,
                                        spacing=40,
                                        controls=[
                                            Column(
                                                alignment=MainAxisAlignment.CENTER,
                                                horizontal_alignment=CrossAxisAlignment.CENTER,
                                                controls=[
                                                    Text(value="Get In Touch"),
                                                    Text(value="Let's cross Paths"),
                                                    # Space
                                                    Column(height=6),
                                                    # Social Media links
                                                    Column(
                                                        controls=[
                                                            Row(
                                                                controls=[
                                                                    Container(
                                                                        bgcolor="pink",
                                                                        alignment=ft.alignment.center,
                                                                        height=36,
                                                                        width=120,
                                                                        content=Text("Pinterest")
                                                                    ),
                                                                    Container(
                                                                        bgcolor="brown",
                                                                        alignment=ft.alignment.center,
                                                                        height=36,
                                                                        width=120,
                                                                        content=Text("Instagram")
                                                                    ),
                                                                ]
                                                            ),
                                                            Row(
                                                                controls=[
                                                                    Column(width=20),
                                                                    Container(
                                                                        alignment=ft.alignment.center,
                                                                        bgcolor="brown",
                                                                        height=36,
                                                                        width=120,
                                                                        content=Text("Email")
                                                                    ),
                                                                    Container(
                                                                        bgcolor="pink",
                                                                        alignment=ft.alignment.center,
                                                                        height=36,
                                                                        width=120,
                                                                        content=Text("WhatsApp")
                                                                    ),
                                                                ]
                                                            ),
                                                        ]
                                                    )
                                                ]
                                            ),
                                            Container(
                                                bgcolor="pink",
                                                content=Image(src="imgs/img_face.png", width=250)
                                            )
                                        ]
                                    )
                                )
                            ]
                        ),
                        # Section Three
                        Column(
                            controls=[
                                Container(
                                    alignment=ft.alignment.center,
                                    content=Column(
                                        controls=[
                                            Column(height=80),
                                            Text(
                                                value="Don't say, \"He is lazy!",
                                                size=25
                                            ),
                                            Column(height=80),
                                        ]
                                    )
                                )
                            ]
                        )
                    ]
                )
            ),
        ]


class BottomNavBar(Column):
    def __init__(self):
        super().__init__()

        self.controls = [
            Container(
                bgcolor="blue",
                height=240,
                alignment=ft.alignment.center,
                content=Column(
                    alignment=MainAxisAlignment.CENTER,
                    horizontal_alignment=CrossAxisAlignment.CENTER,
                    controls=[
                        Text(
                            value="mirage",
                            size=50
                        ),
                        Text(value="Copyright 2025")
                    ]
                )
            )
        ]


def main(page: Page) -> None:
    page.title = "Portfolio"
    page.horizontal_alignment = "center"
    page.window.width = 1200

    page.theme_mode = ft.ThemeMode.LIGHT
    page.bgcolor = "white"
    page.padding = 0

    page.scroll = ft.ScrollMode.HIDDEN

    page.add(
        NavBar(),
        ContentBody(),
        BottomNavBar()
    )
    page.update()


# Run app
if __name__ == '__main__':
    app(target=main, assets_dir=assets)
