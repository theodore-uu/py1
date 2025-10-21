#과제11

a = input('임의의 숫자를 5개 입력:')
b =  list(map(int,a))

print(b)

a = input('임의의 문자 1개 입력:')
b =  list(map(str,a))

print(b)

#과제12

a = input('임의의 숫자를 5개 입력:')
b =  list(map(int,a))
del b[-2:]
print(b)

#과제13

a = input('임의의 숫자를 5개 입력:')

for index,value in enumerate(a, start = 101):
    print(index,value)
    
#과제14

a = [10,20,30,40,30,20,10]
b = a.count(20)
print('숫자20은',b,'개입니다')

#과제15

a = input('임의의 숫자를 10개 입력:')
b = list(map(int, a.split()))
min_value = min(b)
max_value = max(b)

print('최저값:',min_value,'최대값:',max_value)

#과제16

a = input('임의의 숫자를 10개 입력:')
b = list(map(int, a.split()))

b.remove(min(b))
b.remove(max(b))

result = sum(b)
print(result)

#과제17

a = [10, 20, 30, 40, 30, 20, 10]
while 20 in a:
    a.remove(20)
print(a)  

#과제18

a = list(i for i in range(1,6))
print(a)


#과제19

a = [i for i in range(1,21) if i % 2 == 1]
print(a)

#과제20

a = list(map(int, input('표준입력:').split()))

b = [2 ** i for i in range(a[0], a[1] + 1)]
del b[1]           
del b[-2]          

print('실행결과:', b)

