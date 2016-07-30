#!/usr/bin/python
'''
import f1
print ('that is import file')
#search.py
import argparse
parser = argparse.ArgumentParser(description='Search some file')

parser.add_argument(dest='filename', metavar='filename', nargs='*')

parser.add_argument('-p', '--pat', metavar='parttern', reqired=True,
                    dest='parttern', action='append',
                    help='text pattern to search for')
parser.add_argument('-v', dest='verbose', action='store_true',
                    help='verbose mode')
parser.add_argument('-o', dest='outfile', action='store'
                    help='output file')
parser.add_argument('--speed', dest='speed', action='store',
                    help='search speed')
args = parser.parse_args()
print(args.filename)
print(args.parttern)
print(args.verbose)
print(args.outfile)
print(args.speed)
'''
import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='an integer for the accumulator')
parser.add_argument('--sum', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='sum the integers (default: find the max)')

args = parser.parse_args()
print(args.accumulate(args.integers))
