import flet as ft

def main(page: ft.Page):
    page.title = "Fucking Flet Test"

    def on_button(e):
        button3.disabled=False
        button3.text="On"
        page.update()
    def off_button(e):
        button3.disabled=True
        button3.text = "Off"
        page.update()


    button1 = ft.OutlinedButton("Off", on_click=off_button)
    button2 = ft.OutlinedButton("On", on_click=on_button)
    button3 = ft.OutlinedButton("TestingButton")

    page.add(button1, button2, button3)


if __name__ == "__main__":
    ft.app(target=main)



