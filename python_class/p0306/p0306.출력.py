students =[
     {'stuNo': 'S001', 'name': '홍길동', 'kor': 100, 'eng': 99, 'math': 87, 'total': 286, 'avg': 95.33},
    {'stuNo': 'S002', 'name': '유관순', 'kor': 98, 'eng': 93, 'math': 87, 'total': 278, 'avg': 92.67},
    {'stuNo': 'S003', 'name': '이순신', 'kor': 88, 'eng': 76, 'math': 30, 'total': 194, 'avg': 64.67},
    {'stuNo': 'S004', 'name': '김구', 'kor': 100, 'eng': 100, 'math': 100, 'total': 300, 'avg': 100.0},
    {'stuNo': 'S005', 'name': '강감찬', 'kor': 98, 'eng': 85, 'math': 44, 'total': 227, 'avg': 75.67}]

cnt = len(students)+1 #학번
while True:
     count = input('학생전체출력을 하시겠습니까? (1. 확인 0.취소) >> ')
     if count == '0':
          print('성적전체출력을 취소합니다')
          break
     print('\t[ 학생전체성적 출력 ]')
     print('-'*50)
     print('학번\t이름\t국어\t영어\t수학\t합계\t평균')
     print('-'*50)
     for s_dic in students:
          for s_key in s_dic:
               print(s_dic[s_key],end = '\t')

          print()
     print('-'*50)








# while True:
#      #먼저 학생찾기
#      for name in students:
#           search = input('찾고자 하는 학생의 이름을 입력해주세요 (0.취소) >> ')
#           if search == '0':
#                print('학생찾기를 종료합니다')
#                break
#           if search == students[name]:
#                print(f'{search}학생을 찾았습니다.' )
          
          
          