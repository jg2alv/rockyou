# rockyou

Combination-based password generator.

### Usage

Optional arguments:

* `-p` (`--path`): Specifies the path where the file will be saved into and where temp files (deleted on demand) will be created (defaults to `$PWD`).
* `-f` (`--file`): Specifies the end file name (defaults to `rockyou.txt`)
* `-l` (`---disable-lowercase`): If given, the script will not use lowercase letters, from the character set, on password generation (used characters, if given: `*.?@#$ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789`)
* `-U` (`---disable-uppercase`): If given, the script will not use uppercse letters, from the character set, on password generation (used characters, if given: `*.?@#$abcdefghijklmnopqrstuvwxyz0123456789`)
* `-n` (`---disable-numbers`): If given, the script will not use numbers, from the character set, on password generation (used characters, if given: `*.?@#$abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ`)
* `-c` (`---disable-special-chars`): If given, the script will not use special characters, from the character set, on password generation (used characters, if given: `abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789`)
* `-d` (`---disable-chars`): If used, the script will not use the given characters, from the character set, on password generation (format: `abcdefgh`)
* `-C` (`--character-set`): If used, the script will only use the given characters (format: `abcdefgh`)
* `-m` (`---min-length`): Minimum password length (default: 4)
* `-m` (`---max-length`): Maximum password length (default: 16)
* `-s` (`--separator`): Character to split combinations (defaults to a comma)
* `---estimate-size`: Prints the hard-disk storage size the end-file will consume (units depend on the ammount of bytes. They're auto-converted up to yottabytes) and exits
* `---estimate-time`: Prints the time the script would take to generate all constraint-respecting passwords (units depend on the ammount of seconds. They're auto-converted up to milleniums) and exits. Note that this depends upon the device in which the script is running (RAM, CPU, etc)
* `---estimate-ammount`: Prints the number of (different) password combinations that can be generated (based on given constraints) and exits
* `-e` (`--estimate`): Alias to `---estimate-size ---estimate-time ---estimate-ammount`
* `--prefix`: Add the given prefix to all generated passwords. That's useful when one knows one or more of the starting characters of a password
* `--suffix`: Add the given suffix to all generated passwords. That's useful when one knows one or more of the ending characters of a password


Examples:
```shell
$ python3 app.py -m 4 -M 4 -lUc # generates all 4 digit combinations possible (from 0000 to 9999)
$ python3 app.py -m 8 -M 8 -U -c # generates all combinations with lowercase letters (a-z) and numbers (0-9). i.e a1b2c3d4 will be among them
$ python3 app.py -e # prints the number of different combinations that can be generated, the hard-disk storage space and time required to finish password generation
$ python3 app.py ---estimate-ammount # will print 212117604223062189336279045376 and exit
$ python3 app.py -m 1 -M 2 -lUc --prefix 00 # will generate all 2 digit passwords possible -which will start with 00 (e.g 0001, 0002, 0003, 0004, etc)
$ python3 app.py -m 1 -M 2 -lUc --suffix 00 # will generate all 2 digit passwords possible -which will end in 00 (e.g 0100, 0200, 0300, 0400, etc)
```

### Dependencies

There are no dependencies. The script uses only Python3 built-in modules.
