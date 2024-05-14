data = [1,2,3]

# for문 안의 data부분이 중요
for d in data: 
    print(d, sep=',',end='')

string = 'hello'

for s in string:
    print(s)

data = (1,2,3)
for i in data:
    print(i)
# data[1] = 5 안됨
# print(data(type(data)))

data3 = []
for i in data:
    # if문
    data3.append(i**2)
    print(data3)

# 간단하게
data2 = [i**2 for i in data if i**2 <5]
print(data2, type(data2))

# for(int i=0;i<10;i++)간단하게
# for(item :array)
data = []
for d in data:
    print(d)

# for i in range(10):
#     print(i)

# for i in range(1,6):

for idx, d in enumerate(data):
    print(idx, d)


data_2d = [[1,2,3],
           [4,5,6]]
for data in data_2d:
    for d in data:
        print(d, end = '')



# 구구단 range(1,10)
for i in range(1,10):
    # python은 tab으로 묶음 구분(들여쓰기 중요)
    for j in range(1, 10):
        print(f'{i} X {j} = {i*j}')
        print(i*j)

# range(1, 11) 1~10까지 sum, min, max, average

print(sum(range(1,11)))

# data = list(range(1, 1001))
# print(data, type(data))
# for d in data:
#     print(d, end='')

data = range(1, 1001, 2)
print(data, type(data))
for d in data:
        print(d, end=' ')

        