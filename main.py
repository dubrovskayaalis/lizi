# Задание 1
# Создайте класс, выполняющий операции с массивом:
# отображение данных в файл или на экран, переворот
# данных, нахождение максимума, нахождение минимума.
# Класс может получить набор значений с клавиатуры или
# из файла. При реализации используйте паттерн Strategy
# и другие необходимые паттерны.

from abc import ABC, abstractmethod
from typing import List, Union

class InputStrategy(ABC):
    @abstractmethod
    def get_data(self) -> List[int]:
        pass

class OutputStrategy(ABC):
    @abstractmethod
    def output(self, data: List[int]) -> None:
        pass

class KeyboardInputStrategy(InputStrategy):
    def get_data(self) -> List[int]:
        print('INFO: Введите числа в одну строку через пробел')
        try:
            data = list(map(int, input().split()))
            return data
        except ValueError:
            print("Error: Input integer number")
            return []

class FileInputStrategy(InputStrategy):
    def __init__(self, filename: str):
        self.filename = filename

    def get_data(self) -> List[int]:
        try:
            with open(self.filename, 'r') as biba:
                boba = biba.read()
                data = list(map(int, boba.split()))
                return data
        except ValueError:
            print('Error: in your file integer number')
            return []
        except FileNotFoundError:
            print(f'Error: your file {self.filename} no search')
            return []

class ConsoleOutputStrategy(OutputStrategy):
    def output(self, data: List[int]) -> None:
        print('Массив: ', data)

class FileOutputStrategy(OutputStrategy):
    def __init__(self, filename: str):
        self.filename = filename

    def output(self, data: List[int]) -> None:
        try:
            with open(self.filename, 'w', encoding='utf-8') as file:
                file.write(" ".join(map(str, data)) + "\n")
            print(f"INFO: Данные сохранены в файл: {self.filename}")
        except Exception as e:
            print(f"Error: Ошибка при записи в файл: {e}")

class ArrayProcess:
    def __init__(self, input_strategy: InputStrategy, output_strategy: OutputStrategy):
        self._input_strategy = input_strategy
        self._output_strategy = output_strategy
        self._data: List[int] = []

    def set_input_strategy(self, input_strategy: InputStrategy) -> None:
        self._input_strategy = input_strategy

    def set_output_strategy(self, output_strategy: OutputStrategy) -> None:
        self._output_strategy = output_strategy

    def load_data(self) -> None:
        self._data = self._input_strategy.get_data()
        if self._data:
            print(f"INFO: Loaded {len(self._data)} elements")

    def display_data(self) -> None:
        if not self._data:
            print('INFO: in massive not elements')
            return
        self._output_strategy.output(self._data)

    def reverse_data(self) -> None:
        if not self._data:
            print('INFO: in massive not elements')
            return
        self._data.reverse()
        print('INFO: massive reserved')

    def find_max(self) -> Union[int, None]:
        if not self._data:
            print('INFO: in massive not elements')
            return None
        max_value = max(self._data)
        print('INFO: max element searched')
        return max_value

    def find_min(self) -> Union[int, None]:
        if not self._data:
            print('INFO: in massive not elements')
            return
        min_value = min(self._data)
        print('INFO: min element searched')
        return min_value

    def get_data(self) -> List[int]:
        return self._data.copy()

if __name__ == '__main__':
    pr = ArrayProcess(KeyboardInputStrategy(), FileOutputStrategy("данные.txt"))

    while True:
        print("\n=== Меню операций с массивом ===")
        print("1. Загрузить данные с клавиатуры")
        print("2. Загрузить данные из файла")
        print("3. Отобразить данные")
        print("4. Перевернуть массив")
        print("5. Найти максимум")
        print("6. Найти минимум")
        print("7. Изменить стратегию вывода")
        print("0. Выход")

        choice = input("Выберите операцию: ")

        if choice == '1':
            pr.set_input_strategy(KeyboardInputStrategy())
            pr.load_data()

        elif choice == '2':
            f_n = input('Введите имя файла с расширением: ')
            pr.set_input_strategy(FileInputStrategy(f_n))
            pr.load_data()

        elif choice == '3':
            pr.display_data()

        elif choice == '4':
            pr.reverse_data()

        elif choice == '5':
            pr.find_max()

        elif choice == '6':
            pr.find_min()

        elif choice == '7':
            print("Выберите стратегию вывода:")
            print("1. Консоль")
            print("2. Файл")
            output_choice = input("Ваш выбор: ")

            if output_choice == '1':
                pr.set_output_strategy(ConsoleOutputStrategy())
                print("Стратегия вывода изменена на консоль")
            elif output_choice == '2':
                filename = input("Введите имя файла для вывода: ")
                pr.set_output_strategy(FileOutputStrategy(filename))
                print("Стратегия вывода изменена на файл")
            else:
                print("Неверный выбор!")

        elif choice == '0':
            print("Выход из программы")
            break

        else:
            print("неверный ввод")