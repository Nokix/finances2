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

if __name__ == '__main__':
    with open("../files/private/KKB-Umsätze_20220824_1547.csv", encoding="utf-8") as csv_file:
        import csv
        csv_reader = csv.reader(csv_file, delimiter=";")

        merchants = (row[3].lower() for row in list(csv_reader)[2::])

        merchants = list(set(merchants))
        merchants.sort()
        # print(merchants)

        closest_match = {m: find_closest_match(m, merchants, self_allowed=False) for m in merchants}
        # print(closest_match)

        from difflib import SequenceMatcher
        closest_match = {key: {"closest_match":value, "ratio":round(SequenceMatcher(a=key,b=value).ratio(),3)}for key, value in closest_match.items()}
        print(closest_match)

