print('Hello, World!')

print(len('Hello, World!'))

print(type('Hello, World!'))

print(str(10))

print(int('10'))

input('Pon tu Nombre: ')

#Variables en Python
first_name = 'Oliver'
last_name = 'Camacho'
country = 'México'
city = 'Aguascalientes'
age = '18'
is_married = 'Falso'
skills = ['Python', 'Guitarra', 'Crochet', 'HandCraft']
person_info = {
    'first_name': 'Oliver',
    'lastname': 'Camacho',
    'country': 'México',
    'city':'Aguascalientes'
    }

print('Hello, World!')
print('Hello',',', 'World','!')
print(len('Hello, World!'))

#Printing the values stored in the variables

print('Nombre: ', first_name)
print('Longitud del nombre: ', len(first_name))
print('Apellido: ', last_name)
print('Longitud del apellido: ', len(last_name))
print('Pais: ', country)
print('Ciudad: ', city)
print('Edad: ', age)
print('¿Está Casado? ', is_married)
print('Habilidades: ', skills)
print('Información Personal', person_info)

#Declaring multiple variables in one line

First_name, Last_name, Country, Age, Is_married = 'Oliver','Camacho','Mexico','18','False'

print(First_name, Last_name, Country, Age, Is_married)
print('Nombre: ', First_name)
print('Apellido: ', Last_name)
print('Pais: ', Country)
print('Edad: ', Age)
print('¿Está Casado? ', Is_married)


first_name = input('What is your name?')
age = input('How old are you?')

print(first_name)
print(age)