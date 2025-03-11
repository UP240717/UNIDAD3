#1
lst = []

#2
lista1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

#3
print(len(lista1))

#4
firstitem = lista1[0]
middleitem = lista1[3]
lastitem = lista1[-1]
print(firstitem, middleitem, lastitem)

#5
mixed_data_types = ['Oliver', 18, 1.84, 'Single', 'PepePecas 45']
name, age, height, marital_status, address = mixed_data_types

#6
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

#7
print(it_companies)

#8
print(len(it_companies))

#9
firstcompany = it_companies[0]
middlecompany = it_companies[3]
lastcompany = it_companies[-1]
print(firstcompany, middlecompany, lastcompany)

#10
it_companies.pop()
print(it_companies)

#11 y 12
it_companies.insert(3, 'IT')
print(it_companies)

#13
it_companies[0] = it_companies[0].upper()
print(it_companies)

#14
joined_companies = '# '.join(it_companies)
print(joined_companies)

#15
doesexits = 'Google' in it_companies
print(doesexits)

#16
it_companies.sort()
print(it_companies)

#17
it_companies.reverse()
print(it_companies)

#18
first_three = it_companies[:3]
print(first_three)

#19
last_three = it_companies[-3:]
print(last_three)

#20
mid_three = it_companies[1:6]
newlist = [company for company in it_companies if company not in mid_three]
print(newlist)

#21
it_companies_1 = it_companies[1:7]
print(it_companies_1)

#22
mid = it_companies[3]
it_companies_2 = [company for company in it_companies if company not in mid]
print(it_companies_2)

#23
it_companies_3 = it_companies[0:6]
print(it_companies_3)

#24
it_companies.clear()
print(it_companies)

#25
