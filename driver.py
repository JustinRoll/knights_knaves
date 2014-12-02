from logicparser import *
from puzzleDict import *
from nltk import *
from nltk.sem.drt import *
from nltk.sem import * 
read_expr = nltk.sem.Expression.fromstring

def main():
    puzzleDict = PuzzleInfo().puzzleQuestions
    logicParser = LogicParser(puzzleDict["1"])

def test():
#Q:You meet two inhabitants: Zoey and Mel. Zoey tells you that Mel is a knave. Mel says, `Neither Zoey nor I are knaves.'
#Z: Unop: ~M, M:Binop  ~Z and ~M
#both knaves
        logic._counter._value = 0
        prover = Prover9()

        lp = LogicParser()  
        p1 = read_expr('-knight(mel) and -knight(zoey)') #zoey and mel are knaves
        c  = read_expr('knight(mel) and -(knight(zoey) and knight(mel))')
        prover = ResolutionProverCommand(c, [p1])
        print(prover.prove())

        logic._counter._value = 0
        prover = Prover9()

        lp = LogicParser()  
        p1 = read_expr('knight(mel) and knight(zoey)') #zoey and mel are knights
        c  = read_expr('-knight(mel) and (knight(zoey) and knight(mel))') #we are trying to prove that Zoey is a knight, Mel is a knave
        prover = ResolutionProverCommand(c, [p1])
        print(prover.prove())

        logic._counter._value = 0
        prover = Prover9()

        lp = LogicParser()  
        p1 = read_expr('-knight(mel) and knight(zoey)') #zoey knight, mel knave
        c  = read_expr('-knight(mel) and -(knight(zoey) and knight(mel))') #we are trying to prove that Zoey is a knight, Mel is a knave
        prover = ResolutionProverCommand(c, [p1])
        print(prover.prove()) 


        logic._counter._value = 0
        prover = Prover9()

        lp = LogicParser()  
        p1 = read_expr('knight(mel) and -knight(zoey)') #zoey knave, mel knight
        c  = read_expr('(knight(mel)) and (knight(zoey) and knight(mel))') #we are trying to prove that Zoey is a knight, Mel is a knave
        #prover = Prover9Command(c, [p1])
        prover = ResolutionProverCommand(c, [p1])
        print(prover.prove())
        print(prover.proof())
test()
