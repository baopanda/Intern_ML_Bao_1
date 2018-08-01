import time
start = time.time()
def sum(n):
    tong = 0
    for i in range(1, n + 1):
        tong += i
    return tong

if __name__ == '__main__':
    while True:
        n = int(input("Nhap so n:"))
        if(n<0):
            print("So n phai lon hon 0")
            print("Moi ban nhap lai so!")
            continue
        else:
            break
    print(sum(n))
    print('Entire job took:', time.time() - start)