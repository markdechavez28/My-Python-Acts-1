def check_word_order(word):
    sorted_word = ''.join(sorted(word))
    reversed_word = ''.join(sorted(word, reverse=True))
    
    if word == sorted_word:
        return "ALPHABETIC"
    elif word == reversed_word:
        return "REVERSE"
    else:
        return ""

def main():
    n = int(input("Enter n: "))
    words = [input() for _ in range(n)]
    
    for word in words:
        result = check_word_order(word)
        if result:
            print(f"{word}: {result}")
        else:
            print(word)

if __name__ == "__main__":
    main()
