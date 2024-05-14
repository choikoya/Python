# pizza_data = ['포테이토','치즈','쉬림프']
# for pizza in pizza_data: 
#     # print(pizza)
#     print(f'나는 {pizza} 피자를 좋아한다')


# # 107p

# for n in range(1, 21):
#     print(n, end=' ')

# for num in range(1, 1000001):
#     list = []
    

data = list(range(1, 11))
print(data, data[1:5], sep='\n')
print(data, data[-10], sep='\n')
print(data, data[1:-1], sep='\n')
print(data, data[:5], data[5:], sep='\n')
print(data, data[::-1], sorted(data, reverse=True), sep='\n')


# 113p

pizza_data = ['포테이토','치즈','쉬림프']
friend_pizza = ['포테이토','치즈','쉬림프']
pizza_data.append('페퍼로니')
friend_pizza.append('베이컨')

print(pizza_data)
print(friend_pizza)

# 129p

car = 'hundai'
if car == 'audi':
    print("Is car == 'hundai'? I predict True")

print(car == 'hundai')

# 137p

alien_color = 'red'
if alien_color == 'green':
    print("player가 5점 획득")
elif alien_color != 'yellow':
    print("out")
else:
    print("restart")



age = 2
if age < 2:
    print('baby')
elif 2<= age and age <4:
    print('toddler')



# 142p

names = ['a','b','c','admin']

for name in names:  
    if name == 'admin'  :
        print('관리자 접속')
    elif name != 'admain':
        print('안녕히가세요')












    