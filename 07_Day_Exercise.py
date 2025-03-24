#Level 1

#1
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}

print(f"The lenght of it companies is {len(it_companies)}")

#2
it_companies.add("Twitter")
print(it_companies)

#3
it_companies.update(["Youtube","Linux","Opera"])
print(it_companies)

#4
it_companies.discard("Youtube")
print(it_companies)

#5
print("The discard() method removes the specified element from the set. Unlike the remove() method, discard() does not raise an error if the specified element is not present.")

#Level 2

A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}


C = A.union(B)
print(C)

print(A.intersection(B))
print(A.isdisjoint(B))

AB = A.union(B)
BA = B.union(A)
print(AB,BA)

print(A.symmetric_difference(B))

del A,B

#Level 3

age_list = [22, 19, 24, 25, 26, 24, 25, 24]

age_set = set(age_list)

if len(age_set) == len(age_list):
    print('The set and the list are equal')

elif len(age_set) > len(age_list):
    print('Set is bigger')

else:
    print('List is bigger')

sentence = 'I am a teacher and I love to inspire and teach people'
words = set(sentence.split())
print(f'The number of unique words is {len(words)}')

