def find_closest_match(word, possibilities, self_allowed=True):
    from difflib import get_close_matches

    possibilities = possibilities if self_allowed else [i for i in possibilities if i != word]

    try:
        return get_close_matches(word, possibilities, n=1, cutoff=0)[0]
    except IndexError:
        print (f"The word {word} does not have any match!")
        if len(possibilities) == 0:
            print("That is because there are no possible matches left!")
        raise IndexError

from dataclasses import dataclass
import datetime as dt


@dataclass
class Invoice:
    date: dt
    amount: float
    category: str
    text: str


if __name__ == '__main__':
    with open("../files/private/KKB-Umsätze_20220824_1547.csv", encoding="utf-8") as csv_file:
        import csv
        csv_reader = csv.reader(csv_file, delimiter=";")

        # merchants = (row[3].lower() for row in list(csv_reader)[2::])

        # merchants = list(set(merchants))
        # merchants.sort()
        # print(merchants)

        # closest_match = {m: find_closest_match(m, merchants, self_allowed=False) for m in merchants}
        # print(closest_match)

        # from difflib import SequenceMatcher
        # closest_match = {key: {"closest_match":value, "ratio":round(SequenceMatcher(a=key,b=value).ratio(),3)}for key, value in closest_match.items()}
        # print(closest_match)

        items = list()
        for row in list(csv_reader)[2::]:
            new_item = Invoice(date=dt.datetime.strptime(row[1],"%d.%m.%Y"),
                               amount=float(row[8].replace(",",".")),
                               text=row[3],
                               category=row[4])
            print()
            print(f"Date: {new_item.date}, Amount: {new_item.amount},")
            print(f"{new_item.text}")
            print(f"Expected category: {new_item.category}")
            x = input("Is this correct? (enter for yes, ? for other catgories, otherwise type in new category)")

            import re
            if(len(x)==0):
                pass
            elif(re.search("\?",x)):
                # show categories
                categories = set((item.category for item in items))
                categories = {i:item for item, i in zip(categories, range(len(categories)))}
                print(categories)
                y = int(input("Which item?"))
                categories = categories[y]

            else:
                new_item.category = x

            print(new_item)
            items.append(new_item)

        print(items)
