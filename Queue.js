class Node{
    constructor(value){
        this.next = null;
        this.val = value;
    }
}

class Queue{
    constructor(){
        this.first = null;
        this.last = null;
        this.size = 0; 
    }

    enqueue(val){
        var newNode = new Node(val);
        if(!this.first){
            this.first = this.last = newNode;
        } else {
            this.last.next = newNode;
            this.last = newNode;
        }
        return ++this.size;
    }

    dequeue(){
        if(!this.first){
            return null;
        } 
        var temp = this.first;
        if(this.first === this.last){
            this.last = null;
        }
        this.first = this.first.next;
        this.size--;

        return `Deqeued element is ${temp.val}`

    }

    print(){
        if(!this.first){
            return 'Empty stack';
        }
        var temp = this.first
        while(temp){
            console.log(temp.val);
            temp = temp.next;
        }
        return 0;
    }
}

var queue = new Queue();

console.log(queue.print());
console.log(queue.enqueue(10));
console.log(queue.enqueue(20));
console.log(queue.enqueue(30));
console.log(queue.enqueue(40));
queue.print();
console.log(queue.dequeue());
queue.print();
console.log(queue.dequeue());
console.log(queue.dequeue());
console.log(queue.dequeue());
console.log(queue.dequeue());
console.log(queue.print());