def main():
    with open("/home/hloops/workspace/bookbot/books/frankenstein.txt") as f:
        file_contents = f.read()
    
    lowered_str = file_contents.lower()
    counter_for_chars = {}
    
    for c in lowered_str:
        if c not in counter_for_chars:
            counter_for_chars[c] = 1
        else:
            counter_for_chars[c] += 1

    print(counter_for_chars)    

if __name__ == "__main__":
    main()