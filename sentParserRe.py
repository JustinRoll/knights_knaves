from puzzleDict import PuzzleInfo
import re
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize

class KKLogic:
    def __init__(self):
        self.entities = ()
        self.statements = []

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

    def parseSentence(self, sent, kkLogic):
        sentText = sent
        if "You meet two inhabitants" in sentText:
            kkLogic.entities = self.parseEntities(sentText)
        else:
            self.parseSentLogic(sentText, kkLogic)
    
    def containsNot(self, sent):
        if "it is false that" in sent or "not the case that" in sent:
            return True
        else:
            return False

    def containsBoth(self, sent):
        if "both knights or both knaves" in sent or "both knaves or both knights" in sent or "are the same" in sent:
            return True
        else:
            return False

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
        print(sentText)
        if self.containsConjunction(sentText):
            print(self.getConjunctionStatement(sentText, speaker))
        elif self.containsXor(sentText):
            print("  " +self.generateXor(sentText, kkLogic))
        elif self.containsCouldSay(sentText):
            self.genCouldSay(sentText, speaker, kkLogic)
        elif self.containsBoth(sentText):
            print("  " + self.genBoth(kkLogic)) #both knights or both knaves
        elif self.containsOnlyA(sentText):
            print(self.genOnlyA(sentText))
        elif self.containsBasicStatement(sentText):
            print("  " + self.getBasicStatement(sentText, speaker))
        
        #if baseResult and baseResult.group(1) and baseResult.group(2):                                                                       
           # print(baseResult.group(1) + " " + baseResult.group(2))
        #parse the basic logic, then see if we need to not stuff
        
        #kkLogic.statements.append(speaker, logic)

    def getConjunctionStatement(self, sentText, speaker):
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
            statement = "%s(%s) %s %s(%s)" % (result.groups(1)[2], result.groups(2)[0], result.groups(3)[5], result.groups(4)[9], result.groups(5)[8])) 
            return statement


        #I and marge are knights
        leastExp = r"I and ([A-Z][a-z]*) are ((knights)|(knaves))"
        result = re.search(leastExp, sentText)
        if result and result.groups(3):
            statement = "%s(%s) %s %s(%s)" % (result.groups(1)[2], result.groups(2)[0], result.groups(3)[5], result.groups(4)[9], result.groups(5)[8])) 
            return statement 

        #Zed tells you, `I am a knight or Alice is a knave.'
        leastExp = r"I am a ((knight)|(knave)) or ([A-Z][a-z]+) is a ((knight)|(knave))" 

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
            print("  (knave(%s) and knight(%s) or (knight(%s) and knave(%s)" % (kkLogic.entities[0], kkLogic.entities[1], kkLogic.entities[0], kkLogic.entities[1]))  
        elif result and result.groups(0)[4] == "knight":
            print("  (knight(%s) and knight(%s)) or knave(%s) and knave(%s)" % (kkLogic.entities[0], kkLogic.entities[1], kkLogic.entities[0], kkLogic.entities[1]))

        
        regExp = r"([A-Z][a-z]*) would ((claim)|(would tell you)) that I am a ((knight)|(knave))"
        result = re.search(regExp, sentText)
        if result and result.groups(0)[4] == "knave":
            print("  (knave(%s) and knight(%s) or (knight(%s) and knave(%s)" % (kkLogic.entities[0], kkLogic.entities[1], kkLogic.entities[0], kkLogic.entities[1]))  
        elif result and result.groups(0)[4] == "knight":
            print("  (knight(%s) and knight(%s)) or knave(%s) and knave(%s)" % (kkLogic.entities[0], kkLogic.entities[1], kkLogic.entities[0], kkLogic.entities[1])) 



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
        if "least one of the following is true" in sentText or "Both" in sentText or "Either" in sentText:
            return True
        else:
            return False

    def containsXor(self, sentText):
        if "exactly one is a" in sentText or "is different" in sentText or "not the same" in sentText:
            return True
        else:
            return False

    def generateXor(self, sentText, kkLogic):
        return "(knight(%s) and knave(%s)) or (knave(%s) and knight(%s))"% (kkLogic.entities[0], kkLogic.entities[1], kkLogic.entities[0], kkLogic.entities[1]) 


pInfo = PuzzleInfo()
sentParser = SentParser()
for number, question in pInfo.puzzleQuestions.items():
#    print(question)
    sentParser.parseLogic(question)
