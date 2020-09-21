function insertionSort(arr){
    for(let i=1; i<arr.length;i++){
        var currentVal = arr[i]
        for(var j=i-1;j>=0 && arr[j]> currentVal;j--){
            arr[j+1] = arr[j]
        }
        arr[j+1] = currentVal
    }
    return arr
}

console.log(insertionSort([10,9,8,7,6,5,4,3,2,1]))

function bubbleSort(arr){
    for(var i=arr.length; i>0 ;i--){
        var noSwaps = true
        for(var j=0;j<i-1;j++){
            if(arr[j]> arr[j+1]){
                var temp = arr[j+1]
                arr[j+1] = arr[j]
                arr[j] = temp
                noSwaps = false
            }
        }
        if(noSwaps)  break;
    }
    console.log(arr)
}

bubbleSort([10,9,8,7,6,5,4,3,2,1]);
bubbleSort([8,1,2,3,4,6,5,7])

function countSwaps(arr){
    let numOfSwaps = 0;
    for(var i=arr.length;i>=0;i--){
        for(var j=0; j<i-1;j++){
            if(arr[j] > arr[j+1]){
                //perform swap
                numOfSwaps++;
                var temp = arr[j];
                arr[j] = arr[j+1]
                arr[j+1] = temp
             }
        }
    }

   console.log(`Array is sorted in ${numOfSwaps} swaps.`)
   console.log(`First element: ${arr[0]}`)
   console.log(`Last element: ${arr[arr.length - 1]}`)
}

countSwaps([8,1,2,3,4,5,6,7])


function markAndToys(arr, target){
    let countOfToys = 0;
    let toysCost = 0;
    let afterSorting = insertionSort(arr);
    for(var i=0;i<afterSorting.length;i++){
       toysCost += afterSorting[i] 
       if(toysCost > target) break;
       else countOfToys++;

    }

    return countOfToys;
}

console.log(markAndToys([1,12,5,111,200,1000,10], 50))

/**
 * Merge sort
 * Time complexity  - O(n * log n) where `n` stands for comparisons made and `log n` bounds the dividing array to the last 1 element
 * Space complexity - O(n)
 * */ 


/**
 * Function to merge two sorted arrays of varying length
 * @param {Array} arr1 - left hand side of the divided array
 * @param {Array} arr2 - right hand side of the divided array
 */
function merge(arr1, arr2){
    let results = []
    var i =j =0;
    while(i <arr1.length && j<arr2.length){
        if(arr1[i] < arr2[j]){
            results.push(arr1[i]);
            i++;
        }  else {
            results.push(arr2[j]);
            j++;
        }
    }

    if(i<arr1.length){
        while(i<arr1.length){
            results.push(arr1[i]);
            i++;
        }
    }
    else{
        while(j<arr2.length){
            results.push(arr2[j]);
            j++;
        }
    }

    return results
}

console.log(merge([7,34,72,86,3423,9552,],[3,5,577,5446,58754,60000,61200]));
console.log(merge([],[1,2,4]))

/**
 * @param {Array} arr - A series of unsorted numerical elements 
 * @description - Perform merge sort on an unordered set of data, recursive function to handle the dividing of an array 
 */
function mergeSort(arr){
    if(arr.length <= 1) return arr;
    let mid = Math.floor(arr.length/2);
    let left = mergeSort(arr.slice(0,mid));
    let right = mergeSort(arr.slice(mid));

    return merge(left, right);
}

console.log(mergeSort([10,9,8,7,6,5,4,3,22,1]))