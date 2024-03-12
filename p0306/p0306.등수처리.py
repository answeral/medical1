students =[
     {'stuNo': 'S001', 'name': '홍길동', 'kor': 100, 'eng': 99, 'math': 87, 'total': 286, 'avg': 95.33},
    {'stuNo': 'S002', 'name': '유관순', 'kor': 98, 'eng': 93, 'math': 87, 'total': 278, 'avg': 92.67},
    {'stuNo': 'S003', 'name': '이순신', 'kor': 88, 'eng': 76, 'math': 30, 'total': 194, 'avg': 64.67},
    {'stuNo': 'S004', 'name': '김구', 'kor': 100, 'eng': 100, 'math': 100, 'total': 300, 'avg': 100.0},
    {'stuNo': 'S005', 'name': '강감찬', 'kor': 98, 'eng': 85, 'math': 44, 'total': 227, 'avg': 75.67}]
# 등수처리 -> 합계를 가지고 처리

for i, s_dic in enumerate(students): #위치 파악 필요 enumerate 사용
     rank_cnt = 1 #등수처리 변수
     for i_dic in students:
          print(s_dic['total'])
          if s_dic['total']<i_dic['total']: #등수를 비교해서 
               rank_cnt += 1 # 현재학생의 합계보다 크면 1증가
     s_dic['rank'] = rank_cnt
     
     
print(students)

# [{'stuNo': 'S001', 'name': '홍길동', 'kor': 100, 'eng': 99, 'math': 87, 
# 'total': 286, 'avg': 95.33, 'rank': 2}, 
# {'stuNo': 'S002', 'name': '유관순', 'kor': 98, 'eng': 93, 'math': 87, 
# 'total': 278, 'avg': 92.67, 'rank': 3}, {'stuNo': 'S003', 'name': '이순신', 'kor': 88, 
# 'eng': 76, 'math': 30, 'total': 194, 'avg': 64.67, 'rank': 5}, 
# {'stuNo': 'S004', 'name': '김 
# 구', 'kor': 100, 'eng': 100, 'math': 100, 'total': 300, 'avg': 100.0, 'rank': 1}, 
# {'stuNo': 'S005', 'name': '강감찬', 'kor': 98, 'eng': 85, 'math': 44, 
# 'total': 227, 'avg': 75.67, 'rank': 4}]