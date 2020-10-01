class Node{
    constructor(val){
        this.value = val;
        this.next = null;
    }
}

class SinglyLinkedList{
    constructor(){
        this.head = this.tail =  null;
        this.length =0;
    }

    push(val){
        var newNode = new Node(val);
        if(!this.head){
            this.head = this.tail = newNode;
        } else {
            this.tail.next = newNode;
            this.tail = newNode;
        }
        this.length++;
        return `Inserted element ${newNode.value}`;
    }

    pop(){
        if(!this.head){
            return "Empty list";
        }
        var current = this.head;
        var newTail = current;
        while(current.next){
            newTail = current;
            current = current.next;
        }
        this.tail = newTail;
        this.tail.next = null;
        
        this.length--;
        if(this.length === 0 ){
            this.head = this.tail = null;
        }       
        return `Popped element ${current.value}`;
    }
    shift(){
        if(!this.head){
            return "Empty list";
        }
        var current = this.head;
        this.head = current.next;
        current.next = null;
        this.length--;
        return `shifted element ${current.value}`;

    }
    getListLength(){
        return this.length
    }

    traverse(){
        var temp  = this.head;
        if(!this.head){
            return "Nothing to display";
        }
        while(temp){
            process.stdout.write(`${temp.value}=====>`);
            temp = temp.next;
        }
        console.log("\n")
    }

}

var list = new SinglyLinkedList();
list.push(10)
list.push(20)
list.push(30)
console.log(list.traverse());
console.log(list.pop());console.log(list.pop());console.log(list.pop());console.log(list.pop())
console.log(list.traverse());
console.log(list.push(15));console.log(list.push(25));console.log(list.push(35));console.log(list.push(45));
console.log(list.traverse());
console.log(list.shift());
console.log(list.traverse());
console.log(list.shift())
console.log(list.traverse());
console.log(list.shift())
console.log(list.traverse());
console.log(list.shift())
console.log(list.traverse());
console.log(list.shift())
console.log(list.traverse());