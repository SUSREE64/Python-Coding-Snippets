def sortarray(array):
    needsort = True
    while(needsort):
        needsort = False
        for m in range (1, len(array)):
            if (array[m-1] > array[m]):
                # set needsort = 1 still needs sorting.
                needsort = True
                #swamp them within in place
                array[m], array[m-1] = array[m-1], array[m]
    return(array) 
    
array = [3,5,6, 80, 1, 5, 2, 300, 7, 34, 5, 8, 100]   
print(sortarray(array))
  
  
