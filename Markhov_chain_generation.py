import json
import jieba

with open("corpus_text.txt", "r", encoding="utf8") as file:
    text_cuts = []
    for text in file:
        text_cut = list(jieba.cut(text))
        if len(text_cut) < 3:
            continue
        text_cuts.append(text_cut)

Markhoff_chain_dict = {}
for sentence in text_cuts:
    for word1, word2, predict in zip(sentence[0:-2], sentence[1:-1], sentence[2:]):
        source_word = word1+word2
        source_dict = Markhoff_chain_dict.get(source_word, {})
        source_dict[predict] = source_dict.get(predict, 0)+1
        Markhoff_chain_dict[source_word] = source_dict
with open("Markhoff_chain.json", 'w', encoding="utf8") as json_file:
    json.dump(Markhoff_chain_dict, json_file, ensure_ascii=False)
