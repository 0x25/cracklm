# cracklm
Crack ntlm/lm with regex 💕


Need to active md4 in /etc/ssl/openssl.cnf
```
[provider_sect]
default = default_sect
legacy = legacy_sect

[default_sect]
activate = 1

[legacy_sect]
activate = 1
```


# Help
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

# Example
```
./cracklm.py -f lm-test.txt -i patterns.txt -v
Info: Nb hash loaded: 4
Info: Nb pattern: 8
Info: pattern [pP][a@][s$][s$]w[o0]rd[0-9]{0 ...
Info: nb iteration 259 296
Info: nb threads 4
Debut :  2023-11-17 09:26:08.265307
Start [password] .. to [P@$$w0rd99@@]
>> value [P@$sword22@] ntlm [68850f5d49992ac53e6d79f93c92df81] MATCH
Fin :  2023-11-17 09:26:08.481860
Temps total :  0.2165529727935791
Info: pattern [Aa@]zerty[0-9]{0,3}[?!*$@]{0, ...
Info: nb iteration 103 323
Info: nb threads 4
Debut :  2023-11-17 09:26:08.535599
Start [Azerty] .. to [@zerty999@@]
>> value [@zerty123!$] ntlm [d156bc2e3a09e4673c61a4632464670b] MATCH
Fin :  2023-11-17 09:26:08.619338
Temps total :  0.08373904228210449
Info: pattern [zZ]erty[u]{0,1}[0-9]{0,4}[?!* ...
Info: nb iteration 1 377 764
Info: nb threads 4
Debut :  2023-11-17 09:26:09.551140
Start [zerty] .. to [Zertyu9999@@]
Fin :  2023-11-17 09:26:10.632003
Temps total :  1.0808629989624023
Info: pattern [0-9]{1,4}[Aa@]zerty[?!*$@]{0, ...
Info: nb iteration 1 033 230
Info: nb threads 4
Debut :  2023-11-17 09:26:11.125824
Start [0Azerty] .. to [9999@zerty@@]
Fin :  2023-11-17 09:26:11.767662
Temps total :  0.6418380737304688
Info: pattern 1234567[0-9]{1,3}[?!*$@]{0,2} ...
Info: nb iteration 34 410
Info: nb threads 4
Debut :  2023-11-17 09:26:11.791322
Start [12345670] .. to [1234567999@@]
>> value [123456712!!] ntlm [b585f388973b17b5ca71239503455706] MATCH
Fin :  2023-11-17 09:26:11.846948
Temps total :  0.05562591552734375
Info: pattern [0]{6,10}[?!*$@]{0,3} ...
Info: nb iteration 780
Info: nb threads 4
Debut :  2023-11-17 09:26:11.848057
Start [000000] .. to [0000000000@@@]
Fin :  2023-11-17 09:26:11.863529
Temps total :  0.015471935272216797
Info: pattern Welcome[0-9]{0,4}[?!*$@]{0,2}} ...
Info: nb iteration 344 441
Info: nb threads 4
Debut :  2023-11-17 09:26:12.047166
Start [Welcome}] .. to [Welcome9999@@}]
Fin :  2023-11-17 09:26:12.291512
Temps total :  0.24434590339660645
Info: pattern (Root|Secret|Administrator)[0- ...
Info: nb iteration 103 323
Info: nb threads 4
Debut :  2023-11-17 09:26:12.344816
Start [Root] .. to [Administrator999@@]
>> value [Secret123@!] ntlm [a921a67c4e7497f866f9aa208f19c16a] MATCH
Fin :  2023-11-17 09:26:12.434215
Temps total :  0.08939909934997559
P@$sword22@|68850f5d49992ac53e6d79f93c92df81|1
@zerty123!$|d156bc2e3a09e4673c61a4632464670b|1
123456712!!|b585f388973b17b5ca71239503455706|1
Secret123@!|a921a67c4e7497f866f9aa208f19c16a|1
```


or use hashcat ^^
