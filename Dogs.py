from tkinter import *
from tkinter import messagebox as mb
import requests
from PIL import Image, ImageTk
from io import BytesIO


def show_image():
    image_url = get_dog_image()
    if image_url:
        try:
            response = requests.get(image_url, stream=True)  # Ответ будет равен запросу. В ответ получим что-то загруженное по этой ссылке
            response.raise_for_status()  # Получаем статус ответа, пригодится для обработки исключений
            img_data = BytesIO(response.content)  # Теперь по этой ссылке с помощью BytesIO загрузили изображение в двоичном коде
            img = Image.open(img_data)  # С помощью PIL обрабатываем. Теперь здесь ккртинка
            img.thumbnail((300,300))  # Загруженная картинка будет подогнана под размер 300x300
            label.config(Image=img)
            label.image = img  # Чтобы картинку сборщик мусора не собрал
        except Exception as e:
            mb.showerror("Ошибка", f"Возникла ошибка {e}")








window = Tk()
window.title("Картинки с собачками")
window.geometry("360x420")

label = Label()
label.pack(pady=10)

button = Button(text="Загрузить изображение", command=show_image)
button.pack(pady=10)

window.mainloop()
