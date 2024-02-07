import flet as ft


def ExampleView(page: ft.Page):
    
    containerExampleText = ft.Container(
        alignment=ft.alignment.top_center,
        content=ft.Text("THIS IS AN EXAMPLE VIEW")
    )
    
    viewExample = [
        containerExampleText
        ]
    
    return (
        viewExample
    )
    