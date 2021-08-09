""" Планирование программыю
Перед созданием нового графического элемента необходимо составить план построения
1. Назначение программы: Программа должна генерировать числа в диапозоне от 1 до 49и иметь возможность перезагрузки.
2. Требуемая функциональность: Функция для генерации и последующего вывода шести уникальных случайных чисел;
Функция для удаления всех сгенерированных чисел.
3. Необходимые элементы интерфейса: Одно базовое окно постоянного размера, в котором будут содержаться  все остальные
виджеты и отображаться заголовок нашего приложения; Один виджет label на который мы помести статическое изображение
логотипа приложения; Шесть виджетов label для динамического отображения набора сгенерированных чисел (по одному на
каждый виджет); Один виджет Button для генерации и вывода чисел на виджеты label при нажатии кнопки; Ещё один виджет
Button для очистки данных с виджета label при его нажатии"""

# виджеты:
from tkinter import *
# Доступ к cgi
window = Tk()
# Создание окна
img = PhotoImage(file='liza_lotto.gif')
# Создание изображения
imgLbl = Label(window, image=img)
label1 = Label(window, relief='groove', width=2) # relief - определяет стиль рамки
label2 = Label(window, relief='groove', width=2) # width - ширина метки в симолах
label3 = Label(window, relief='groove', width=2)
label4 = Label(window, relief='groove', width=2)
label5 = Label(window, relief='groove', width=2)
label6 = Label(window, relief='groove', width=2)
getBtn = Button(window)
resBtn = Button(window)
# Создание необходимых (описанных выше) виджетов
# Размещение:
imgLbl.grid()
label1.grid()
label2.grid()
label3.grid()
label4.grid()
label5.grid()
label6.grid()
getBtn.grid()
resBtn.grid()
# Обработка событий окна
window.mainloop()
