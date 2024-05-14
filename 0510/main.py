print('hello, world!')

hh = 5
bb = 3.14
c = 'hello, world!'
dada = [1, 2, 3]
eeee = 'everything' or 'object'

print(type(hh), type(bb), type(c), type(dada), type(eeee))

a=5
b=0
print(a+b)
print(a-b)
print(a*b)
if b !=0:
    print(a/b)
    print(a//b)
else:
    print('error, b is 0')


a=2
b=2
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a**3) 
print(a**b)


def calc(a,b):
    print(a+b)
a=3.14
b=1.2
calc(a,b)
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a**b)

a=3.14
b=1_000_000
print(a,b)
calc(a,b)


a=5
b=3

#swap
temp =a
a=b
b=temp
print(a,b)
b, a = a,b
# a, b = map(int, input().split())

print(a,b)

msg = 'hello, world!'
print(msg, type(msg))

# print(msg.title())
print(msg.capitalize())

print(msg.find('l'))

print(msg[0])
print(msg[0:2])
print(msg[1])
# msg[0] ='H'
print(msg)

# str은 못바꿈 바꾸려면 아예 새로 새 값을 지정해야함
# msg = 'Hello, world!' 이렇게

a = 'hello'
b = 'world'

def add(a,b):
    return a+b
print(f'{a},{b}, {add(1,2)}! \n\t hahaha!')

msg = '     hello     '
print(len(msg))
print(len(msg.rstrip()))
print(len(msg.lstrip().rstrip()))
msg.lstrip().rstrip()
print(len(msg))
msg = msg.lstrip().rstrip()
print(len(msg))

msg = 'hello, hello, hello, world'
print(msg.replace('hello', 'Hello'))
print(msg.replace('hello', '').replace(',','').lstrip().rstrip())
print(msg)


