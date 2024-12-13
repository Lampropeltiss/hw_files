def write_recipes_from_file(file_name, recipe_book):
    with open(file_name, 'r', encoding='utf-8') as file:
        data = []
        for line in file:
            data.append(line.strip())
        while data[-1] == '':  # обрезка пустых строк в конце файла
            data = data[:-1]
        recipes_number = data.count('') + 1
        for i in range(1, recipes_number):
            recipe = data[:data.index('')]
            write_recipe(recipe, recipe_book)
            data = data[data.index('') + 1:]
        write_recipe(data, recipe_book)


def write_recipe(recipe, recipe_book):
    dish = recipe[0]
    ingredient_list = []
    for raw_line in recipe[2:]:
        line = raw_line.split(' | ')
        ingredient = {'ingredient_name': line[0],
                      'quantity': int(line[1]),
                      'measure': line[2]}
        ingredient_list.append(ingredient)
    recipe_book |= {dish: ingredient_list}


def print_recipe_book(recipe_book):
    for dish, ingredient_list in recipe_book.items():
        print(dish)
        for line in ingredient_list:
            print(line)
        print()


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for ingredient in cook_book[dish]:
            if ingredient['ingredient_name'] not in shop_list:
                shop_list.update({ingredient['ingredient_name']: {'measure': ingredient['measure'],
                                                                  'quantity': ingredient['quantity'] * person_count}})
            else:
                shop_list[ingredient['ingredient_name']]['quantity'] += ingredient['quantity'] * person_count
    for ingredient in shop_list.items():
        print(ingredient)


cook_book = {}
write_recipes_from_file('recipes.txt', cook_book)

get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
