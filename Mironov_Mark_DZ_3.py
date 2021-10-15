import pymorphy2
morph = pymorphy2.MorphAnalyzer()
word = morph.parse("Процент")
v1, v2, v3 = word.inflect({"sing", "nomn"}), word.inflect({"gent"}), word.inflect({"plur", "gent"})
print(v1.word, v2.word, v3.word)