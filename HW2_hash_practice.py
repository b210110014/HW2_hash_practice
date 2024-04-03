# 定義檔案路徑
file_path = "hw2_data.txt"

# 建立一個空字典來存放每個英文單字出現的次數
word_counts = {}

# 開啟檔案
with open(file_path, 'r') as file:
    # 逐行讀取檔案
    for line in file:
        # 去除每行文字中的換行符號
        word = line.strip()
        # 更新字典
        if word not in word_counts:
            word_counts[word] = 1
        else:
            word_counts[word] += 1

# 計算不重複的英文單字數量
num_unique_words = len(word_counts)

# 輸出結果
print("總共有 {} 個不重複的英文單字。".format(num_unique_words))
print("每一個英文單字出現次數為：")
for word, count in word_counts.items():
    print("'{}' 出現 {} 次。".format(word, count))

# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 16:39:15 2024

@author: jxc
"""

