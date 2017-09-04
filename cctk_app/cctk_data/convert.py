import kenlm
import jieba
import itertools
import sys
import codecs

keys = set()
phrase_mapper = {}
char_mapper = {}
model = kenlm.Model('./cctk_app/cctk_data/dictionary/text.binary')

with open("./cctk_app/cctk_data/dictionary/readable_multi.txt") as f:
    for line in f:
        segs = line.decode('utf-8').strip().split("\t")
        keys.add(segs[0])
        for e in segs[1].split():
            keys.add(e)
        source = segs[0]
        targets = segs[1].split()
        char_mapper[source] = targets

with open("./cctk_app/cctk_data/dictionary/readable_multi_phrase") as f:
    for line in f:
        segs = line.decode('utf-8').strip().split("\t")
        keys.add(segs[0])
        for e in segs[1].split():
            keys.add(e)
        source = segs[0]
        target = segs[1]
        phrase_mapper[source] = target

def wordlevel(sentence):
    words = jieba.cut(sentence, cut_all=False)
    new_words = []
    for w in words:
        if w in phrase_mapper:
            new_words.append(phrase_mapper[w])
        else:
            new_words.append(w)
    return "".join(new_words)

def translate_char(char):
    if char in char_mapper:
        res = char_mapper[char]
    else:
        res = [char]
    return res
    

def verify_number(chars):
    count = 0
    for char in chars:
        if char in char_mapper:
            if len(char_mapper)>1:
                count += 1
    if count<10:
        return False
    else:
        return True
    
def charlevel(sentence):
    chars = [w for w in sentence]
    if verify_number(chars):
        length = len(sentence)
        a = translate_sentence(sentence[:int(0.5*length)])
        b = translate_sentence(sentence[int(0.5*length):])
        return a+b
    else:
        target_chars = [translate_char(w) for w in chars]
        poss = list(itertools.product(*target_chars))
        cands = [" ".join(p) for p in poss]
        intmax = -sys.maxint
        best = None
        for cand in cands:
            score = model.score(cand)
            if score > intmax:
                intmax = score
                best = cand
    best_sent = "".join(best.split())

    return best_sent

def translate_sentence(t):
    t1 = wordlevel(t)
    t2 = charlevel(t1)
    return t2

def processed(w):
    ret = ""
    for c in w:
        ret += '<span class="name" style="background-color:#00ff00">'
        ret += c
        ret += '</span>'
    return ret
    
def change(seq):
    new_seq = translate_sentence(seq)
    for k in keys:
        if len(k)==1:
            print k
        new_seq = new_seq.replace(k, processed(k))
    return new_seq

