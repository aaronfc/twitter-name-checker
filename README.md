TwitterNameChecker
==================
Dumb script to check from command line if a Twitter account name is already registered.

Installation
------------
```
git clone https://github.com/aaronfc/twitter-name-checker
cd twitter-name-checker
python setup.py install
```

Usage
-----
```
twitter-name-check [name ...]
```

Samples
-------
```
$ twitter-check-name aaronfc
aaronfc [X]
```
```
$ twitter-check-name aaronfc github nonexistent123456
aaronfc [X]
github [X]
nonexistent123456 [V]
```

