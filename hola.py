import flet as ft
import time as time
def main(page: ft.Page):
   t1=ft.Text(value="Oriol", color="red", size=20)
   t2=ft.Text(value="Rayan", color="blue", italic=True)
   t3=ft.Text(value="francesc", color="green")
   t4=ft.Text(value="Jan", color="yellow")
   t5=ft.Text(value="Eduardo", color="brown")
   t6=ft.Text(value="Cristina", color="grey")
   page.add(t1, t2, t3, t4, t5, t6)
   pass

   contador=ft.Text()
   contador.color="Cyan"
   contador.size=20
   page.add(contador)
   for i in range(11):
      contador.value=f"Contador: {i}"
      page.update()
      time.sleep(1)

   contador2=ft.Text()
   contador2.color="green"
   contador2.size=20
   page.add(contador2)
   for l in range(101):
      contador2.value=f"segon contador: {l}"
      page.update()
      time.sleep(1)

   contador3=ft.Text()
   contador3.color="Red"
   contador3.size=25
   page.add(contador3)
   for k in range(101):
      contador3.value=f" tercer contador: {k}"
      page.update()
      time.sleep(1)


   ft.app(target=main)