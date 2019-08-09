#!/usr/bin/env python

import string


class SubstitutionComponent(object):
    def __init__(self, wiring):
        assert isinstance(wiring, dict), 'wiring must be a dictonary'
        self.wiring = wiring
    def __str__(self):
        return str(self.wiring)
    def getLetterOutput(self, letterInput):
        '''
        Return the outputLetter corresponding to the inputLetter
        '''
        assert letterInput in string.ascii_letters, 'input must be a letter'
        return self.wiring[letterInput.upper())]

class Rotor(SubstitutionComponent):
    I = {'A':'E', 'B':'K', 'C':'M', 'D':'F', 'E':'L', 'F':'G', 'G':'D', 'H':'Q', 'I':'V', 'J':'Z', 'K':'N', 'L':'T', 'M':'O', 'N':'W', 'O':'Y', 'P':'H', 'Q':'X', 'R':'U', 'S':'S', 'T':'P', 'U':'A', 'V':'I', 'W':'B', 'X':'R', 'Y':'C', 'Z':'J'}
    II = {'A':'A', 'B':'J', 'C':'D', 'D':'K', 'E':'S', 'F':'I', 'G':'R', 'H':'U', 'I':'X', 'J':'B', 'K':'L', 'L':'H', 'M':'W', 'N':'T', 'O':'M', 'P':'C', 'Q':'Q', 'R':'G', 'S':'Z', 'T':'N', 'U':'P', 'V':'Y', 'W':'F', 'X':'V', 'Y':'O', 'Z':'E'}
    III = {'A':'B', 'B':'D', 'C':'F', 'D':'H', 'E':'J', 'F':'L', 'G':'C', 'H':'P', 'I':'R', 'J':'T', 'K':'X', 'L':'V', 'M':'Z', 'N':'N', 'O':'Y', 'P':'E', 'Q':'I', 'R':'W', 'S':'G', 'T':'A', 'U':'K', 'V':'M', 'W':'U', 'X':'S', 'Y':'Q', 'Z':'O'}
#    IV = {'A':'', 'B':'', 'C':'', 'D':'', 'E':'', 'F':'', 'G':'', 'H':'', 'I':'', 'J':'', 'K':'', 'L':'', 'M':'', 'N':'', 'O':'', 'P':'', 'Q':'', 'R':'', 'S':'', 'T':'', 'U':'', 'V':'', 'W':'', 'X':'', 'Y':'', 'Z':''}
    #V = {'A':'', 'B':'', 'C':'', 'D':'', 'E':'', 'F':'', 'G':'', 'H':'', 'I':'', 'J':'', 'K':'', 'L':'', 'M':'', 'N':'', 'O':'', 'P':'', 'Q':'', 'R':'', 'S':'', 'T':'', 'U':'', 'V':'', 'W':'', 'X':'', 'Y':'', 'Z':''}
    #VI = {'A':'', 'B':'', 'C':'', 'D':'', 'E':'', 'F':'', 'G':'', 'H':'', 'I':'', 'J':'', 'K':'', 'L':'', 'M':'', 'N':'', 'O':'', 'P':'', 'Q':'', 'R':'', 'S':'', 'T':'', 'U':'', 'V':'', 'W':'', 'X':'', 'Y':'', 'Z':''}
    #VII = {'A':'', 'B':'', 'C':'', 'D':'', 'E':'', 'F':'', 'G':'', 'H':'', 'I':'', 'J':'', 'K':'', 'L':'', 'M':'', 'N':'', 'O':'', 'P':'', 'Q':'', 'R':'', 'S':'', 'T':'', 'U':'', 'V':'', 'W':'', 'X':'', 'Y':'', 'Z':''}
    #VIII = {'A':'', 'B':'', 'C':'', 'D':'', 'E':'', 'F':'', 'G':'', 'H':'', 'I':'', 'J':'', 'K':'', 'L':'', 'M':'', 'N':'', 'O':'', 'P':'', 'Q':'', 'R':'', 'S':'', 'T':'', 'U':'', 'V':'', 'W':'', 'X':'', 'Y':'', 'Z':''}
    ROTOR_TYPE = {1:I, 2:II, 3:III}
    ROTOR_NOTCH = {1:'Q', 2:'E', 3:'V'}

    def __init__(self, number, ringSetting, position):
        '''
        Enigma rotor object:
        Takes the rotor number 1-8, the ring setting and the starting postition.
        '''
        assert number in ROTOR_TYPE.keys(), str('rotor number must be one of ' + (str(ROTOR_TYPE.keys())))
        self.rotorNumber = number
        self.rotorWiring = self.ROTOR_TYPE[number].copy()
        self.notch = self.ROTOR_NOTCH[number]
        assert ringSetting in string.ascii_letters, 'ringSetting must be a letter'
        self.ringSetting = ringSetting.upper()
        self.setRingSetting(self.ringSetting)
        assert position in string.ascii_letters, 'position must be a letter'
        self.position = position.upper()

    def __str__(self):
        return str(self.position) + str(self.rotorNumber)

    def setRingSetting(self, ringSetting):
        '''
        Setter to change the wiring according to the ringstellung (ring setting) on the rotor
        '''
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
        
        return self.rotorWiring(letterInput.upper())

    def setRotorPosition(self, position):
        '''
        Set the rotor position
        '''
        assert position in string.ascii_letters, 'position must be a letter'
        self.position = position.upper()

    def rotate(self):
        '''
        Advance the rotor position (self.position) by one character
        '''
        alphabet_index = string.ascii_uppercase.index(self.position)
        if alphabet_index >= (len(string.ascii_uppercase) -1):
            alphabet_index = alphabet_index % (len(string.ascii_uppercase) -1)
        self.position = string.ascii_uppercase[alphabet_index]


class Reflector(SubstitutionComponent):
    REFLECTOR_A = {'A':'Y', 'B':'R', 'C':'U', 'D':'H', 'E':'Q', 'F':'S', 'G':'L', 'H':'D', 'I':'P', 'J':'X', 'K':'N', 'L':'G', 'M':'O', 'N':'K', 'O':'M', 'P':'I', 'Q':'E', 'R':'B', 'S':'F', 'T':'Z', 'U':'C', 'V':'W', 'W':'V', 'X':'J', 'Y':'A', 'Z':'T'}
    REFLECTOR_B = {'A':'F', 'B':'V', 'C':'P', 'D':'J', 'E':'I', 'F':'A', 'G':'O', 'H':'Y', 'I':'E', 'J':'D', 'K':'R', 'L':'Z', 'M':'X', 'N':'W', 'O':'G', 'P':'C', 'Q':'T', 'R':'K', 'S':'U', 'T':'Q', 'U':'S', 'V':'B', 'W':'N', 'X':'M', 'Y':'H', 'Z':'L'}
    REFLECTOR_TYPE = {'REFLECTOR_A':REFLECTOR_A, 'REFLECTOR_B':REFLECTOR_B}
    def __init__(self, reflector):
        assert reflector in REFLECTOR_TYPE.keys(), str('reflector must be one of ' + str(REFLECTOR_TYPE.keys()))
        self.reflector = reflector
        SubstitutionComponent.__init__(self, REFLECTOR_TYPE[self.reflector])
    def __str__(self):
        return self.reflector

class Plugboard(SubstitutionComponent):
    def __init__(self, wiring):
        SubstitutionComponent.__init__(self, wiring)

class StaticRotor(SubstitutionComponent):
    STATIC_WIRING = {'A':'A', 'B':'B', 'C':'C', 'D':'D', 'E':'E', 'F':'F', 'G':'G', 'H':'H', 'I':'I', 'J':'J', 'K':'K', 'L':'L', 'M':'M', 'N':'N', 'O':'O', 'P':'P', 'Q':'Q', 'R':'R', 'S':'S', 'T':'T', 'U':'U', 'V':'V', 'W':'W', 'X':'X', 'Y':'Y', 'Z':'Z'}
    def __init__(self, wiring=STATIC_WIRING)
        SubstitutionComponent.__init__(self, wiring)
        

class Enigma(object):
    def __init__(self, plugboard_wiring, rotorL, rotorM, rotorR, reflector):
        assert isinstance(rotor_a, Rotor), 'rotor_a must be a Rotor object'
        assert isinstance(rotor_b, Rotor), 'rotor_b must be a Rotor object'
        assert isinstance(rotor_c, Rotor), 'rotor_c must be a Rotor object'
        assert isinstance(rotor_c, Reflector), 'reflector must be a reflector object'
        self.rotorL = rotorL
        self.rotorM = rotorM
        self.rotorR = rotorR

    def stepRotors(self):
        '''
        Step the right rotor by one, advance any remaining rotors that hit a notch
        '''
        
        

    def keyboardInput(self, key):
        '''        
