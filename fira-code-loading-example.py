from time import sleep

length = 50

for i, wheel in zip(range(0,length+1), "\uee06\uee07\uee08\uee09\uee0a\uee0b"*length):
    if i == 0:
        print("\uee00", end="")
    else:
        print("\uee03", end="")

    for j in range(1, length-1):
        if i <= j:
            print("\uee01", end="")
        else:
            print("\uee04", end="")

    if i == length:
        print("\uee05", end="", flush=True)
    else:
        print("\uee02", end="", flush=True)

    print(f" {wheel} ", end="", flush=True)
    sleep(0.1)
    print("\r", end="", flush=True)
