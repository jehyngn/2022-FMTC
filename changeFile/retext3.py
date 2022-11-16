import os, sys

# 본선(신호등+표지판)
# 첫번 째 열 10, 11, 12, 13, 15 삭제
# 14->10, 16->11, 17->12, 18->13, 19->14, 20->15 변경

# 삭제내용
modify1 = {
    "10": "0",
    "11": "1",
    "12": "2",
    "13": "3",
    "15": "4",
}

# 변환내용
modify2 = {
    "14": "10",
    "16": "11",
    "17": "12",
    "18": "13",
    "19": "14",
    "20": "15",
}



path = './file_path2_txt/'
path2 = './file_path2_txt2/'
file_list = os.listdir(path)

print('FILE CNT : {}'.format(len(file_list)))
for file in file_list:
    f_read = open(path+file, 'r').read()

    out_str = ''
    for line in f_read.strip('\n').split('\n'):
        if len(line) == 0: continue
        words = line.split()

        # 삭제
        if words[0] in modify1.keys():
            continue
        if words[0] in modify2.keys():
            words[0] = modify2[words[0]]

        out_str += " ".join(words) + '\n'
        # print(words)

    res_str = out_str.rstrip('\n')
    print(file)
    print(f_read.strip())
    print('=======================')
    print(res_str)
    print()

    with open(path2+file, 'w') as f:
        f.write(res_str)
        f.close()

