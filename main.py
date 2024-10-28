from TypingTest import TypingTest
from TypingAnalysis import TypingAnalysis


def main():
    test = TypingTest()
    test.Test_Run() 
    test2 = TypingAnalysis(test)
    test2.Analysis_Run()
    
    
main()

'''
Currently

    
Dwell time 
- Records the dwell time for each key except the space key.
- Records dwell time for specific keys

Inter Key Delay
- Records inter key delay for every sequence except letter to space transitions
- Records the key transitions and respective time in a dictionary. (doesnt do the above yet)

Error Rate/Accuracy/Consistency
- Records incorrectly typed words

WPM



    
    
    
To do:
- Accuracy 
- Consistency
- Error rate
- Finger Specific Keys
- Rows and Column keys

Assumptions:
    1. QWERTY keyboard.
    2. Fingers follow the standard approach to typing - i.e. each key has associated finger is pressed by it.
    3. Fingers do not stray past their allocated starting position, only when a letter is typed and will return to neutral state after letter
    4. Positions of fingers are totally neglected.

Consider:

    Currently it is not feasible to operate on the knowledge of how each person types without some device at the least. So whilst this may not entirely cater accurately to a person's typing ability,  
    it does at the very least promote good typing habits, i.e. making sure to utilise the correct finger for each key.
    I consider these trade offs for now.

    What data can we record:
    The idea is to identify areas where the typist has discomfort.
    At this stage, this would be primarily be present within specific letter sequences.
    To do that we have to see what makes a typist stutter or produce an error.

    Consistently throughout the test we want to analyse the time between letter sequences to see where stutter occurs.
    In the event where there an error emerges, we can analyse that word and find where the error started and see if it is common or uncommon occurrence.

    These two help us identify areas of weakness. Within these we can then analyse why these letter sequences are uncomfortable for the user.
    - finger specific keys
    - row or column movement specific keys
    
    


'''
