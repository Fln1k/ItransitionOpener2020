  
def printTaxicab2(N): 
    i, count = 1, 0
    while (count < N):  
      
        int_count = 0
  
        for j in range(1, int(pow(i, 1.0 / 3)) + 1):  
              
            for k in range(j + 1, int(pow(i, 1.0 / 3)) + 1):  
                if (j * j * j + k * k * k == i): 
                    int_count += 1
          
        if (int_count == 2):  
          
            count += 1
            print(count, " ", i)  
  
        i += 1
      
N = 2
printTaxicab2(N) 