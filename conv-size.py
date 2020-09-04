#!/usr/bin/python3
import sys
initial_length={'A':1189000,'B':1456000}
root2=2**0.5
inputs = sys.argv
in_type_from = inputs[1][0]
in_type_to = inputs[2][0]
if (in_type_from != 'A' and in_type_from != 'B') or (in_type_to != 'A' and in_type_to != 'B'):
    sys.exit('error! A series or B series only!') 
else:
    length_from = initial_length[in_type_from]*((1/root2)**int(inputs[1][1:]))
    length_to = initial_length[in_type_to]*((1/root2)**int(inputs[2][1:]))
    result = (length_to/length_from)*100
    print('{before} to {after}: {result}%'.format(before=inputs[1],after=inputs[2],result=result))
