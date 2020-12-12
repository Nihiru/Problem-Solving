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
    if (Array.isArray(department))
        return department.reduce((prev, curr) => prev + curr.salary, 0)
    else {
        let sum = 0;
        for (let subdep of Object.values(department)) {
            sum += sumSalaries(subdep)
        }
    }
    return sum
}
console.log(sumSalaries(company))