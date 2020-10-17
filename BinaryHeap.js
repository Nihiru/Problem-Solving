class MaxBinaryHeap {
    constructor() {
        this.values = [41, 39, 33, 18, 27, 12];
    }

    insert(element) {
        this.values.push(element);
        this.bubbleUp();
    }

    bubbleUp() {
        let idx = this.values.length - 1;
        const element = this.values[idx];
        while (idx > 0) {
            //finding the parent element
            let parentIdx = Math.floor((idx - 1) / 2)
            let parent = this.values[parentIdx];
            if (element <= parent) break;
            this.values[parentIdx] = element;
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

    extractMax(){
        let root = this.removeFirst(); // returns first element i.e, root element
        let last = this.removeLast();
        if(this.getLength()  > 0){
            // replace root with the last element 
            this.values[0] = last;
            // sink down operation
            this.sinkDown();
            this.print();
        }
        return root === undefined ? console.log('Empty List'): root;
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
                 if(leftChild > element){
                     swap = leftChildIdx; // getting the position to swap 
                 }
             }

            if(rightChildIdx < length){
                rightChild = this.values[rightChildIdx];
                if(
                    // 
                    (swap === null && rightChild > element) ||
                    // if rightChild is larger than leftChild if and leftChildIdx has been set as the largest
                    (swap !== null && rightChild > leftChild)
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

let heap = new MaxBinaryHeap();
heap.insert(55);
heap.print();
heap.extractMax();
heap.extractMax();
heap.extractMax();
heap.extractMax();
heap.extractMax();
heap.extractMax();
heap.extractMax();
heap.extractMax();
heap.extractMax();


