import flet as ft

class TasksApp(ft.UserControl):
    def build(self):
        self.textField = ft.TextField(width=350)
        self.addBtn = ft.FloatingActionButton(text="+",
                                              on_click=self.addClick)
        self.tasks = ft.Column()
        taskRow = ft.Column(controls=[ft.Row(controls=[self.textField, self.addBtn]),
                                      self.tasks])
        return taskRow

    def addClick(self, e):
        pass
    def taskDelete(self, task):
        pass

class Task(ft.UserControl):
    # 14.34



def main(page: ft.Page):
    page.title = "Tasking App By Kiordev"
    page.window_height = 700
    page.window_width = 500
    page.bgcolor = "WHITE"

    taskingApp=TasksApp()
    page.add(taskingApp)

if __name__ == "__main__":
    ft.app(target=main)