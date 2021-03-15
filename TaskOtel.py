class Hotel:
    """Класс отеля"""

    def __init__(self, hotelname,  # название отеля
                 adress,  # адрес отеля
                 countsingleroom=3,  # количество однокомнатных номеров
                 countdoublerooms=2,  # количество однокомнатных номеров
                 counttriplerooms=1,  # количество однокомнатных номеров
                 status=3,  # статус (количество звезд)
                 ):
        self.hotelname = hotelname
        self.adress = adress
        self.countsingleroom = countsingleroom
        self.countdoublerooms = countdoublerooms
        self.counttriplerooms = counttriplerooms
        self.status = status
        self.singlerooms = [Room(100 + i) for i in range(self.countsingleroom)]
        self.doublerooms = [Room(200 + i, room_rate=2_000, room_area=2, classrooms='люкс') for i in range(self.countdoublerooms)]
        self.triplerooms = [Room(300 + i, room_rate=3_000, room_area=3, classrooms='бизнесс') for i in range(self.counttriplerooms)]
        self.allrooms = self.singlerooms + self.doublerooms + self.triplerooms


    def spisok_free_number(self):
        for i in self.allrooms:
            if i.status == 'свободна':
                print(f"{i.number} {i.classrooms}")

    def human_in_hotel(self, number_room, roomer):
        for i in self.allrooms:
            if i.number == number_room:
                i.status = 'занята'
                i.human = roomer
                roomer.number_nomer = number_room
                print(f'Добро пожаловать {i.human.roomername} в {self.hotelname}, ваш номер {number_room}')

    def human_out_hotel(self, roomer):
        for i in self.allrooms:
            if i.number == roomer.number_nomer:
                i.status = 'свободна'
                i.human = None
                print(f'{roomer.roomername} выписали из номера {roomer.number_nomer} отеля {self.hotelname}')

    def human_replace_hotel(self, number_room_in, roomer):
        self.human_out_hotel(roomer)
        self.human_in_hotel(number_room_in, roomer)

    def change_status_rooms(self, status, roomer):
        for i in self.allrooms:
            if i.number == roomer.number_nomer:
                i.status = f'Ремонт! Причина: {status}'
                print(f"{i.number} {i.classrooms} {i.status} проживает: {i.human.roomername}")

    def spisokallrooms(self):
        for i in self.allrooms:
            if i.human != None:
                print(f"{i.number} {i.classrooms} {i.status} {i.human.roomername}")
            else:
                print(f"{i.number} {i.classrooms} {i.status}")


class Room:
    """Класс комнат в отеле"""

    def __init__(self, number=100,  # номер комнаты
                 classrooms='эконом',  # класс номера (бизнесс, эконом, люкс...)
                 room_area=1,  # количество комнат в номере
                 room_rate=1_000,  # стоимость номера
                 status='свободна',  # статус комнаты (свободна, ремонт, занята)
                 ):
        self.number = number
        self.classrooms = classrooms
        self.room_area = room_area
        self.room_rate = room_rate
        self.status = status
        self.human = None

class Roomer:
    """Класс посетителей отеля"""

    def __init__(self, roomername, age, document="паспорт"):
        self.roomername = roomername
        self.age = age
        self.document = document
        self.number_nomer = None

if __name__ == '__main__':
    otelastoria = Hotel('Hotel Astoria', 'г. Чита, ул. Бутина 120')

    while True:
        quest = '1 - Заселиться\n2 - Выселиться\n3 - Сменить номер\n4 - Отремонтировать\
                \n5 - Просмотр всех комнат\
                \n6 - Выход\n'
        try:
            str_vibor = input(quest)
        except ValueError:
            print("Ввели не число")
            continue

        if str_vibor == '1':
            name = input('Введите имя ')
            age = input('Введите возраст ')
            human = Roomer(name, age)
            print(otelastoria.spisok_free_number())
            number_room = int(input('Введите № номера для заселения '))
            otelastoria.human_in_hotel(number_room, human)

        elif str_vibor == '2':
            otelastoria.human_out_hotel(human)

        elif str_vibor == '3':
            print(otelastoria.spisok_free_number())
            number_room_in = int(input('Введите № номера для переселения '))
            otelastoria.human_replace_hotel(number_room_in, human)

        elif str_vibor == '4':
            status = input('Введите название поломки ')
            otelastoria.change_status_rooms(status, human)

        elif str_vibor == '5':
            print(otelastoria.spisokallrooms())

        elif str_vibor == '6':
            exit()
