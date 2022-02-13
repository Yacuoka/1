from random import choice
import json


def gen_person():
    name = ''
    tel = ''

    letters = ['a', 'b', 'd', 'e', 'f', 'e', 'g']
    num = ['1', '2', '3', '4', '6', '8', '9', '0']

    while len(name) != 7:
        name += choice(letters)

    while len(tel) != 10:
        tel += choice(num)

    person = {
        'name': name,
        'tel': tel
    }

    return person, tel


def write_json(person_dict, num):
    try:
        data = json.load(open('person_data.json'))
    except FileNotFoundError:
        data = {}

    data[num] = person_dict

    with open('person_data.json', 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


for i in range(5):
   write_json(gen_person()[0], gen_person()[1])


# with open('person_data.json', 'r') as f:
#     json.dump(persons, f, indent=2, ensure_ascii=False)