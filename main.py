def cut_word(sentence, word_dict_name):
    word_dict = get_lines(word_dict_name)
    word_length_list = [len(word) for word in word_dict]
    # max_length是字典中最长的词的长度
    max_length = max(word_length_list)

    # word_length为词的长度，初始值为句子长度。
    sentence_length = len(sentence)

    # 返回序列
    cut_word_list = []

    while sentence_length > 1:
        # 剪切长度，初始为句长和字典最大词长的小值
        max_cut_length = min(max_length, sentence_length)
        subsentence = sentence[0:max_cut_length]
        while max_cut_length > 1:  # 当词长缩短至1时跳出
            if subsentence in word_dict:
                cut_word_list.append(subsentence)
                break
            else:
                max_cut_length = max_cut_length - 1
                subsentence = subsentence[0:max_cut_length]
        # 句长去掉1或已提取的词长，生成新的句子进行下一个循环。
        sentence = sentence[max_cut_length:]
        sentence_length = sentence_length - max_cut_length
    return cut_word_list


def get_lines(filename):
    data_set = []
    with open(filename, 'rb') as f:
        line = f.readline()
        while line:
            line = line.decode("gb18030", "ignore")
            data_set.append(line.strip())
            line = f.readline()
    return data_set


if __name__ == '__main__':
    lines = get_lines("chp0520825-2.txt")
    words = []
    for text_line in lines:
        cut_result = cut_word(text_line, "word_dict.txt")
        if cut_result:  # 筛掉空字符
            words.append(cut_result)
    print(words)
