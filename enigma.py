#!/usr/bin/env python

import string

class Rotor:
    I = {'A':'E', 'B':'K', 'C':'M', 'D':'F', 'E':'L', 'F':'G', 'G':'D', 'H':'Q', 'I':'V', 'J':'Z', 'K':'N', 'L':'T', 'M':'O', 'N':'W', 'O':'Y', 'P':'H', 'Q':'X', 'R':'U', 'S':'S', 'T':'P', 'U':'A', 'V':'I', 'W':'B', 'X':'R', 'Y':'C', 'Z':'J', 'notch':'Q'}
    II = {'A':'A', 'B':'J', 'C':'D', 'D':'K', 'E':'S', 'F':'I', 'G':'R', 'H':'U', 'I':'X', 'J':'B', 'K':'L', 'L':'H', 'M':'W', 'N':'T', 'O':'M', 'P':'C', 'Q':'Q', 'R':'G', 'S':'Z', 'T':'N', 'U':'P', 'V':'Y', 'W':'F', 'X':'V', 'Y':'O', 'Z':'E', 'notch':'E'}
    III = {'A':'B', 'B':'D', 'C':'F', 'D':'H', 'E':'J', 'F':'L', 'G':'C', 'H':'P', 'I':'R', 'J':'T', 'K':'X', 'L':'V', 'M':'Z', 'N':'N', 'O':'Y', 'P':'E', 'Q':'I', 'R':'W', 'S':'G', 'T':'A', 'U':'K', 'V':'M', 'W':'U', 'X':'S', 'Y':'Q', 'Z':'O', 'notch':'V'}
#    IV = {'A':'', 'B':'', 'C':'', 'D':'', 'E':'', 'F':'', 'G':'', 'H':'', 'I':'', 'J':'', 'K':'', 'L':'', 'M':'', 'N':'', 'O':'', 'P':'', 'Q':'', 'R':'', 'S':'', 'T':'', 'U':'', 'V':'', 'W':'', 'X':'', 'Y':'', 'Z':''}
    #V = {'A':'', 'B':'', 'C':'', 'D':'', 'E':'', 'F':'', 'G':'', 'H':'', 'I':'', 'J':'', 'K':'', 'L':'', 'M':'', 'N':'', 'O':'', 'P':'', 'Q':'', 'R':'', 'S':'', 'T':'', 'U':'', 'V':'', 'W':'', 'X':'', 'Y':'', 'Z':''}
    #VI = {'A':'', 'B':'', 'C':'', 'D':'', 'E':'', 'F':'', 'G':'', 'H':'', 'I':'', 'J':'', 'K':'', 'L':'', 'M':'', 'N':'', 'O':'', 'P':'', 'Q':'', 'R':'', 'S':'', 'T':'', 'U':'', 'V':'', 'W':'', 'X':'', 'Y':'', 'Z':''}
    #VII = {'A':'', 'B':'', 'C':'', 'D':'', 'E':'', 'F':'', 'G':'', 'H':'', 'I':'', 'J':'', 'K':'', 'L':'', 'M':'', 'N':'', 'O':'', 'P':'', 'Q':'', 'R':'', 'S':'', 'T':'', 'U':'', 'V':'', 'W':'', 'X':'', 'Y':'', 'Z':''}
    #VIII = {'A':'', 'B':'', 'C':'', 'D':'', 'E':'', 'F':'', 'G':'', 'H':'', 'I':'', 'J':'', 'K':'', 'L':'', 'M':'', 'N':'', 'O':'', 'P':'', 'Q':'', 'R':'', 'S':'', 'T':'', 'U':'', 'V':'', 'W':'', 'X':'', 'Y':'', 'Z':''}
    ROTOR_TYPE = {1:I, 2:II, 3:III}
    def __init__(self, number, ringSetting):
        '''
        Enigma rotor object:
        Takes the rotor number 1-8, the ring setting and the starting postition.
        '''
        self.rotorWiring = self.ROTOR_TYPE[number].copy()
        self.ringSetting = ringSetting
        self.setRingSetting(self.ringSetting)

    def __str__(self):
        return str(self.rotorWiring)

    def setRingSetting(self, ringSetting):
        # Set the new rotor wiring based on ringSetting
        assert ringSetting in string.ascii_letters
        wiring = self.rotorWiring.copy()
        vals = list(wiring.values())
        alphabet = string.ascii_uppercase
        index = alphabet.index(ringSetting)
        newWiring = vals[index:] + vals[:index] # shift the output letters
        for i in range(len(wiring)):
            wiring[i] = newWiring[i]
        self.rotorWiring = newWiring # set the new wiring
        
    def getLetterOutput(self, letterInput):
        return self.rotorWiring(letterInput)
        
        
