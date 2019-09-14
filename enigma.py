#!/usr/bin/env python

import string


class SubstitutionComponent(object):
    '''
    A wiring component that substitutes one letter for another
    '''
    def __init__(self, wiring):
        assert isinstance(wiring, dict), 'wiring must be a dictonary'
        self.wiring = wiring

    def __str__(self):
        return str(self.wiring)

    def produceLetterOutput(self, letterInput):
        '''
        Return the outputLetter corresponding to the inputLetter
        '''
        assert letterInput in string.ascii_letters, 'input must be a letter'
        return self.wiring[letterInput.upper()]

    def getWiring(self):
        '''
        returns a dictionary of the wiring substitutions
        '''
        return self.wiring.copy()

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
        Takes the rotor number: 1-8 (1-3 currently)
        Ring setting: A-Z 
        Starting postition: A-Z
        '''
        assert number in self.ROTOR_TYPE.keys(), str('rotor number must be one of ' + (str(self.ROTOR_TYPE.keys())))
        self.rotorNumber = number
        self.wiring = self.ROTOR_TYPE[number].copy()
        self.notch = self.ROTOR_NOTCH[number]

        # RingSetting
        assert ringSetting in string.ascii_letters, 'ringSetting must be a letter'
        self.ringSetting = ringSetting.upper()
        self.ringSettingShift = string.ascii_uppercase.index(self.ringSetting)

        assert position in string.ascii_letters, 'position must be a letter'
        self.position = position.upper()

    def __str__(self):
        return str(self.position) + str(self.rotorNumber)

    def setRotorPosition(self, position):
        '''
        Set the rotor position
        '''
        assert position in string.ascii_letters, 'position must be a letter'
        self.position = position.upper()

    def getRotorPosition(self):
        '''
        Returns the rotor position, a letter
        '''
        return self.position

    def rotate(self):
        '''
        Advance the rotor position (self.position) by one character
        '''
        alphabet_index = string.ascii_uppercase.index(self.position)
        if alphabet_index >= (len(string.ascii_uppercase) -1):
            alphabet_index = alphabet_index % (len(string.ascii_uppercase) -1)
        alphabet_index += 1
        self.position = string.ascii_uppercase[alphabet_index]
    
    def getRingSetting(self):
        '''
        Getter for ringsetting
        '''
        return self.ringSetting
    
    def produceLetterOutput(self, letterInput):
        '''
        Return the outputLetter corresponding to the inputLetter
        '''
        assert letterInput in string.ascii_letters, 'input must be a letter'
        rawWiring = self.getWiring()
        rawOutput = rawWiring[letterInput]
        rawIndex = string.ascii_uppercase.index(rawOutput)
        ringsettingShift = string.ascii_uppercase.index(self.getRingSetting())
        outIndex = rawIndex + ringsettingShift
        if outIndex > len(string.ascii_uppercase) -1: # wrap if shift goes over z-a
            outIndex = outIndex % (len(string.ascii_uppercase) - 1)
        return string.ascii_uppercase[outIndex]

    def produceReverseOutput(self, letterInput):
        '''
        Returns the reverse path wiring output from the reflector
        letterInput should be BEFORE calulating the ringsetting
        '''
        assert letterInput in string.ascii_letters, 'input must be a letter'
        
        # reverse mapping of keys -> values to values -> keys
        rawWiring = self.getWiring()
        reverseWiring = {}
        for k in rawWiring:
            reverseWiring[rawWiring[k]] = k

        # shift ringsetting before because it operates on left side of rotor
        ringsettingShift = string.ascii_uppercase.index(self.getRingSetting())
        letterIndex = string.ascii_uppercase.index(letterInput) + ringsettingShift
        if letterIndex > len(string.ascii_uppercase) -1: # wrap if shift goes over z-a
            letterIndex = letterIndex % (len(string.ascii_uppercase) - 1)
        shiftedInput = string.ascii_uppercase[letterIndex]

        return reverseWiring[shiftedInput]
        
class Reflector(SubstitutionComponent):
    REFLECTOR_A = {'A':'Y', 'B':'R', 'C':'U', 'D':'H', 'E':'Q', 'F':'S', 'G':'L', 'H':'D', 'I':'P', 'J':'X', 'K':'N', 'L':'G', 'M':'O', 'N':'K', 'O':'M', 'P':'I', 'Q':'E', 'R':'B', 'S':'F', 'T':'Z', 'U':'C', 'V':'W', 'W':'V', 'X':'J', 'Y':'A', 'Z':'T'}
    REFLECTOR_B = {'A':'F', 'B':'V', 'C':'P', 'D':'J', 'E':'I', 'F':'A', 'G':'O', 'H':'Y', 'I':'E', 'J':'D', 'K':'R', 'L':'Z', 'M':'X', 'N':'W', 'O':'G', 'P':'C', 'Q':'T', 'R':'K', 'S':'U', 'T':'Q', 'U':'S', 'V':'B', 'W':'N', 'X':'M', 'Y':'H', 'Z':'L'}
    REFLECTOR_TYPE = {'REFLECTOR_A':REFLECTOR_A, 'REFLECTOR_B':REFLECTOR_B}
    def __init__(self, reflector):
        assert reflector in self.REFLECTOR_TYPE.keys(), str('reflector must be one of ' + str(self.REFLECTOR_TYPE.keys()))
        self.reflector = reflector
        SubstitutionComponent.__init__(self, self.REFLECTOR_TYPE[self.reflector])
    def __str__(self):
        return self.reflector

class Plugboard(SubstitutionComponent):
    STATIC_WIRING = {'A':'A', 'B':'B', 'C':'C', 'D':'D', 'E':'E', 'F':'F', 'G':'G', 'H':'H', 'I':'I', 'J':'J', 'K':'K', 'L':'L', 'M':'M', 'N':'N', 'O':'O', 'P':'P', 'Q':'Q', 'R':'R', 'S':'S', 'T':'T', 'U':'U', 'V':'V', 'W':'W', 'X':'X', 'Y':'Y', 'Z':'Z'}
    def __init__(self, wiring=STATIC_WIRING):
        SubstitutionComponent.__init__(self, wiring)

class StaticRotor(SubstitutionComponent):
    STATIC_WIRING = {'A':'A', 'B':'B', 'C':'C', 'D':'D', 'E':'E', 'F':'F', 'G':'G', 'H':'H', 'I':'I', 'J':'J', 'K':'K', 'L':'L', 'M':'M', 'N':'N', 'O':'O', 'P':'P', 'Q':'Q', 'R':'R', 'S':'S', 'T':'T', 'U':'U', 'V':'V', 'W':'W', 'X':'X', 'Y':'Y', 'Z':'Z'}
    def __init__(self, wiring=STATIC_WIRING):
        SubstitutionComponent.__init__(self, wiring)
        
class Enigma(object):
    def __init__(self, plugboard_wiring, rotorL, rotorM, rotorR, reflector):
        assert isinstance(rotorL, Rotor), 'rotorL must be a Rotor object'
        assert isinstance(rotorM, Rotor), 'rotorM must be a Rotor object'
        assert isinstance(rotorR, Rotor), 'rotorR must be a Rotor object'
        assert isinstance(reflector, Reflector), 'reflector must be a reflector object'
        self.reflector = reflector
        self.rotorL = rotorL
        self.rotorM = rotorM
        self.rotorR = rotorR
        self.static = StaticRotor() 

    def keyPress(self, keyInput):
        self.stepRotors()
        # static rotor output position
        self.static.produceLetterOutput(keyInput)

    def stepRotors(self):
        '''
        Step the right rotor by one, advance any remaining rotors that hit a notch
        '''
        # set a flag on the rotors that are on the notch letter
        rotorR_notch = False
        if self.rotorR.position == self.rotorR.notch:
            rotorR_notch = True
        rotorM_notch = False
        if self.rotorM.position == self.rotorM.notch:
            rotorM_notch = True

        self.rotorR.rotate() # always step the right rotor
        if rotorR_notch: # if the right rotor is on the notch rotate the middle rotor
            self.rotorM.rotate()
            if rotorM_notch: # if the middle rotor is also on the notch, rotate the left most rotor
               self.rotorL.rotate()

    def letterToPosition(self, rotor, letter):
        '''
        finds the position of a letter inside the enigma machine
        rotor: must be one of the 3 self rotors objects
        letter: the letter that you are trying to find the position of
        side: 0 or 1, 0 is the left side of the rotor 1 is the right
        '''
        assert isinstance(rotor, Rotor)
        assert lettter in string.ascii_uppercase, 'must be an uppercase letter'
        rotor_s = string.ascii_uppercase.index(rotor.getRotorPosition())
        letter_s = string.ascii_uppercase.index(letter)
        shift = letter_s - rotor_s 
        if shift < 0:
            shift = shift % len(string.ascii_uppercase)

        return shift
    
    def positionToLetter(self, rotor, position):
        assert isinstance(rotor, Rotor)
        assert position <= (len(string.ascii_uppercase) - 1)
        rotor_i = string.ascii_uppercase.index(rotor.getRotorPosition())
        

    def keyboardInput(self, key):
        '''
        Enter a plaintext character and return an ciphertext character
        '''
        self.stepRotors() # step the rotor before input
        # little board mapping transposition between rotors
        s = self.static.produceLetterOutput(key)
        s_i = self.letterToPosition(self.static, s)

        r = self.rotorR.produceLetterOutput(r_i)
        m = self.rotorM.produceLetterOutput(m_i)
        l = self.rotorL.produceLetterOutput(l_i)
        e = self.rotorL.produceLetterOutput(e_i)
        l2 = self.rotorL.produceLetterOutput(e)
        m2 = self.rotorM.produceLetterOutput(l2)
        r2 = self.rotorR.produceLetterOutput(m2)
        s2 = self.static.produceLetterOutput(r2)
        return s2
        
       
        

