import sys


def main():
    script = sys.argv[0]
    option = sys.argv[1]
    inputFile = sys.argv[2]
    outputFile = sys.argv[3]

    print(f' \n script {script} wird ')
    print(f' \n mit option {option} \n ')
    print(f' input file is  "{inputFile}" ')
    print(f' output file is "{outputFile}" ')

    inf = open(inputFile, 'r')
    a = int(inf.readline())
    b = a + 1
    outf = open(outputFile, 'w')
    outf.write(str(b))
    inf.close
    outf.close


if __name__ == '__main__':
    main()
