def apply_all_func(int_list, *functions):
    # Создаем пустой словарь для хранения результатов
    results = {}

    # Перебираем все функции из *functions
    for func in functions:
        # Применяем функцию к списку int_list и сохраняем результат в словарь
        results[func.__name__] = func(int_list)

    # Возвращаем словарь с результатами
    return results


# Примеры вызова функции
print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))