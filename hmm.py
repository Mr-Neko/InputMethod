import pickle


def hmm(init_pro: dict, change_pro: dict, biu_pro: dict, pinyin):
    table = [[]]
    for key in init_pro:
        if pinyin[0] in biu_pro[key]:
            table[0].append([biu_pro[key][pinyin[0]] * init_pro[key], key, 0])
    for index in range(1, len(pinyin)):
        table.append([])
        for key in init_pro:
            if pinyin[index] in biu_pro[key]:
                maxs = 0
                pos = 0
                for jn in range(len(table[index-1])):
                    # print(table[index-1][jn])
                    if key in change_pro[table[index-1][jn][1]]:
                        if table[index-1][jn][0] * change_pro[table[index-1][jn][1]][key] > maxs:
                            maxs = table[index-1][jn][0] * change_pro[table[index-1][jn][1]][key]
                            pos = jn
                table[-1].append([maxs * biu_pro[key][pinyin[index]], key, pos])
    length = len(pinyin) - 2
    temp = []
    answer = []
    sort_list = sorted(table[-1], key=lambda x: x[0], reverse=True)
    # print(sort_list)
    for i in sort_list:
        if i[0] == 0:
            break
        temp.append(i[1])
        temp_pos = i[2]
        for j in range(length, -1, -1):
            temp.insert(0, table[j][temp_pos][1])
            temp_pos = table[j][temp_pos][2]
        answer.append(''.join(temp))
        temp.clear()
    for i in range(len(answer)):
        answer[i] = str(i % 5 + 1) + '、' + answer[i]
    return answer


def link_test():
    print("Link Success!!")


if __name__ == "__main__":
    with open("init_pro_dict.pkl", "rb") as f:
        init_pros = pickle.load(f)
    with open("biu_pro_dict.pkl", "rb") as f:
        biu_pros = pickle.load(f)
    with open("change_pro_dict.pkl", "rb") as f:
        change_pros = pickle.load(f)
    hmm(init_pros, change_pros, biu_pros, "acz")
