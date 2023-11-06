import flet as ft


def main(page: ft.page):
    def button_clicked(e):
        page.clean()
    
    titulo=ft.Text(value="Qüestionari",color="cyan",size=100)
    input_name=ft.TextField(label="Name")
    input_age=ft.TextField(label="age")
    inputdistrite=ft.TextField(label="street")
    input_topas=ft.TextField(label="trops")
    input_phone=ft.TextField(label="phone")
    send_mail=ft.ElevatedButton(text="submit", on_click=button_clicked)
    page.add(
        ft.Row(
            controls=[titulo],
            alignment="center"
        ),
        ft.Row(
            controls=[input_name, input_age],
            alignment="center" 
        ),
        ft.Row(
            controls=[input_street, input_mail],
            alignment="center" 
        ),
        ft.Row(
            controls=[input_phone],
            alignment="center" 
        ),
        ft.Row(
            controls=[send_button],
            alignment="center" 
        )
    )

ft.app(target=main)