/* 
    This is the typical problem where the program terminates at n =1
    The input is the integer, n
    The output is the sequence of the number intil n = 1
    The while loop is used with the termination conditions to include the non-negative and not 
    zero input
    -> You can upset that if you want
    We would have the n as the primal codinated to live
*/

// function 3n + 1
function sequence_3n_1(n){
    // this variable is to keep account of the number of times the loop has runned
    let count = 0;
    console.log("\nTrial start with the sequence 3n + 1 program");
    // start the loop 
    while(n > 0){ // While n not equals to one and not less than 0, then we are in the loop
        console.log(n); // print the n
        count++;

        // including the version where if n = 1, terminate due to output
        if (n === 1) break;

        // Find out is the n is even or odd
        if(n % 2 == 0){ // even
            n /= 2; // divide by two    
        } else {
            // n is odd
            n = 3*n + 1
        }
    }

    console.log("It took %d iteration for the 3n + 1 challange", count);
}

// trial case with 22
sequence_3n_1(22);