import flet as ft

def main(page: ft.Page):
    # Window_Settings
    page.title = "Login and Password form"
    page.window_width = 400
    page.window_height = 600


ft.app(target=main)