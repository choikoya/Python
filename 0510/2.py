data = [1,2,3]
data1 = [1,2,3,4,5]
print(data, type(data))

# # 객체생성
# data = list() 
# print(data, type(data))

print(data[0])
print(data[1])
print(data[2])
print(len(data))
print(len(data1))

# data넣음
data.append(6)
data.append(7)
data.append(8)
print(data, len(data))

data[3] = 4
data[4] = 5
print(data, len(data), sum(data), min(data), max(data))


# data = list(range(1,2,3,4,5,6,7,8,9,10))
data = list(range(1, 11))

data = list(range(10, 0, -1))
print(data, type(data), sorted(data))

# 10
# 10 9 8 7 6 5 4 3 2 1
# 합계, 정렬, 최댓값, 최솟값 구하라

# # 10 9 8 7 6 5 4 3 2 1
# data = input()
# # 데이터 타입 꼭 적어서 뭔지 알아야 함
# data  = list(map(int, data))

# # data  = list(map(int, input().split()))
# print(data, type(data), type(data[0]))
# print(sum(data))

# # print(data.split(), type(data.split())) 
# number = int('56')
# print(number, type(number))


data = [1,2,3]
del data[1]
print(data)


data = [1,2,3.14, 'hello', len, range(5)]
print(data, type(data))