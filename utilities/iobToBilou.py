
def iob_scheme_to_bilou(file):
    from spacy.gold import iob_to_biluo
    import csv

    iob_tags = []
    for line in open(file, 'r').read().splitlines():
        if len(line) > 0:
            iob_tags.append(line.split()[1])
        else:
            iob_tags.append('*')

    print(iob_tags)
    bilou_tags = iob_to_biluo(iob_tags)
    print(bilou_tags)

    r = csv.reader(open(file, 'r'), delimiter='\t', quoting=csv.QUOTE_NONE)
    lines = list(r)
    print(lines)
    for index, line in enumerate(lines):
        if len(line) > 0:
            line[1] = bilou_tags[index]
        print(line)
    writer = csv.writer(open('output.tsv', 'w'), delimiter='\t')
    writer.writerows(lines)





