from operator import itemgetter


class House:
    """Дом"""
    def __init__(self, id, h_num, build_num, people_i, street_id):
        self.id = id
        self.h_num = h_num
        self.build_num = build_num
        self.people_i = people_i
        self.street_id = street_id


class Street:
    """Улица"""
    def __init__(self, id, name):
        self.id = id
        self.name = name


class HouseStreet:
    """Дома на улице"""
    def __init__(self, street_id, house_id):
        self.street_id = street_id
        self.house_id = house_id


streets_arr = [
    Street(1, 'Ленина'),
    Street(2, 'Шарикоподшипниковская'),
    Street(3, 'Абрамцевская'),


    Street(11, 'Мясницкая'),
    Street(22, 'им.Олега Диндича'),
    Street(33, 'Бауманская')
]

houses_arr = [
    House(1, 13, 2, 112, 1),
    House(2, 26, 1, 137, 2),
    House(3, 5, 3, 244, 2),
    House(4, 25, 1, 272, 3),
    House(5, 14, 1, 182, 3),
    House(6, 29, 4, 212, 3)
]

houses_streets = [
    HouseStreet(1, 1),
    HouseStreet(2, 2),
    HouseStreet(2, 3),
    HouseStreet(3, 4),
    HouseStreet(3, 5),
    HouseStreet(3, 6),

    HouseStreet(11, 1),
    HouseStreet(22, 2),
    HouseStreet(22, 3),
    HouseStreet(33, 4),
    HouseStreet(33, 5),
    HouseStreet(33, 6)
]

def main():
    one_to_many = [
        (h.h_num, h.build_num, h.people_i, s.name)
        for h in houses_arr
        for s in streets_arr
        if h.street_id == s.id
    ]

    many_to_many = [
        (h.h_num, h.build_num, h.people_i, [s.name for s in streets_arr if s.id == h_s.street_id][0])
        for h in houses_arr
        for h_s in houses_streets
        if h.id == h_s.house_id
    ]
    '''
    print('1_to_m')
    print(one_to_many)
    print('m_to_m')
    print(many_to_many)
    '''

    print('Задание Г1')

    print(list(filter(lambda x: x[3].startswith("А"), one_to_many)))
    #print(list(filter(lambda x: x[3][0][0] = 'А', one_to_many)))
    
    print('\nЗадание Г2')

    streets_max_pi_house = []

    for s in streets_arr:
        st_h_num = [(s_n, p_i) for h_n, b_n, p_i, s_n in one_to_many if s.name == s_n]
        if len(st_h_num) > 0:
            streets_max_pi_house.append(max(st_h_num))
    
    result_2 = sorted(streets_max_pi_house, key=itemgetter(1), reverse=True)

    print(result_2)
 
    print('\nЗадание Г3')

    print(sorted(many_to_many,key = lambda x: x[3]))
 
if __name__ == '__main__':
    main()