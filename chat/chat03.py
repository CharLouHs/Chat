
def read_file(filename):
    with open(filename,'r',encoding='utf-8-sig') as f:
        new=[]
        for line in f:

            new.append(line.strip())
        print(new)
    return new

def cal(new):
    for i in new:
        i=i.split(' ')
        print(i[0][5:])

def main():
    k=read_file('3.txt')
    cal(k)

main()