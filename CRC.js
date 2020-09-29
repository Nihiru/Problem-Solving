/**
 * CRC 
 * -) calculate CRC for `data`
 * 
 * 
 */

 const readlineInterface = require('readline').createInterface({
     input: process.stdin,
     output: process.stdout
 });

 const polynomialGenerator = () => {}

 const checkZerosOnes = (data) => data === 1 || 0? true: false;

 const 

 function CRC(){
    /**
     * polynomial expression of 16-bit
     * static polynomial expression - x^16 + x^12 + x^5 + x^0
     */
    let polynomialExpression = [1,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,1]
    readlineInterface.question('Throw me an data in bits: ', function(datum){

        // converting string into Array
        if(datum.trim().split(' ').every(checkZerosOnes)){
            if(convData.length > 16){
                console.log('Oops!!... This is a 16-bit CRC');
                // readlineInterface.close();
            } else {
                
            }

        } else {
            console.log("Input consists of invalid data")
        }
        

        readlineInterface.close();
    })
 }

 CRC();