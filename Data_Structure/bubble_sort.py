def bubble_sort(a):
    for i in range(0, len(a)):
        for j in range (0, len(a)-i-1):
            if (a[j]>a[j+1]):
                a[j],a[j+1] = a[j+1], a[j]

if __name__ == '__main__':
    a = [2,9,7,17,10,8]
    bubble_sort(a)
    print(a)
