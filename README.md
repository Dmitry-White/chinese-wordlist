# chinese.py

Embarassingly simple script for converting a utf8-encoded word list into a utf8-encoded output file with the Google Translate definitions and pinyin.  This is a good starting point for building Chinese word lists.  尽管玩儿!

## Requirements

* [Google Trans](https://pypi.org/project/googletrans/)
* [tqdm/tqdm](https://github.com/tqdm/tqdm)

## Usage

```cmd
python3 chinese.py test.txt -o out.csv
```

`chinese.py` takes one positional argument: the input filename
* `-o/--output` flag specifies a file to output

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

