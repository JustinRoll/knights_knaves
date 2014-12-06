from puzzleDict import PuzzleInfo
import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk.sem.drt import *
from nltk.sem import logic
from nltk.sem.logic import *
from nltk.inference.resolution import *
read_expr = nltk.sem.Expression.fromstring 
import sys

class KKLogic:
    def __init__(self):
        self.entities = ()
        self.statements = []


    def validateStatement(self, assumptionStr, goalStr):
        lp = LogicParser()  
    
#        print("assumption: %s goal: %s" % (assumptionStr, goalStr))
        assumption = read_expr(assumptionStr) #zoey and mel are knaves
        goal  = read_expr(goalStr)
        prover = ResolutionProverCommand(goal, [assumption])
        return prover.prove()        

    def evalKnightKnave(self):
        #person -> knight_knave -> stmt
        logicDict = {}
        bothKnights = "knight(%s) and knight(%s)" % (self.entities[0], self.entities[1])
        bothKnaves = "-knight(%s) and -knight(%s)" % (self.entities[0], self.entities[1])
        firstKnight = "knight(%s) and -knight(%s)" % (self.entities[0], self.entities[1])
        secondKnight = "-knight(%s) and knight(%s)" % (self.entities[0], self.entities[1])
        
        bothKnightsResult = "%s is a knight. %s is a knight." % (self.entities[0], self.entities[1])
        bothKnavesResult = "%s is a knave. %s is a knave." % (self.entities[0], self.entities[1])
        firstKnightResult = "%s is a knight. %s is a knave." % (self.entities[0], self.entities[1])
        secondKnightResult = "%s is a knave. %s is a knight." % (self.entities[0], self.entities[1])
        #(-((knight(Ted) and -knight(Zippy)) or (-knight(Ted) and knight(Zippy))) and -knight((knight(Ted) and -knight(Zippy)) or (-knight(Ted) and knight(Zippy)))) and (-(-knight(Ted)) and -knight(Zippy))

        #check possibility that both are knights
        andedStatements = "((%s) and knight(%s)) and ((%s) and knight(%s))" % (self.statements[0][1], self.statements[0][0], self.statements[1][1], self.statements[1][0])  #need to and in more?
        kkTrue = self.validateStatement(bothKnights, andedStatements)
        if kkTrue:
            return bothKnightsResult
        #bothKnaves 
        knaveKnaveTrue = self.validateStatement(bothKnaves, "(-(%s) and -knight(%s)) and (-(%s) and -knight(%s))" % (self.statements[0][1], self.statements[0][0], self.statements[1][1], self.statements[1][0]))
        if knaveKnaveTrue:
            return bothKnavesResult
        #firstKnave
        firstKnightTrue = self.validateStatement(firstKnight, "((%s) and knight(%s)) and (-(%s) and -knight(%s))" % (self.statements[0][1], self.statements[0][0], self.statements[1][1], self.statements[1][0]))
        if firstKnightTrue:
            return firstKnightResult


        #secondKnave
        secondKnightTrue = self.validateStatement(secondKnight, "(-(%s) and -knight(%s)) and ((%s) and knight(%s))" % (self.statements[0][1], self.statements[0][0], self.statements[1][1], self.statements[1][0]))
        if secondKnightTrue:
            return secondKnightResult
       
        return None    


class SentParser:

    def __init__(self):
        pass

    def parseEntities(self, text):
        entities = []
        entityRegExp = r"You meet two inhabitants: ([A-Z][a-z]+) and ([A-Z][a-z]+)"
        result = re.search(entityRegExp, text)
        entities.append(result.group(1))
        entities.append(result.group(2))

        return entities

    def parseLogic(self, text):
        entities = self.parseEntities(text)
        #tokenize each sentence
        sents = [sent for sent in sent_tokenize(text)]
        kkLogic = KKLogic()
        for sent in sents:
            self.parseSentence(sent, kkLogic)
        return kkLogic

    def parseSentence(self, sent, kkLogic):
        sentText = sent
        if "You meet two inhabitants" in sentText:
            kkLogic.entities = self.parseEntities(sentText)
        else:
            self.parseSentLogic(sentText, kkLogic)
    
    def containsNot(self, sent):
        if "it is false that" in sent or "it's false that" in sent or "not the case that" in sent:
            return True
        else:
            return False

    def containsAreBoth(self, sent):
        if "are both knights" in sent or "are both knaves" in sent:
            return True
        else:
            return False

    def containsBoth(self, sent):
        if "both knights or both knaves" in sent or "both knaves or both knights" in sent or "are the same" in sent:
            return True
        else:
            return False

    def genAreBoth(self, text, kkLogic):
        regExp = r"are both ((knights)|(knaves))"
        result = re.search(regExp, text)
        if result and result.group(1):
            ty = result.group(1)
            if ty == "knights":
                return "knight(%s) and knight(%s)" % (kkLogic.entities[0], kkLogic.entities[1])
            elif ty == "knaves":
                return "knave(%s) and knave(%s)" % (kkLogic.entities[0], kkLogic.entities[1]) 

    def genBoth(self, kkLogic):
        return "(knight(%s) and knight(%s)) or (knave(%s) and knave(%s))" % (kkLogic.entities[0], kkLogic.entities[1], kkLogic.entities[0], kkLogic.entities[1])

    #check for compound sentence. If the sentence is compound, break it up
    #check for notted statements
    def parseSentLogic(self, sentText, kkLogic):
        #we need to get the speaker as well as the logical breakdown
        #print(sentText)
        speakerRegExp = "([A-Z][a-z]*) ((tells you that)|(says)|(claims)|(tells you))"
        result = re.search(speakerRegExp, sentText)
        speaker = result.group(1) #always a speaker
        #print(speaker)
        #print(sentText)
        statement = ""
        if self.containsConjunction(sentText):
            statement = self.getConjunctionStatement(sentText, speaker, kkLogic)
            #print(self.getConjunctionStatement(sentText, speaker, kkLogic))
        elif self.containsXor(sentText):
            statement = self.generateXor(sentText, kkLogic)
            #print("  " +self.generateXor(sentText, kkLogic))
        elif self.containsCouldSay(sentText):
            statement = self.genCouldSay(sentText, speaker, kkLogic)
            #print(self.genCouldSay(sentText, speaker, kkLogic))
        elif self.containsBoth(sentText):
            statement = self.genBoth(kkLogic)
            #print("  " + self.genBoth(kkLogic)) #both knights or both knaves
        elif self.containsOnlyA(sentText):
            #print(self.genOnlyA(sentText))
            statement = self.genOnlyA(sentText)
        elif self.containsAreBoth(sentText):
           statement = self.genAreBoth(sentText, kkLogic)
           #print(self.genAreBoth(sentText, kkLogic))
        elif self.containsNor(sentText):
            statement = self.genNor(sentText, kkLogic)
            #print(self.genNor(sentText, kkLogic))
        elif self.containsBasicStatement(sentText):
            statement = self.getBasicStatement(sentText, speaker)
            #print("  " + self.getBasicStatement(sentText, speaker))
        
        #if baseResult and baseResult.group(1) and baseResult.group(2):                                                                       
           # print(baseResult.group(1) + " " + baseResult.group(2))
        #parse the basic logic, then see if we need to not stuff
        
        if statement:
            kkLogic.statements.append((speaker, statement.replace("knave", "-knight")))

    def getConjunctionStatement(self, sentText, speaker, kkLogic):
        #Either Zed is a knight or I am a knight.
        #At least one of the following is true: that I am a knight or that Bozo is a knight.'
        #`Zoey and I are both knights or both knaves.'
        #Zed says, `Both I am a knight and Bob is a knave.'
        sentText = sentText.replace(" I ", " " + speaker + " ")
        regExp = r"Both ([A-Z][a-z]*) ((is)|(am)) a ((knight)|(knave)) ((or)|(and)) ([A-Z][a-z]*) ((is)|(am)) a ((knight|knave))"
        result = re.search(regExp, sentText)
        if result and result.groups(3):
            statement = "%s(%s) %s %s(%s)" % ( result.groups(0)[5], result.groups(0)[0],result.groups(0)[7], result.groups(0)[14], result.groups(0)[10])
            
            return statement
        
        regExp = r"Either ([A-Z][a-z]*) ((is)|(am)) a ((knight)|(knave)) ((or)|(and)) ([A-Z][a-z]*) ((is)|(am)) a ((knight|knave))"
        result = re.search(regExp, sentText)
        if result and result.groups(3):
            statement = "%s(%s) %s %s(%s)" % ( result.groups(0)[4], result.groups(0)[0],result.groups(0)[7], result.groups(0)[14], result.groups(0)[10])
        
            return statement 
        
        leastExp = r"At least one of the following is true: that (([A-Z])[a-z]*) am a ((knight)|(knave)) ((and)|(or)) that ([A-Z][a-z]*) is a ((knight)|(knave))"
        result = re.search(leastExp, sentText)
        if result and result.groups(3):
            statement = "%s(%s) %s %s(%s)" % (result.groups(1)[2], result.groups(2)[0], result.groups(3)[5], result.groups(4)[9], result.groups(5)[8]) 
            return statement


        #I and marge are knights
        leastExp = r"I and ([A-Z][a-z]*) are ((knights)|(knaves))"
        result = re.search(leastExp, sentText)
        if result:
            grp = result.groups()[2][:-1]
            return "%s(%s) and %s(%s)" % (grp, kkLogic.entities[0], grp, kkLogic.entities[1]) 

        #Zed tells you, `I am a knight or Alice is a knave.'

        leastExp = r"([A-Z][a-z]*) ((is)|(am)) a ((knight)|(knave)) ((and)|(or)) ([A-Z][a-z]*) ((is)|(am)) a ((knight)|(knave))"
        result = re.search(leastExp, sentText.replace("I ", speaker + " "))
        if result:
            return "%s(%s) %s %s(%s)" % (result.group(5), result.group(1), result.group(8), result.group(15), result.group(11))

    def containsBasicStatement(self, sentText):
        baseRegExp = r"([A-Z][a-z]*) ((am)|(is)) a ((knight)|(knave))"
        result = re.search(baseRegExp, sentText)
        if result and result.group(1) and result.group(2):
            return True
        else:
            return False

    def containsOnlyA(self, sentText):
        if "only a knight" in sentText or "only a knave" in sentText:
            return True
    #Ted says that only a knave would say that Bob is a knave.
    def genOnlyA(self, sentText):
        regExp = r"O|only a ((knight)|(knave)) would say that (([A-Z][a-z]*)) is a ((knight)|(knave))"
        result = re.search(regExp, sentText)
        #('knave', None, 'knave', 'Bob', 'Bob', 'knave', None, 'knave')
        first = result.group(1)
        person = result.group(5)
        isA = result.group(3)

        #print("%s %s %s" % (first, person, isA))

        if isA == "knave" and first == "knave":
            return "knight(%s)" % person
        elif isA == "knight" and first == "knave":
            return "knave(%s)" % person
        elif first == "knight":
            return "%s(%s)" % (isA, person)

    #Ted claims, `Zeke could say that I am a knave.' knight(ted) and knave(zeke) OR knave(ted) and knight(zeke)
    #Rosa claims, 'Steve could say that I am a knight.' knight(steve) and knight(rosa) or knave(steve) and knave(rosa)
    #Ted tells you, `Bart would tell you that I am a knave.'
    def containsCouldSay(self, sentText):
        if "could claim" in sentText or "could say" in sentText or ("would tell you" in sentText and "I would tell you" not in sentText):
            return True
        else:
            return False

    def genCouldSay(self, sentText, speaker, kkLogic):
        regExp = r"([A-Z][a-z]*) could ((claim)|(say)) that I am a ((knight)|(knave))"
        #either I'm telling the truth and zeke is a knave, or I am lying and Zeke is a knight
        result = re.search(regExp, sentText)
        
        if result and result.groups(0)[4] == "knave":
            return "(knave(%s) and knight(%s)) or (knight(%s) and knave(%s))" % (kkLogic.entities[0], kkLogic.entities[1], kkLogic.entities[0], kkLogic.entities[1])  
        elif result and result.groups(0)[4] == "knight":
            return "(knight(%s) and knight(%s)) or (knave(%s) and knave(%s))" % (kkLogic.entities[0], kkLogic.entities[1], kkLogic.entities[0], kkLogic.entities[1])

        
        regExp = r"([A-Z][a-z]*) would ((claim)|(tell you)) that I am a ((knight)|(knave))"
        result = re.search(regExp, sentText)
        if result and result.groups(0)[4] == "knave":
            return "(knave(%s) and knight(%s)) or (knight(%s) and knave(%s))" % (kkLogic.entities[0], kkLogic.entities[1], kkLogic.entities[0], kkLogic.entities[1])  
        elif result and result.groups(0)[4] == "knight":
            return "(knight(%s) and knight(%s)) or (knave(%s) and knave(%s))" % (kkLogic.entities[0], kkLogic.entities[1], kkLogic.entities[0], kkLogic.entities[1]) 

    #Mel says, `Neither Zoey nor I are knaves.'
    def containsNor(self, sentText):
        if "Neither" in sentText and "nor" in sentText:
            return True
        else:
            return False

    def genNor(self, sentText, kkLogic):
         regExp = r"Neither ([A-Z][a-z]*) nor ([A-Z][a-z]*) are ((knights)|(knaves))"
         result = re.search(regExp, sentText)
         role = result.group(3)[:-1]
         if role == "knight":
             role = "knave"
         else:
             role = "knight"

         return "%s(%s) and %s(%s)" % (role, kkLogic.entities[0], role, kkLogic.entities[1])
    def getBasicStatement(self, sentText, speaker):
        containsNot = self.containsNot(sentText)
        baseRegExp = r"([A-Z][a-z]*) is a ((knight)|(knave))"
        result = re.search(baseRegExp, sentText)
        kk = result.group(2)
        person = result.group(1)
        returnStr = "%s(%s)" % (kk, person)
        if containsNot and kk == "knight":
            returnStr = "knave(%s)" % person

        elif containsNot and kk == "knave":
            returnStr = "knight(%s)" % person

        return returnStr

    #if we have two statements, break them down
    def containsConjunction(self, sentText):
        #At least one of the following is true: 
        #Either Ted is a knave or I am a knight.
        containsAnd = False
        match2 = False
        regExp = r"I and ([A-Z][a-z]*) are ((knights)|(knaves))" 
        regExp2 = r"([A-Z][a-z]*) ((is)|(am)) a ((knight)|(knave)) ((and)|(or)) ([A-Z][a-z]*) ((is)|(am)) a ((knight)|(knave))"
        if len(re.findall(regExp2, sentText)) > 0:
            match2 = True
        #Zed says, `Bart is a knight or I am a knight.
        if len(re.findall(regExp, sentText)) > 0:
            containsAnd = True
        if "least one of the following is true" in sentText or "Both" in sentText or "Either" in sentText or containsAnd or match2:
            return True
        else:
            return False

    def containsXor(self, sentText):
        if "exactly one is a" in sentText or "is different" in sentText or "are different" in sentText or "not the same" in sentText:
            return True
        else:
            return False

    def generateXor(self, sentText, kkLogic):
        return "(knight(%s) and knave(%s)) or (knave(%s) and knight(%s))"% (kkLogic.entities[0], kkLogic.entities[1], kkLogic.entities[0], kkLogic.entities[1]) 


pInfo = PuzzleInfo()
sentParser = SentParser()
#nums = sorted(pInfo.puzzleQuestions.keys())
#for num in nums:
#    print(question)
#    kkLogic = sentParser.parseLogic(pInfo.puzzleQuestions[num])
#    print(kkLogic.evalKnightKnave())
if len(sys.argv) > 1:
    f = open(sys.argv[1])
    text = f.readlines()
    for line in text:
        print(line)
        kkLogic = sentParser.parseLogic(line)
        print(kkLogic.evalKnightKnave())
else:
    print("please input a valid file name")
