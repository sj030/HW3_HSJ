def fac(x):
    if(x <= 1):
        return 1
    else:
        return x * fac(x-1)
        
def main():
    for i in range(8):
        result = fac(2 * i)
        print(str(2*i) + ": " + str(result))




if __name__ == "__main__":
    main()
