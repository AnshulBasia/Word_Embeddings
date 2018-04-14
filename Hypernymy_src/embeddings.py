from data import get_data
from gensim.models import Word2Vec
from Word import Word
from typing import Any, Iterable, List, Optional, Set, Tuple
#from main import find_word

from load import load_words
import math
import vectors as v
from vectors import Vector

def find_word(text: str, words: List[Word]) -> Optional[Word]:
    try:
       return next(w for w in words if text == w.text)
    except StopIteration:
       return None

list_words = get_data()
words = []
for entry in list_words:
    words.append(entry[0])
    words.append(entry[1])
# # train model
# model = Word2Vec(words, min_count=1)
# # summarize the loaded model
# print(model)

loaded = load_words('data/words-long.vec')
em = find_word(words[0],loaded)
print(em)
