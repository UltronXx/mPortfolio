import flet as ft
from flet import (
    Page, app,
    Container,
    Column, Row,
    Image,
    Text, TextStyle,
    MainAxisAlignment,
    CrossAxisAlignment,
)

from pathlib import Path
assets = f"{Path(__file__).parent}/src/assets"

def main(page: Page) -> None:
    page.title = "Portfolio"
    # page.padding = 0

    page.add(
        Container(
            height=400,
            width=300,
            bgcolor="grey200"
        ),
        Text(
            value="Portfolio",
            weight=ft.FontWeight.BOLD,
            size=120
        )
    )
    page.update()


# Run app
if __name__ == '__main__':
    app(target=main, assets_dir=assets)
