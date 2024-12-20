import logging
import string
from collections.abc import Iterable
from typing import Dict, List, Optional

"""
№ 1 Реализовать класс MultiTempAttributes, который позволяет временно изменять значения атрибутов объекта.
Этот класс должен поддерживать контекстный менеджер, который изменяет указанные атрибуты объекта на новые значения,
а после завершения работы с объектом автоматически восстанавливает исходные значения атрибутов.

Класс MultiTempAttributes должен реализовывать следующие методы:

__init__(self, obj, attrs_values): Конструктор, принимающий два аргумента:

obj: Объект, атрибуты которого будут временно изменяться.
attrs_values: Словарь, где ключи — это имена атрибутов, которые нужно изменить, а значения — новые значения для этих атрибутов.
__enter__(self): Метод, который сохраняет исходные значения указанных атрибутов и устанавливает новые значения.

__exit__(self, exc_type, exc_value, traceback): Метод, который восстанавливает исходные значения атрибутов после выхода из контекстного менеджера, независимо от того, произошла ли ошибка.
"""
# Контекстный менеджер
class MultiTempAttributes:
    def __init__(self, obj, attrs_values):
        self.obj = obj
        self.attrs_values = attrs_values
        self.original_values = {}

    def __enter__(self):
        for attr, new_value in self.attrs_values.items():
            self.original_values[attr] = getattr(self.obj, attr, None)
            setattr(self.obj, attr, new_value)
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        for attr, original_value in self.original_values.items():
            setattr(self.obj, attr, original_value)

"""
№ 2 Подсчет уникальных слов

Вам дан текст в виде строки, содержащий слова и пунктуацию.
Напишите функцию, которая определяет количество уникальных слов в этом тексте. Для подсчета уникальных слов следует учитывать следующие условия:

Текст должен быть приведен к нижнему регистру, чтобы слова с разными регистрами считались одинаковыми.
Все знаки пунктуации должны быть удалены из текста.
После удаления пунктуации текст следует разбить на слова, разделенные пробелами.
Слово считается уникальным, если оно встречается в тексте только один раз после удаления пунктуации и приведения текста к нижнему регистру.
"""
import string

def count_unique_words(text: str) -> int:
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    words = text.split()

    unique_words = set()
    
    unique_words_count = 0
    
    for word in words:
        if word not in unique_words:
            unique_words_count += 1
            unique_words.add(word)
    
    return unique_words_count
"""
№ 3 Анализ четных чисел

Аргументы:
numbers: Список целых чисел.


Возвращаемое значение:
Словарь с ключами:
"count": Количество четных чисел.
"sum": Сумма четных чисел (или None, если четных чисел нет).
"average": Среднее значение четных чисел (или None, если четных чисел нет).
"max": Максимальное значение четных чисел (или None, если четных чисел нет).
"min": Минимальное значение четных чисел (или None, если четных чисел нет).
"""
from typing import List, Dict, Optional

def analyze_even_numbers(numbers: List[int]) -> Dict[str, Optional[float]]:
    even_numbers = [num for num in numbers if num % 2 == 0]

    count = len(even_numbers)
    
    if count == 0:
        return {
            "count": 0,
            "sum": None,
            "average": None,
            "max": None,
            "min": None,
        }
    
    total_sum = sum(even_numbers)
    
    average = total_sum / count
    
    max_even = max(even_numbers)
    min_even = min(even_numbers)
    
    return {
        "count": count,
        "sum": total_sum,
        "average": average,
        "max": max_even,
        "min": min_even,
    }

"""
№ 4 Проверка уникальности элементов в вложенных структурах данных

Реализовать функцию all_unique_elements, которая проверяет,
содержатся ли в заданной структуре данных только уникальные элементы.

Поддерживаются следующие типы данных:
Строки
Списки
Кортежи
Множества
Вложенные структуры (например, списки внутри списков и т.д.)
Функция должна игнорировать значения типа None.
"""
def all_unique_elements(data) -> bool:
    def flatten(d, seen=None):
        if seen is None:
            seen = set()
        
        if isinstance(d, (str, int, float, bool)):
            if d is not None:
                if d in seen:
                    return False
                seen.add(d)
            return True
        
        if isinstance(d, (list, tuple, set)):
            for item in d:
                if not flatten(item, seen):
                    return False
            return True
        
        if isinstance(d, dict):
            frozen_dict = frozenset(d.items())
            if frozen_dict in seen:
                return False
            seen.add(frozen_dict)
            return True
        
        return True

    return flatten(data)

"""
№ 5 

Напишите функцию enumerate_list,
которая принимает на вход список data и возвращает новый список,
содержащий элементы из data, но каждый элемент дополнен его индексом.
Индекс каждого элемента рассчитывается начиная с start и увеличивается на step для каждого следующего элемента.

Функция должна поддерживать следующие параметры:

data (list): список, элементы которого нужно перечислить.
start (int, по умолчанию 0): начальный индекс.
step (int, по умолчанию 1): шаг, на который увеличивается индекс.
recursive (bool, по умолчанию False): если True, функция должна рекурсивно обрабатывать вложенные списки.
Функция должна возвращать список, в котором каждый элемент является кортежем из двух элементов: индекса и значения из исходного списка.
"""


def enumerate_list(
    data: list, start: int = 0, step: int = 1, recursive: bool = False
) -> list:
    def recursive_enumerate(lst, idx):
        result = []
        for item in lst:
            if isinstance(item, list) and recursive:
                nested_result, idx = recursive_enumerate(item, idx)
                result.append(nested_result)
            else:
                result.append((idx, item))
                idx += step
        return result, idx

    if recursive:
        result, _ = recursive_enumerate(data, start)
        return result
    else:
        return [(start + i * step, item) for i, item in enumerate(data)]


"""
№ 6 Реализация контекстного менеджера для подключения к базе данных (симуляция)

Вам необходимо реализовать класс DatabaseConnection,
который будет управлять подключением к базе данных и транзакциями(симуляция в виде сообщений),
используя менеджер контекста. Класс должен поддерживать следующие функции:

Инициализация: При создании экземпляра класса, он должен принимать имя базы данных (db_name), к которой будет подключаться.

Менеджер контекста: Класс должен реализовывать методы __enter__ и __exit__, чтобы использовать его в блоке with. 
При входе в блок контекста должно происходить подключение к базе данных, а при выходе из блока — закрытие соединения и обработка возможных ошибок.

Подключение к базе данных: Метод connect должен инициировать подключение к базе данных и сохранять его состояние.

Выполнение запроса: Метод execute_query должен выполнять запрос, если активна транзакция. В противном случае должен выбрасываться исключение.

Управление транзакциями: Методы start_transaction, commit и rollback должны управлять транзакциями. Транзакция должна быть активна для выполнения запросов, и должна быть закрыта после коммита или отката.

Логирование: Класс должен использовать встроенный модуль logging для записи логов подключения, выполнения запросов, начала и завершения транзакций, а также для обработки ошибок.
"""
import logging

logging.basicConfig(level=logging.INFO)

class DatabaseConnection:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = None
        self.transaction_active = False

    def __enter__(self):
        self.connect()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            self.rollback()
            logging.error(f"Exception occurred: {exc_type}, {exc_value}")
        self.close()

    def connect(self):
        self.connection = f"Connected to {self.db_name} database"
        logging.info(f"Connected to {self.db_name}")

    def close(self):
        if self.connection:
            logging.info(f"Disconnected from {self.db_name}")
            self.connection = None

    def start_transaction(self):
        if self.transaction_active:
            raise RuntimeError("Transaction is already active")
        self.transaction_active = True
        logging.info("Transaction started")

    def commit(self):
        if not self.transaction_active:
            raise RuntimeError("No active transaction to commit")
        self.transaction_active = False
        logging.info("Transaction committed")

    def rollback(self):
        if not self.transaction_active:
            raise RuntimeError("No active transaction to rollback")
        self.transaction_active = False
        logging.info("Transaction rolled back")

    def execute_query(self, query):
        if not self.transaction_active:
            raise RuntimeError("No active transaction")
        logging.info(f"Executing query: {query}")
        return f"Result of '{query}'"