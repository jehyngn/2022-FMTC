import os, sys

# 협로 수정
modify1 = {
    "15": "0",
    "21": "1"
}

path = './narrow_path_txt/'
path2 = './narrow_path_txt2/'
file_list = os.listdir(path)

print('FILE CNT : {}'.format(len(file_list)))
for file in file_list:
    f_read = open(path+file, 'r').read()

    out_str = ''
    for line in f_read.strip('\n').split('\n'):
        if len(line) == 0: continue
        words = line.split()
        if words[0] in modify1.keys():
            words[0] = modify1[words[0]]

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

