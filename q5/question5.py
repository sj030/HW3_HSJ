def reverse_words(x):
    word = x.split()
    result = ""
    for i in range(len(word)):
        k = len(word) - i - 1
        result += word[k] +" "
    return result
        
    

def main():
    print(reverse_words("Two roads diverged in a yellow wood, And sorry I could not travel both And be one traveler, long I stood And looked down one as far as I could To where it bent in the undergrowth;"))
    


if __name__ == "__main__":
    main()
