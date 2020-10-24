 /**
  * 
  * @param {String} key key from which hash is generated
  * @param {Number} len represents length of the hash, gives a index upon which data needs to be stored
  */
 function hash(key, len, choice) {

     let total = 0;
     switch (choice) {
         case 1:
             console.log('For small amount of keys');
             for (let char of key) {
                 let value = char.charCodeAt(0) - 96
                 total = (total + value) % len
             }
             break;
         case 2:
             console.log('For a million keys');
             let WEIRD_PRIME = 31;
             for (let i = 0; i < Math.min(key.length, 100); i++) {
                 let char = key[i]
                 let value = char.charCodeAt(0) - 96
                 total = (total * WEIRD_PRIME + value) % len
             }
             break;

         default:
             break;
     }

     return total
 }


 console.log(hash('hello', 11, 1))
 console.log(hash('hello', 11, 2))