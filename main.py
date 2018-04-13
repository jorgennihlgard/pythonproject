from randim import Rand 



class A:
    Correctnr = Rand.getrandom()
    print(Correctnr)
    count = 0
    while True:
        count += 1
        guess = int(input("Gissa ett nummer mellan 1 och 10\n"))
        if guess == Correctnr:
            break
        else:
            continue
    print(f"Grattis, numret var {Correctnr} Du behövde {count} gissningar")
