/**
 * @param {String} passphrase  - A passpharse out of which a sub-string needs to be found
 * @param {String} pattern  - The sub-string that needs to be matched with passphrase
 */
function naiveSearch(passphrase, pattern){
    let count = 0;
    for(let i=0;i<passphrase.length;i++){
        for(let j=0;j<pattern.length;j++){
            if(pattern[j] !== passphrase[i+j]) break;
            if(j === pattern.length -1) count++;
        }
    }

    return count;
}
console.log(naiveSearch("The world is going to change a lot", "o"))
