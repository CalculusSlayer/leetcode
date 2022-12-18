from collections import defaultdict, Counter

def dict_test():
    a = "aabcd"
    b = "abce"

    a = Counter(a)
    b = Counter(b)
    print(a, b, sep='\n')

    c = a - b 
    print(Counter(b)-Counter(b))
    print(c)

def main():
    dict_test()

if __name__ == '__main__':
    main()