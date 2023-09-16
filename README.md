# Markhov_chain_text_generationn
## 介紹
這是一個基於馬可霍夫練的文本生成器。使用前兩個單字當作狀態，按照機率分布隨機出下個單字，並更新狀態。

## 使用方法
下載`Markhov_chain_sampling.py`與`Markhoff_chain.json`，需確保兩個檔案在同個目錄底下。
使用開發環境或直接開啟`Markhov_chain_sampling.py`，會提示使用者輸入文字，其輸入必須「大於兩個單字」且「在文本中出現過」才能續寫。

## 檔案註解
`corpus_text.txt`：文本資料，以換行為分割文句。

`Markhoff_chain.json`：儲存指向關係。每兩個單字會指向一個對表，其中儲存下個單字與其接續次數。次數越高，隨機時的權重也越高，目的是模擬文本續寫的下個單字出現機率。

`Markhov_chain_generation.py`：將`corpus_text.txt`轉換為`Markhoff_chain.json`。

`Markhov_chain_sampling.py`：使用`Markhoff_chain.json`生成(續寫)文本。
