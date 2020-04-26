import pickle
import pypinyin


def dictionary():
    temp = dict()
    with open("pinyin.txt", 'r') as f:
        for lines in f:
            pos = lines.index(':')
            temp[lines[0:pos]] = lines[pos+1:-1]
    with open("dictionary_dict.pkl", "wb") as f:
        pickle.dump(temp, f, pickle.HIGHEST_PROTOCOL)
    print(temp)


def init_pro():
    init_pro_word = dict()
    sums = 0
    with open("pinyin_train.txt", "r", encoding="utf-8") as f:
        for lines in f:
            for word in lines:
                if '\u4e00' <= word <= '\u9fff':
                    sums += 1
                    if word in init_pro_word:
                        init_pro_word[word] += 1
                    else:
                        init_pro_word[word] = 1
    # print(init_pro_word)
    # print(sums)
    for i in list(init_pro_word.keys()):
        init_pro_word[i] = init_pro_word[i] / sums
    with open("init_pro_dict.pkl", "wb") as f:
        pickle.dump(init_pro_word, f, pickle.HIGHEST_PROTOCOL)


def ch_pro():
    change_pro = dict()
    with open("pinyin_train.txt", "r", encoding="utf-8") as f:
        for lines in f:
            for index in range(len(lines)-1):
                if '\u4e00' <= lines[index] <= '\u9fff':
                    if lines[index] in change_pro:
                        change_pro[lines[index]]["sum"] += 1
                    else:
                        change_pro[lines[index]] = dict()
                        change_pro[lines[index]]["sum"] = 1
                    if '\u4e00' <= lines[index+1] <= '\u9fff':
                        if lines[index+1] in change_pro[lines[index]]:
                            change_pro[lines[index]][lines[index+1]] += 1
                        else:
                            change_pro[lines[index]][lines[index + 1]] = 1
    for i in list(change_pro.keys()):
        for j in change_pro[i]:
            if j == "sum":
                continue
            change_pro[i][j] = change_pro[i][j] / change_pro[i]["sum"]
    print(change_pro["中"])
    with open("change_pro_dict.pkl", "wb") as f:
        pickle.dump(change_pro, f, pickle.HIGHEST_PROTOCOL)


def biu_pro():
    biu_pro_dict = dict()
    temp = []
    with open("pinyin_train.txt", "r", encoding="utf-8") as f:
        for lines in f:
            for word in lines:
                if '\u4e00' <= word <= '\u9fff':
                    temp.append(word)
                else:
                    strs = ''.join(temp)
                    pinyinstrs = pypinyin.lazy_pinyin(strs, pypinyin.FIRST_LETTER)
                    temp.clear()
                    for index in range(len(strs)):
                        if strs[index] in biu_pro_dict:
                            biu_pro_dict[strs[index]]["sum"] += 1
                            if pinyinstrs[index] in biu_pro_dict[strs[index]]:
                                biu_pro_dict[strs[index]][pinyinstrs[index]] += 1
                            else:
                                biu_pro_dict[strs[index]][pinyinstrs[index]] = 1
                        else:
                            biu_pro_dict[strs[index]] = dict()
                            biu_pro_dict[strs[index]]["sum"] = 1
                            biu_pro_dict[strs[index]][pinyinstrs[index]] = 1
    for i in list(biu_pro_dict.keys()):
        for j in biu_pro_dict[i]:
            if j == "sum":
                continue
            else:
                biu_pro_dict[i][j] = biu_pro_dict[i][j]/biu_pro_dict[i]["sum"]
    print(biu_pro_dict)
    with open("biu_pro_dict.pkl", "wb") as f:
        pickle.dump(biu_pro_dict, f, pickle.HIGHEST_PROTOCOL)


if __name__ == "__main__":
    # dictionary()
    # init_pro()
    ch_pro()
    # biu_pro()

