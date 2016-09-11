class Card(object):
    def __init__(self, num, tags, fields, score):
        self.num = num
        self.tags = tags
        self.fields = fields
        self.score = score
    def commit(self):
        database.writecard(self)
    def delete(self):
        database.removecard(self)


def getcards(carddir):
    ''' Return a list of all cards (as Card objects) in carddir '''
    cardlist = []
    i = 0
    with open(carddir, "r") as f:
        for line in f:
            if line == '' or line == '\n':
                i += 1
                continue
            card = line.split('\t')
            cardfields = {}
            for field in card[0:-1]:
                cardfields[field.split(':')[0]] = field.split(':')[1]
            tags = card[-1].split(' ')
            cardlist.append(Card(i, tags, cardfields, None))
            i += 1

    return cardlist
