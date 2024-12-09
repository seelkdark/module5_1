class House:
    def __init__(self, name, number_of_floors):
        # Инициализация атрибутов объекта
        self.name = name  # Название дома
        self.number_of_floors = number_of_floors  # Количество этажей

    def go_to(self, new_floor):
        # Метод для перехода на указанный этаж
        if 1 <= new_floor <= self.number_of_floors:
            # Если этаж существует, выводим этажи до нового этажа
            for floor in range(1, new_floor + 1):
                print(floor)
        else:
            # Если этаж не существует, выводим сообщение
            print("Такого этажа не существует")

h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)

h1.go_to(5)   # Выводит этажи от 1 до 5
h2.go_to(10)  # Выводит сообщение о недоступном этаже