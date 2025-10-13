"""
Завдання 4: Перевірка входження чисел в інтервал

Програма перевіряє, чи входять три введені цілі числа в заданий інтервал [1, N],
де N - остання цифра номера за списком студента.

Наприклад, якщо номер за списком 25, то N = 5, і інтервал буде [1, 5].
"""


def check_number_in_interval(number, min_value, max_value):
    """
    Перевіряє, чи входить число в заданий інтервал.

    Args:
        number (int): Число для перевірки
        min_value (int): Мінімальне значення інтервалу (включно)
        max_value (int): Максимальне значення інтервалу (включно)

    Returns:
        bool: True якщо число входить в інтервал, False якщо ні

    Example:
        >>> check_number_in_interval(3, 1, 5)
        True  # 3 входить в інтервал [1, 5]

        >>> check_number_in_interval(7, 1, 5)
        False  # 7 не входить в інтервал [1, 5]

        >>> check_number_in_interval(1, 1, 5)
        True  # 1 входить в інтервал [1, 5] (межа інтервалу)
    """
    # Перевіряємо, чи число більше або дорівнює мінімуму
    # і одночасно менше або дорівнює максимуму
    return min_value <= number <= max_value


def filter_numbers_in_interval(numbers, n_value):
    """
    Фільтрує список чисел, залишаючи тільки ті, що входять в інтервал [1, N].

    Args:
        numbers (list): Список цілих чисел для перевірки
        n_value (int): Верхня межа інтервалу (N)

    Returns:
        tuple: (список чисел в інтервалі, список чисел поза інтервалом)

    Example:
        >>> filter_numbers_in_interval([2, 7, 4], 5)
        ([2, 4], [7])
        # 2 і 4 входять в [1, 5], а 7 - ні
    """
    # Мінімальна межа інтервалу завжди дорівнює 1
    MIN_VALUE = 1

    # Списки для зберігання результатів фільтрації
    numbers_inside = []   # Числа, що входять в інтервал
    numbers_outside = []  # Числа, що не входять в інтервал

    print(f"Перевірка чисел на входження в інтервал [{MIN_VALUE}, {n_value}]:")
    print("-" * 70)

    # Проходимо по кожному числу та перевіряємо його
    for index, number in enumerate(numbers, start=1):
        # Перевіряємо, чи число входить в інтервал
        is_in_interval = check_number_in_interval(number, MIN_VALUE, n_value)

        if is_in_interval:
            # Число входить в інтервал
            numbers_inside.append(number)
            status = "✓ ВХОДИТЬ"
        else:
            # Число не входить в інтервал
            numbers_outside.append(number)
            status = "✗ НЕ ВХОДИТЬ"

        # Виводимо результат перевірки для поточного числа
        print(f"Число {index}: {number:>3} → {status} в інтервал [{MIN_VALUE}, {n_value}]")

    print("-" * 70)

    return numbers_inside, numbers_outside


def display_filtering_results(numbers_inside, numbers_outside, n_value):
    """
    Виводить результати фільтрації чисел у зручному форматі.

    Args:
        numbers_inside (list): Числа, що входять в інтервал
        numbers_outside (list): Числа, що не входять в інтервал
        n_value (int): Верхня межа інтервалу
    """
    print()
    print("=" * 70)
    print("РЕЗУЛЬТАТИ ФІЛЬТРАЦІЇ")
    print("=" * 70)
    print()

    # Виводимо числа, що входять в інтервал
    print(f"Числа, що входять в інтервал [1, {n_value}]:")
    if numbers_inside:
        print(f"  {numbers_inside}")
        print(f"  Кількість: {len(numbers_inside)}")
    else:
        print("  (немає таких чисел)")

    print()

    # Виводимо числа, що не входять в інтервал
    print(f"Числа, що НЕ входять в інтервал [1, {n_value}]:")
    if numbers_outside:
        print(f"  {numbers_outside}")
        print(f"  Кількість: {len(numbers_outside)}")
    else:
        print("  (немає таких чисел)")

    print()

    # Статистика
    total_count = len(numbers_inside) + len(numbers_outside)
    inside_percentage = (len(numbers_inside) / total_count * 100) if total_count > 0 else 0

    print("Статистика:")
    print(f"  Всього чисел перевірено: {total_count}")
    print(f"  Відсоток чисел в інтервалі: {inside_percentage:.1f}%")


def run_interval_filtering():
    """
    Головна функція для запуску програми фільтрації чисел за інтервалом.

    Послідовно:
    1. Запитує останню цифру номера за списком (N)
    2. Запитує три цілі числа для перевірки
    3. Фільтрує числа за інтервалом [1, N]
    4. Виводить детальні результати фільтрації
    """
    print("=" * 70)
    print("ФІЛЬТРАЦІЯ ЧИСЕЛ ЗА ІНТЕРВАЛОМ")
    print("=" * 70)
    print()
    print("Програма перевіряє, чи входять три числа в інтервал [1, N]")
    print("де N - остання цифра вашого номера за списком")
    print()
    print("=" * 70)
    print()

    try:
        # Крок 1: Запитуємо останню цифру номера за списком
        n_input = int(input("Введіть останню цифру вашого номера за списком (N): "))

        # Перевірка коректності N (має бути від 1 до 9)
        if n_input < 1 or n_input > 9:
            print()
            print("Помилка! Остання цифра має бути в діапазоні від 1 до 9.")
            return

        print()
        print(f"Інтервал для перевірки: [1, {n_input}]")
        print()

        # Крок 2: Запитуємо три цілі числа
        print("Введіть три цілі числа для перевірки:")
        number1 = int(input("  Число 1: "))
        number2 = int(input("  Число 2: "))
        number3 = int(input("  Число 3: "))

        # Створюємо список з введених чисел
        input_numbers = [number1, number2, number3]

        print()
        print("=" * 70)
        print("ПРОЦЕС ФІЛЬТРАЦІЇ")
        print("=" * 70)
        print()

        # Крок 3: Фільтруємо числа
        inside_numbers, outside_numbers = filter_numbers_in_interval(input_numbers, n_input)

        # Крок 4: Виводимо результати
        display_filtering_results(inside_numbers, outside_numbers, n_input)

        print()
        print("=" * 70)

    except ValueError as error:
        print()
        print("=" * 70)
        print("ПОМИЛКА ВВЕДЕННЯ")
        print("=" * 70)
        print("Введено некоректне значення. Будь ласка, введіть ціле число.")
        print("=" * 70)

    except Exception as error:
        print()
        print("=" * 70)
        print("НЕСПОДІВАНА ПОМИЛКА")
        print("=" * 70)
        print(f"Виникла помилка: {str(error)}")
        print("=" * 70)


# Точка входу в програму
# Цей блок виконується тільки якщо файл запущено безпосередньо
if __name__ == "__main__":
    run_interval_filtering()
