# Problem: Given an array A of n elements and a permutation P, apply P to A. For example, the permutation
#          <2,0,1,3> applied to A = <a,b,c,d> yields the array <b,c,a,d>

# EPI Judge: apply_permutation.py
def apply_permutation(perm, A):
    
    for i in range(len(A)):
        while perm[i] != i:
            A[perm[i]], A[i] = A[i], A[perm[i]]
            perm[perm[i]], perm[i] = perm[i], perm[perm[i]]
    return A