import flet as ft


def main(page: ft.page):
    def button_clicked(e):
        page.clean()
        name=input_name.value
        age=int(input_age.value)
        text_name=ft.Text(value="hola "+ name)
        
        if (age >= 18):
            text_edad=ft.Text(value=f"tens {age} te queda menos crack")
        else:
            text_edad=ft.Text(value=f"tens {age}, ets major d'edat")
        page.add(
            ft.Row(
                controls=[text_name],
                alignment="center"
            ),
            ft.Row(
                controls=[text_edad],
                alignment="center"
            )
        )
    
    titulo=ft.Text(value="Qüestionari",color="cyan",size=100)
    input_name=ft.TextField(label="Name")
    input_age=ft.TextField(label="age")
    input_street=ft.TextField(label="street")
    input_mail=ft.TextField(label="mail")
    input_phone=ft.TextField(label="phone")
    send_button=ft.ElevatedButton(text="submit", on_click=button_clicked)
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