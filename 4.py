n = 2

while n <= 50:
    je_prastevilo = True
    delitelj = 2
    
    while delitelj < n:
        if n % delitelj == 0:
            je_prastevilo = False
            break
        delitelj += 1

    if je_prastevilo:
        print(n)

    n += 1
