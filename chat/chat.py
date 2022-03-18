import os

liness = []


def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            liness.append(line.strip())
        # print(liness)
    return liness





def coll(lines):
    person = None
    linee = []
    for m in lines:
        if m == 'Allen':
            person = 'Allen'
            continue
        elif m == 'Tom':
            person = 'Tom'
            continue
        if person:
            linee.append(person + ':' + m
    #print(linee)
    return linee


def showw(ll):
    for i in ll:
        print(i)


def write_file(filename, liness):
    with open(filename, 'w') as f:
        for line in liness:
            f.write(line+'\n')


a = ['juice', 'melidy', 'canada']


def main():
    linesy = read_file('input.txt')
    linesy = coll(linesy)
    showw(linesy)
    write_file('output.txt', linesy)

main()


