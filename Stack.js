class Node{
    constructor(value){
        this.next = null;
        this.val = value;
    }
}

class Stack{
    constructor(){
        this.first = null;
        this.last = null;
        this.size = 0;
    }

    push(value){
        var newNode = new Node(value);
        if(!this.first){
            this.first = newNode;
            this.last = newNode;
        } else {
            var temp = this.first;
            this.first = newNode;
            this.first.next = temp;
        }
        return ++this.size;
    }

    pop(){
        if(!this.first){
            return null;
        }
        var temp = this.first;
        if(this.first === this.last){
            this.last = null;
        }
        this.first = this.first.next;
        this.size--;
        return  `popped element is ${temp.val}`;
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

var stack = new Stack();

stack.print();
stack.push(10);
stack.push(20);
stack.push(30);
stack.print();
console.log(stack.pop());
stack.print();
console.log(stack.pop());
console.log(stack.pop());
console.log(stack.pop());
console.log(stack.print());