""" Find Euler number with tolerance Tol=0.0001"""
import math
Total=0
Count =0
Euler=2.71828182
Tolerance=0.0001
while True:
        Total+=1/(math.factorial(Count))
        if(math.fabs(Total-Euler)<Tolerance):
            print("Euler Number: ", Total, "Number of Steps:", Count)
            break
        Count+=1


