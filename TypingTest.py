from WordGeneration import WordGeneration
from pynput import keyboard
import time
import os

class TypingTest:
    def __init__(self):
        # Initialise WordGen class
        self.words = WordGeneration()

        # Text being displayed and typed
        self.displayedText = ""
        self.activeWord = ""

        # Track inter-key delay
        self.previousKeyTime = None

        #Key transitions - inter key delay
        self.currentKey = ""
        self.keyTransition = {}

        # Start the typing test
        print('Type these words:')
        self.completedWords = []
        self.targetWords = self.words.Randomise_Words()
        self.words.Display_Words()


        self.startTime = None
        self.finishTime = None
        

    def Pressed(self, key):
        if len(self.completedWords) == 0:
            self.startTime = time.time()
        
        currentTime = time.time()
        

        # Handle special keys (space and backspace)
        if key == keyboard.Key.space:
            self.currentKey = " "
            self.Handle_Space()
        elif key == keyboard.Key.backspace:
            self.Handle_Backspace(currentTime)

        # Handle normal alphanumeric keys and avoid auto-repeat
        elif hasattr(key, 'char') and key.char is not None:
            self.currentKey = key.char
            self.Handle_Letter(key, currentTime)

        # Display the text being typed in real-time
        print(f"\r{self.displayedText}", end = '')

    def Released(self, key):
        # Terminate on Esc or when all words are typed
        if self.Terminate(key):
            self.finishTime = time.time() - self.startTime
            print("\nTest Terminating...")
            return False
        

    def Get_Completed_Words(self) -> list:
        return self.completedWords

    def Get_Target_Words(self) -> list:
        return self.targetWords
    
    def Get_InterKey_Delay(self) -> dict:
        return self.interKeyDelay
    
    def Handle_Space(self):
        self.completedWords.append(self.activeWord)
        
        self.previousKey = self.currentKey
        self.displayedText += " "
        self.activeWord = ""

    def Handle_Backspace(self, currentTime):
        if self.displayedText:
            self.displayedText = self.displayedText[:-1]
            print('\b \b', end = "")
            self.previousKeyTime = currentTime

    def Handle_Letter(self, key, currentTime):

        # Displaying text and recording what you write
        self.displayedText += key.char
        self.activeWord += key.char

        #Appending Inter Key Delay times
        if self.previousKeyTime is not None: # Same as if self.previousKey is not None
            keySequence = self.previousKey + key.char
            self.keyTransition[keySequence] = []
            
            self.keyTransition[keySequence].append(round(currentTime - self.previousKeyTime, 4))
            
    
            
        self.previousKey = self.currentKey
        self.previousKeyTime = currentTime

    
    def Terminate(self, key) -> bool:
        return key == keyboard.Key.esc or len(self.completedWords) == len(self.targetWords)
    

    def Test_Run(self):
        # Start the keyboard listener
        with keyboard.Listener(on_press = self.Pressed, on_release = self.Released) as listener:
            listener.join()

        wpm = len(self.completedWords)/self.finishTime * 60

        # Display results after the test
        print("\nWords typed:")
        print(self.completedWords)
        print("\nIKD for Key Transitions:")
        print(self.keyTransition)
        print("\n WPM:")
        print(round(wpm, 1))



