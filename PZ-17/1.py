# . Создайте класс "Товар" с атрибутами "название", "цена" и "количество". Напишите
# метод, который выводит информацию о товаре в формате "Название: название,
# Цена: цена, Количество: кол-во".

class Tovar:
    nazv = 'Яблоко'
    pay = 10.0
    qua = 1
    def info(self):
        return print("Название: ", self.nazv,"Цена: ", self.pay,"Количество: ", self.qua)

t = Tovar()
t.info()
