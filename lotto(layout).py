
""" Построение интерфейса
После создания всех виджетов можно приступить к разработке шаблона интерфеса. Для этого надо задать аргументы,
определяющие параметры размещения виджетов на экране. Будет использовать горизонтальное расположение, при котором
слева разместим виджет Label  с логотипом, а справа от него шесть виджетов для номеров лотереии, под которыми будут
находиться две управляющие кнопки. Для этого используем менеджер размещения grid(), который позволяет распологать
виджеты в ячейках таблицы. В результате виджет с логотипом будет находиться в первом столбце и занимать строки,
виджеты для номеров займут ячейки в верхней строке начиная со второй по седьмую, первая кнопка расположится на
второй строке  заняв четыре ячейки начиная со второй, а вторая кнопка на второй строке в оставшихся двух ячейакх"""
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
imgLbl.grid(row=1, column=1, rowspan=2)
label1.grid(row=1, column=2, padx=10)
label2.grid(row=1, column=3, padx=10)
label3.grid(row=1, column=4, padx=10)                      #row -  строк
label4.grid(row=1, column=5, padx=10)                      #column - ячейка
label5.grid(row=1, column=6, padx=10)                      #columnspan - количество ячеек
label6.grid(row=1, column=7, padx=10)                      #padx - колво пикселов пространсва между ячейками
getBtn.grid(row=2, column=2, columnspan=3)
resBtn.grid(row=2, column=6, columnspan=2)
# Обработка событий окна
window.mainloop()
