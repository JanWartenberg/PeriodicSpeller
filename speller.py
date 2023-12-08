import copy
import json
from pathlib import Path


class PeriodicTable:
    # load JSON only once
    table_path = Path(__file__).parent / "static" / "periodic-table.json"
    with open(table_path, "r") as f:
        elements = json.load(f)
    # the symbols are unique, so a dict is nicer than a pure list
    elements = {el["symbol"].lower(): el for el in elements}

    @staticmethod
    def lookup(symbol):
        return PeriodicTable.elements.get(symbol, {})


def spell_check(word):
    """determine if `inputWord` can be spelled
    with periodic table symbols;
    return array with them if so (empty array otherwise)"""

    # Iterate over the word and look for match(es)
    possible_solution = []
    ambiguity = []  # (index, possible_solution_then)
    i = 0
    while True:
        single = word[i]
        double = word[i : i + 2]

        if (
            len(double) == 2
            and double in PeriodicTable.elements
            and single in PeriodicTable.elements
        ):
            #  if both cases possible, remember the state, go on with double
            #  if we fail later, fall back to this state and continue with single
            ambiguity.append((i, copy.copy(possible_solution)))
            i += 1
            possible_solution.append(double)
        elif double in PeriodicTable.elements:
            i += 1
            possible_solution.append(double)
        elif single in PeriodicTable.elements:
            possible_solution.append(single)
        else:
            # no match
            if len(ambiguity) == 0:
                break
            else:
                #  fall back if we had a different branch earlier
                i, possible_solution = ambiguity.pop()
                possible_solution.append(word[i])

        i += 1
        if i >= len(word):
            break

    print(possible_solution)
    if "".join(possible_solution) == word:
        return possible_solution
    else:
        return []

    # def inner_check(word_part):
    #   """ TODO trying recursive approach,
    #    since multiple matches can exist - but this is still wrong """
    #   # base case -> 1 character left
    #     if len(word_part) == 1:
    #         if word_part in PeriodicTable.elements:
    #             return [word_part]
    #         else:
    #             return []
    #
    #     # TODO what about 2 characters left?
    #     # how to branch?
    #     if len(word_part) == 2:
    #         if word_part in PeriodicTable.elements:
    #             return [word_part]
    #         # else: --> try it with further recursion
    #
    #     # recurse -> check smaller sub-string
    #     #  but we need to append the results..
    #     subpart = inner_check(word_part[:-1])
    #     last = inner_check(word_part[-1])
    #     if len(subpart) == 0 or len(last) == 0:
    #         return []
    #     return subpart + last

    # def inner_check(word):
    #     """ getify's first version """
    #     if len(word) == 0:
    #         return []
    #     for symbol in PeriodicTable.elements:
    #         if len(symbol) <= len(word):
    #             # did it match the first or two chars?
    #             if word[:len(symbol)] == symbol:
    #                 # still chars left?
    #                 if len(word) > len(symbol):
    #                     res = inner_check(word[len(symbol):])
    #                     # matched successfully?
    #                     if len(res) > 0:
    #                         return [symbol] + res
    #                 else:
    #                     return [symbol]
    #     return []

    # ret = inner_check(word)
    # if "".join(ret) == word:
    #     return ret
    # else:
    #     return []


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
