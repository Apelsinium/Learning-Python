#ТЗ: Функция, возвращающая строку, являющуюся результатом решения fizzbuzz, где каждый элемент последовательности разделен строкой вида "|число, являющееся суммой левого и правого элемента|"
def FizzBuzzPlus(lgth):
#First, we need an array to begin with
    Arr=[i for i in range(lgth)]
#Then, a standard FizzBuzz plays its role

#WARNING! CRINGE DAMAGE HAZARD! Женя, ты просил не делать как было в том примере, т.е. с проверкой делимости вида i%3==0. УЗРИ ЖЕ ЕБАБОЛУ, КОТОРАЯ ДЕЛАЕТ ТО ЖЕ САМОЕ!
#Естественно я ее закомментил, ибо она даже меня кринжует

#    def dividable(n):
#        count=[int(i) for i in str(n)]
#        while len(str(sum(count)))>1:
#            count=[int(i) for i in str(sum(count))]
#        return sum(count)==3 or sum(count)==6 or sum(count)==9 or sum(count)==0
#
#    for i in Arr:
#        if dividable(i) and (str(i)[-1]=="0" or str(i)[-1]=="5"):
#            Arr[i]="FizzBuzz"
#        elif str(i)[-1]=="0" or str(i)[-1]=="5":
#            Arr[i]="Buzz"
#        elif dividable(i):
#            Arr[i]="Fizz"
    for i in Arr:
        if i%3==0 and i%5==0:
            Arr[i]="FizzBuzz"
        elif i%5==0:
            Arr[i]="Buzz"
        elif i%3==0:
            Arr[i]="Fizz"
    #Now we go with sums
    for i in range(1,len(Arr)*2-1,2):
        if (isinstance(Arr[i-1],int)) and (isinstance(Arr[i],int)):
            Arr.insert(i,"|"+str(Arr[i-1]+Arr[i])+"|")
        else:
            Arr.insert(i,"|"+str(Arr[i-1])+str(Arr[i])+"|")
    print(" ".join([str(Thingy) for Thingy in Arr]))
FizzBuzzPlus(100)