# cracklm
crack ntlm/lm with regex 💕

```
usage: cracklm.py [-h] [-t THREAD] [-f FILE] [-i PFILE] [-x HASH] [-p PATTERN] [-v] [-o OUTPUT] [-n]

 Parallel Brute Force LM hash based on regex pattern

options:
  -h, --help            show this help message and exit
  -t THREAD, --thread THREAD
                        Number of concurent thread
  -f FILE, --file FILE  File with one hash line by line
  -i PFILE, --pfile PFILE
                        File with one pattern line by line
  -x HASH, --hash HASH  hash
  -p PATTERN, --pattern PATTERN
                        regex pattern based on exrex lib
  -v, --verbose         verbose mode
  -o OUTPUT, --output OUTPUT
                        file to save result
  -n, --password        use pattern as password not regex
```

or use hashcat ^^
