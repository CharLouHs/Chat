def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        new = []
        for line in f:
            s = line.strip().split(' ')
            new.append(s)
    return new


def cal(new):
    Allen_words_count=0
    Viki_words_count=0
    Allen_stickers=0
    Viki_stickers=0
    Allen_picture=0
    Viki_picture=0
    for i in new:
        time=i[0]
        name=i[1]

        if name=='Allen':
            if i[2]=='貼圖':
                Allen_stickers+=len(i[2])
            elif i[2]=='圖片':
                Allen_picture+=len(i[2])
            else:
                for i in i[2:]:
                    Allen_words_count+=len(i)
        elif name=='Viki':
            if i[2]=='貼圖':
                Viki_stickers+=len(i[2])
            elif i[2]=='圖片':
                Viki_picture+=len(i[2])
            else:
                for i in i[2:]:
                    Viki_words_count+=len(i)

    print('Allen共講',Allen_words_count,' 個字')
    print('Allen共傳' , Allen_stickers , ' 張貼圖')
    print('Allen共傳',Allen_picture,' 張圖片')
    print('Viki共講' , Viki_words_count , ' 個字')
    print('Viki共傳' , Viki_stickers , ' 張貼圖')
    print('Viki共傳' , Viki_picture , ' 張圖片')
def main():
    total=read_file('LINE-Viki.txt')
    cal(total)

main()
