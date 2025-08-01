import numpy as np
def sum_non_neg_diag(X: np.ndarray) -> int:
    if np.all(np.diag(X)<0): return -1
    return(sum(np.diag(X).clip(0)))
def are_multisets_equal(x: np.ndarray, y: np.ndarray) -> bool:
    return np.array_equal(np.sort(x),np.sort(y))

def max_prod_mod_3(x: np.ndarray) -> int:
    if np.all(np.array(x)%3!=0): return -1
    print(type(x))
    a=np.array([x[i]*x[i+1] for i in range(len(x)-1)])
    return(max(a[a%3==0]))
    """
    Вернуть максимальное прозведение соседних элементов в массиве x, 
    таких что хотя бы один множитель в произведении делится на 3.
    Если таких произведений нет, то вернуть -1.
    """
    pass

def convert_image(image: np.ndarray, weights: np.ndarray) -> np.ndarray:
    return(np.dot(np.array(image),np.array(weights)))
def rle_scalar(x: np.ndarray, y: np.ndarray) -> int:
    if len(np.repeat(np.array(x)[:,0],np.array(x)[:,1]))!=len(np.repeat(np.array(y)[:,0],np.array(y)[:,1])): return -1
    return np.dot( np.repeat(np.array(x)[:,0],np.array(x)[:,1]), np.repeat(np.array(y)[:,0],np.array(y)[:,1]))

def cosine_distance(X: np.ndarray, Y: np.ndarray) -> np.ndarray:
    #return np.dot(X,np.transpose(Y))/np.outer(np.linalg.norm(X, axis=1),np.linalg.norm(Y,axis=1))
    pass
"""
    Вычислить матрицу косинусных расстояний между объектами X и Y.
    В случае равенства хотя бы одно из двух векторов 0, косинусное расстояние считать равным 1.
    """