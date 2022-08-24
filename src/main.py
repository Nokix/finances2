def find_closest_match(word, possibilities, self_allowed=True):
    from difflib import get_close_matches

    possibilities = possibilities if self_allowed else [i for i in possibilities if i != word]

    try:
        return get_close_matches(word, possibilities, n=1, cutoff=0)[0]
    except IndexError:
        print (f"The word {word} does not have any match!")
        if len(possibilities) == 0:
            print("That is because there are no possible matches left!")
        raise
