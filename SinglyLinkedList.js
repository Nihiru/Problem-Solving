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
        return this;
    }

    pop(){
        if(this.head){
            return "Empty list";
        }
        var temp = this.head;
        while(temp.next.next){
            temp = temp.next.next;
        }
        temp = temp.next;
        temp.next = null;
        return temp.value;
    }

    getListLength(){
        return this.length
    }

    traverse(){
        var temp  = this.head;
        while(temp !== null){
            process.stdout.write(`${temp.value}=====>`);
            temp = temp.next;
        }
    }

}

var list = new SinglyLinkedList();
list.push(10)
list.push(20)
list.push(30)
console.log(list.traverse())
list.pop()
console.log(list.traverse())