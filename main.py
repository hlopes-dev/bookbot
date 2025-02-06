def main():
    with open("/home/hloops/workspace/bookbot/books/frankenstein.txt") as f:
        file_contents = f.read()
    
    words = len(file_contents.split())

    print(words)

if __name__ == "__main__":
    main()