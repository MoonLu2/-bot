import random

def generate(pass_length):
    elements = 'abcdefgyigklmnopqrstuvwxyz123456<>@!#*%'
    password = ''
    for i in range(pass_length):
        password += random.choice(elements)
    return password
