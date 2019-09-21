from unittest.mock import patch
import dns.exception

import dnslink
import mocks


def test_resolve_any_protocol_with_subdomain_search():
    records = [[
        'dnslink=/ipfs/QmZGNUyrwwqHnaD8cgMWNUGDubny7Ro3pJ2P5yJ8LiVxMu',
        'dnslink=/zeronet/1HeLLo4uzjaLetFx6NH3PMwFP3qbRbTf3D',
        'dnslink=/foo/bar/baz',
    ]]
    dnslinks = [record.replace('dnslink=', '') for record in records[0]]

    query = mocks.query(records)

    with patch('dns.resolver.Resolver.query', query):
        assert dnslink.resolve('example.com') == dnslinks
        assert dnslink.resolve('_dnslink.example.com') == dnslinks


def test_resolve_any_protocol_without_subdomain_search():
    records = [[], [
        'dnslink=/ipfs/QmZGNUyrwwqHnaD8cgMWNUGDubny7Ro3pJ2P5yJ8LiVxMu',
        'dnslink=/zeronet/1HeLLo4uzjaLetFx6NH3PMwFP3qbRbTf3D',
        'dnslink=/foo/bar/baz',
    ]]
    dnslinks = [record.replace('dnslink=', '') for record in records[1]]

    query = mocks.query(records)

    with patch('dns.resolver.Resolver.query', query):
        assert dnslink.resolve('example.com') == dnslinks
        assert dnslink.resolve('_dnslink.example.com') == dnslinks


def test_resolve_specific_protocol():
    records = [[
        'dnslink=/ipfs/QmZGNUyrwwqHnaD8cgMWNUGDubny7Ro3pJ2P5yJ8LiVxMu',
        'dnslink=/zeronet/1HeLLo4uzjaLetFx6NH3PMwFP3qbRbTf3D',
        'dnslink=/foo/bar/baz',
    ]]
    dnslinks = [records[0][1].replace('dnslink=', '')]

    query = mocks.query(records)

    with patch('dns.resolver.Resolver.query', query):
        assert dnslink.resolve('example.com', 'zeronet') == dnslinks


def test_resolve_chaining_with_path():
    records = [
        ['dnslink=/dnslink/foo.example.com/ccc/ddd'],
        ['dnslink=/ipfs/QmZGNUyrwwqHnaD8cgMWNUGDubny7Ro3pJ2P5yJ8LiVxMu/aaa/bbb'],
    ]
    dnslinks = [records[1][0].replace('dnslink=', '') + '/ccc/ddd']

    query = mocks.query(records)

    with patch('dns.resolver.Resolver.query', query):
        assert dnslink.resolve('example.com') == dnslinks


def test_resolve_chaining_without_path():
    records = [
        ['dnslink=/dnslink/foo.example.com'],
        ['dnslink=/ipfs/QmZGNUyrwwqHnaD8cgMWNUGDubny7Ro3pJ2P5yJ8LiVxMu'],
    ]
    dnslinks = [records[1][0].replace('dnslink=', '')]

    query = mocks.query(records)

    with patch('dns.resolver.Resolver.query', query):
        assert dnslink.resolve('example.com') == dnslinks


def test_not_valid_records():
    records = [[
        'foo',
        'foo=',
        'foo=bar',
        'foo=/bar',
        'foo=/bar/baz',
        'dnslink',
        'dnslink=',
        'dnslink=foo',
        'dnslink=/foo',
    ]]
    dnslinks = []

    query = mocks.query(records)

    with patch('dns.resolver.Resolver.query', query):
        assert dnslink.resolve('example.com') == dnslinks


def test_resolve_no_records():
    records = [[]]
    dnslinks = []

    query = mocks.query(records)

    with patch('dns.resolver.Resolver.query', query):
        assert dnslink.resolve('example.com') == dnslinks


def test_resolve_dns_exception():
    query = lambda _, __, ___: (_ for _ in ()).throw(dns.exception.DNSException())

    with patch('dns.resolver.Resolver.query', query):
        assert dnslink.resolve('example.com') == []
