DNSLink for Python
==================

[![version][icon-version]][link-pypi]
[![downloads][icon-downloads]][link-pypi]
[![license][icon-license]][link-license]
[![python][icon-python]][link-python]

[![linux build][icon-travis]][link-travis]
[![windows build][icon-appveyor]][link-appveyor]
[![coverage][icon-coverage]][link-coverage]
[![quality][icon-quality]][link-quality]

Python implementation of DNSLink protocol.

## Description

DNSLink is a very simple protocol to link content and services directly from DNS. DNSLink leverages the powerful distributed architecture of DNS for a variety of systems that require internet-scale mutable names or pointers. For more details see [DNSLink website][link-dnslink].

This package provides a simple way to get and resolve DNSLink TXT records for any domain name.

## Installation

### Requirements

DNSLink requires Python 3.5 or higher.

### From PyPI

The recommended way to install DNSLink is from PyPI with PIP.

```bash
pip install dnslink
```

### From Source

Alternatively, you can also install it from the source.

```bash
git clone https://github.com/filips123/DNSLinkPy.git
cd DNSLinkPy
python setup.py install
```

## Usage

You can use a `resolve` function to resolve DNSLink records for a specific domain. It first tries to resolve the domain's `_dnslink` subdomain and then fall back to the main domain if no records were found.

**Note:** To illustrate examples, we will assume that domains are using this example DNSLink configuration.

```bash
$ dig +short TXT example.com
dnslink=/ipfs/QmaYRVyPKpN8FXy9HS1t9Zhtjo4RpYXgiuNj1ins9fiLuW
dnslink=/ipns/website.ipfs.io

$ dig +short TXT foo.com
dnslink=/dnslink/bar.com

$ dig +short TXT bar.com
dnslink=/ipfs/QmaYRVyPKpN8FXy9HS1t9Zhtjo4RpYXgiuNj1ins9fiLuW
```

The function takes a domain name as a first (`domain`) argument and returns a list of all DNSLink records for that domain.


```py
import dnslink

domain = 'example.com'
records = dnslink.resolve(domain=domain)

for record in records:
    print(record)

# /ipfs/QmaYRVyPKpN8FXy9HS1t9Zhtjo4RpYXgiuNj1ins9fiLuW
# /ipns/website.ipfs.io
```

It is also possible to get only DNSLink records containing a specific protocol type. You can specify it as a second (`protocol`) argument.

```py
import dnslink

domain = 'example.com'
protocol = 'ipns'
records = dnslink.resolve(domain=domain, protocol=protocol)

for record in records:
    print(record)

# /ipns/website.ipfs.io
```

As RFC 1034 specifies, DNSLinks also supports chaining. If the record's protocol type is `dnslink`, it will try to resolve records of the domain that it is specified in it. The default recursion limit is 16. It is possible to change it with a third (`depth`) argument. When a recursion limit is reached, a record will be returned as is, without any future resolving.

```py
import dnslink

print(dnslink.resolve(domain='foo.com')[0]) # /ipfs/QmaYRVyPKpN8FXy9HS1t9Zhtjo4RpYXgiuNj1ins9fiLuW
print(dnslink.resolve(domain='foo.com', depth=1)[0]) # /dnslink/bar.com
```

You can specify a custom DNSPython resolver object as a fourth (`resolver`) argument. This can be used to provide a custom resolver configuration.

```py
import dns.resolver
import dnslink

domain = 'example.com'
resolver = dns.resolver.Resolver()
records = dnslink.resolve(domain=domain, resolver=resolver)

for record in records:
    print(record)

# /ipfs/QmaYRVyPKpN8FXy9HS1t9Zhtjo4RpYXgiuNj1ins9fiLuW
# /ipns/website.ipfs.io
```

## Versioning

This library uses [SemVer][link-semver] for versioning. For the versions available, see [the tags][link-tags] on this repository.

## License

This library is licensed under the MIT license. See the [LICENSE][link-license-file] file for details.

[icon-version]: https://img.shields.io/pypi/v/dnslink.svg?style=flat-square&label=version
[icon-downloads]: https://img.shields.io/pypi/dm/dnslink.svg?style=flat-square&label=downloads
[icon-license]: https://img.shields.io/pypi/l/dnslink.svg?style=flat-square&label=license
[icon-python]: https://img.shields.io/pypi/pyversions/dnslink.svg?style=flat-square&label=python

[icon-travis]: https://img.shields.io/travis/com/filips123/DNSLinkPy.svg?style=flat-square&label=linux+build
[icon-appveyor]: https://img.shields.io/appveyor/ci/filips123/DNSLinkPy.svg?style=flat-square&label=windows+build
[icon-coverage]: https://img.shields.io/scrutinizer/coverage/g/filips123/DNSLinkPy.svg?style=flat-square&label=coverage
[icon-quality]: https://img.shields.io/scrutinizer/g/filips123/DNSLinkPy.svg?style=flat-square&label=quality

[link-pypi]: https://pypi.org/project/dnslink/
[link-license]: https://choosealicense.com/licenses/mit/
[link-python]: https://python.org/
[link-travis]: https://travis-ci.com/filips123/DNSLinkPy/
[link-appveyor]: https://ci.appveyor.com/project/filips123/DNSLinkPy/
[link-coverage]: https://scrutinizer-ci.com/g/filips123/DNSLinkPy/code-structure/
[link-quality]: https://scrutinizer-ci.com/g/filips123/DNSLinkPy/
[link-semver]: https://semver.org/

[link-dnslink]: https://dnslink.io/

[link-tags]: https://github.com/filips123/DNSLinkPy/tags/
[link-license-file]: https://github.com/filips123/DNSLinkPy/blob/master/LICENSE
