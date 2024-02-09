import flet as ft
from uiMware.views.libs.DropDownMenu import DropDownMenuAppsAndSMS


def DefineCardsInfoDevice(
        gradiantCard = None,
        width: int = 200,
        padding: int = 10,
        iconCard: ft.Icon = ft.Icon(ft.icons.PERSON),
        titleCard: str = "Desconocido",
        *descriptionCard
    ):
    
    descriptionsCards = "\t\n".join(descriptionCard)
    
    cards = ft.Card(
        content=ft.Container(
        
        gradient=gradiantCard,
        
        border_radius=ft.border_radius.all(15),
            content=ft.Column(
                scroll=ft.ScrollMode.ALWAYS,
                controls=[
                    ft.ListTile(
                        leading=iconCard,
                        title=ft.Text(titleCard),
                        subtitle=ft.Column(
                            controls=[
                                ft.Text(
                                    descriptionsCards
                                )
                            ]
                        )    
                    ),
                
                ]
            ),
            width=width,
            padding=padding,
        )
    )
    
    return (
        cards
    )
    


def DefineCardsAPPS_SMS_Device(
        gradiantCard = None,
        width: int = 200,
        padding: int = 10,
        iconCard: ft.Icon = ft.Icon(ft.icons.PERSON),
        titleCard: str = "Desconocido",
        label_DropDown: str = "Desconocido",
        *options: str
    ):
    
    
    cards = ft.Card(
        content=ft.Container(
        
        gradient=gradiantCard,
        
        border_radius=ft.border_radius.all(15),
            content=ft.Column(
                scroll=ft.ScrollMode.ALWAYS,
                controls=[
                    ft.ListTile(
                        leading=iconCard,
                        title=ft.Text(titleCard),
                        subtitle=ft.Column(
                            controls=[
                                DropDownMenuAppsAndSMS(ft.Page, width-10, label_DropDown, options)
                            ]
                        )    
                    ),
                
                ]
            ),
            width=width,
            padding=padding,
        )
    )
    
    return (
        cards
    )