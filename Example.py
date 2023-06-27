import flet as ft

def main(page: ft.Page):

    def addTask(p): # Making Func for Add Task
        checkBox = ft.Checkbox(value=False)
        checkBoxText = ft.Text(value=textField.value, width=350, size=24)
        taskRow = ft.Row(controls=[checkBox, checkBoxText],
                         alignment=ft.MainAxisAlignment.START)
        page.add(taskRow)

    # Window Settings
    page.title = "Testing"
    page.window_width = 500 # Size Window
    page.window_height = 800
    page.bgcolor = '#2B2730' # Color Background

    # Creating Widgets (controls)
    textField = ft.TextField(width=350)
    addBtn = ft.ElevatedButton(text="Add", on_click=addTask)

    # Creating "Frame" in Row and add here controls
    entriesRow = ft.Row(controls=[textField, addBtn],
                        alignment=ft.MainAxisAlignment.CENTER)


    # Adding Widgets
    page.add(entriesRow)


ft.app(target=main)
