class PuzzleInfo:
    def __init__(self):
        self.puzzleQuestions = {}
        self.puzzleAnswers = {}
        
        self.puzzleQuestions["1"] = "You meet two inhabitants: Zoey and Mel. Zoey tells you that Mel is a knave. Mel says, `Neither Zoey nor I are knaves.'" 
        self.puzzleQuestions["2"] = "You meet two inhabitants: Peggy and Zippy. Peggy tells you that 'of Zippy and I, exactly one is a knight'. Zippy tells you that only a knave would say that Peggy is a knave." 
        self.puzzleQuestions["3"] = "You meet two inhabitants: Sue and Zippy. Sue says that Zippy is a knave. Zippy says, `I and Sue are knights.'"  
        self.puzzleQuestions["4"] = "You meet two inhabitants: Sally and Zippy. Sally claims, `I and Zippy are not the same.' Zippy says, `Of I and Sally, exactly one is a knight.'"
        self.puzzleQuestions["5"] = "You meet two inhabitants: Homer and Bozo. Homer tells you, `At least one of the following is true: that I am a knight or that Bozo is a knight.' Bozo claims, `Homer could say that I am a knave.'"
        self.puzzleQuestions["6"] = "You meet two inhabitants: Marge and Zoey. Marge says, `Zoey and I are both knights or both knaves.' Zoey claims, `Marge and I are the same.'"
        self.puzzleQuestions["7"] = "You meet two inhabitants: Mel and Ted. Mel tells you, `Either Ted is a knight or I am a knight.' Ted tells you that Mel is a knave."
        self.puzzleQuestions["8"] = "You meet two inhabitants: Zed and Alice. Zed tells you, `I am a knight or Alice is a knave.' Alice tells you, `Of Zed and I, exactly one is a knight.'"
        self.puzzleQuestions["9"] = "You meet two inhabitants: Ted and Zeke. Ted claims, `Zeke could say that I am a knave.' Zeke claims that it's not the case that Ted is a knave."
        self.puzzleQuestions["10"] = "You meet two inhabitants: Ted and Zippy. Ted says, `Of I and Zippy, exactly one is a knight.' Zippy says that Ted is a knave."
        self.puzzleQuestions["11"] = "You meet two inhabitants: Zed and Bart. Zed says, `Bart is a knight or I am a knight.' Bart tells you, `Zed could claim that I am a knave.'"
        self.puzzleQuestions["12"] = "You meet two inhabitants: Bob and Betty. Bob claims that Betty is a knave. Betty tells you, `I am a knight or Bob is a knight.'"
        self.puzzleQuestions["13"] = "You meet two inhabitants: Bart and Ted. Bart claims, `I and Ted are both knights or both knaves.' Ted tells you, `Bart would tell you that I am a knave.'"
        self.puzzleQuestions["14"] = "You meet two inhabitants: Bart and Mel. Bart claims, `Both I am a knight and Mel is a knave.' Mel tells you, `I would tell you that Bart is a knight.'"
        self.puzzleQuestions["15"] = "You meet two inhabitants: Betty and Peggy. Betty tells you that Peggy is a knave. Peggy tells you, `Betty and I are both knights.'"
        self.puzzleQuestions["16"] = "You meet two inhabitants: Bob and Mel. Bob tells you, `At least one of the following is true: that I am a knight or that Mel is a knave.' Mel claims, `Only a knave would say that Bob is a knave.'"
        self.puzzleQuestions["17"] = "You meet two inhabitants: Zed and Alice. Zed tells you, `Alice could say that I am a knight.' Alice claims, `It's not the case that Zed is a knave.'"
        self.puzzleQuestions["18"] = "You meet two inhabitants: Alice and Ted. Alice tells you, `Either Ted is a knave or I am a knight.' Ted tells you, `Of I and Alice, exactly one is a knight.'"
        self.puzzleQuestions["19"] = "You meet two inhabitants: Zeke and Dave. Zeke tells you, `Of I and Dave, exactly one is a knight.' Dave claims, `Zeke could claim that I am a knight.'"
        self.puzzleQuestions["20"] = "You meet two inhabitants: Zed and Zoey. Zed says that it's false that Zoey is a knave. Zoey claims, `I and Zed are different.'"
        self.puzzleQuestions["21"] = "You meet two inhabitants: Sue and Marge. Sue says that Marge is a knave. Marge claims, `Sue and I are not the same.'"
        self.puzzleQuestions["22"] = "You meet two inhabitants: Bob and Ted. Bob says, `I am a knight or Ted is a knave.' Ted says that only a knave would say that Bob is a knave."
        self.puzzleQuestions["23"] = "You meet two inhabitants: Zed and Peggy. Zed says that Peggy is a knave. Peggy tells you, `Either Zed is a knight or I am a knight.'"
        self.puzzleQuestions["24"] = "You meet two inhabitants: Zed and Bob. Zed says, `Both I am a knight and Bob is a knave.' Bob says, `Zed could say that I am a knight.'"
        self.puzzleQuestions["25"] = "You meet two inhabitants: Rex and Marge. Rex tells you, `I and Marge are knights.' Marge says, `I would tell you that Rex is a knight.'"


        self.puzzleAnswers["1"] = "Zoey is a knight. Mel is a knave."
        self.puzzleAnswers["2"] = "Peggy is a knave. Zippy is a knave."
        self.puzzleAnswers["3"] = "Sue is a knight. Zippy is a knave."
        self.puzzleAnswers["4"] = "Sally is a knave. Zippy is a knave"
        self.puzzleAnswers["5"] = "Homer is a knave. Bozo is a knave"
        self.puzzleAnswers["6"] = "Marge is a knight. Zoey is a knight"
        self.puzzleAnswers["7"] = "Mel is a knight. Ted is a knave"
        self.puzzleAnswers["8"] = "Zed is a knave. Alice is a knight"
        self.puzzleAnswers["9"] = "Ted is a knave. Zeke is a knave"
        self.puzzleAnswers["10"] = "Ted is a knight. Zippy is a knave"
        self.puzzleAnswers["11"] = "Zed is a knave. Bart is a knave"
        self.puzzleAnswers["12"] = "Bob is a knave. Betty is a knight"
        self.puzzleAnswers["13"] = "Bart is a knave. Ted is a knight"
        self.puzzleAnswers["14"] = "Bart is a knave. Mel is a knave"
        self.puzzleAnswers["15"] = "Betty is a knight. Peggy is a knave"
        self.puzzleAnswers["16"] = "Bob is a knight. Mel is a knight"
        self.puzzleAnswers["17"] = "Zed is a knight. Alice is a knight"
        self.puzzleAnswers["18"] = "Alice is a knave. Ted is a knight"
        self.puzzleAnswers["19"] = "Zeke is a knight. Dave is a knave"
        self.puzzleAnswers["20"] = "Zed is a knave. Zoey is a knave"
        self.puzzleAnswers["21"] = "Sue is a knave. Marge is a knight"
        self.puzzleAnswers["22"] = "Bob is a knight. Ted is a knight"
        self.puzzleAnswers["23"] = "Zed is a knave. Peggy is a knight"
        self.puzzleAnswers["24"] = "Zed is a knight. Bob is a knave"
        self.puzzleAnswers["25"] = "Indeterminate"



#1
#Q:You meet two inhabitants: Zoey and Mel. Zoey tells you that Mel is a knave. Mel says, `Neither Zoey nor I are knaves.'
#A:zoey is knight, mel is a knave

#2Q:You meet two inhabitants: Peggy and Zippy. Peggy tells you that 'of Zippy and I, exactly one is a knight'. Zippy tells you that only a knave would say that Peggy is a knave.
#A: Peggy is 

#3You meet two inhabitants: Sue and Zippy. Sue says that Zippy is a knave. Zippy says, `I and Sue are knights.'

#4 You meet two inhabitants: Sally and Zippy. Sally claims, `I and Zippy are not the same.' Zippy says, `Of I and Sally, exactly one is a knight.'

#5 You meet two inhabitants: Homer and Bozo. Homer tells you, `At least one of the following is true: that I am a knight or that Bozo is a knight.' Bozo claims, `Homer could say that I am a knave.'

#6 You meet two inhabitants: Marge and Zoey. Marge says, `Zoey and I are both knights or both knaves.' Zoey claims, `Marge and I are the same.'

#7 You meet two inhabitants: Mel and Ted. Mel tells you, `Either Ted is a knight or I am a knight.' Ted tells you that Mel is a knave.

#8You meet two inhabitants: Zed and Alice. Zed tells you, `I am a knight or Alice is a knave.' Alice tells you, `Of Zed and I, exactly one is a knight.'

#9 You meet two inhabitants: Ted and Zeke. Ted claims, `Zeke could say that I am a knave.' Zeke claims that it's not the case that Ted is a knave.

#10 You meet two inhabitants: Ted and Zippy. Ted says, `Of I and Zippy, exactly one is a knight.' Zippy says that Ted is a knave.

#11 You meet two inhabitants: Zed and Bart. Zed says, `Bart is a knight or I am a knight.' Bart tells you, `Zed could claim that I am a knave.'

#12 You meet two inhabitants: Bob and Betty. Bob claims that Betty is a knave. Betty tells you, `I am a knight or Bob is a knight.'

#13 You meet two inhabitants: Bart and Ted. Bart claims, `I and Ted are both knights or both knaves.' Ted tells you, `Bart would tell you that I am a knave.'

#14 You meet two inhabitants: Bart and Mel. Bart claims, `Both I am a knight and Mel is a knave.' Mel tells you, `I would tell you that Bart is a knight.'

#15 You meet two inhabitants: Betty and Peggy. Betty tells you that Peggy is a knave. Peggy tells you, `Betty and I are both knights.'

#16 You meet two inhabitants: Bob and Mel. Bob tells you, `At least one of the following is true: that I am a knight or that Mel is a knave.' Mel claims, `Only a knave would say that Bob is a knave.'

#17 You meet two inhabitants: Zed and Alice. Zed tells you, `Alice could say that I am a knight.' Alice claims, `It's not the case that Zed is a knave.'

#18 You meet two inhabitants: Alice and Ted. Alice tells you, `Either Ted is a knave or I am a knight.' Ted tells you, `Of I and Alice, exactly one is a knight.'

#19 You meet two inhabitants: Zeke and Dave. Zeke tells you, `Of I and Dave, exactly one is a knight.' Dave claims, `Zeke could claim that I am a knight.'

#20 You meet two inhabitants: Zed and Zoey. Zed says that it's false that Zoey is a knave. Zoey claims, `I and Zed are different.'

#21 You meet two inhabitants: Sue and Marge. Sue says that Marge is a knave. Marge claims, `Sue and I are not the same.'

#22 You meet two inhabitants: Bob and Ted. Bob says, `I am a knight or Ted is a knave.' Ted says that only a knave would say that Bob is a knave.

#23 You meet two inhabitants: Zed and Peggy. Zed says that Peggy is a knave. Peggy tells you, `Either Zed is a knight or I am a knight.'

#24 You meet two inhabitants: Zed and Bob. Zed says, `Both I am a knight and Bob is a knave.' Bob says, `Zed could say that I am a knight.'

#25 You meet two inhabitants: Rex and Marge. Rex tells you, `I and Marge are knights.' Marge says, `I would tell you that Rex is a knight.' 
