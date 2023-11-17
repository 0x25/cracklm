#!/usr/bin/env python3
__author__      = "0x25"
__copyright__   = "GNU General Public Licence"

# https://stackoverflow.com/questions/69938570/md4-hashlib-support-in-python-3-8
import hashlib, binascii
import exrex
import os, sys, argparse
from multiprocessing import Pool
import subprocess
import multiprocessing
import time
from datetime import datetime
import itertools

defaultThread = multiprocessing.cpu_count()
defaultPattern = '[pP][a@][s$][s$]w[o0]rd[0-9]{0,2}[+;!?*$&@]{0,2}'

description ="\033[1;31m Parallel Brute Force LM hash based on regex pattern \033[0m"
epilog="\033[0;35m If you like this tool you can send me some monero \o/ { 4Ahnr36hZQsJ3P6jowXvs7cLkSVbkq2KyfQBVURYVftcj9tDoA592wT1jskroZEk2QDEZFPYMLqVvJWZHecFwQ9nL15SzRG } \033[0m"

# parse args
parser = argparse.ArgumentParser(description=description, epilog=epilog)
parser.add_argument('-t','--thread', type=int, default=defaultThread, help='Number of concurent thread')
parser.add_argument('-f','--file', help='File with one hash line by line')
parser.add_argument('-i','--pfile', help='File with one pattern line by line')
parser.add_argument('-x','--hash', help='hash')
parser.add_argument('-p','--pattern', default=defaultPattern, help='regex pattern based on exrex lib')
parser.add_argument('-v','--verbose', action='store_true', help='verbose mode')
parser.add_argument('-o','--output', help='file to save result')
parser.add_argument('-n','--password', action='store_true', help='use pattern as password not regex')

args = parser.parse_args()

def crack(job):

    values = job['values']
    hashs = job['hashs']
    result = []
    for value in values:
        hash = hashlib.new('md4', value.encode('utf-16le')).digest() #LM
        ntlm = binascii.hexlify(hash).decode()
        if ntlm in hashs:
            if verbose : 
                print('>> value [{}] ntlm [{}] MATCH'.format(value,ntlm))
            result.append("{}:{}".format(value,ntlm))

    return result

def main(args):

    hashs = []
    hash = ''
    chunk_size = 10000
    patterns = []

    if args.hash is None and args.file is None:
        print('Error: Need hash, set -f or -x')
        sys.exit()

    if args.hash is not None and args.file is not None:
        print('Error: Select -f OR -x')
        sys.exit() 

    threads = args.thread
    filename = args.file
    hash = args.hash
    nbProcess = args.thread
    pattern = args.pattern
    pfilename = args.pfile
    verbose = args.verbose
    outputfilename = args.output
    ispassword = args.password

    if filename is not None:
        if not os.path.isfile(filename):
            print('Error: file not exist')
            sys.exit()
        else:
            file = open(filename,'r')
            tmp = file.read().splitlines()
            hashs = [l.strip('\n\r').lower() for l in tmp]

    if pfilename is not None:
        if not os.path.isfile(pfilename):
            print('Error: pattern file not exist')
            sys.exit()
        else:
            file = open(pfilename,'r')
            tmp = file.read().splitlines()
            patterns = [l.strip('\n\r') for l in tmp]
            pattern = None

    if pattern is not None:
        patterns.append(pattern)

    if hash is not None:
        hashs.append(hash.lower())

    if verbose:
        print('Info: Nb hash loaded: {}'.format(len(hashs)))
        print('Info: Nb pattern: {}'.format(len(patterns)))

    out = []
    for pattern in patterns:
        
        if ispassword:
            values = [pattern]
        else:
            nb_iterration = exrex.count(pattern)  

            if verbose:
                print('Info: pattern {:.30} ...'.format(pattern))
                print('Info: nb iteration {:,}'.format(nb_iterration).replace(',',' '))
                print('Info: nb threads {}'.format(threads))

            # takes sometimes depend of your pattern 
            values = list(exrex.generate(pattern))

        tps1 = datetime.now()
        if verbose:
            print("Debut : ", tps1)
            print('Start [{}] .. to [{}]'.format(values[0],values[-1]))

        jobs = []
        for i in range(0,len(values),chunk_size):
            chunk = values[i:i + chunk_size]
            jobs.append({'values':chunk,'hashs':hashs})
        
        p = Pool(threads)
        results = p.map(crack,jobs)
        p.close()
        p.join()

        tps2 = datetime.now()
        if verbose:
            print("Fin : ", tps2)
            print("Temps total : ", datetime.timestamp(tps2)-datetime.timestamp(tps1))

        out.append(list(itertools.chain.from_iterable(results)))

    out = list(itertools.chain.from_iterable(out))
    out = mylist = list(dict.fromkeys(out))

    lines = []
    for elem in out:
        value,ntlm = elem.rsplit(':',1)
        freq = hashs.count(ntlm)
        res = "{}|{}|{}".format(value,ntlm,freq) # not perfect
        print(res)
        lines.append(res)

    if outputfilename is not None:
        f = open(outputfilename,'a')
        for line in lines:
            f.write(line + "\n")
        f.close()
    
if __name__ == "__main__":
    main(args)
    
