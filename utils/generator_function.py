import json
import random
import string


file_name = "dane.json"


def generate_male_name(save_data_to_file=False):
    male_name = generate_name(False)
    if save_data_to_file:
        save_data(male_name)
    return male_name


def generate_female_name(save_data_to_file=False):
    female_name = generate_name(True)
    if save_data_to_file:
        save_data(female_name)
    return female_name


def generate_unisex_last_name(save_data_to_file=False):
    last_name = random_value_for_key("unisex_last_names")
    if save_data_to_file:
        save_data(last_name)
    return last_name


def generate_domain(save_data_to_file=False):
    domain = random_value_for_key("domains")
    if save_data_to_file:
        save_data(domain)
    return domain


def generate_street(save_data_to_file=False):
    street = random_value_for_key("streets")
    if save_data_to_file:
        save_data(street)
    return street


def generate_city(save_data_to_file=False):
    city = random_value_for_key("cities")
    if save_data_to_file:
        save_data(city)
    return city


def generate_address(save_data_to_file=False):
    adress = generate_street() + " " + generate_city()
    if save_data_to_file:
        save_data(adress)
    return adress


def generate_female_person(save_data_to_file=False):
    person = json.dumps({
        "first_name": generate_female_name(),
        "last_name": generate_unisex_last_name(),
        "email": generate_random_email(),
        "nick": generate_nick(6, 2),
        "adress": generate_address()})
    if save_data_to_file:
        save_data(person)
    return person


def generate_nick(letters_nb, num_range, save_data_to_file=False):
    nick = letters_generator(letters_nb) + numbers_generator(num_range)
    if save_data_to_file:
        save_data(nick)
    return nick


def letters_generator(letters_nb):
    return ''.join(random.choice(string.ascii_uppercase) for y in range(letters_nb))


def numbers_generator(num_range):
    return ''.join(random.choice(string.digits) for x in range(num_range))


def generate_name(sex):
    if sex:
        return random_value_for_key("first_names_female")
    else:
        return random_value_for_key("first_names_male")


def generate_random_email(save_data_to_file=False):
    email = generate_unisex_last_name() + "@" + generate_domain()
    if save_data_to_file:
        save_data(email)
    return email


def random_value_for_key(key_name):
    with open(file_name) as f:
        data = json.load(f)
        value = data[key_name]
        return random.choice(list(value))


def save_data(value):
    with open('result.json', 'w', encoding="utf-8") as data_file:
        json.dump([value], data_file, ensure_ascii=False)
