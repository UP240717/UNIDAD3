#Number 1-3

Age = int(18)
Height = float(1.8)
Complex_Number = (1 + 1j)


# Number 4

base = int(input('Enter base:'))

height = int(input('Enter height:'))

area_triangle = float(base * height * 0.5)

print('The area of the triangle is:', area_triangle)


#Number 5

a = int(input('Enter side a:'))
b = int(input('Enter side b:'))
c = int(input('Enter side c:'))

perimeter = int(a + b + c)

print('The perimeter of the triangle is', perimeter)


#Number 6

Lenght= int(input('Lenght: '))
Width= int(input('Width: '))
Area= int(Lenght * Width)
Perimeter= int(2 * (Lenght + Width))
print('Area of a rectangle:', Area)
print('Perimeter of a rectangle:', Perimeter)


#Number 7

Radius= int(input('Radius: '))
Area= int(3.14 * Radius ** 2)
Perimeter= int(2 * 3.14 * Radius)
print('Area of a circle:', Area)
print('Perimeter of a circle:', Perimeter)


#Number 8

x1 = int(input('x1: '))
y1 = int(input('y1: '))
x2 = int(input('x2: '))
y2 = int(input('y2: '))
slope= int(y2-y1) / int(x2-x1)
print('slope:', slope)


#Number 9

Y1= int(input('y1: '))
Y2= int(input('y2: '))
X1= int(input('x1: '))
X2= int(input('x2: '))
Slope = (Y2 - Y1) / (X2 - X1)
print('slope:', Slope)


x1= int(X1)
y1= int(Y1)
x2= int(X2)
y2= int(Y2)
distance= int((X2 - X1) * 2 + (Y2 - Y1) * 2)
print('distance:', distance)


#Number 10
#Boolean
#True, False

print(Slope >= slope)
print(Slope <= slope)
print(Slope == slope)
print(Slope != slope)
print(Slope > slope)
print(Slope < slope)


#Number 11

x= int(input('x: '))
X= int(input('X: '))
y= int(x**2 + 6*X + 9)
print('y:', y)


#Number 12

print(len('python') == len('dragon'))
print(len('python') != len('dragon'))
print(len('python') < len('dragon'))
print(len('python') > len('dragon'))
print(len('python') >= len('dragon'))
print(len('python') <= len('dragon'))


#Number 13
#boolean
#True, False

python = 'python'
dragon = 'dragon'
print("on" in python and "on" in dragon)


#Number 14
print('I hope this course is not full of jargon.')
if 'jargon' in 'I hope this course is not full of jargon.':
    print('jargon is in the sentence')


#Number 15
print('Palabras: python, dragon')
if 'on' in 'python' and 'on' in 'dragon':
    print('True, There is "on" in both: dragon and python')
else: print('False, There is no "on" in both: dragon and python')


#Number 16
print('Letras en la palabra "python"')
print(float(len('python')))
print(str(len('python')))


#Number 17
numero = int(input('Ingrese un número: '))
if numero % 2 == 0:
    print('El número es par')
else: print('El número es impar')


#Number 18
Pordividir = 7
Divisor = float(Pordividir / 3)
if Divisor == int(2.7):
    print('True')
else: print('False')


#Number 19
if type(10) == '10':
    print('True')
else: print('False')


#Number 20
if int(9.8) == 10:
    print('True')
else: print('False')


#Number 21
hours = int(input('Enter hours: '))
rate_per_hour = int(input('Enter rate per hour: '))
weekly_earning = int(hours * rate_per_hour)
print('Your weekly earning is', weekly_earning)

#Number 22
years = int(input('Enter number of years you have lived: '))
seconds = int(years * 365 * 24 * 60 * 60)
print('You have lived for', seconds, 'seconds')

#Number 23
print("i  i^0  i^1  i^2  i^3")
for i in range(1, 6):
    print(f"{i}  {i**0}  {i**1}  {i**2}  {i**3}")

