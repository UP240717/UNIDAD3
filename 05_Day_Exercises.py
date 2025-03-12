#Level1
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
del it_companies

#26
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

#27
extra = ['Python', 'SQL'] 
full_stack = front_end + extra
print(full_stack)


#Level2
#1
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

ages.sort()
print(ages)
minimum = min(ages)
maximum = max(ages)

print(f"The min value is {minimum}, the max value is {maximum}")

ages.insert(0,minimum)
ages.insert(len(ages),maximum)
print(ages)

midValue = len(ages)
mid2 = int(midValue // 2)
mid1 = int(midValue // 2) -1
mid = (ages[mid1] + ages[mid2])/2
print(mid)

suma =  sum(ages)

avarage = suma / len(ages)
print(avarage)

rang = max(ages) - min(ages)
print(rang)

compare = abs(min(ages) - avarage) < abs(max(ages) - avarage)

#1
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe']

#2
if len(countries) % 2 == 1:
    midValue = len(countries)
    mid2 = int(midValue // 2)
    mid1 = int(midValue // 2) -1
    print(countries[mid1],countries[mid2])
else:
    mid = int(len(countries))
    print(countries[mid])

n = len(countries)
    

 #2
if n % 2 == 1:
    middle = [countries[n // 2]]
else:
    middle = [countries[n // 2 - 1], countries[n // 2]]

first_half = countries[: (n + 1) // 2]
second_half = countries[(n + 1) // 2 :]

#3
countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
chn, rss, usa, *scandic = countries
print(chn)
print(rss)
print(usa)
print(scandic)


