import random
def quiksort(left,right,array):
    if left>=right:
        return

    i=0
    j=right
    while (j-left)/(right-left)>0.75:
         i=left
         j=right
         p=random.randint(i,j)
         array[p],array[left]=array[left],array[p]
         temp=array[left]
         while i<j:
             while i<j and temp<=array[j]:
                 j-=1
             while i<j and temp>=array[i]:
                 i+=1
             if i<j:
                array[i],array[j]=array[j],array[i]
         array[i],array[left]=array[left],array[i]
    quiksort(left,i-1,array)
    quiksort(i+1,right,array)


def main():
    array=[random.randint(0,10000) for i in range(100000)]
    quiksort(0,999,array)
    print(array)
main()