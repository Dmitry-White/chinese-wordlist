# chinese.py

Embarassingly simple script for converting a word list (utf8 encoded) into a (utf8-encoded) output file with the Google translate definitions and the pinyin in it.  This is a good starting point for building Chinese word lists.

## Requirements

* [Google Trans](https://pypi.org/project/googletrans/)

## Usage

```cmd
python3 chinese.py words.txt > output.csv
```

__Input file:__
```
律师
法律
```

__Output file:__
```
律师,Lǜshī,lawyer
法律,Fǎlǜ,legal
```

