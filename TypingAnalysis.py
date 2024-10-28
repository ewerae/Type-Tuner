from TypingTest import TypingTest

class TypingAnalysis:

    def __init__(self, typingTest: TypingTest) -> None:
        self.typingTest = typingTest
        self.completedWords = self.typingTest.Get_Completed_Words()  # Get typed words
        self.targetWords = self.typingTest.Get_Target_Words()

        
    def Get_Incorrect_Words(self) -> dict:
        """
        Returns the words typed incorrectly with their corresponding index as the key

        Returns:
            dict: Dictionary of incorrectly typed words
        """
        errorWords = {}

        # Loop to compare completed words and target words
        for i in range(len(self.completedWords)):
            if self.completedWords[i] != self.targetWords[i]:
                errorWords[i] = self.completedWords[i]  # Store the incorrect words

        return errorWords
    

    def Remove_Unwanted_Times(self, listTimes: dict, ikd = 0) -> list: 
        """
        When a word does not match the target word, we want the times only corresponding with the correct letters. Everything else is redundant.
        This will remove those times.

        Args:
            listTimes (dict): The dict that needs the times removed
            ikd (int, optional): If list is an interkeydelay list set to 1. Defaults to 0.

        Returns:
            list: returns the new list with the times you need to analyse
        """
        errorWords = self.Get_Incorrect_Words()
        print("\nIncorrect words:")
        print(errorWords)  # Print incorrect words
        targetWords = self.targetWords

        incorrectWordIndices = list(errorWords.keys())# Get the index of the incorrect word
        incorrectWords = list(errorWords.values()) # Get the error word at that index

        

        for incorrectIndex, incorrectWord in zip(incorrectWordIndices, incorrectWords):
            if self.Determine_Index_Start_Common_Prefix(targetWords[incorrectIndex], incorrectWord) == -1:
                listTimes[incorrectIndex] = []
                return listTimes
            
            if ikd == 1:
                ind = self.Determine_Index_Start_Common_Prefix(targetWords[incorrectIndex], incorrectWord) + 1 # Retrieve the place where we need to slice till
            else: 
                ind = self.Determine_Index_Start_Common_Prefix(targetWords[incorrectIndex], incorrectWord) + 1
            
            listTimes[incorrectIndex] = listTimes[incorrectIndex][:ind]

        print(f"\n {listTimes}")
        return listTimes
    




    def Determine_Index_Start_Common_Prefix(self, targetWord: str, errorWord: str) -> int:
        """
        Returns the index at which the correct parts of typed and target word is the same

        Args:
            targetWord (str): target word from word generation
            errorWord (str): error word from human typing

        Returns:
            int: index
        """
        
        iLen = len(targetWord) - 1
        jLen = len(errorWord) - 1
        ind = 0
        i = 0
        j = 0

        if not errorWord or targetWord[0] != errorWord[0]:
            return -1

        while i <= iLen and j <= jLen and targetWord[i] == errorWord[j]:
            ind = j
            i += 1
            j += 1

        return ind

        
    def Analysis_Run(self):
        pass
        #self.Remove_Unwanted_Times(self.typingTest.Get_Dwell_Time())
        #self.Remove_Unwanted_Times(self.typingTest.Get_InterKey_Delay(), 1)
        


"""
    def Determine_Index_Start_Common_Suffix(self, targetWord: str, errorWord: str) -> int:
        
        Determines the index the user started to retype the correct word

        Args:
            targetWord (str): target word from word generation
            errorWord (str): user typed error word

        Returns:
            int: index
        
        i = len(targetWord) - 1
        j = len(errorWord) - 1
        ind = 0

        while i >= 0 and j >= 0 and targetWord[i] == errorWord[j]:
            ind = j
            i -= 1
            j -= 1
        
        return ind

"""