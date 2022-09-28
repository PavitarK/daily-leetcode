"""
Algorithm Practice
Merge Sort
"""

def mergeSort(arr): 
    if len(arr) > 1: 
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        
        mergeSort(L)
        mergeSort(R)
        
        i = j = k = 0 
        
        while i < len(L) and j < len(R): 
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else: 
                arr[k] = R[j]
                j += 1
            
            k +=1
        
        if i < len(L):
            arr[k] = L[i]
            k += 1 
            i += 1
            
        if j < len(R): 
            arr[k] = R[j]
            k += 1 
            j += 1
        
    return None 


values = [4,65,23,2,1,4,63,77,100]
print(f"Unsorted Array = {values}")
mergeSort(values)
print(f"Sorted Array: {values}")