/**
 * 
 * @param {Array} arr 
 */
function jumpingOnClouds(arr){
    let numberOfJumps = 0;
    if(arr[0] === 1){
        return "You lost the game due to being present on thunderheads";
    }
    for(let i=0;i<arr.length - 1;){
        if(arr[i] === 0){
            if(arr[i + 1] === 1){
                i+=2; numberOfJumps++;
            } else if(arr[i+2] === 0) {
                i+=2; numberOfJumps++;
            } else {
                i+=1; numberOfJumps++;
            }            
        }        
    }

    return numberOfJumps;
}

console.log(jumpingOnClouds([0,1,0,0,0,1,0,0,1,0,0]))
console.log(jumpingOnClouds([0,0,1,0,0,1,0]))
console.log(jumpingOnClouds([0,0,0,0,1,0]))