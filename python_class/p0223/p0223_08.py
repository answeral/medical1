# 점수를 입력받아서
# 90점 이상이면 A 80점 이상이면 B 70점이상이면 C 나머지는 F

grd = int(input('점수를 입력해주세요 >>'))
'''
if grd >= 90:
  print("A")
elif 80 <= grd < 90:
  print ("B")
elif 70 <= grd <80:
  print("C")
else:
    print("F")
'''    
 # 2. 98점이상 A+ 90-93사이는 A- 91 92 
 # B+, B-, C+, c- (중첩 if)    c+ 79 78 77 c 76 75 74 c- 73 72 71 
 # B+ = 87,88,89 B- 81,82 B 80 c+ 77,76,75


if grd >= 98:
 print("A+")
 if 90<= grd <= 93:
     print("A-")
 if 94<= grd <98:
     print("A-")
if 90>grd >= 88:
 print("B+")
 if 80 <= grd <= 83:
     print ("B")
 else:
     print("B-")  
if 80>grd >= 78:
  print("C+")
  if 70<=grd<=73:
      print(("C"))
  else:
     print("C-")                
else:
    print("F")     



'''
if grd >= 98:
    print("A+")
elif 94 <= grd <=97:
       print("A")
elif 90 <= grd <=93 :
        print("A-")
elif 83 <= grd <= 86:
      print ("B")
elif 87<= grd <= 89:
       print("B+")    
elif 80<grd<=82:
       print("B-")  
elif 70 <= grd <80:
        print("C") 
elif  77 <= grd <= 79:
        print("C+")
elif 71 <= grd <=73:
        print("c-")
else:
    print("F") 
    '''