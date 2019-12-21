# chinese.py

Embarassingly simple script for converting a utf8-encoded word list into a utf8-encoded output file with the Google Translate definitions and pinyin.  This is a good starting point for building Chinese word lists.  尽管玩儿!

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

