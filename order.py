import numpy as np
import re


def get_choices(choices: list, choice_type: str):
    max_choices = len(choices)
    while True:
        prompt = input(f'How many {choice_type} would you like? (up to {max_choices}) ')
        if bool(re.findall(r'^\d+$', prompt)):
            choice_num = int(prompt)
            break
        print('Not a valid response! Try again.')
    if choice_num > max_choices:
        choice_num = max_choices
    elif choice_num == 0:
        choice_num = 1
    results = np.random.choice(choices, choice_num, replace=False)
    while 'Red Sauce' in results and 'White Sauce' in results and len(results) < len(choices):
        results = np.random.choice(choices, choice_num, replace=False)
    return results


def main():
    order = dict()
    sauces = ['BBQ', 'Garlic Rub', 'Mushroom Pesto', 'Olive Oil', 'Pesto', 'Red Sauce',
              'Spicy Calabrian Chili Red Sauce', 'White Sauce']
    cheeses = ['Asiago', 'Feta', 'Gorgonzola', 'Mozzarella', 'Parmesan', 'Ricotta']  # no dairy-free cheese
    meats = ['Anchovies', 'Bacon', 'Canadian Bacon', 'Grilled Chicken', 'Ground Beef', 'Mild Sausage', 'Pepperoni',
             'Plant-Based Italian Sausage', 'Salami', 'Spicy Chicken Sausage']
    veggies = ['Artichokes', 'Arugula', 'Basil - Fresh Chopped', 'Black Olives', 'Broccoli - Roasted',
               'Corn - Roasted', 'Garlic - Chopped', 'Garlic - Roasted', 'Green Bell Peppers', 'Jalapenos',
               'Mama\'s Little Sweet Hot Peppas', 'Mushrooms', 'Oregano', 'Pineapple', 'Red Onion',
               'Red Peppers - Roasted', 'Rosemary - Fresh Chopped', 'Salt & Pepper', 'Serrano Peppers', 'Spinach',
               'Tomatoes - Diced', 'Tomatoes - Sliced']
    finishing_sauces = ['Balsamic Fig Glaze', 'BBQ Swirl', 'Hot Buffalo Sauce', 'Mike\'s Hot Honey', 'Pesto Drizzles',
                        'Ranch', 'Red Sauce Dollops', 'Sri-rancha']
    for i, j in zip([sauces, cheeses, meats, veggies, finishing_sauces], ['sauces', 'cheeses', 'meats', 'veggies', 'finishing sauces']):
        order[j] = get_choices(i,j)
    for i, j in order.items():
        print(f'{i}:', ', '.join(j))


if __name__ == '__main__':
    main()
