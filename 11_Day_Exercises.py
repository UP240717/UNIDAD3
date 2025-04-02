import re
import math

countries_data = {
    "country_list": [
        {
            "name": "Afghanistan",
            "languages": ["Pashto", "Dari"],
            "population": 38928346,
        },
        {
            "name": "Albania",
            "languages": ["Albanian"],
            "population": 2877797,
        },
        {
            "name": "Algeria",
            "languages": ["Arabic", "Tamazight"],
            "population": 43851044,
        },
        {
            "name": "Andorra",
            "languages": ["Catalan"],
            "population": 77265,
        },
        {
            "name": "Angola",
            "languages": ["Portuguese"],
            "population": 32866272,
        }
    ]
}

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


# Level 1

# 1
def add_two_numbers(a, b):
    return a + b


# 2
def area_of_circle(r):
    return 3.14 * r * r


# 3
def add_all_nums(arr):
    sum_of_nums = 0
    for i in arr:
        if isinstance(i, int):
            sum_of_nums += i
    return sum_of_nums


# 4
def convert_celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


# 5
def check_season(month):
    if month in ["September", "October", "November"]:
        print("Autumn")
    if month in ["December", "January", "February"]:
        print("Winter")
    if month in ["March", "April", "May"]:
        print("Spring")
    else:
        print("Summer")


# 6
def calculate_slope(x1, x2, y1, y2):
    m = (y2 - y1) / (x2 - x1)
    return m


# 7
# noinspection PyPep8Naming
def solve_quadratic_eqn(a, b, c):
    D = b * b - 4 * a * c
    X1 = (-b + D) / (2 * a)
    X2 = (-b - D) / (2 * a)
    print(X1, X2)


# 8
def print_list(lst):
    for i in lst:
        print(i)


# 9
def reverse_list(a):
    return a[::-1]


# 10
def capital_list_terms(a):
    for i in a:
        a[a.index(i)] = i.capitalize()
    return a


# 11
def add_item(mutable, tba):
    mutable.append(tba)
    return mutable


# 12
def remove_item(mutable, tbr):
    mutable.remove(tbr)
    return mutable


# 13
def sum_of_numbers(high):
    sum_of_numbers = 0
    for i in range(high + 1):
        sum_of_numbers += i
    return sum_of_numbers


# 14
def sum_of_odds(high):
    sum_of_odd_nums = 0
    for i in range(high + 1):
        if i % 2 == 1:
            sum_of_odd_nums += i
    return sum_of_odd_nums


# 15
def sum_of_even(high):
    sum_of_even_nums = 0
    for i in range(high + 1):
        if i % 2 == 0:
            sum_of_even_nums += i
    return sum_of_even_nums


# Level 2

# 1
def evens_and_odds(high):
    odds = 0
    evens = 0
    for i in range(high + 1):
        if i % 2 == 0:
            evens += i
        else:
            odds += i
    print(odds, evens)


# 2
def factorial(fac):
    fact = 1
    for i in range(fac + 1):
        fact *= i
    return fact


# 3
def is_empty(check):
    if check:
        return True
    else:
        return False


# 4
def mean(dataset):
    return sum(dataset) / len(dataset)


def median(dataset):
    data = sorted(dataset)
    index = len(data) // 2

    if len(dataset) % 2 != 0:
        return data[index]

    return (data[index - 1] + data[index]) / 2


def mode(dataset):
    frequency = {}

    for value in dataset:
        frequency[value] = frequency.get(value, 0) + 1

    most_frequent = max(frequency.values())

    modes = [key for key, value in frequency.items() if value == most_frequent]

    return modes


def variance(dataset):
    n = len(dataset)
    mean = sum(dataset) / n
    deviations = [(x - mean) ** 2 for x in dataset]
    variance = sum(deviations) / n
    return variance


def stdev(dataset):
    var = variance(dataset)
    std_dev = var ** 0.5
    return std_dev


# Level 3

# 1
def is_prime(n):
    if n <= 1:
        return False
    max_div = math.floor(math.sqrt(n))
    for i in range(2, 1 + max_div):
        if n % i == 0:
            return False
    return True


# 2
def checK_list(test_list):
    return len(set(test_list)) == len(test_list)


# 3
def homogeneous_type(seq):
    iseq = iter(seq)
    try:
        first_type = type(next(iseq))
    except StopIteration:
        return True  # Si la secuencia está vacía, se considera homogénea
    return first_type if all((type(x) is first_type) for x in iseq) else False

# 4
def isVar(test):
    return re.match(r"[_a-z]\w*$", test, flags=re.I)


list_data = countries_data["country_list"]  # Corregido el acceso a los datos
total_languages_initial = []
for country in list_data:
    total_languages_initial.extend(country["languages"])

print("Languages = ", len(set(total_languages_initial)))

counts = {}
for language in total_languages_initial:
    counts[language] = counts.get(language, 0) + 1

def sort_dict_by_value(d, reverse=False):
    return dict(sorted(d.items(), key=lambda x: x[1], reverse=reverse))

counts = sort_dict_by_value(counts, True)
print("Top 20 most spoken languages:")
for language, count in list(counts.items())[:20]:
    print(f"{language}: {count}")

populations = {}
for country in list_data:
    populations[country["name"]] = country["population"]

populations = sort_dict_by_value(populations, True)
print("Top 20 most populated countries:")
for country, population in list(populations.items())[:20]:
    print(f"{country}: {population}")