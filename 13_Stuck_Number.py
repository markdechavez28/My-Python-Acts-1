def unstuck_numbers(s):
    result = []
    i = 0
    while i < len(s):
        
        for length in [3, 2, 1]:
            if i + length <= len(s):
                num = int(s[i:i + length])
                if not result or num == result[-1] - 1:
                    result.append(num)
                    i += length
                    break
        else:
            return "Impossible"
    
    return ' '.join(map(str, result))

def main():
    s = input("Enter numbers stuck together: ")
    result = unstuck_numbers(s)
    print(result)

if __name__ == "__main__":
    main()
