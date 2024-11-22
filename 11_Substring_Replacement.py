def find_and_replace_all(original, substring, replacement):
    result = original.replace(substring, replacement)
    return result

def main():
    original = input("Enter string: ")
    substring = input("Enter substring: ")
    replacement = input("Replace with: ")
    
    result = find_and_replace_all(original, substring, replacement)

    print("Result =", result)

if __name__ == "__main__":
    main()
