/* 

    It isconjectured(butnotyetproven)thatthisalgorithmwill terminateatn=1for
    everyintegern.Still,theconjectureholdsforall integersuptoatleast1,000,000.
    Foraninputn, thecycle-lengthofnisthenumberofnumbersgenerateduptoand
    including the1. Inthe exampleabove, the cycle lengthof 22 is 16.Givenanytwo
    numbers i andj, youare todetermine themaximumcycle lengthoverall numbers
    betweeniandj, includingbothendpoints.
    Input
    The inputwill consistofaseriesofpairsof integers iandj,onepairof integersper
    line.All integerswillbelessthan1,000,000andgreaterthan0.
    Output
    Foreachpairof input integers iandj, output i, j inthesameorder inwhichthey
    appeared inthe inputandthenthemaximumcycle lengthfor integersbetweenand
    includingiandj.Thesethreenumbersshouldbeseparatedbyonespace,withallthree
    numbersononelineandwithonelineofoutputforeachlineof input.
    SampleInput
    110
    100200
    201210
    9001000
    SampleOutput
    11020
    100200125
    20121089
    9001000174
*/

// import the function from the solutionjs
const {sequence_3n_1} = require("./solution1");

// a function to take in the min and the max
function threenPlusOneProblem(min, max){
    // the min must be less than max
    if(min > max){
        // attempting to resolve
        let store1 = min, store2 = max;
        max = store1, min = store2; // swapping though I could just terminaate the program
    }
    // check the range of the min and the max
    if(min < 0 || max < 0 || max > 1000000 || min > 1000000){
        // print the range is out 
        console.log("Out of range");
        return; // terminate the function
    }

    // the else part of it
    // the iteration count and variables
    let maxIteration = 0, iterations = 0;

    // used the for loop to loop aroind the range
    for( i = min; i <= max; i ++){
        iterations = sequence_3n_1(i); // return the number of iterations

        // then confirm if it is the largest
        if (iterations > maxIteration) maxIteration = iterations;
    }

    // print the output
    console.log("For this range we had the following results:")
    console.log("%d %d %d", min, max, maxIteration);
}

// trial cases
threenPlusOneProblem(1, 10);
threenPlusOneProblem(100, 200);
threenPlusOneProblem(201, 210);
threenPlusOneProblem(900, 1000);