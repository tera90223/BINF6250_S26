import numpy as np


def cal_score(matrix, seq1, seq2, i, j, match, mismatch, gap):
    '''Calculate score for position (i,j) in scoring matrix, also record move to trace back
    
    Args:
        matrix (numpy array): scoring matrix
        seq1 (str): sequence 1
        seq2 (str): sequence 2
        i (int): current row number
        j (int): current column number
        
    Returns:
        score in position (i,j)    
        move to trace back: 0-END, 1-DIAG, 2-UP, 3-LEFT
        
    Pseudocode:
        Calculate scores based on upper-left, up, and left neighbors:
            diag_score = upper-left + (match or mismatch)
            up_score = up + gap
            left_score = left + gap
        score = max(0, diag_score, up_score, left_score)
        traceback = maximum direction or end
        
    '''
   
    # Create dictionary {'0-END': 0, '1-DIAG': 0, '2-UP': 0, '3-LEFT': 0} to track moves and scores
    score_dict = {'0-END': 0.1, '1-DIAG': 0, '2-UP': 0, '3-LEFT': 0}  # END is 0.1 so that it is always max if there are other 0 scores

    # Check if seqs match or mismatch at position (i, j) and calculate diagonal score 
    if seq1[i-1] == seq2[j-1]:  # Subtract 1 from index since matrix is one position bigger than seqs
        score_dict['1-DIAG'] = int(match + matrix[i - 1, j - 1])
    else: 
        score_dict['1-DIAG'] = int(mismatch + matrix[i - 1, j - 1])

    # Calculate up score
    score_dict['2-UP'] = int(gap + matrix[i - 1, j])

    # Calculate left score
    score_dict['3-LEFT'] = int(gap + matrix[i, j - 1])

    # Get max score and move
    move = max(score_dict, key=score_dict.get)
    score = int(score_dict[move])

    return score, move    


def traceback(seq1, seq2, traceback_matrix, maximum_position):
    '''Find the optimal path through scoring marix
        
        diagonal: match/mismatch
        up: gap in seq1
        left: gap in seq2
        
    Args:
        seq1 (str) : First sequence being aligned
        seq2 (str) : Second sequence being aligned
        traceback_matrix (numpy array): traceback matrix
        maximum_position (tuple): starting position to trace back from
        
    Returns:
        aligned_seq1 (str): e.g. GTTGAC
        aligned_seq2 (str): e.g. GTT-AC
        
    Pseudocode:
        while current_move != END:
            current_move = traceback_matrix[current_row][current_col]
            if current_move == DIAG:
                ...
            elif current_move == UP:
                ...
            elif current_move == LEFT:
                ...
            
    '''

    # Start at max position

    # Identify starting bases for seq1 (maximum_position[0]) and seq2 (maximum_position[2])

    # Access move in traceback_matrix using maximum_position
    current_move = traceback_matrix[maximum_position]
    current_row = maximum_position[0]
    current_column = maximum_position[1]

    aligned_seq1 = ''
    aligned_seq2 = ''

    # Iterate through each of the moves until we end at a "END" move (while loop)
    while current_move != '0-END':

        # current_position (row, column)
        # current_move (string)

        # If curent move is DIAG
        if current_move == '1-DIAG':

            # Extend aligned_seq1 with the corresponding base from seq1 (seq1[row]) -- account for 1 less position from matrix dimensions
            aligned_seq1 += seq1[current_row-1]

            # Extend aligned_seq2 with the corresponding base from seq2 (seq2[column])
            aligned_seq2 += seq2[current_column-1]

            # Update current_position to matrix[row-1, column-1]
            current_row -= 1
            current_column -= 1
            
        # If current move is UP
        elif current_move == '2-UP':

            # Extend aligned_seq1 with the corresponding base from seq1 (seq1[row])
            aligned_seq1 += seq1[current_row-1]

            # Extend aligned_seq2 with - (vertical gap)
            aligned_seq2 += '-'

            # Update current_position to matrix[row-1, column]
            current_row -= 1

        # If current move is LEFT
        elif current_move == '3-LEFT':

            # Extend aligned_seq1 with - (horizontal gap)
            aligned_seq1 += '-'

            # Extend aligned_seq2 with the corresponding base from seq2 (seq2[column])
            aligned_seq2 += seq2[current_column-1]

            # Update current_position to matrix[row, column-1]
            current_column -= 1

        # Update current move
        current_move = traceback_matrix[current_row][current_column]

    # Reverse aligned_seqs (so they are in order)
    ordered_aligned_seq1 = aligned_seq1[::-1]
    ordered_aligned_seq2 = aligned_seq2[::-1]

    # Return the aligned sequences 
    return ordered_aligned_seq1, ordered_aligned_seq2