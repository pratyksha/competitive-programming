from collections import Counter
n,m = [int(i) for i in input().split()]
chef_dict = {}
name, country = [], []
for _ in range(n):
    x, y = [i for i in input().split()]
    name.append(x)
    country.append(y)
    chef_dict[x] = y
subject = []
country_arr = []
for i in range(m):
    subject.append(input())
    country_arr.append(chef_dict[subject[i]])

c = Counter(country_arr)
val = c.most_common()
country_arrr =[]
for i in val:
    if val[0][1] == i[1]:
        country_arrr.append(i[0])
print(min(country_arrr))

s = Counter(subject)
val = s.most_common()
name_arr = []
for i in val:
    if val[0][1] == i[1]:
        name_arr.append(i[0])
print(min(name_arr))

