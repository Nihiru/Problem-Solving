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
        return this;

    }

    pop(){
        if(!this.head){
            return null;
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
        return current;

    }

    shift(){
        if (!this.head){
            return null;
        }
        var current = this.head;
        if(this.length === 1){
            this.head = this.tail = null;
        } else {
            this.head = current.next;
            this.head.prev = null;
            current.next = null;
        }
        this.length--;
        return current;
    }
    
    unshift(value){
        var newNode = new Node(value);
        if(!this.head){
            this.head = this.tail = newNode;
        } else {
            this.head.prev = newNode;
            newNode.next = this.head;
            this.head = newNode
        }
        this.length++;
        return this;
    }

    get(index=1){
        if(index <= 0 || index > this.length){
            return null;
        }

        if(!this.head){
            return null;
        }

        var mid = Math.floor((this.length - 1)/2);
        var counter = 1;
        var current = null;
        
        if (mid === index){
            current = this.head    
            while(counter < index){
                current = current.next;
                counter++;
            }
            return current;       
        }else if(index < mid){
            current = this.head;
            while(counter < index){
                current = current.next;
                counter++;
            }
        } else {
            current = this.tail;
            counter = this.length;
            while(counter > index){
                current = current.prev;
                counter--;
            }
        }

        return current;
    }
    
    set(index, value){
        var foundNode = this.get(index);
        if(foundNode){
            foundNode.val = value;
            console.log(this.print());
            return true;
        }
        this.print();
        return false;
    }

    insert(index, value){
        if(index < 0 || index> this.length)
            return false;
        if(index === 1) return this.unshift(value);
        if(index === this.length) return this.push(value);
        var newNode = new Node(value);
        var afterNode = this.get(index);
        var beforeNode = afterNode.prev
        if(afterNode){ 
             newNode.next = afterNode;
             newNode.prev = afterNode.prev;
             beforeNode.next = newNode;
             afterNode.prev = newNode;
        }
        this.length++;
        return this.print();
    }

    remove(index=1){
        if(index <= 0 || index > this.length){
            return 'Invalid index';
        }

        if(index === 1) return this.shift();

        if(index === this.length -1) return this.pop();
        var removeNode = this.get(index);
        removeNode.prev.next = removeNode.next;
        removeNode.next.prev = removeNode.prev;
        removeNode.next = null;
        removeNode.prev = null; 

        this.length--;
        return removeNode;
    }

    getListLength(){
        return this.length;
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
console.log(dll.print());
dll.push('Hii');
dll.push('Supp');
console.log(dll.print());
dll.pop()
console.log(dll.print());
dll.pop()
console.log(dll.print());
dll.push(99);
dll.push(100);
console.log(dll.print());
dll.shift();
console.log(dll.print());
dll.shift();
console.log(dll.print());
dll.unshift(101);
dll.unshift(201);
dll.unshift(301);
dll.unshift(401);
dll.unshift(501);
dll.unshift(601);
console.log(dll.print());
console.log(dll.get(3).val)
console.log(dll.get(6).val);
console.log(dll.get(0));
console.log(dll.get(4).val);
console.log(dll.get(1).val);
console.log(dll.get(50));
dll.set(1, 701);
dll.insert(3,'Insert Node');
dll.insert(1,'Beginning Node');
console.log(dll.print());
dll.remove(1);
dll.remove(dll.getListLength() - 1);
console.log(dll.print())
dll.remove(dll.getListLength() - 1)
console.log(dll.print())
dll.remove((dll.getListLength() -1)/2);
console.log(dll.print())
dll.remove()
dll.remove();
dll.remove();
console.log(dll.print())
dll.remove();
dll.remove();
console.log(dll.print())