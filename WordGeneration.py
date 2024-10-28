from random import randrange

class WordGeneration:
    targetList = [
        "apple", "river", "book", "sun", "train", "elephant", "cloud", "guitar", "stone", "flower",
        "keyboard", "forest", "mountain", "bicycle", "star", "computer", "car", "phone", "window", "tree",
        "desk", "ocean", "cup", "mirror", "camera", "pencil", "clock", "giraffe", "lamp", "candle", 
        "door", "island", "shoes", "house", "hat", "bridge", "shirt", "school", "leaf", "notebook", "dog",
        "fish", "painting", "television", "pillow", "piano", "glasses", "fire", "ice", "moon", "suitcase",
        "rain", "football", "tennis", "carpet", "forest", "road", "river", "chocolate", "bottle", "tiger",
        "cat", "laptop", "pen", "bowl", "water", "balloon", "baker", "mountain", "plane", "backpack", 
        "violin", "cactus", "pizza", "penguin", "duck", "ball", "sock", "sand", "bat", "whale", "fox", 
        "wolf", "kite", "camera", "orange", "train", "panda", "rabbit", "towel", "game", "ladder", 
        "globe", "button", "watch", "radio", "drum", "map", "couch", "boat", "fence", "airplane", 
        "bike", "skateboard", "beach"
    ]
    
    

    def __init__(self):
        self.testList = []
        
   
    def Randomise_Words(self, numWords = 2) -> list:
        self.testList = ["map", "clock"]
        return self.testList
        for i in range(numWords):
            x = randrange(100)
            self.testList.append(self.targetList[x])
        return self.testList
            
    def Display_Words(self):
        print(" ".join(self.testList))
        