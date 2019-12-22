# chinese.py

Embarassingly simple script for converting a word list (utf8 encoded) into a (utf8-encoded) output file with the Google translate definitions and the pinyin in it.  This is a good starting point for building Chinese word lists.

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

