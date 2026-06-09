""" 
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
    1 10
    100 200
    201 210 
    900 1000
    SampleOutput
    1 10 20
    100 200 125
    201 210 89
    900 1000 174
"""

# import the file of the 3n+ 1
from solution import sequence_3n_1 as seqIterations

# the function to carry out the excercise in 
def maxIterationsSeq(i, j):
    print("Finding the highest iterations:")
    if i < 0 or j < 0 or j > 1e6 or i > 1e6:
        print("Out of range")
        return # terminate the function
    
    # if the conditions are satisfied
    highestIter = 0; iteration = 0 # initialize the variables 
    
    for i  in range(i, j):
        iteration = seqIterations(i) # find the number of iterations
        if iteration > highestIter: 
            highestIter = iteration # change that 
    
    # dispay the result
    print(str(i) + " " + str(j) + " " + str(highestIter) + "\n")

# trial cases
maxIterationsSeq(1, 10)
maxIterationsSeq(100, 200)
maxIterationsSeq(201, 210)
maxIterationsSeq(900, 1000)