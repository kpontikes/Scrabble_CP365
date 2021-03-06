import twl

def evaluate_word(word, index, spaces_before, letters, hand):
    original_hand_size = len(hand)
    # explained later in the code
    letters_search = letters + " "

    offset = spaces_before - index
    if offset < 0:
        return -1
    if offset != 0 and letters[offset-1] != ' ':
        return -1
    else:
        words_match = True
        if offset + len(word) > len(letters):
            return -1
        for i in range(0, len(word)):
            offset_i = i + offset
            if letters[offset_i] != ' ':
                if letters[offset_i] != word[i]:
                    words_match = False
                    break
            else:

                if not word[i] in hand:
                    return -1
                else:
                    letter_index = hand.index(word[i])
                    hand = hand[:letter_index] + hand[letter_index+1:]
        if words_match:
            # check if any letter from hand has been used
            if len(hand) >= original_hand_size:
                return -1

            # previously we appended a space to the letters on board, so that we don't run into
            # a non-existing index issue
            if letters_search[offset+len(word)] == ' ':
                return offset
    return -1



def anagram(boardword, hand):
    letters = boardword
    cleanstring = letters.strip()
    combo = cleanstring + hand
    combinations = list(twl.anagram(combo))

    possible_words = []

    for i in range(len(letters)):
        if letters[i] != ' ':
            spaces_before = i
            letter = letters[i]

            for word in combinations:
                letter_occurrences = [index for index, char in enumerate(word) if char == letter]
                for index in letter_occurrences:
                    offset = evaluate_word(word, index, spaces_before, letters, hand)
                    if (offset > -1):
                        possible_words.append((offset, word ))

    return list(set(possible_words))