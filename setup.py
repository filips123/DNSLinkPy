from setuptools import setup

def readme():
    with open('README.md') as f:
            return f.read()

setup(
    name = 'dnslink',
    description = 'Python implementation of DNSLink protocol',
    long_description = readme(),
    long_description_content_type='text/markdown',
    license = 'MIT',

    version_format = '{tag}',
    setup_requires = ['setuptools-git-version'],

    packages = ['dnslink'],

    entry_points = {
        'console_scripts': ['dnslink=dnslink.__main__:main'],
    },

    install_requires = [
        'dnspython>=1.0.0,<3.0.0',
    ],

    extras_require = {
        'lint': ['pylint'],
        'test': ['pytest', 'pytest-cov'],
    },

    python_requires = '>= 3.5',

    author = 'Filip Š',
    author_email = 'projects@filips.si',
    url = 'https://github.com/filips123/DNSLinkPy/',
    keywords = 'dns, dnslink, content-addressing, web3, decentralized',

    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: Name Service (DNS)',
        'Topic :: Scientific/Engineering :: Interface Engine/Protocol Translator',
        'Topic :: Security :: Cryptography',
        'Topic :: Software Development :: Libraries',
        'Topic :: Utilities',
    ],

    include_package_data = True,
)
