n=int(input("Enter the Number:"));
l=len(str(n));
sum = 0;
mul = 1;
for i in range(l):
    a=n % 10;
    print(a);
    print(n);
    sum += a;
    mul *= a;
    n=int(n / 10);
    print(n);
print(mul - sum);