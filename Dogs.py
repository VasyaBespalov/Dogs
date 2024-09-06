from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
import requests
from PIL import Image, ImageTk
from io import BytesIO


def get_dog_image():
    try:
        response = requests.get("https://dog.ceo/api/breeds/image/random")  # в response получаем json
        response.raise_for_status()  # Если все хорошо, то статус 200. Если ошибка showerror покажет
        data = response.json()  # В data лежит ответ в формате json
        return data['message']  # Функция get_dog_image вернет информ по ключу message, адрес картинки
    except Exception as e:
        mb.showerror("Ошибка", f"Возникла ошибка при запросе к API {e}")
        return None  # Обязательно возвращаем ответ. Если возвращать нечего, то None


def show_image():
    image_url = get_dog_image()
    if image_url:
        try:
            response = requests.get(image_url, stream=True)  # Ответ будет равен запросу. В ответ получим что-то загруженное по этой ссылке
            response.raise_for_status()  # Получаем статус ответа, пригодится для обработки исключений
            img_data = BytesIO(response.content)  # Теперь по этой ссылке с помощью BytesIO загрузили изображение в двоичном коде
            img = Image.open(img_data)  # С помощью PIL обрабатываем. Теперь здесь картинка
            img.thumbnail((300, 300))  # Загруженная картинка будет подогнана под размер 300x300
            img = ImageTk.PhotoImage(img)  #
            label.config(image=img)
            label.image = img  # Чтобы картинку сборщик мусора не собрал
        except Exception as e:
            mb.showerror("Ошибка", f"Возникла ошибка при загрузке изображения {e}")
    progress.stop()


def prog():
    progress["value"] = 0  # Начальное значение прогрессбара 0
    progress.start(30)  # Увеличение будет происходить один раз в 30 миллисекунд
    window.after(3000, show_image)  # Ждем 3 сек и запускаем функцию




window = Tk()
window.title("Картинки с собачками")
window.geometry("360x420")

label = ttk.Label()
label.pack(pady=10)

button = ttk.Button(text="Загрузить изображение", command=prog)
button.pack(pady=10)

progress = ttk.Progressbar(mode="determinate", length=300)
progress.pack(pady=10)

window.mainloop()
