


def collect_basic_information():
  
    print("=" * 70)
    print("АНКЕТА СТУДЕНТА - БАЗОВА ІНФОРМАЦІЯ")
    print("=" * 70)
    print()

    # Створюємо словник для зберігання всієї інформації
    student_info = {}

    # Збираємо 6 базових питань
    student_info['Ім\'я'] = input("1. Введіть ваше ім'я: ")
    student_info['Прізвище'] = input("2. Введіть ваше прізвище: ")
    student_info['Вік'] = input("3. Введіть ваш вік: ")
    student_info['Група'] = input("4. Введіть вашу групу: ")
    student_info['Спеціальність'] = input("5. Введіть вашу спеціальність: ")
    student_info['Університет'] = input("6. Введіть назву вашого університету: ")

    return student_info


def collect_additional_information():

    print()
    print("=" * 70)
    print("АНКЕТА СТУДЕНТА - ДОДАТКОВА ІНФОРМАЦІЯ")
    print("=" * 70)
    print()

    # Створюємо словник для додаткової інформації
    additional_info = {}

    # Збираємо 10 додаткових питань
    additional_info['Місто'] = input("7. Введіть ваше місто проживання: ")
    additional_info['Телефон'] = input("8. Введіть ваш номер телефону: ")
    additional_info['Email'] = input("9. Введіть вашу email адресу: ")
    additional_info['Хобі'] = input("10. Введіть ваші хобі та інтереси: ")
    additional_info['Улюблений предмет'] = input("11. Введіть ваш улюблений предмет: ")
    additional_info['Плани'] = input("12. Введіть ваші плани після навчання: ")
    additional_info['Досвід роботи'] = input("13. Опишіть ваш досвід роботи (якщо є): ")
    additional_info['Мови'] = input("14. Якими мовами ви володієте: ")
    additional_info['Навички'] = input("15. Які мови програмування ви знаєте: ")
    additional_info['Проекти'] = input("16. Чи брали ви участь у проектах (які саме): ")

    return additional_info


def display_survey_results(basic_info, additional_info):
   
    print()
    print("=" * 70)
    print("РЕЗУЛЬТАТИ АНКЕТУВАННЯ")
    print("=" * 70)
    print()

    # Виводимо базову інформацію
    print("БАЗОВА ІНФОРМАЦІЯ:")
    print("-" * 70)
    for question, answer in basic_info.items():
        print(f"{question}: {answer}")

    print()

    # Виводимо додаткову інформацію
    print("ДОДАТКОВА ІНФОРМАЦІЯ:")
    print("-" * 70)
    for question, answer in additional_info.items():
        print(f"{question}: {answer}")

    print()
    print("=" * 70)
    print("Дякуємо за заповнення анкети!")
    print("=" * 70)


def run_survey():
   
    # Збираємо базову інформацію (6 питань)
    basic_information = collect_basic_information()

    # Збираємо додаткову інформацію (10 питань)
    additional_information = collect_additional_information()

    # Виводимо всі результати анкетування
    display_survey_results(basic_information, additional_information)


# Точка входу в програму
# Цей блок виконається тільки якщо файл запущено безпосередньо
if __name__ == "__main__":
    run_survey()
