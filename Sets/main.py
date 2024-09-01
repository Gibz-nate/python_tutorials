def remove_duplicates(spells):
    sp = set()
    no_duplicates = []
    for spell in spells:
        sp.add(spell)
    for spe in sp:
        if spe not in no_duplicates:
            no_duplicates.append(spe)

    return no_duplicates    