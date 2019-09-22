"""Example for DNSLink protocol."""

import dnslink


def main():
    """Handle example."""

    # Resolve any DNSLink record of domain
    records = dnslink.resolve('ipfs.io')
    print('\n'.join(records))

    # Resolve IPFS DNSLink record of domain
    records = dnslink.resolve('libp2p.io', 'ipfs')
    print('\n'.join(records))


if __name__ == '__main__':
    main()
