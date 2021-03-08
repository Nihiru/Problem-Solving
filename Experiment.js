/**
 * Recursion being used effectively
 */
let company = {
    sales: [
        {
            "name": "John",
            "salary": 10000
        },
        {
            "name": "Joy",
            "salary": 20000
        }
    ],
    development: {
        sites: [
            {
                "name": "Josh",
                "salary": 15000
            },
            {
                "name": "David",
                "salary": 20000
            }
        ],
        internals: [
            {
                "name": "Jason",
                "salary": 25000
            }
        ]
    }
}

function sumSalaries(department) {
    let sum = 0;
    if (Array.isArray(department))
        return department.reduce((prev, curr) => prev + curr.salary, 0)
    else {
        for (let subdep of Object.values(department)) {
            sum += sumSalaries(subdep)
        }
    }
    return sum
}
// console.log(sumSalaries(company))

/***
 * implementing groupBy function 
 */

var groupBy = function (xs, key) {
    return xs.reduce(function (rv, x) {
        /**
         * Here,
         * x[key] == x['length'] where x is string object, string has a length property and it can be accessed via "."  or "[]" operator i.e, x.length or x['length']
         * typeof(rv[x[key]] = rv[x[key]] || []) returns object ???
         * grouping operator () controls the precedence of evaluation in expression
         * 
         */
        let result = (rv[x[key]] = rv[x[key]] || [])
        result.push(x)
        return result;
    }, {})
}
console.log(groupBy(['one', 'two', 'three'], 'length'))
