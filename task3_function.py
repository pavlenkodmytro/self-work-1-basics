"""
Завдання 3: Обчислення значення функції за заданою формулою

Програма обчислює значення математичної функції для заданого значення x.
Формула: f(x) = x² + 2x - 5

де:
- x - значення змінної (вводиться користувачем)
- x² - квадрат числа x
- f(x) - результат обчислення функції
"""


def calculate_function(x_value):
    """
    Обчислює значення функції f(x) = x² + 2x - 5

    Функція складається з трьох частин:
    1. x² - квадрат числа x
    2. 2x - подвоєне значення x
    3. -5 - константа

    Args:
        x_value (float): Значення змінної x

    Returns:
        float: Результат обчислення функції f(x)

    Example:
        >>> calculate_function(3)
        # f(3) = 3² + 2×3 - 5 = 9 + 6 - 5 = 10
        10

        >>> calculate_function(-2)
        # f(-2) = (-2)² + 2×(-2) - 5 = 4 - 4 - 5 = -5
        -5

        >>> calculate_function(0)
        # f(0) = 0² + 2×0 - 5 = 0 + 0 - 5 = -5
        -5
    """
    # Крок 1: Обчислюємо квадрат числа x
    x_squared = x_value ** 2
    print(f"Крок 1: Обчислення x²")
    print(f"  x² = {x_value}² = {x_squared}")
    print()

    # Крок 2: Обчислюємо подвоєне значення x
    two_x = 2 * x_value
    print(f"Крок 2: Обчислення 2x")
    print(f"  2x = 2 × {x_value} = {two_x}")
    print()

    # Крок 3: Обчислюємо фінальне значення функції
    # f(x) = x² + 2x - 5
    result = x_squared + two_x - 5

    print(f"Крок 3: Обчислення f(x)")
    print(f"  f(x) = x² + 2x - 5")
    print(f"  f({x_value}) = {x_squared} + {two_x} - 5")
    print(f"  f({x_value}) = {result}")

    return result


def analyze_function_value(x_value, f_x):
    """
    Аналізує обчислене значення функції.

    Виводить додаткову інформацію про:
    - Знак результату (додатний, від'ємний, нульовий)
    - Парність/непарність результату (якщо ціле число)

    Args:
        x_value (float): Значення аргументу x
        f_x (float): Значення функції f(x)
    """
    print()
    print("=" * 70)
    print("АНАЛІЗ РЕЗУЛЬТАТУ")
    print("=" * 70)

    # Аналіз знаку результату
    if f_x > 0:
        sign_description = "додатнє"
    elif f_x < 0:
        sign_description = "від'ємне"
    else:
        sign_description = "дорівнює нулю"

    print(f"Значення функції {sign_description}: f({x_value}) = {f_x}")

    # Перевірка на парність (якщо результат ціле число)
    if f_x == int(f_x):
        if int(f_x) % 2 == 0:
            parity = "парне"
        else:
            parity = "непарне"
        print(f"Результат є цілим числом і {parity}")


def run_function_calculation():
    """
    Головна функція для запуску програми обчислення функції.

    Послідовно:
    1. Запитує у користувача значення x
    2. Обчислює значення функції f(x) = x² + 2x - 5
    3. Виводить покрокове обчислення
    4. Аналізує отриманий результат
    """
    print("=" * 70)
    print("ОБЧИСЛЕННЯ ЗНАЧЕННЯ ФУНКЦІЇ")
    print("=" * 70)
    print()
    print("Формула: f(x) = x² + 2x - 5")
    print()
    print("=" * 70)
    print()

    try:
        # Запитуємо у користувача значення x
        x_input = float(input("Введіть значення x: "))

        print()
        print("=" * 70)
        print("ПОКРОКОВЕ ОБЧИСЛЕННЯ")
        print("=" * 70)
        print()

        # Обчислюємо значення функції
        function_result = calculate_function(x_input)

        # Аналізуємо результат
        analyze_function_value(x_input, function_result)

        # Виводимо фінальний результат
        print()
        print("=" * 70)
        print("РЕЗУЛЬТАТ")
        print("=" * 70)
        print(f"f({x_input}) = {function_result}")
        print("=" * 70)

    except ValueError as error:
        print()
        print("=" * 70)
        print("ПОМИЛКА ВВЕДЕННЯ")
        print("=" * 70)
        print("Введено некоректне значення. Будь ласка, введіть число.")
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
    run_function_calculation()
