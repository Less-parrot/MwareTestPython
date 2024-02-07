import flet as ft
from db.script import ReadTableDb

def main(page: ft.Page, width: int, label: str, *options):

    dropDownMenu = ft.Dropdown(
        prefix_text=label,
        label=label,
        width=width,
        options=[]
    )

    for i in options[0]:
        idDevice, device = i
        dropDownMenu.options.append(ft.dropdown.Option(text=f"{idDevice}) {device}", disabled=True))

    return dropDownMenu


def useDropDown(page: ft.Page):
    
    readMessages =  ReadTableDb(
        "db/smsDevices.db",
        f"""
        SELECT * FROM sms_device_1
        
        """    
    )
    
    retornar = main(page,
                    700,
                    "sms",
                    readMessages
            )
    

    page.add(retornar)    