eps = 1e-5
x = 1 + eps
while x > 1:
    x = 1 + eps
    eps = eps / 2
    print(eps)
print("WYNIK: " + str(eps))