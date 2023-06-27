import flet as ft
def main(page: ft.Page):
    def check(e):
        if loginField.value == login and passwordField.value == password:
            result_message.value = "RIGHT DATA!"
            result_message.color = "green"
            page.update()
        else:
            result_message.value = "WRONG DATA!"
            result_message.color = "red"
            page.update()
    # Window_Settings
    page.title = "Login and Password form"
    page.window_width = 700
    page.window_height = 900
    page.bgcolor = '#2B2730'  # Color Background
    login = "1"
    password = "2"
    # Meet Text and Controls
    text = ft.Text("HELLO USER!", size=20, font_family="Gotham", weight=ft.FontWeight.BOLD)
    loginField = ft.TextField(width=500)
    passwordField = ft.TextField(width=500)
    button = ft.OutlinedButton("Enter", on_click=check)
    result_message = ft.Text(" ",
                     size=20,
                     font_family="Gotham",
                     weight=ft.FontWeight.BOLD)

    controls_layout = ft.Column(controls=[text,
                                          loginField,
                                          passwordField,
                                          button,
                                          result_message],
                                alignment=ft.MainAxisAlignment.CENTER)
    page.add(controls_layout)

if __name__ == "__main__":
    ft.app(target=main, view=ft.WEB_BROWSER)


