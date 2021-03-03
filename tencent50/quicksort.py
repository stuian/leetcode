def swap(l,a,b):
    c = l[a]
    l[a] = l[b]
    l[b] = c

def fast_sort(a,start,end):
    if start < end : # ；老是忘记
        key = a[start]
        i = start
        j = end
        while i < j:
            while j > i and a[j] >= key:
                j -= 1
            while i < j and a[i] <= key:
                i += 1
            swap(a,i,j)
        swap(a,i,start)
        fast_sort(a,start,i-1)
        fast_sort(a,i+1,j)

if __name__ == '__main__':
    data = [3,2,4,1]
    fast_sort(data,0,3)
    print(data)