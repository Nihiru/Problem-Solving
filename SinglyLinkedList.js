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
        let newNode = new Node(val);
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
        let current = this.head;
        let newTail = current;
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
        let current = this.head;
        this.head = current.next;
        current.next = null;
        this.length--;
        return `shifted element ${current.value}`;

    }

    unshift(val){
        let newNode = new Node(val);

        if(!this.head){
            this.head = this.tail = newNode;
        } else {
            newNode.next = this.head
        this.head = newNode
        }
        
        this.length++;
        return `unshifted element ${val}`
    }

    get(position){
        if(position >= this.length|| position <= 0){
            return null;
        }
        let current = 1;
        let temp = this.head
        while(current < position){
            temp = temp.next;
            current++;
        }
        return temp;
    }

    set(position, value){
    
        let foundNode = this.get(position);
        if(foundNode){
            foundNode.value = value;
            return true;
        }
        return false;
    }

    insert(position, value){
        let foundNode = this.get(position);
        let newNode = new Node(value);
        if(foundNode){
            newNode.next = foundNode.next;
            foundNode.next = newNode;
            return `Inserted succesfully`
        }
        if(position >= this.length){
            this.push(value);
        } else {
            this.unshift(value);
        }
        this.length++;
        return 
    }

    remove(position=1){
        if(position <= 0 || position >= this.length){
            return `Cannot remove item with given ${position}`
        }

        if(position === this.length - 1){
            return this.pop();
        }

        if(position === 0){
            return this.shift();
        }

        var removedNode = this.get(position);
        var nextNode = removedNode.next;
        removedNode.next = null;
        if(position === 1){
            this.head = nextNode;
        }
        this.length--;
        return `Removed node is ${removedNode.value}`
    }

    getListLength(){
        return this.length
    }

    traverse(){
        let temp  = this.head;
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

let list = new SinglyLinkedList();
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
console.log(list.unshift(25))
console.log(list.traverse());
console.log(list.push(15));console.log(list.push(25));console.log(list.push(35));console.log(list.push(45));
console.log(list.get(4));
console.log(list.set(4, 'Hello World'));
console.log(list.traverse());
console.log(list.insert(-1, 'Beginning'));
console.log(list.insert(3, '3rd Position'));
console.log(list.insert(list.getListLength()+1, 'The End'));
console.log(list.traverse());
console.log(list.remove())
console.log(list.traverse())