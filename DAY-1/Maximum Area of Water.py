def maxArea(A, Len) : 
     area = 0 
     for i in range(Len) : 
         for j in range(i + 1, Len) : 
             area = max(area, min(A[j], A[i]) * (j - i)) 
     return area 
 a = [ 1, 5, 4, 3 ] 
 len1 = len(a) 
 print(maxArea(a, len1))
