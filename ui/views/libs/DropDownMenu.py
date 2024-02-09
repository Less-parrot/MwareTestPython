import flet as ft

def DropDownMenuAppsAndSMS(page: ft.Page, width: int, label: str, *options):

    dropDownMenu = ft.Dropdown(
        prefix_text=label,
        label=label,
        width=width,
        options=[],
        autofocus=True
    )

    
    for i in options[0][0]:
        idDevice, device = i
        dropDownMenu.options.append(ft.dropdown.Option(text=f"{idDevice}) {device}", disabled=True))

    return dropDownMenu