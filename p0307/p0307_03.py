students = {"stuNo":1,'stuName':'홍길동','tel':'010-0000-0000',
            'gender':'male','id':'aaa','pw':1111}
#nicName : 길동스
students['stuNo'] = students['stuNo'] +1
print(students['stuNo'])

# print(students['studentNo']) # 키값이 없는 것을 불러오면 에러

if 'studentNo' in students:
     print('key가 있습니다')
else:
     print('key가 존재하지 않습니다')
     
