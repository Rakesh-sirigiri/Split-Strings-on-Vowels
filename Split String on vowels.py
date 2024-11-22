test_str = 'GFGaBste4oCS'
print("The original string is : " + str(test_str))
x= [97, 101, 111, 117, 65, 69, 73, 79, 85]
for i in test_str:
    if ord(i) in x:
        test_str=test_str.replace(i,"*")
    res=test_str.split('*')
    print("The splitted string : " + str(res))
