from random import choices
import time
import jieba
import json
import logging

jieba.setLogLevel(logging.INFO)

with open("Markhoff_chain.json", 'r', encoding="utf8") as json_file:
    Markhoff_chain_dict: dict = json.load(json_file)
while True:
    input_text = input("請輸入文字：").replace(
        "!", "！").replace("...", "…").replace("?", "？")
    text_cut = list(jieba.cut(input_text))
    if len(text_cut) < 2:  # 長度不足
        print("請輸入更長的開頭。")
        continue
    
    print(input_text, end="")
    while text_cut[-1] != "\n":
        source_word = text_cut[-2]+text_cut[-1]
        probability_dict: dict = Markhoff_chain_dict.get(source_word)
        if probability_dict == None or len(text_cut) > 500:
            print("找不到可接續的文字。無法採樣，請增加文本數量。")
            break
        choice_word = choices(list(probability_dict.keys()),
                            weights=list(probability_dict.values()),
                            k=1)
        text_cut += choice_word
        print(choice_word[0], end="")
        time.sleep(0.01)
        
    print()
