import  numpy as  np  

# EX1 
# a, b = map(int,input().split())

# n=np.ones((a,b))
# n[1:a-1,1:b-1] = 0 
# print(n)

# n=np.zeros((a,b))
# n[1:a-1,1:b-1] = 1
# print(n) 

# EX2
# b= int(input("Nhap "))
# l=[]
# a=[]
# for i in range(1,b*b+1) :
#     if i % 2 == 0 :
#         l.append(1)
#         if i<b+1 :
#             a.append(1)
#     else :
#         l.append(0)
#         if i<b+1 :
#             a.append(0)
# n=np.array(l).reshape(b,b)
# a=a[::-1]
# n[b-1,:] = a 
# print(n)

# n=np.ones((8,8))
# for clum in range (n.shape[1]) :
#     if clum % 2 == 0 :
#         n[0:7,clum] = 0 
#     else :
#         n[7,clum] = 0
# print(n)

# EX3
l=[
    [53,12,88],
    [3,32,18],
    [77,42,1998]
]
# n=np.array(l)
# max=0
# indx = [] 
# for i in range (n.shape[0]) :
#     for j in range(n.shape[1]) :
#         if max< n[i,j] :
#             max=n[i,j]
#             indx=[i,j]         
# print(max,indx)

# min=None
# indn = [] 
# for i in range (n.shape[0]) :
#     for j in range(n.shape[1]) :
#         if min == None or  min > n[i,j] :
#             min=n[i,j]
#             indn=[i,j]         
# print(min,indn)

# EX4
n=np.array(l,dtype=float)
a=list(n[:,2])
n[:,2] = n[:,0] 
n[:,0] = a 
print(n) 
# EX5