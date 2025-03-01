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
                    color=black, size=14,
                    font_family="semibold",
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
    def __init__(self, main_page: Page):
        super().__init__()
        self.main_page = main_page

        self.width = 780

        self.controls = [
            Container(
                # bgcolor="green",
                content=Column(
                    expand=True,
                    controls=[
                        Column(height=50),
                        # Hero Section
                        Container(
                            bgcolor=white,
                            height=480,
                            alignment=ft.alignment.center,
                            border_radius=30,
                            content=Column(
                                alignment=MainAxisAlignment.CENTER,
                                horizontal_alignment=CrossAxisAlignment.CENTER,
                                controls=[
                                    Text(
                                        value="Site Under\nConstruction",
                                        font_family="heavy",
                                        size=70, color=black,
                                        text_align=ft.TextAlign.CENTER,
                                        style=TextStyle(letter_spacing=-1, height=1),
                                    ),
                                    Column(height=10),
                                    Text(
                                        value="Your patience,\nis everything we need.",
                                        font_family="semibold",
                                        size=15, color=black,
                                        style=TextStyle(height=1.2),
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
                                Column(height=90),
                                Text(
                                    value="Building for you",
                                    font_family="bold",
                                    size=30, color=black,
                                    style=TextStyle(letter_spacing=-0.2),
                                ),
                                Column(height=20),
                                Row(
                                    vertical_alignment=CrossAxisAlignment.START,
                                    height=350,
                                    controls=[
                                        Container(
                                            expand=True,
                                            # bgcolor="pink",
                                            content=Column(
                                                alignment=MainAxisAlignment.SPACE_BETWEEN,
                                                controls=[
                                                    Container(
                                                        bgcolor=black,
                                                        border_radius=20,
                                                        alignment=ft.alignment.center,
                                                        expand=True,
                                                        content=Column(
                                                            alignment=MainAxisAlignment.CENTER,
                                                            horizontal_alignment=CrossAxisAlignment.CENTER,
                                                            controls=[
                                                                Text(
                                                                    value="Less Is More",
                                                                    text_align=ft.TextAlign.CENTER,
                                                                    font_family="bold",
                                                                    size=30, color=white,
                                                                ),
                                                                Text(
                                                                    value="A minimalist approach to\n"
                                                                          "everything you do.",
                                                                    color=white,
                                                                    text_align=ft.TextAlign.CENTER,
                                                                    font_family="regular",
                                                                ),
                                                            ]
                                                        )
                                                    ),
                                                    Container(
                                                        alignment=ft.alignment.center,
                                                        bgcolor=white,
                                                        border_radius=20,
                                                        padding=ft.padding.only(top=40, bottom=40),
                                                        content=Text(
                                                            value="Just for you",
                                                            font_family="bold",
                                                            size=20, color=black,
                                                        )
                                                    )
                                                ]
                                            )
                                        ),
                                        Container(
                                            expand=True,
                                            border_radius=20,
                                            gradient=ft.LinearGradient(
                                                begin=ft.alignment.top_left,
                                                end=ft.alignment.bottom_right,
                                                colors=[white_grey, white_mid]
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
                                Column(height=90),
                                Text(
                                    value="See Our next moves",
                                    font_family="bold",
                                    size=30, color=black,
                                ),
                                Column(height=20),
                                Container(
                                    height=400,
                                    bgcolor=black,
                                    border_radius=30,
                                    content=Row(
                                        alignment=MainAxisAlignment.CENTER,
                                        spacing=40,
                                        controls=[
                                            Column(
                                                alignment=MainAxisAlignment.CENTER,
                                                horizontal_alignment=CrossAxisAlignment.CENTER,
                                                controls=[
                                                    Column(
                                                        horizontal_alignment=CrossAxisAlignment.CENTER,
                                                        spacing=5,
                                                        controls=[
                                                            Text(
                                                                value="Get In Touch",
                                                                font_family="bold",
                                                                size=28, color=cream,
                                                            ),
                                                            Text(
                                                                value="Let's cross Paths",
                                                                font_family="semibold",
                                                                size=15, color=cream,
                                                            ),
                                                        ]
                                                    ),
                                                    # Space
                                                    Column(height=6),
                                                    # Social Media links
                                                    Column(
                                                        controls=[
                                                            Row(
                                                                controls=[
                                                                    Container(
                                                                        bgcolor=cream,
                                                                        alignment=ft.alignment.center,
                                                                        height=36, width=120,
                                                                        border_radius=25,
                                                                        content=Text(
                                                                            value="Pinterest",
                                                                            color=black,
                                                                            font_family="semibold",
                                                                        ),
                                                                        on_click=lambda
                                                                            e: self.social_media_button_clicked(e),
                                                                        on_hover=lambda
                                                                            e: self.social_media_g2_hover(e),
                                                                        scale=1,
                                                                        animate=ft.animation.Animation(
                                                                            duration=200,
                                                                            curve=ft.AnimationCurve.EASE_IN
                                                                        ),
                                                                        animate_scale=ft.animation.Animation(
                                                                            duration=200,
                                                                            curve=ft.AnimationCurve.EASE_IN
                                                                        ),
                                                                    ),
                                                                    Container(
                                                                        alignment=ft.alignment.center,
                                                                        height=36, width=120,
                                                                        border_radius=25,
                                                                        border=ft.border.all(
                                                                            width=1,
                                                                            color=cream,
                                                                        ),
                                                                        content=Text(
                                                                            value="Instagram",
                                                                            color=cream,
                                                                            font_family="semibold",
                                                                        ),
                                                                        on_click=lambda
                                                                            e: self.social_media_button_clicked(e),
                                                                        on_hover=lambda
                                                                            e: self.social_media_g1_hover(e),
                                                                        scale=1,
                                                                        animate=ft.animation.Animation(
                                                                            duration=200,
                                                                            curve=ft.AnimationCurve.EASE_IN
                                                                        ),
                                                                        animate_scale=ft.animation.Animation(
                                                                            duration=200,
                                                                            curve=ft.AnimationCurve.EASE_IN
                                                                        ),
                                                                    ),
                                                                ]
                                                            ),
                                                            Row(
                                                                controls=[
                                                                    Column(width=20),
                                                                    Container(
                                                                        alignment=ft.alignment.center,
                                                                        height=36, width=120,
                                                                        border_radius=25,
                                                                        border=ft.border.all(
                                                                            width=1,
                                                                            color=cream,
                                                                        ),
                                                                        content=Text(
                                                                            value="Email",
                                                                            color=cream,
                                                                            font_family="semibold",
                                                                        ),
                                                                        on_click=lambda
                                                                            e: self.social_media_button_clicked(e),
                                                                        on_hover=lambda
                                                                            e: self.social_media_g1_hover(e),
                                                                        scale=1,
                                                                        animate=ft.animation.Animation(
                                                                            duration=200,
                                                                            curve=ft.AnimationCurve.EASE_IN
                                                                        ),
                                                                        animate_scale=ft.animation.Animation(
                                                                            duration=200,
                                                                            curve=ft.AnimationCurve.EASE_IN
                                                                        ),
                                                                    ),
                                                                    Container(
                                                                        bgcolor=cream,
                                                                        alignment=ft.alignment.center,
                                                                        height=36, width=120,
                                                                        border_radius=25,
                                                                        content=Text(
                                                                            value="WhatsApp",
                                                                            color=black,
                                                                            font_family="semibold",
                                                                        ),
                                                                        on_click=lambda
                                                                            e: self.social_media_button_clicked(e),
                                                                        on_hover=lambda
                                                                            e: self.social_media_g2_hover(e),
                                                                        scale=1,
                                                                        animate=ft.animation.Animation(
                                                                            duration=200,
                                                                            curve=ft.AnimationCurve.EASE_IN
                                                                        ),
                                                                        animate_scale=ft.animation.Animation(
                                                                            duration=200,
                                                                            curve=ft.AnimationCurve.EASE_IN
                                                                        ),
                                                                    ),
                                                                ]
                                                            ),
                                                        ]
                                                    )
                                                ]
                                            ),
                                            Container(
                                                bgcolor=cream,
                                                border_radius=20,
                                                content=Image(
                                                    src="imgs/img_face.png",
                                                    width=250
                                                )
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
                                            Column(height=100),
                                            Text(
                                                value="Don't say, \"He is lazy!\"",
                                                size=40, color=black,
                                                font_family="bold",
                                            ),
                                            Column(height=100),
                                        ]
                                    )
                                )
                            ]
                        )
                    ]
                )
            ),
        ]


    def social_media_g1_hover(self, e: ft.ControlEvent) -> None:
        e.control.bgcolor = "#3E3E3E" if e.control.bgcolor is None else None
        e.control.scale = 1.1 if e.control.scale == 1 else 1
        self.update()

    def social_media_g2_hover(self, e: ft.ControlEvent) -> None:
        e.control.bgcolor = "#3E3E3E" if e.control.bgcolor == cream else cream
        e.control.scale = 1.1 if e.control.scale == 1 else 1
        e.control.content.color = cream if e.control.content.color == "#161617" else "#161617"
        self.update()

    def social_media_button_clicked(self, e: ft.ControlEvent) -> None:
        button_text: str = e.control.content.value
        if button_text == "Pinterest":
            self.main_page.launch_url("https://www.pinterest.com/ObjectZero/")
        if button_text == "Instagram":
            self.main_page.launch_url("https://www.instagram.com/_objectzero_/")
        if button_text == "WhatsApp":
            self.main_page.launch_url("https://wa.me/+233505767395")
        if button_text == "Email":
            self.main_page.launch_url(
                "https://mail.google.com/mail/?view=cm&fs=1&to=nessahjefferson7@gmail.com"
            )


class BottomNavBar(Column):
    def __init__(self):
        super().__init__()

        self.controls = [
            Container(
                bgcolor=white,
                height=220,
                alignment=ft.alignment.center,
                content=Column(
                    alignment=MainAxisAlignment.CENTER,
                    horizontal_alignment=CrossAxisAlignment.CENTER,
                    controls=[
                        Text(
                            value="mirage", size=60,
                            color=black,
                            font_family="bold",
                        ),
                        Text(
                            value="Copyright 2025",
                            size=18, color=black,
                            font_family="semibold",
                        )
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

    page.fonts = {
        "regular": "fonts/SF-Pro-Display-Regular.otf",
        "medium": "fonts/SF-Pro-Display-Medium.otf",
        "semibold": "fonts/SF-Pro-Display-Semibold.otf",
        "bold": "fonts/SF-Pro-Display-Bold.otf",
        "heavy": "fonts/SF-Pro-Display-Heavy.otf",
    }

    page.add(
        NavBar(),
        ContentBody(page),
        BottomNavBar()
    )
    page.update()


# Run app
if __name__ == '__main__':
    app(target=main, assets_dir=assets)
