aa = [[1,2,3,4],[5,6],[7,8,9]]
a = [1,2,3,4,5]
aaa=[[[1,2],[3,4,5]],[[6],[7,8,9]]] 
a2 = [[1,[3,4,5],3,4],[5,6],[7,8,9]]
for i in a:
    print(i)
print('-'*50)   

for i in aa:
    for j in i:
        print(j)
print('-'*50)           

for i in aaa:
    for j in i:
        for k in j:
            print(k)
            
for i in a2:
    for j in i:
            if isinstance(j,list):
                for k in j:
                    print(k)
                else:
                    print(j)
                    
