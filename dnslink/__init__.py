"""Python implementation of DNSLink protocol."""

# pylint: disable=multiple-statements

import dns.resolver


def resolve(domain, protocol=None, depth=16, resolver=None):
    """
    Resolve a DNSLink TXT record.

    :param str domain: a domain to resolve
    :param str protocol: a record protocol
    :param int depth: a recursion depth
    :param dns.resolver.Resolver: a DNSPython resolver

    :return: the DNSLink records
    :rtype: list[str]
    """

    # With `_dnslink` subdomain

    if not domain.startswith('_dnslink.'): name = '_dnslink.' + domain
    else: name = domain

    records = _get_and_parse_record(name, protocol, depth, resolver)
    if records: return records

    # Without `_dnslink` subdomain

    if domain.startswith('_dnslink.'): name = domain[9:]
    else: name = domain

    records = _get_and_parse_record(name, protocol, depth, resolver)
    if records: return records

    # Not found

    return []


def _get_and_parse_record(domain, protocol=None, depth=16, resolver=None):
    """
    Get and parse DNSLink TXT record.

    :param str domain: a domain to resolve
    :param str protocol: a record protocol
    :param int depth: a recursion depth
    :param dns.resolver.Resolver: a DNSPython resolver

    :return: the DNSLink records
    :rtype: list[str]
    """

    if not isinstance(resolver, dns.resolver.Resolver):
        resolver = dns.resolver.get_default_resolver()

    try:
        answers = resolver.query(domain, 'TXT')
    except dns.exception.DNSException:
        return []

    records = []

    for rdata in answers:
        for txt in rdata.strings:
            record = txt.decode('utf-8')

            # Not valid TXT record
            if not record.count('=') == 1:
                continue

            content = record.split('/', 3)

            # Not valid DNSLink record
            if not len(content) >= 3 or not content[0] == 'dnslink=':
                continue

            # Chaining record
            if content[1] == 'dnslink' and depth > 1:
                records.extend([
                    record + ('/' + content[3] if len(content) > 3 else '')
                    for record
                    in resolve(content[2], protocol, depth - 1, resolver)
                ])

            # Normal record
            elif protocol in (content[1], None):
                content[0] = ''
                records.append('/'.join(content))

    return records
