a = int(input("Masukan Bilangan A :"))
b = int(input("Masukan Bilangan B :"))
c = int(input("Masukan Bilangan C :"))

if a > b and a > c:
    terbesar = a
else:
    if b > c and b > a:
     terbesar = b
    else:
     terbesar = c

print("Jadi bilangan yang terbesar adalah :",terbesar)