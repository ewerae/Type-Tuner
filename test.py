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
        self.interKeyDelay = {}
        self.tempIKDList = []

        #Key transitions - inter key delay
        self.currentKey = ""
        self.previousKey = None
        self.keyTransition = {}

        #Key - dwell time
        self.dwellTimeKey = {}


        # Track dwell time
        self.keyPressTimes = {}  # Store press time of each key
        self.dwellTime = {}
        self.tempListDwell = []  # Store dwell times

        # Start the typing test
        print('Type these words:')
        self.completedWords = []
        self.targetWords = self.words.Randomise_Words()
        self.words.Display_Words()

        self.index = 0

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
        elif hasattr(key, 'char') and key.char is not None and key not in self.keyPressTimes:
            self.currentKey = key.char
            self.Handle_Letter(key, currentTime)

        # Display the text being typed in real-time
        print(f"\r{self.displayedText}", end = '')

    def Released(self, key):
        # Record dwell time if key was previously pressed
        if key in self.keyPressTimes:
            self.tempListDwell.append(round(time.time() - self.keyPressTimes[key], 4))
            if key not in self.dwellTimeKey:
                self.dwellTimeKey[key] = []

            self.dwellTimeKey[key].append(round(time.time() - self.keyPressTimes[key], 4))
                                          
            del self.keyPressTimes[key]  # Remove key after releasing

        # Terminate on Esc or when all words are typed
        if self.Terminate(key):
            self.finishTime = time.time() - self.startTime
            print("\nTest Terminating...")
            return False
        

    def Get_Completed_Words(self) -> list:
        return self.completedWords

    def Get_Target_Words(self) -> list:
        return self.targetWords
    
    def Get_Dwell_Time(self) -> dict:
        return self.dwellTime
    
    def Get_InterKey_Delay(self) -> dict:
        return self.interKeyDelay
    
    def Handle_Space(self):
        self.completedWords.append(self.activeWord)

        
        #self.dwellTime[self.activeWord] = self.tempListDwell
        self.dwellTime[self.index] = self.tempListDwell

        #self.interKeyDelay[self.activeWord] = self.tempIKDList
        self.interKeyDelay[self.index] = self.tempIKDList

        #Reset list
        self.tempListDwell = []
        self.tempIKDList = []

        self.index += 1
        
        self.previousKey = self.currentKey
        self.displayedText += " "
        self.activeWord = ""

    def Handle_Backspace(self, currentTime):
        if self.displayedText:
            self.displayedText = self.displayedText[:-1]
            print('\b \b', end = "")
            self.previousKeyTime = currentTime

    def Handle_Letter(self, key, currentTime):

        # Dwell Time to check if key is being pressed
        self.keyPressTimes[key] = currentTime

        # Displaying text and recording what you write
        self.displayedText += key.char
        self.activeWord += key.char

        #Appending Inter Key Delay times
        if self.previousKeyTime is not None: # Same as if self.previousKey is not None
            self.tempIKDList.append(round(currentTime - self.previousKeyTime, 4)) # Appends to dictionary that has key of the index of the word and value as the list of times

            keySequence = self.previousKey + key.char
            if keySequence not in self.keyTransition:
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
        print("\nInter Key Delay:")
        print(self.interKeyDelay)
        print("\nDwell Time:")
        print(self.dwellTime)
        print("\nIKD for Key Transitions:")
        print(self.keyTransition)
        print("\nDwell Time Per Key:")
        print(self.dwellTimeKey)
        print("\n WPM:")
        print(round(wpm, 1))



