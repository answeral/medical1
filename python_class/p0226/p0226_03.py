#list
#데이터를 잘 관리하기 위해서 묶어서 관리하는 자료형
#리스트 변수명 = [요소1, 요소2, 요소3 .... ]
list = []
list2 = [0,2,4]
list3 = ['짝수', '홀수']
list4 = ['홍길동', 100,100,100]
list5 = ['짝수', [2,4,6],'홀수',[1,3,5]]
#list자체도 하나의 요소로 사용가능

#인덱싱 (index) 리스트를 검색, 접근 할 때 사용
#index는 0부터 시작
numL = [0,1,2,3,4]
# 0을 출력
print(numL[0])
print(numL[-1])

#인덱스의 범위를 넘어가면 오류출력 numL[10]

#인덱스를 가지고 리스트의 특정 요소의 값을 수정 할 수 있다.
#리스트명[n] = 값
numL[0] = 20
print(numL)
numL[-1] = 222
print(numL)

# list5 = ['짝수', [2,4,6],'홀수',[1,3,5]]
#숫자 2에 접근하기 위해서는
print(list5[1]) # [2,4,6]
print(list4[1][0])
print(list5[3][2])
print(list5[-1][-1])

#리스트 슬라이싱 : 리스트자르기
# 콜론 : 을 사용해서 ~부터 ~까지
#리스트명[시작인덱스 : 끝인덱스+1]
# numL = [0,1,2,3,4]

print(numL[2:4]) # 2이상 4미만
print(numL[1:]) #1번 인덱스부터 끝까지
print(numL[:-1]) #마지막 전까지
print(numL[:3]) #처음부터 3번미만까지 (2번index까지)
print(numL[:])#처음부터 끝까지
print(numL[1:-1]) #처음부터 끝 바로 앞까지

# 리스트의 길이 : len(리스트명)
print(len[list])

#특정요소 삭제 :del(리스트명[n])

aa = [100,200,300,400,500,600,700]
print(aa)
del(aa[1]) 
print(aa) #[100,300,400,500,600,700]
del(aa[3:5]) 
print(aa)

#리스트 값 추가 : 리스트명.append(값)
aa = [100,200,300,400,500,600,700]
aa.append(800)
print(aa)
aa.append('숫자')
print(aa)
aa.append([1,2,3])
print(aa)

#리스트에서 특정값 제거
#리스트명.remove(값)
aa.remove(200) #200을 삭제시킴
print(aa)

aa.append(100)
aa.append(400)
aa.append(100)
#결과값 [100,300,400,500,600,700,800,'숫자,[1,2,3],100,400,100]
aa.remove(100) # 같은 값이 2개 이상
print(aa) #여러개가 있다해도 맨 앞에 있는 값을 삭제

#aa.remove(1) #1은 존재하지 않기 때문에 오류출력

#요소 확인 : 내부 포함된 요소의 존재를 확인하는 방법
# in, not in 
print(100 in aa) #True
print(200 not in aa) #True
print(2 in aa) # False

f=['사과','딸기','복숭아','수박','배']
print('딸기' in f)

if '사과' in f :
    print('사과가 있습니다')
else:
    print('사과가 없습니다') #사과가 있습니다
    
if '사과' not in f:
    print('사과가 없습니다')
else :
    print('사과가 있습니다')#사과가 있습니다
    
