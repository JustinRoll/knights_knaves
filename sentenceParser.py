import nltk
#from nltk import CFG
from nltk import ChartParser


kk_grammar = nltk.grammar.ContextFreeGrammar.fromstring("""
S -> Sp Sa St
Sp -> P
Sa -> 'tells' 'you' 'that' | 'says' | 'says' 'that' | 'claims' | 'claims' 'that' | 'tells you'
St -> PG Is Class | PG Quant Is Class | 
Quant -> Comp Count
Comp -> 'exactly'
Count -> 'one'
Not -> 'neither' | 'nor' 
PG -> 'i' | PG PG | Not P | P | 'of' PG | PG 'and' PG
P -> 'zoey' | 'mel' | 'peggy' | 'zippy' | 'sue' | 'sally' | 'homer' | 'bozo' | 'marge' | 'zed' | 'alice' | 'ted' | 'bart' | 'bob' | 'betty'
Is -> 'is' 'a' | 'are'
Class -> Kni | Kna
Kni -> 'knight' | 'knights'
Kna -> 'knave' | 'knaves'
""")

def preprocess(sent):
    return "".join([letter for letter in sent.lower() if letter in "qwertyuiopasdfghjklzxcvbnm "]).split()

sents = ["Zoey tells you that mel is a Knave",
         "Mel says, `Neither Zoey nor I are knaves.'",
         "Peggy tells you that 'of Zippy and I, exactly one is a knight'."]
sents = [preprocess(sent) for sent in sents]
parser = ChartParser(kk_grammar)
for sent in sents:
    for tree in parser.parse(sent):
        print(tree)




