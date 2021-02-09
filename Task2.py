def add_order(orders, topings):
    for toping in topings:
        if toping in orders:
            continue
        if input(f'Добавляем {toping}? y/n ') == 'y':
            orders.append(toping)
            print('Добавили')


    return orders

def vibor_zakaza():
    topings = ('sous', 'luk', 'perec')
    orders = []

    exit_vibor = input('Хотите произвести заказ? y/n ')
    while exit_vibor == 'y':
        orders = add_order(orders, topings)
        if len(orders) == 0:
            exit_vibor = input('Вы ничего не добавили. Хотите попробовать снова? y/n ')
        elif len(orders) == len(topings):
            print('Вы выбрали все что можно. Спасибо за заказ')
            exit_vibor = 'n'
        else:
            exit_vibor = input(f'Ваш заказ {orders}. Хотите еще добавить? y/n ')

    print('Всего доброго')


if __name__ == '__main__':
    vibor_zakaza()
