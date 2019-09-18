#!/usr/bin/env python

import string

I = 'EKMFLGDQVZNTOWYHXUSPAIBRCJ'
II = 'AJDKSIRUXBLHWTMCQGZNPYFVOE'
III = 'BDFHJLCPRTXVZNYEIWGAKMUSQO'
IV = 'ESOVPZJAYQUIRHXLNFTGKDCMWB'
V = 'VZBRGITYUPSDNHLXAWMJQOFECK'
VI = 'JPGVOUMFYQBENHZRDKASXLICTW'
VII = 'NZJHGRCXMYSWBOUFAIVLPEKQDT'
VIII = 'FKQHTLXOCBJSPDZRAMEWNIUYGV'

a = (I, II, III, IV, V, VI, VII, VIII)
y = ('I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII')
b = []

for e in a:
    output_dict = {}
    for each in range(len(string.ascii_uppercase)):
        output_dict[string.ascii_uppercase[each]] = e[each]
    b.append(output_dict)

for x in range(len(y)):
    print(y[x] + ' = ' + str(b[x]))
    



