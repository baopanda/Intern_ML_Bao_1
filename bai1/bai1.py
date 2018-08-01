def ktnguyento(n):
    count=0
    if(n==1):
        count+=1
    else:
        for i in range(2,n):
            if(n%i==0):
                count+=1

    if(count == 0):
        return True
    else:
        return False

if __name__ == '__main__':
    while True:
        n = int(input("Nhap so n:"))
        if(n<0):
            print("So n phai lon hon 0")
            print("Moi ban nhap lai so!")
            continue
        else:
            break

    i = 2
    kq = []
    while (i <= n):
        if (ktnguyento(i)):
            kq.append(i)
        i += 1
    print (kq)


