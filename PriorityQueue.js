class Node{
    constructor(val, priority){
        this.value = val;
        this.priority = priority;
    }
}

class PriorityQueue {
    constructor() {
        this.values = [];
    }

    enqueue(val, priority) {
        var newNode = new Node(val, priority);
        this.values.push(newNode);
        this.bubbleUp();
    }

    /**
     * function to find the place the maximum element at the root 
     * 0th position would be the maximum element
     * parentIndex is being calculated from the end of the list 
     */
    bubbleUp() {
        let idx = this.values.length - 1;
        const lastElement = this.values[idx];
        while (idx > 0) {
            //finding the parent element
            let parentIdx = Math.floor((idx - 1) / 2)
            let parent = this.values[parentIdx];
            if (lastElement.priority <= parent.priority) break;
            this.values[parentIdx] = lastElement;
            this.values[idx] = parent;
            idx = parentIdx;

        }
    }

    removeFirst(){
        return this.values.shift();
    }

    removeLast(){
        return this.values.pop()
    }

    getLength(){
        return this.values.length;
    }

    dequeue(){
        let root = this.values[0]; // returns first element i.e, root element
        let last = this.removeLast();
        if(this.getLength()  > 0){
            // replace root with the last element 
            this.values[0] = last;
            // sink down operation
            this.sinkDown();
            this.print();
        }
        return root === undefined ? console.log('Empty List'): console.log(`${root.value} and its priority ${root.priority}`);
    }

    sinkDown(){
         let idx = 0;
         const length = this.values.length;
         const element = this.values[0];
         while(true){
             // get the left and right child of the element indexes
             let rightChildIdx = 2 * idx + 1;
             let leftChildIdx = 2 * idx + 2;

             let leftChild, rightChild;
             let swap = null;

             // get maximum element by comparing root with its child
             if(leftChildIdx < length){
                 leftChild = this.values[leftChildIdx];
                 if(leftChild.priority > element.priority){
                     swap = leftChildIdx; // getting the position to swap 
                 }
             }

            if(rightChildIdx < length){
                rightChild = this.values[rightChildIdx];
                if(
                    // 
                    (swap === null && rightChild.priority > element.priority) ||
                    // if rightChild is larger than leftChild if and leftChildIdx has been set as the largest
                    (swap !== null && rightChild.priority > leftChild.priority)
                ){
                    swap = rightChildIdx
                }
            }

            if(swap === null) break;
            this.values[idx] = this.values[swap];
            this.values[swap] = element;
            idx = swap;
         }

    }

    print(){
        console.log(this.values);
    }
}

let PQ = new PriorityQueue();
PQ.enqueue('TWO', 2);
PQ.enqueue('ONE', 1);
PQ.enqueue('THREE', 3);
PQ.enqueue('FOUR', 4);
console.log(PQ)
PQ.dequeue();
PQ.dequeue();
PQ.dequeue();
PQ.dequeue()

