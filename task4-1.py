from typing import List
def sum_non_neg_diag(X: List[List[int]]) -> int:
    k=0
    s=0
    for i in range(min(len(X),len(X[1]))):
        if X[i][i]>=0:
            k+=X[i][i]
        if X[i][i]<0: s+=1
    if s==min(len(X),len(X[1])): return -1
    return k
    
def are_multisets_equal(x: List[int], y: List[int]) -> bool:
    if (set(x)!=set(y)): return False
    for i in set(x):
        if y.count(i)!=x.count(i): return False
    return True

def max_prod_mod_3(x: List[int]) -> int:
    a=[x[i]*x[i+1] for i in range(len(x)-1)]
    i=0
    while i<len(a):
        if a[i]%3!=0:
            del a[i]
            i-=1
        i+=1
    if len(a)==0: return -1
    return max(a)

def convert_image(image: List[List[List[float]]], weights: List[float]) -> List[List[float]]:
    res=[[0 for j in range(len(image[0]))] for i in range(len(image))]
    for i in range(len(image)):
        for j in range(len(image[0])):
            sum=0
            for k in range(len(image[0][0])):
                sum+=(image[i][j][k]*weights[k])
            res[i][j]=sum
    return res


def rle_scalar(x: List[List[int]], y:  List[List[int]]) -> int:
    a=[]
    b=[]
    for i in range(len(x)):
        for j in range(x[i][1]):
            a.append(x[i][0])
    for i in range(len(y)):
        for j in range(y[i][1]):
            b.append(y[i][0])
    if len(a)!=len(b): return -1
    return sum(map(lambda m,n: m*n,a,b))

def cosine_distance(X: List[List[float]], Y: List[List[float]]) -> List[List[float]]:
    cosin=[[sum(map(lambda a,b: a*b, X[i],Y[j])) for j in range(len(Y))]for i in range(len(X))]
    for i in range(len(X)):
        for j in range(len(Y)):
            if (sum(map(lambda a: a*a,X[i]))**0.5)*(sum(map(lambda a: a*a,Y[j]))**0.5)==0:
                cosin[i][j]=1.0
            else:
                cosin[i][j]=cosin[i][j]/(sum(map(lambda a: a*a,X[i]))**0.5)/(sum(map(lambda a: a*a,Y[j]))**0.5)
    return cosin