

#------------------------------------------------------------------------------------------------------------------------------------------------
#https://www.youtube.com/watch?v=6XPIKAxwIcI
#Python Vs MicroPython | Comparison & Installation Locations
#------------------------------------------------------------------------------------------------------------------------------------------------

#micro python is extremely efficient, as opposed to normal python
#
#it includes an operating system
#
#rapsberry can run micropython
#
#takes less than 1MB storage and only 16KB RAM under load
#
#webpage - micropython and python
#https://micropython.org/download/


#------------------------------------------------------------------------------------------------------------------------------------------------







#------------------------------------------------------------------------------------------------------------------------------------------------
#https://www.youtube.com/watch?v=0K_eZGS5NsU
#------------------------------------------------------------------------------------------------------------------------------------------------

def main():
    
    print("\ndynamic typed - implicit. determined at runtime\n")
    
    print("\nmultiple assignments\n")
    a, b = 0, "text"
    print(a)
    print(b)
    
    print("\nno ++ increment!  (a++ is illegal)\n")
    a = 1
    a += 1
    print(a)
    
    #NULL is None in python
    
    #no need for parathesis in conditions (add :  at the end of the condition) if a condition is multiline then paranthesis is required
    
    print("\nidentation defines the scopes/blocks\n")
    a, b = True, False
    if a and b:
        c = a or b
        print(c)
    #"else if" is "elif"
    elif a or b:
        c = a or b
        print(c)
    
    print("\n&& is \"and\", || is \"or\"\n")
    a, b, c = True, False,  False
    if a and b or c:
        print("test")
    
    print("\nfor loop with normal iteration. iterator is incremented implicitly 0 to positive incrementing\n")
    for i in range(5):
        print(i)
    
    
    print("\npositive to positive incrementing\n")
    for i in range(2,6):
        print(i)
    
    print("\ndecrementing\n")
    for i in (5,1,-1):
        print(i)
    
    print("\ndecrementing different increment size\n")
    for i in (5,1,-2):
        print(i)
        
    
    print("\ndivision is by default decimal (floating point) - /\n")
    print (5/2)
    print("\ndivid with integers - //\n")
    print(5//2)
    
    
    print("\nin python, rounding integer division is DOWN! most laguages round towards 0!\n")
    print(-3//2)
    print("to work around it, decimal divid and then cast to integer")
    print(int(-3/2))
    
    
    print("\nmodules also different with negative numbers.\n")
    print(10%3)
    print(-10%3)
    print("\nin C we'll get 1 as expected. solution is to use \"fmod\" func in math import\n")
    import math
    print(math.fmod(-10,3))
    
    print("\nmin max for integer is given as infinity and -infinity\n")
    print(float("inf"))
    print(float("-inf"))
    
    print("\n*** in python the numbers NEVER OVERFLOW! ***")
    import math
    print(math.pow(2,200))
    print("** we can make if statments with these values! **")
    print(math.pow(2, 200) < float("inf"))
    
    print("\narrays are called \"lists\" in python\n")
    arr = [1,2,3]
    arr[0] = 1
    print(arr)
    
    print("\nthey are dynamic by default - it can be used like stacks. append is push\n")
    arr.append(4)
    print(arr)
    arr.pop();
    print(arr)
    print("can insert to array at specific point. insert is O(n) ")
    arr.insert(1,7)
    print(arr)
    
    print("\ninitialize to specific size and an initial value\n")
    arr = [1] * 7
    print(arr)
    
    print("\narray length given in\n")
    print(len(arr))
    
    print("\nnegative indexes are valid! -1 is the last value, -2 is the value before last\n")
    arr[-1] = 5
    print(arr)
    
    print("\nslicing an array (subarray). (top index is non inclusive)\n")
    print(arr[1:3])
    
    print("\nmultiple init at the same line\n")
    a,b,c = [10,20,30]
    print(a,b,c)
    
    print("\niterate over the array\n")
    for i in range(len(arr)):
        arr[i] = i*3
    print(arr)
    
    
    print("\niterate with index and value - enumerate keyword\n")
    for i,v in enumerate(arr):
        arr[i] = v*2
    print(arr)
        
    
    print("\niterate over multiple array at the same time - zip keyword\n")
    arr1 = [10,20,30]
    arr2 = [40,50,60]
    for v1,v2 in zip(arr1, arr2):
        print(v1,v2)
    
    print("\nreverse array\n")
    print(arr)
    arr.reverse()
    print(arr)
    
    print("\nsort array \n")
    arr = [1,44,2,-5,5]
    print(arr)
    print("\naccending order\n")
    arr.sort()
    print(arr)
    print("\ndecending order\n")
    arr.sort(reverse=True)
    print(arr)
    
    print("\nsort string array\n")
    arr = ["bob", "alice", "jane", "dave"]
    print(arr)
    arr.sort()
    print(arr)
    
    print("\ncustom sort string array with lambda function\n")
    arr.sort(key=lambda x: len(x)) #sort the array by the length of each item 
    print(arr)
    
    print("\nuse lambda to set each value in the array to its \n")
    arr = [i*5 for i in range(5)]
    print(arr)
    
    
    print("\ncreate a 4*4 matrix\n")
    arr = [[0] * 4 for i in range(4)]
    print(arr)
    
    print("\ncan slice strings the same as arrays\n")
    s = "abc"
    print(s)
    print(s[0:2])
    
    print("\nstrings are immutable unlike arrays\n")
    print("s[0] = \"A\"  - strings are immutable this wont work")
    
    print("\ncan only concatenate into a string\n")
    s += "def"
    print(s)
    
    print("\nstrings can be converted into integers\n")
    print(int("123") + int("123"))
    print(str(123) + str(123))

    print("\nascii value of a string with the \"ord\" func\n")
    print(ord("a"))
    
    print("\njoining strings together\n")
    strings = ["ab", "cd", "ef"]
    print(strings)
    print("".join(strings)) 
    
    
    print("\nqueues\n")
    from collections import deque
    queue = deque()
    queue.append(1)
    print(queue)
    queue.append(2)
    print(queue)
    
    print("\nwe can pop a value as if it was a stack\n")
    queue.popleft()
    print(queue)
    
    print("\nwe can also append a value to the left\n")
    queue.appendleft(1)
    print(queue)

    print("\nwe can as usual pop from the right side like a stack\n")
    queue.pop()
    print(queue)

    print("\n\n")
    print("\nhashsets\n")
    myset = set()
    myset.add(1) #insert
    myset.add(2) #insert
    print(myset) #print all
    print(len(myset)) #print the length of the set

    print(1 in myset)  #this searches the set for the value 1 -> exists
    print(2 in myset)  #this searches the set for the value 2 -> exists
    print(3 in myset)  #this searches the set for the value 3 -> does NOT exists
    
    myset.remove(2) # remove the value 2 
    print(2 in myset) # this searches the set for the value 2 -> does NOT exists
    
    print("\ninitializing a set \n")
    print("\nwith predefined values\n")
    print(set([1,2,3]))
    print("\ninit a set with an iterator values\n")
    myset = { i for i in range(5) }
    print(myset)
    
    print("\nhash maps  (dictionary)\n")
    myMap = {}
    myMap["alice"] = 88
    myMap["bob"] = 77
    print(myMap)
    print(len(myMap))
    
    print("\n\n")
    myMap["alice"] = 80  #//modifying a key value
    print(myMap["alice"]) #// get a value of specific key
    
    print("alice" in myMap) #//search for a value existance
    myMap.pop("alice")  #// remove a specific key
    print(myMap)
    
    myMap = { "alice" :2, "bob": 77 } #init with key-value pairs
    print(myMap)
    
    myMap = { i: 2*i for i in range(3) } #//initialize with lambda (comprehension)
    print(myMap)
    
    print("\nlooping over a map\n")
    myMap = { "alice" :88, "bob": 70 }
    #iterate over the pairs
    for key in myMap:
        print(key, myMap[key])  
    #iterate over the values only
    for val in myMap.values():
        print(val)
    #iterating over items
    for key, val in myMap.items():
        print(key, myMap[key])  
        
    
    print("\ntuples\n")
    tup = (1, 2, 3) #// init with paranthesis and NOT curly braces
    print(tup)
    print(tup[0])
    print(tup[-1])
    
    print("\ncannot modify values of a tuple\n")
    print("tup[0] = 5 # immutable")
    
    print("\nmyMap[[3, 4]] = 5 #this is illegal - lists cannot be keys for maps and sets so we use tuples\n")
    
    myMap = { (1,2): 3 }  # tuple used as a key in a hashmap
    print(myMap[(1,2)])
    
    print("\ntuples used as a key of a hashsets\n")
    mySet = set()
    mySet.add((1, 2))
    print((1,2) in mySet)
    
    
    print("\nheaps - under the hood they are arrays\n")
    print("\n** heaps are good to find min and max of an array **\n")
    
    import heapq
    minHeap = [] # create empty lists
    heapq.heappush(minHeap, 3) # static function of heapq to push a value 
    
    print("\nby default heaps are minimum heaps. minimum value will always be at idx 0\n")
    heapq.heappush(minHeap, 2)
    heapq.heappush(minHeap, 4)
    print(minHeap[0])
    
    print("\nloop through a heappush (with poping of the values)\n")
    print("\nit is a minimum heap so poping will be in ascending order\n")
    while len(minHeap):
        print(heapq.heappop(minHeap))
    
    print("\nthere's no max heap. to work around we push the negative values and negate again when poping\n")
    maxHeap = []
    heapq.heappush(maxHeap, -3)
    heapq.heappush(maxHeap, -4)
    heapq.heappush(maxHeap, -2)
    print(-1 * maxHeap[0])
    while len(maxHeap):
        print(-1 * heapq.heappop(maxHeap))
    
    print("\nto insert values at init time and save compute time, we create an array and then \"heapify\" it\n")
    arr = [2, 1, 8, 4, 5]
    heapq.heapify(arr)
    while arr:  # while arr not empty
        print(heapq.heappop(arr))
    
    print("\nfunctions\n")
    def func(param1, param2):
        return param1*param2

    print(func(2,3))
    
    print("\nnested functions -> definition of functions within functions. saves passing arguments\n")
    def outer(a, b):
        c = "c"
        def inner():
            return a + b + c
        return inner()
    print(outer("a", "b"))
    
    
    print("\nmodifying value passes params into inner functions will not change the value of its outer instance. arrays and objects will change but all primitives such as int params will be passed by values and so will not change.\n")
    print("\nto overcome (basically pass it by ref), add \"nonlocal\" keyword\n")

    def double(arr, val):
        def helper():
            # array will be modified
            for i, n in enumerate(arr):
                arr[i] *= 2
            # val will NOT be modified
            #val *= 2
            
            #use nonlocal - will change the original integer param given at "double" func
            nonlocal val
            val *= 2
        # call the inner without passing the params
        helper()
        print(arr, val) # val will be changed
    
    nums = [1,2,3]
    val = 4
    print(double(nums,val))
    
    
    print("\n\n")
    
    print("\nclasses - a bit limited comparaed to other languages              \n")
    print("\nconstructor - __init__                                            \n")
    print("\nmembers declared at ctor                                          \n")
    print("\neach method must be given the \"self\" object. basically \"this\" \n")
    print("\nat each point in the class, the self is accessable.               \n")
    class myClass:
        #ctor 
        def __init__(self, nums):
            self.nums = nums  # this automatically declares members of the class
            self.size = len(nums)
            
        def getLength(self):
            return self.size
            
        def getDoubleLength(self):
            return 2*self.getLength()
    
    
    c = myClass([1,2,3,66,-1])
    print(c.getLength())
    print(c.getDoubleLength())

if __name__ == "__main__":
    main()
















