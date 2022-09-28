// task-1
function calculate(min, max, step){
    let sum = 0;
    for(let i = min; i <= max; i += step){
        sum += i;
    }
    console.log(sum);
}
    calculate(1, 3, 1); 
    calculate(4, 8, 2);
    calculate(-1, 2, 2);

// task-2
function avg(data){
    let sum = 0;
    let man = 0;
    for(let i = 0; i < data.employees.length; i++){
        if(data.employees[i].manager == false){
            sum += data.employees[i].salary;
            man += 1;
        }
    } 
    console.log(sum / man);
}

avg({
    "employees":[
    {
        "name":"John",
        "salary":30000,
        "manager":false 
    },
    {
        "name":"Bob",
        "salary":60000,
        "manager":true 
    },
    {
        "name":"Jenny",
        "salary":50000,
        "manager":false 
    },
    {
        "name":"Tony",
        "salary":40000,
        "manager":false }
    ]
    });

// task-3
function func(a){
    function innerFunc(b, c){
        console.log(a + b * c);
        return a + b * c;
    }
    return innerFunc;
}

func(2)(3, 4);
func(5)(1, -5); 
func(-3)(2, 9);

// task-4
function maxProduct(nums){
    let maxResult = Number.NEGATIVE_INFINITY;
    let result = 0;
    for(let i = 0; i < nums.length; i++){
        for(let j = i + 1; j < nums.length; j++){
            result = nums[i] * nums[j];
            if(result > maxResult){
                maxResult = result;
            }
        }
    }
    console.log(maxResult);
}
maxProduct([5, 20, 2, 6]);
maxProduct([10, -20, 0, 3]);
maxProduct([10, -20, 0, -3]);
maxProduct([-1, 2]);
maxProduct([-1, 0, 2]);
maxProduct([5, -1, -2, 0]);
maxProduct([-5, -2]);

// task-5
function twoSum(nums, target){
    for(let i = 0; i < nums.length; i++){
        for(let j = i + 1; j < nums.length; j++){
            if(nums[i] + nums[j] == target){
                return [i, j];
            }
        }
    }
    }
    let result=twoSum([2, 11, 7, 15], 9);
    console.log(result);

// task-6
function maxZeros(nums){
    let curMax = 0;
    let lenMax = 0;
    for(let i = 0; i < nums.length; i++){
        if(nums[i] == 0){
            curMax += 1;
            lenMax = Math.max(curMax, lenMax);
        } else {
            lenMax = Math.max(curMax, lenMax);
            curMax = 0;
        }
    }
    console.log(lenMax);
}
    maxZeros([0, 1, 0, 0]); 
    maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0]);
    maxZeros([1, 1, 1, 1, 1]);
    maxZeros([0, 0, 0, 1, 1]);
