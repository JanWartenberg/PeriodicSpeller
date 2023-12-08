import json


class PeriodicTable:
    # load JSON only once
    with open("./static/periodic-table.json", "r") as f:
        elements = json.load(f)
    # the symbols are unique, so a dict is nicer than a pure list
    elements = {el['symbol'].lower(): el for el in elements}

    @staticmethod
    def lookup(symbol):
        return PeriodicTable.elements.get(symbol, {})

    @staticmethod
    def symbols():
        return list(PeriodicTable.elements.keys())


def spell_check(word):
    """determine if `inputWord` can be spelled
    with periodic table symbols;
    return array with them if so (empty array otherwise)"""

    # naive: Iterate over the word and look for match
    # TODO but: recursive/pathfinding approach might be needed,
    #   if multiple matches exist
    possible_solution = []
    i = 0
    while True:
        single = word[i]
        double = word[i:i+2]

        i += 1
        if double in PeriodicTable.symbols():
            i += 1
            possible_solution.append(double)
        elif single in PeriodicTable.symbols():
            possible_solution.append(single)
        else:
            break

        if i >= len(word):
            break

    print(possible_solution)
    if "".join(possible_solution) == word:
        return possible_solution
    else:
        return []


def check(word):
    word = str.lower(word).strip()
    # validate the input
    if not word.isalpha() or len(word) < 3:
        return "Enter a word at least 3 letters long!"
    # try to spell word
    symbols = spell_check(word)

    if len(symbols) > 0:
        elements = []
        for symbol in symbols:
            elements.append(PeriodicTable.lookup(symbol))
        return elements
    return "Konnte es nicht buchstabieren."
