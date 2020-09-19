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