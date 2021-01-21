"""
如果生成一个平方列表，比如[1,4,9]，使用for循环怎么写，使用列表生成式怎么写
"""
# list_test=[]
# for i in range(1,4):
#     list_test.append(i**2)
# print(list_test)
#
# list_test2=[i**2 for i in range(1,4)]
# print(list_test2)
#
# list_test3=[]
# for i in range(1,4):
#     if i != 1 :
#      list_test3.append(i**2)
# print(list_test3)
#
# list_test4=[i**2 for i in range (1,4) if i != 1]
# print(list_test4)

# list_test5=[]
# for i in range(1,4):
#     for j in range(2,5):
#         list_test5.append(i*j)
# print(list_test5)
#
# list_test6=[i*j for i in range (1,4) for j in range (2,5)]
# print(list_test6)


"""
0-30之间能被3整除的数
"""
# list_test1=[i for i in range (0,31) if i % 3 == 0]
# print(list_test1)

"""
.求M,N中矩阵对应元素的和元素的乘积    (提示：使用2个for遍历)
 m =[[1,2,3],  
      [4,5,6],  
     [7,8,9]]  
 n =[[2,2,2],  
     [3,3,3],  
    [4,4,4]] 
"""

# list_test2=[i*j for i in [] for j in range (1,4)]
# list_test3=[i+j for i in range(1,4) for j in range (1,4)]
# print(list_test2)
# print(list_test3)

list2 = []
m = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

n = [[2, 2, 2],
     [3, 3, 3],
     [4, 4, 4]]
list01 = [m[i][j] * n[i][j] for i in range(0, 3) for j in range(0, 3)]

print(list01)
print(sum(list01))
for i in range(0,3):
    for j in range(0, 3):
        a = m[i][j] * n[i][j]
        list2.append(a)
print(list2)


