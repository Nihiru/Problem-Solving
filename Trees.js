class Node {
  constructor(value) {
    this.value = value;
    this.left = null;
    this.right = null;
  }
}

class BST {
  constructor() {
    this.root = null;
  }

  insert(value) {
    var newNode = new Node(value);
    if (this.root === null) {
      this.root = newNode;
      return this;
    } else {
      var current = this.root;
      while (true) {
        if (value === current.value) return "Element exists";
        if (value < current.value) {
          if (current.left === null) {
            current.left = newNode;
            return;
          }
          current = current.left;
        } else if (value > current.value) {
          if (current.right === null) {
            current.right = newNode;
            return;
          }
          current = current.right;
        }
      }
    }
  }

  find(val) {
    if (this.root === null) {
      return null;
    } else {
      var current = this.root;
      while (true) {
        if (current !== null) {
          if (val === current.value) return "Element Found";
          else if (val < current.value) {
            current = current.left;
          } else {
            current = current.right;
          }
        } else {
          return "Element Not found";
        }
      }
    }
  }

  BFS() {
    var node = this.root,
      data = [],
      queue = [];
    queue.push(this.root);
    while (queue.length) {
      node = queue.shift();
      data.push(node.value);
      if (node.left) queue.push(node.left);
      if (node.right) queue.push(node.right);
    }
    return data;
  }

  DFS(choice) {
    var data = [];
    switch (choice) {
      case 1:
        function preOrder(node) {
          data.push(node.value);
          if (node.left) preOrder(node.left);
          if (node.right) preOrder(node.right);
        }
        preOrder(this.root);
        return data;

      case 2:
        function postOrder(node) {
          if (node.left) preOrder(node.left);
          if (node.right) preOrder(node.right);
          data.push(node.value);
        }
        postOrder(this.root);
        return data;

      case 3:
        function inOrder(node) {
          if (node.left) preOrder(node.left);
          data.push(node.value);
          if (node.right) preOrder(node.right);
        }
        inOrder(this.root);
        return data;
      default:
        return "Invalid choice";
    }
  }
}

var tree = new BST();
tree.insert(10);
tree.insert(5);
tree.insert(2);
tree.insert(24);
tree.insert(40);
tree.insert(23);
console.log(tree.find(1));
console.log(tree.find(10));
console.log(tree.find(40));
console.log(tree.BFS());
console.log(tree.DFS(1));
console.log(tree.DFS(2));
console.log(tree.DFS(3));
