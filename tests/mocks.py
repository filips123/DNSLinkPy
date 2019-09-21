from dns.rdtypes.ANY.TXT import TXT


def query(records):
    context = {}
    context['i'] = -1

    def mockable(_, __, ___):
        if context['i'] + 1 < len(records):
            context['i'] += 1

        rdclass = 1
        rdtype = 1
        strings = records[context['i']]

        return [
            TXT(rdclass, rdtype, strings)
        ]

    return mockable
