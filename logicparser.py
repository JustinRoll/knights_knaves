#"You meet two inhabitants: Zoey and Mel. Zoey tells you that Mel is a knave. Mel says, `Neither Zoey nor I are knaves.'" 
import re
import random, operator, nltk
import functools
from nltk.corpus import udhr
from nltk import bigrams, trigrams, ngrams
from nltk.tokenize import word_tokenize, sent_tokenize 
from nltk.corpus import stopwords, wordnet
from nltk.stem.snowball import SnowballStemmer
from nltk.tag import pos_tag
from enum import Enum
from nltk import *
from nltk.sem.drt import *
from nltk.sem import logic




class Op(Enum):
    NEGATION = 1
    AND = 2
    OR = 3
    XOR = 4

class Entity:
    def __init__(self):
        self.TRUTH = True
        self.name = ""

class UnOp:
    def __init__(self):
        self.op = "" #negation or blank
        self.statement = "" #base entity is knight or knave

class BinOp:
    def __init__(self):
        self.op = None #could be AND, OR
        self.left = None #base entity is knight or knave
        self.right = None

#class for parsing abstract syntax trees into a true or false value
class Evaluator:
    def evalUnop(self, unop):
        if isinstance(unop.statement, BinOp):
            result = self.evalBinop(unop.entity)
        elif isinstance(unop.statement, UnOp):
            result = self.evalUnop(entity)
        else:
            result = unop.statement #base case, boolean true if knight, false if not

        #once we are done parsing the recursive data type    
        if unop.op == Op.NEGATION:
            return ~result
        else:
            return result
    
    def evalBinop(self, binop):
        if isinstance(binop.left, BinOp):
            leftResult = self.evalBinop(binop.left)
        elif isinstance(binop.left, UnOp):
            leftResult = self.evalUnop(binop.left)
        else:
            leftResult = binop.left.TRUTH #base case, boolean true if knight, false if not
            
        if isinstance(binop.right, BinOp):
            rightResult = self.evalBinop(binop.right)
        elif isinstance(binop.right, UnOp):
            rightResult = self.evalUnop(binop.right)
        else:
            rightResult = binop.right.TRUTH #base case, boolean true if knight, false if not 
        #once we are done parsing the recursive data type    
        if binop.op == Op.AND:     #account for results going together
            return leftResult and rightResult
        elif binop.op == Op.OR:
            return leftResult or rightResult

        elif binop.op == Op.XOR:
            return leftResult != rightResult
        else:
            return #error here

    def evalOp(self, op):
        if isinstance(op, BinOp):
            result = self.evalBinop(op)
        elif isinstance(op, UnOp):
            result = self.evalUnop(op)
        else:
            result = op.TRUTH #base case, boolean true if knight, false if not
        
        return result


class KnightsOrKnaves:
    def __init__(self, nameLogicDict):
        self.nameLogicDict = nameLogicDict #mapping of name to logic
        self.evaluator = Evaluator()
    #Assume the person P speaking is a knight. Then we can AND the logical statement they are saying with P 
    #and evaluate a result
    def getKnightLogic(self, speaker, logic):
        knightBinop = BinOp()
        knightBinop.left = logic
        entity = Entity()
        entity.name = speaker
        knightBinop.op = Op.AND
        knightBinop.right = entity
        return knightBinop
    #Assume the Person P seaking is a knave. NEGATE their statement, then and everything with ~P
    def getKnaveLogic(self, speaker, logic):
        knaveBinop = BinOp()
        negatedLogic = UnOp()
        negatedLogic.op = Op.NEGATION
        negatedLogic.statement = logic
        knaveBinop.left = logic
        entity = Entity()
        entity.name = speaker
        unop = UnOp()
        unop.op = Op.NEGATION
        unop.statement = entity
        knaveBinop.op = Op.AND
        knaveBinop.right = unop
        return knaveBinop 

    #create a binop with the speaker's logical statement, and that of another speakers
    def evalKnightKnave(self, speakerDict):
        #person -> knight_knave -> stmt
        logicDict = {}
        for speaker, logic in speakerDict.items():
            subDict = {}
            subDict["knight"] = self.getKnightLogic(speaker, logic)
            subDict["knave"] = self.getKnaveLogic(speaker, logic)

            logicDict[speaker] = subDict

        #now attempt to test combinations of spakers and logical statement
        speakers = [speaker for speaker in speakerDict.keys()]
        
        #compare with speaker2 statements
        for knightKnave, statement in logicDict[speakers[0]].items():
            combinedBinop = BinOp()
            combinedBinop.left = statement
            combinedBinop.op = Op.AND
            speaker2Dict = logicDict[speakers[1]]
            for knightKnave2, statement2 in speaker2Dict.items():
                combinedBinop.right = statement2
                result = self.evaluator.evalOp(combinedBinop)
                print(result)
                if result == True:
                    return {knightKnave:speakers[0], knightKnave2:speakers[1]}
        return None
 #Q:You meet two inhabitants: Zoey and Mel. Zoey tells you that Mel is a knave. Mel says, `Neither Zoey nor I are knaves.'
 #Z: Unop: ~M, M:Binop  ~Z and ~M




class KnightProver:
    def __init__(self, text):
        self.entities = self.parseEntities(text)
        sentences = [sent for sent in sent_tokenize(text)]
        print(sentences)
        taggedSentences = [self.tag(sent) for sent in sentences]
        
        for sent in sentences:
            self.parseExpression(sent)

    def evaluate(expr1, expr2, goal):
        logic._counter._value = 0
        lp = LogicParser()
        p1 = lp.parse('man(socrates)')
        p2 = lp.parse('all x.(man(x) -> mortal(x))')
        c  = lp.parse('mortal(socrates)')
        print(Prover9().prove(c, [p1,p2]))

    def evalOp(self, binop):
            if isinstance(binop.left, BinOp):
                leftResult = self.evalBinop(left)
            elif isinstance(binop.left, UnOp):
                leftResult = self.evalUnop(binop.left)
            else:
                leftResult = binop.left.TRUTH #base case, boolean true if knight, false if not
            
            if isinstance(binop.right, BinOp):
                leftResult = self.evalBinop(binop.right)
            elif isinstance(binop.right, UnOp):
                leftResult = self.evalUnop(binop.right)
            else:
                leftResult = binop.right.TRUTH #base case, boolean true if knight, false if not 
            
            if binop.op == Op.AND:
                return leftResult and rightResult
            elif binop.op == Op.OR:
                return leftResult or rightResult

            elif binop.op == Op.XOR:
                return leftResult != rightResult
            return 

    def tag(self, sentence):
        words = word_tokenize(sentence)
        words = pos_tag(words)
        return words



