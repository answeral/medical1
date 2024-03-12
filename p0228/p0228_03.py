member = []

# 입력 : 이름, 점수 ['홍길동','50']
# 총 3명의 정보를  member리스트에 넣으세요
# print(member)= [['홍길동,90'],['유관순,91],['이순신, 95]]
'''
for i in range(3):
    name = input("이름을 입력해주세요 >> ")
    score = int(input("점수를 입력해주세요 >> "))
    t = [name, score]
    member.append(t)
print(member)
'''

member = [['홍길동',55],['유관순',80],['이순신',90]]
#member라는 변수를 사용해서 홍길동님 불합격입니다. 합격입니다. 

for i in range(3):
    if member[i][1] >=60:
        print('{}님 합격입니다'.format(member[i][0]))
    elif member[i][1] <60:
        print('{}님 불합격입니다'.format(member[i][0]))
        

