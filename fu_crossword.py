""" Module to work with crosswords"""

def read_crossword(path):
    """
    str -> list[tuple[str, tuple[int,int]]]
    read file and return list with tuples with letter and tuple with its coordinats
    e.g (y,(1,1)) first coordinat is collumn second row number
    >>> read_crossword('crossword_3_2.txt')
    [('o', ('0', '1')), ('i', ('1', '1')), ('k', ('2', '1')), ('l', ('4', '1')), ('g', ('6', '1')),\
 ('y', ('7', '1')), ('p', ('0', '3')), ('m', ('2', '3')), ('n', ('5', '3')), ('s', ('0', '5')),\
 ('h', ('1', '5')), ('a', ('2', '5')), ('c', ('1', '4')), ('e', ('1', '7')), ('u', ('6', '5'))]
    """
    list_with_tuples = []
    with open(path, 'r', encoding='utf-8') as file:
        full_list = []
        for line in file:
            full_list.append(line.split())
    for current_letter_number in range(0, len(full_list),2):
        letter = full_list[current_letter_number][0]
        coords = full_list[current_letter_number+1][0]
        for cur_position in range(0, len(coords[0]), 2):
            list_with_tuples.append((letter, (coords[cur_position], coords[cur_position+1])))
    return list_with_tuples

# print(read_crossword('crossword_3_2.txt'))

def crossword_words(crossword):
    """
    Return the list of shortests words that sre on horizontal in crossword
    Crosword is givven as list of tuples with letter and ots coordinates
    >>> crossword_words([('o', ('0', '1')), ('i', ('1', '1')), ('k', ('2', '1')),\
 ('l', ('4', '1')), ('g', ('6', '1')), ('y', ('7', '1')), ('p', ('0', '3')), ('m', ('2', '3')),\
 ('n', ('5', '3')), ('s', ('0', '5')), ('h', ('1', '5')), ('a', ('2', '5')), ('c', ('1', '4')),\
 ('e', ('1', '7')), ('u', ('6', '5'))])
    ['shay', 'pomp']
    """
    crossword_list_2 = [[]]
    for _ in range(8):
        crossword_list_2.append([])
        for _ in range(8):
            crossword_list_2.append([])
    for current_letter in crossword:
        crossword_list_2[current_letter[1][1]][current_letter[1][0]] = current_letter[0]
    for i in range(8):
        current_row_words = (','.join(crossword_list_2[i])).replace(',', '')
        list_with_row_words = current_row_words.strip().split()
    minimum_len = 8
    for word in list_with_row_words:
        minimum_len = min(minimum_len, len(word))
    result = []
    for word in list_with_row_words:
        if len(word) > 2:
            if len(word) == minimum_len:
                result.append(word)
    return result
