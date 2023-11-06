import flet as ft

nom1=ft.Text(value="Oriol",color="red",size=17)

nom2=ft.Text(value="Rayan",color="blue",size=20)

nom3=ft.Text(value="Cristina",color="grey",size=24)

nom4=ft.Text(value="Francesc",color="green",size=28)

nom5=ft.Text(value="Marc",color="yellow",size=16)

nom6=ft.Text(value="Jan",color="purple",size=15)

nom7=ft.Text(value="hady",color="cyan",size=16)

def main(page: ft.Page):
    page.add(
    ft.Row(controls=[
            nom1,
            nom2,
            nom3,
    ]),
    ft.Row(controls=[
        nom4,
        nom5,
        nom6,
        nom7,


    ])   
    
    )

ft.app(target=main)