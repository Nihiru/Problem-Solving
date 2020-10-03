class Node{
    constructor(val){
        this.next = null;
        this.prev = null;
        this.val = val;
    }
}

class DoublyLinkedList{
    constructor(){
        this.head = null;
        this.tail = null;
        this.length = 0;
    } 

    push(value){
        var newNode = new Node(value);
        if(!this.head){
            this.head = this.tail = newNode;
        } else {
            this.tail.next = newNode;
            newNode.prev = this.tail;
            this.tail = newNode;
        }
        this.length++;
        console.log(this.print());
        return this;

    }

    pop(){
        if(!this.head){
            return this.print();
        }
        var current = this.tail;

        if(this.length === 1){
            this.tail = this.head = null;
        } else {
            // update the tail to be previous node
            this.tail = current.prev;
            this.tail.next = null;
            current.prev = null;
        }
        this.length--;
        console.log(this.print());
        return this;

    }
    
    print(){
        var arr = [];
        if(this.length === 0){
            return "Empty list";
        }
        var temp  = this.head;
        while(temp){
            arr.push(temp.val)
            temp = temp.next
        }
        return arr
    }
}

var dll = new DoublyLinkedList();
console.log(dll.print())
console.log(dll.push('Hii'))
console.log(dll.push('Supp'))
console.log(dll.pop())
console.log(dll.pop())
console.log(dll.pop())
