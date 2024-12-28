def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        
    word_count = count_words(file_contents)
    character_counts = count_characters(file_contents)
    character_list = convert_to_list(character_counts)

    character_list.sort(key=sort_on, reverse=True)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document")
    for character in character_list:
        if character["char"].isalpha():
            print(f"The '{character['char']}' character was found {character['num']} times")
    print("--- End report ---")     

def sort_on(entry):
    return entry["num"]


def count_words(file_contents):
    words = file_contents.split()
    word_count = 0
    for i in words:
        word_count += 1
    return word_count

def count_characters(file_contents):
    characters = {}
    for i in file_contents:
        lowered_string = i.lower()
        if lowered_string in characters:
            characters[lowered_string] = characters[lowered_string] + 1
        else:
            characters[lowered_string] = 1
    return characters

def convert_to_list(characters):
    character_list = [{"char": char, "num": count} for char, count in characters.items()]
    return character_list
if __name__ == "__main__":
    main()

