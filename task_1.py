# TODO Написать 3 класса с документацией и аннотацией типов

from datetime import datetime


class Furniture:
    """Класс описывает предмет мебели с базовыми характеристиками"""

    def __init__(self, type_: str, material: str, dimensions: tuple, finish: str):
        """
        :param type_: Тип мебели
        :param material: Основной материал
        :param dimensions: Размеры (длина, ширина, высота)
        :param finish: Отделка
        """

        if not all(isinstance(x, str) for x in [type_, material, finish]):
            raise TypeError("Текстовые параметры должны быть строками")
        if not isinstance(dimensions, tuple) or len(dimensions) != 3:
            raise TypeError("Размеры должны быть кортежем из трех чисел")

        self.type = type_
        self.material = material
        self.dimensions = dimensions
        self.finish = finish

    def change_finish(self, new_finish: str) -> str:
        if new_finish == self.finish:
            raise ValueError("Такая отделка уже установлена")
        self.finish = new_finish
        return f"Установлена новая отделка: {new_finish}"

    def get_specs(self) -> str:
        return f"Мебель: {self.type}, Материал: {self.material}, Размеры: {self.dimensions}, Отделка: {self.finish}"


class Vehicle:
    """Класс описывает транспортное средство"""

    def __init__(self, brand: str, type_: str, production_date: str, odometer: int = 0):
        if not isinstance(odometer, int) or odometer < 0:
            raise ValueError("Пробег должен быть неотрицательным целым числом")

        self.brand = brand
        self.type = type_
        self.production_date = production_date
        self.odometer = odometer

    def add_distance(self, km: int) -> None:
        if km < 0:
            raise ValueError("Дистанция должна быть положительной")
        self.odometer += km

    def calculate_age(self) -> int:
        prod_year = int(self.production_date.split('.')[-1])
        return datetime.now().year - prod_year

    def get_info(self) -> str:
        return f"{self.brand} {self.type}, Выпуск: {self.production_date}, Пробег: {self.odometer} км"


class WorkItem:
    """Класс описывает рабочее задание"""

    URGENCY_LEVELS = {"low": 1,
                      "medium": 2,
                      "high": 3}

    def __init__(self, title: str, description: str, urgency: str = "medium"):
        if urgency not in self.URGENCY_LEVELS:
            raise ValueError("Неверный уровень срочности")

        self.title = title
        self.description = description
        self.urgency = urgency
        self.completed = False

    def mark_done(self) -> None:
        if self.completed:
            raise ValueError("Задание уже выполнено")
        self.completed = True

    def change_urgency(self, new_urgency: str) -> None:
        if new_urgency not in self.URGENCY_LEVELS:
            raise ValueError("Неверный уровень срочности")
        self.urgency = new_urgency

    def get_status(self) -> str:
        status = "завершено" if self.completed else "в работе"
        return f"Задание: {self.title}, Срочность: {self.urgency}, Статус: {status}"
