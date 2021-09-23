lux = [490, 334, 550, 18.72]
print(lux)
lux = {'health' : 490, 'mana' : 334, 'melee' : 550, 'armor' : 18.72}
print(lux)
print(lux['health'])

# dict 으로 딕셔너리 만들기
lux1 = dict(health = 490, mana = 334, melee = 550, amor = 18.72)
print("lux1 : ", lux1)

lux2 = dict(zip(['health', 'mana', 'melee', 'armor'], [490, 334, 550, 18.72]))
print("lux2 : ", lux2)

lux3 = dict([('health', 490), ('mana', 334), ('melee', 550), ('armor', 18.72)])
print("lux3 : ", lux3)

lux4 = dict({'health' : 490, 'mana' : 334, 'melee' : 550, 'armor' : 18.72})
print("lux4 : ", lux4)
print("mana : ", lux['mana'])

# 딕셔너리 key 의 값 변경(할당)하기
print("before : ", lux)
lux['mana'] = 543
lux['health'] = 988
lux['mena_regen'] = 3.28
print("after : ", lux)

# 딕셔너리에 key 가 있는지 확인
print('mana' in lux)
print('attack' in lux)

# 딕셔너리 key 개수 구하기
print(len(lux))

#x = {'a' : 10, 'b' : 20}
x = {'Hello' : 10, 'world' : 20}
print(x['Hello'])

#3
