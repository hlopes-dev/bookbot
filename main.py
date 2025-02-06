def main():
    with open("/home/hloops/workspace/bookbot/books/frankenstein.txt") as f:
        file_contents = f.read()
    counter_for_words = len(file_contents.split())
    print(str(counter_for_words) + " words found in the document")
    lowered_str = file_contents.lower()
    counter_for_chars = {}
    list_of_dicts = []

    for c in lowered_str:
        if c not in counter_for_chars:
            counter_for_chars[c] = 1
        else:
            counter_for_chars[c] += 1
    
    for char, count in counter_for_chars.items():
        if char.isalpha():
            list_of_dicts.append({"name": char, "num": count})    

    list_of_dicts.sort(reverse=True, key=sort_on)
    for s in list_of_dicts:
        print("The '"+ s["name"] + "' character was found "+str(s["num"])+" times" )
    
 

def sort_on(dict):
    return dict["num"]
if __name__ == "__main__":
    main()