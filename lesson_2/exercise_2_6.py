product_list = []
while True:
    question = input("Добавить новый продукт? (y/n): ")
    if question == "n":
        break
    elif question == "y":
        title = input("Введите название товара: ")
        price = int(input("Введите цену товара: "))
        count = int(input("Введите кол-во товара: "))
        unit = input("Введите единицу товара: ")
        product = {"название": title, "цена": price, "количество": count, "eд": unit}
        product_list.append(product)
        continue
    else:
        continue

result_products = []
for ind, p in enumerate(product_list):
    result_products.append((ind+1, p))


print(f"Список товаров: {result_products}")

analysis_result = {}
for product in product_list:
    for key, value in product.items():
        # Проверяем есть ли ключ в словаре, елси нет, то добавляем его с первым значением
        if analysis_result.get(key) is None:
            analysis_result[key] = [value]
        # Если ключ уже есть, то добавляем в лист значения новое значение
        else:
            analysis_result[key].append(value)
        # Избавляемся от дубликатов
            analysis_result[key] = list(set(analysis_result[key]))

print(analysis_result)
