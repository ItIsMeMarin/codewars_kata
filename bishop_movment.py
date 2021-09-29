letters_position = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
number_position = ['1','2','3','4','5','6','7','8']
check_board = []

colors = ('Black', 'White')

for i in range(len(letters_position)):
    position = {letter_pos : {'starting_position' : False, 'ending_position' : False, 'position_color' : None} for letter_pos in letters_position}
    check_board.append(position)

for i in range(len(check_board)):
    if (i % 2) == 0:
        index_color = 0;
    else:
        index_color = 1;
    for j in range(len(letters_position)):
        check_board[i][letters_position[j]]['position_color'] = colors[index_color]
        if index_color == 0:
            index_color = 1;
        elif index_color == 1:
            index_color = 0;
    
def bishop(start_pos, end_pos, num_moves):
    start_letter, start_number = start_pos[0], int(start_pos[1])
    end_letter, end_number = end_pos[0], int(end_pos[1])

    check_board[start_number - 1][start_letter]['starting_position'] = True
    check_board[end_number - 1][end_letter]['ending_position'] = True

    if check_board[start_number - 1 ][start_letter]['position_color'] != check_board[end_number - 1 ][end_letter]['position_color']:
        return False

    if start_pos == end_pos:
        return True

    if check_if_on_diag(start_pos , end_pos) and num_moves > 0:
        return True

    elif check_if_on_diag(start_pos , end_pos) and num_moves == 0:
        return False

    if not(check_if_on_diag(start_pos , end_pos)) and num_moves > 1:
        return True
    else:
        return False

def check_if_on_diag(start_pos, end_pos):
    all_diag_postions = []

    letter_index = letters_position.index(start_pos[0])
    number_index = number_position.index(start_pos[1])
    step = 1

    for _ in range(7):

        if not(letter_index - step < 0 or number_index + step > 7):
            top_left = letters_position[letter_index - step] + number_position[number_index+ step]
            all_diag_postions.append(top_left)
        if not(letter_index - step < 0 or number_index - step < 0):
            bottom_left = letters_position[letter_index - step] + number_position[number_index -step]
            all_diag_postions.append(bottom_left)
        if not(letter_index + step > 7 or number_index + step > 7):
            top_right =  letters_position[letter_index + step] + number_position[number_index + step]
            all_diag_postions.append(top_right)
        if not(letter_index + step > 7 or number_index - step < 0):
            bottom_right = letters_position[letter_index + step] + number_position[number_index - step]
            all_diag_postions.append(bottom_right)

        step += 1

    return end_pos in all_diag_postions

    
