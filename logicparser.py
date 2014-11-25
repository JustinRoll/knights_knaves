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

class op(Enum):
    NEGATION = 1
    AND = 2
    OR = 3
    XOR = 4

class entity:
    def __init__(self):
        self.KNIGHT = False

class UnOp:
    def __init__(self):
        self.op = "" #negation or blank
        self.entity = "" #base entity is knight or knave

class BinOp:
    def __init__(self):
        self.op = "" #could be AND, OR
        self.left = "" #base entity is knight or knave
        self.right = ""

#class for parsing abstract syntax trees into a true or false value
class Evaluator:
    def evalUnOp(self, unop):
        if isinstance(unop.entity, BinOp):
            result = self.evalBinop(unop.entity)
        elif isinstance(unop.entity, UnOp):
            result = self.evalUnop(entity)
        else:
            result = unop.entity.KNIGHT #base case, boolean true if knight, false if not

        #once we are done parsing the recursive data type    
        if unop.op == op.NEGATION:
            return ~result
        else:
            return result
    
    def evalBinOp(self, binop):
        if isinstance(binop.left, BinOp):
            leftResult = self.evalBinop(left)
        elif isinstance(binop.left, UnOp):
            leftResult = self.evalUnop(binop.left)
        else:
            leftResult = binop.left.KNIGHT #base case, boolean true if knight, false if not
            
        if isinstance(binop.right, BinOp):
            leftResult = self.evalBinop(binop.right)
        elif isinstance(binop.right, UnOp):
            leftResult = self.evalUnop(binop.right)
        else:
            leftResult = binop.right.KNIGHT #base case, boolean true if knight, false if not 
        #once we are done parsing the recursive data type    
        if binop.op == op.AND:
            return leftResult and rightResult
        elif binop.op == op.OR:
            return leftResult or rightResult

        elif binop.op == op.XOR:
            return leftResult != rightResult
        else:
            return #error here

class LogicParser:
    def __init__(self, text):
        self.entities = self.parseEntities(text)
        sentences = [sent for sent in sent_tokenize(text)]
        print(sentences)
        taggedSentences = [self.tag(sent) for sent in sentences]
        
        for sent in sentences:
            #speaker
            self.parseExpression(sent)

    def evalOp(self, binop):
            if isinstance(binop.left, BinOp):
                leftResult = self.evalBinop(left)
            elif isinstance(binop.left, UnOp):
                leftResult = self.evalUnop(binop.left)
            else:
                leftResult = binop.left.KNIGHT #base case, boolean true if knight, false if not
            
            if isinstance(binop.right, BinOp):
                leftResult = self.evalBinop(binop.right)
            elif isinstance(binop.right, UnOp):
                leftResult = self.evalUnop(binop.right)
            else:
                leftResult = binop.right.KNIGHT #base case, boolean true if knight, false if not 
            
            if binop.op == op.AND:
                return leftResult and rightResult
            elif binop.op == op.OR:
                return leftResult or rightResult

            elif binop.op == op.XOR:
                return leftResult != rightResult
            return 

    def tag(self, sentence):
        words = word_tokenize(sentence)
        words = pos_tag(words)
        return words

    def parseExpression(self, sentence):
        speakerRegExp = r" ?([A-Z][a-z]+) [says]|[tells]|[claims]"  #not fully working
        result = re.search(speakerRegExp, sentence)
        print(result.group(0))

    def parseEntities(self, text):
        entities = []
        entityRegExp = r"You meet two inhabitants: ([A-Z][a-z]+) and ([A-Z][a-z]+)"
        result = re.search(entityRegExp, text)
        entities.append(result.group(1))
        entities.append(result.group(2))

        return entities


