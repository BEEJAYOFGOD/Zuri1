def read_file_content(filename):
    # [assignment] Add your code here
    with open(filename) as f:
        content = f.read()
    return content


def count_words():
    contents = read_file_content("./story.txt")
    # [assignment] Add your code here
    dict = {}
    contents = contents.split()

    # Iterate over each word
    for word in contents:
        # to remove all whitespace and newline characters
        word = word.strip()
        # to convert the words to lowercase
        word = word.lower()
        # To check if word already exists in dictionary
        if word in dict:
            # if word in dict then increase occurence by 1
            dict[word] += dict[word] + 1
        else:
            # if word not in dict then occurence = 1
            dict[word] = 1

    return dict


print(count_words())
print('\n')

dict = count_words()
for key in list(dict.keys()):
    if dict[key] == 1:
        print(f'{key} occurs {dict[key]} time')
    else:
        print(key, 'occurs', str(dict[key]) + ' times')
