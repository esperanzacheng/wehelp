# task-1
def calculate(min, max, step):
    sum = 0
    for i in range(min, max+1, step):
        sum += i
    print(sum)

calculate(1, 3, 1)
calculate(4, 8, 2) 
calculate(-1, 2, 2) 

# task-2
def avg(data):
    sum = 0
    man = 0
    for i in range(len(data["employees"])):
        if data["employees"][i]["manager"] == False:
            sum += data["employees"][i]["salary"]
            man += 1
    print(sum / man)

avg({
    "employees":[
        {
            "name":"John",
            "salary":30000,
            "manager":False
        },
        {
            "name":"Bob",
            "salary":60000,
            "manager":True
        }, 
        {
            "name":"Jenny",
            "salary":50000,
            "manager":False
        }, 
        {
            "name":"Tony",
            "salary":40000,
            "manager":False
        } 
    ]
})

# task-3
def func(a):
    def innerFunc(b, c):
        print(a + b * c)
        return a + b * c
    return innerFunc

func(2)(3, 4) 
func(5)(1, -5) 
func(-3)(2, 9) 

# task-4
def maxProduct(nums):
    maxResult = float('-inf')
    result = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            result = nums[i] * nums[j]
            maxResult = max(maxResult, result)
    print(maxResult)

maxProduct([5, 20, 2, 6])
maxProduct([10, -20, 0, 3])
maxProduct([10, -20, 0, -3]) 
maxProduct([-1, 2]) 
maxProduct([-1, 0, 2]) 
maxProduct([5,-1, -2, 0]) 
maxProduct([-5, -2])

# task-5
def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
result=twoSum([2, 11, 7, 15], 9)
print(result)

# task-6
def maxZeros(nums):
    curMax = 0
    lenMax = 0
    for i in range(len(nums)):
        if nums[i] == 0:
            curMax += 1
            lenMax = max(lenMax, curMax)
        else:
            lenMax = max(lenMax, curMax)
            curMax = 0
    print(lenMax)

maxZeros([0, 1, 0, 0])
maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0])
maxZeros([1, 1, 1, 1, 1])
maxZeros([0, 0, 0, 1, 1])

# if nums[i] == 0 , then maxCache += 1
# elif maxCache > maxLength, then maxLength = maxCache, maxCache = 0
# else maxCache = 0
