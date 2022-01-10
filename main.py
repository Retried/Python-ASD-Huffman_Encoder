from heap import heap_enqueue, heap_dequeue


def read_file(name):
    with open(name, "r") as file:
        return file.read()


def character_count(file):
    chars_dict = dict()

    for char in file:
        if chars_dict.get(char) is None:
            chars_dict[char] = 1
        else:
            chars_dict[char] += 1

    return chars_dict


def priority_queue(chars):
    queue = []

    for char in chars:
        heap_enqueue(queue, (chars.get(char), char))

    return queue


def tree(data):
    while len(data) >= 2:
        a = heap_dequeue(data)
        b = heap_dequeue(data)

        heap_enqueue(data, (a[0] + b[0], "", a, b))

    return heap_dequeue(data)


def encode(i, binary, text, dicts):
    if i[1] != "":
        dicts.append(f'{i[1]}, {binary}')
        text = text.replace(i[1], binary)
        return text

    text = encode(i[2], binary + "0", text, dicts)
    text = encode(i[3], binary + "1", text, dicts)

    return text


def save_file(name, string):
    with open(name, "wb") as file:
        file.write(bytearray(string, "utf-8"))


if __name__ == '__main__':
    input_file = read_file("input.txt")
    char_count = character_count(input_file)
    symbols = char_count.keys()
    probabilities = char_count.values()
    enqueued_char_count = priority_queue(char_count)
    tree = tree(enqueued_char_count)
    dictionary = []

    save_file("output.bin", encode(tree, "", input_file, dictionary))

    print(f'\nCharacters: \t{char_count}')
    print(f'\nDictionary: \t{dictionary}')
    print(f'\nOutput is saved in binary format')

