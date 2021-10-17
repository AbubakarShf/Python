#Question:
    # Python program to interchange first and last elements in a list

#Solution:

#SwapFunction
def swapFunc(list01):
#Get length of list
    size=len(list01)
#Algo to swap last and first element of list
    firstElement=list01[0]
    LastElement=list01[size-1]
    list01[0]=LastElement;
    list01[size-1]=firstElement
# return list after doing changing
    return list01

#MainFunction
list01=[1,2,3,4,5]
print(swapFunc(list01))
