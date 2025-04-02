
import random

chars = 'abcdefghijklmnopqrstuvwxyz1234567890'
char_list = []
char_list[:0] = chars


# Level 1

#1
def random_user_id():
    identity = ''
    for _ in range(6):
        identity += random.choice(char_list)
    return identity
print(random_user_id())

#2
def user_id_gen_by_user():
    charsize = int(input('Enter Character Size: '))
    charlimit = int(input('Enter how many user ids to generate: '))
    for _ in range(charlimit):
        identity = ''.join([random.choice(char_list) for _ in range(charsize)])
        print(identity)

print(user_id_gen_by_user())

#3
def rgb_color_gen():
    r = str(random.randint(0, 255))
    g = str(random.randint(0, 255))
    b = str(random.randint(0, 255))
    return "rgb(" + r + "," + g + "," + b + ")"
print(rgb_color_gen())

# Level 2

#1
def list_of_hexa_colors(many=0):
    if many == 0:
        many = random.randint(1, 10)
    hexas = "1,2,3,4,5,6,7,8,9,0,a,b,c,d,e,f".split(",")
    hexCodes = []
    for _ in range(many):
        hexCodes.append("#" + ''.join([random.choice(hexas) for _ in range(6)]))
    return hexCodes
print(list_of_hexa_colors())

#2
def list_of_rgb_colors(many=0):
    if many == 0:
        many = random.randint(1, 10)
    rgbs = []
    for _ in range(many):
        rgbs.append(rgb_color_gen())
    return rgbs

#3
def generate_colors(type_of_col, many):
    if type_of_col == 'hexa':
        return list_of_hexa_colors(many)
    elif type_of_col == 'rgb':
        return list_of_rgb_colors(many)
    else:
        return "Invalid Input"

generate_colors('hexa', 3)
generate_colors('hexa', 1) 
generate_colors('rgb', 3)  
generate_colors('rgb', 1)


# Level 3

#1
def shuffled_list(array):
    return random.sample(array, len(array))

#2
def seven_random():
    arr = []
    length = -1
    while length <= 7:
        num = random.randint(0, 9)
        if num not in arr:
            arr.append(num)
            length = len(arr)
    return arr
print(seven_random())