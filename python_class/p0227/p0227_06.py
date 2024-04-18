# 이름, 아이디, 비밀번호 입력 받기
# 5명을 입력받아서 member리스트를 만드세요
# 멤버 리스트를 
# 이름  아이디 비밀번호
# 홍길동 aaa    11111
# 이순신  bbb    2222
# 형식으로 출력
member = [] # [[홍길동, aaa,111],[유관순, bbb, 222]]

for i in range(5):
  name = input('이름을 입력해주세요 >>')
  id = input('아이디를 입력해주세요 >>')
  ps = input('비밀번호를 입력해주세요 >>')
  mm = [name, id, ps]
  member.append(mm)
#print(member) 
#[['홍길동', 'aaa', '111'], ['이순신', 'bbb', '222'], ['유관순', 'ccc', '333'], 
# ['김구', 'ddd', '444'], ['이이', 'eee', '555']]
'''
print('이름\t 아이디\t 비밀번호')
print('{}\t{}\t{}'.format(member[0][0],member,[0][1],member[0][2]))
print('{}\t{}\t{}'.format(member[1][0],member[1][1],member[1][2]))
print('{}\t{}\t{}'.format(member[2][0],member[2][1],member[2][2]))
print('{}\t{}\t{}'.format(member[3][0],member[3][1],member[3][2]))
print('{}\t{}\t{}'.format(member[4][0],member[4][1],member[4][2]))
'''
print('이름\t 아이디\t 비밀번호')
for i in range(len(member)): # i =012
 print('{}\t{}\t{}'.format(member[i][0],member,[i][1],member[i][2]))
