from unittest.mock import patch
import sys
import io

from dnslink.__main__ import main
import mocks


def test_command_program_resolve():
    records = [[
        'dnslink=/ipfs/QmZGNUyrwwqHnaD8cgMWNUGDubny7Ro3pJ2P5yJ8LiVxMu',
        'dnslink=/zeronet/1HeLLo4uzjaLetFx6NH3PMwFP3qbRbTf3D',
        'dnslink=/foo/bar/baz',
    ]]
    dnslinks = [record.replace('dnslink=', '') for record in records[0]]

    argv = ['dnslink', 'resolve', 'example.com']
    stdout = io.StringIO()
    query = mocks.query(records)

    with patch.object(sys, 'argv', argv), patch('sys.stdout', stdout), patch('dns.resolver.Resolver.query', query):
        main()

    assert stdout.getvalue().strip().split('\n') == dnslinks
