from flet import (
    MainAxisAlignment,
    CrossAxisAlignment,
    TextField,
    Column,
    Text,
    Image,
    ElevatedButton,
    View,
    border_radius,
    Page
)    

from time import sleep

    
def Login_users(page: Page):
    
    def InputsLogin():
        
        user_name = TextField(label="Usuario", autofocus=True, width=300, height=50)
        user_password = TextField(label="contraseña", password=True, can_reveal_password=True, width=300, height=50)
        widgets = []

        def AccessIndexView(e):
            """
            if user_name.value == "less" and user_password.value == "1234":
                text_error = Text("Acceso concedido", color="green")
                widgets.append(text_error)  # Add error message
                page.update() 
                page.go("/index")
            """
            if 1 == 1:
                #page.go("example")
                page.go("/index")
                
            else:
                text_error = Text("Usuario o contraseña incorrectos", color="red")
                widgets.append(text_error)  # Add error message
                page.update()  # Update UI to display error
                sleep(4)
                widgets.pop()
                page.update()  # Update UI to display error
                

        boton = ElevatedButton("Acceso", on_click=AccessIndexView)
        widgets.append(user_name)
        widgets.append(user_password)
        widgets.extend([boton])
        
        return Column(
            
            controls=widgets,
            alignment=MainAxisAlignment.CENTER,
            horizontal_alignment=CrossAxisAlignment.CENTER
            
        )
        

    return View(
        
        "/",
        vertical_alignment=MainAxisAlignment.CENTER,
        horizontal_alignment=CrossAxisAlignment.CENTER,
        controls=[
        
            Image("imageLogin.jpeg",
                  width=100,
                  height=100,
                  border_radius=border_radius.all(40)),
            InputsLogin()
        
        ]
        
    )
