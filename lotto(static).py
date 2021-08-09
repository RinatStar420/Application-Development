
""" Определение постоянных величин.
Разместив все необходимые виджеты в сеточном шаблоне необходимо определить значения, которые будут постоянные для
виджетов, то есть не будут меняться во время исполнения работы программы."""
# виджеты:
from tkinter import *
# Доступ к cgi
window = Tk()
# Создание окна

# постоянные величины
window.title('Lotto number Picker')
window.resizable(0, 0)
#Инструкция запрета измены размера окна (стандартная кнопка изменеия окна будет диактивирована)

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
""" После создания виджетов значения их свойств могут быть добавлены или изменены при помощи метода configure()"""
getBtn.config(text='Get My Lucky Numbers')
resBtn.config(text='Reset')
# Инструкция определения текста размещенном на кнопке
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
