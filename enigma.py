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
    I = {'A': 'E', 'B': 'K', 'C': 'M', 'D': 'F', 'E': 'L', 'F': 'G', 'G': 'D', 'H': 'Q', 'I': 'V', 'J': 'Z', 'K': 'N', 'L': 'T', 'M': 'O', 'N': 'W', 'O': 'Y', 'P': 'H', 'Q': 'X', 'R': 'U', 'S': 'S', 'T': 'P', 'U': 'A', 'V': 'I', 'W': 'B', 'X': 'R', 'Y': 'C', 'Z': 'J'}
    II = {'A': 'A', 'B': 'J', 'C': 'D', 'D': 'K', 'E': 'S', 'F': 'I', 'G': 'R', 'H': 'U', 'I': 'X', 'J': 'B', 'K': 'L', 'L': 'H', 'M': 'W', 'N': 'T', 'O': 'M', 'P': 'C', 'Q': 'Q', 'R': 'G', 'S': 'Z', 'T': 'N', 'U': 'P', 'V': 'Y', 'W': 'F', 'X': 'V', 'Y': 'O', 'Z': 'E'}
    III = {'A': 'B', 'B': 'D', 'C': 'F', 'D': 'H', 'E': 'J', 'F': 'L', 'G': 'C', 'H': 'P', 'I': 'R', 'J': 'T', 'K': 'X', 'L': 'V', 'M': 'Z', 'N': 'N', 'O': 'Y', 'P': 'E', 'Q': 'I', 'R': 'W', 'S': 'G', 'T': 'A', 'U': 'K', 'V': 'M', 'W': 'U', 'X': 'S', 'Y': 'Q', 'Z': 'O'}
    IV = {'A': 'E', 'B': 'S', 'C': 'O', 'D': 'V', 'E': 'P', 'F': 'Z', 'G': 'J', 'H': 'A', 'I': 'Y', 'J': 'Q', 'K': 'U', 'L': 'I', 'M': 'R', 'N': 'H', 'O': 'X', 'P': 'L', 'Q': 'N', 'R': 'F', 'S': 'T', 'T': 'G', 'U': 'K', 'V': 'D', 'W': 'C', 'X': 'M', 'Y': 'W', 'Z': 'B'}
    V = {'A': 'V', 'B': 'Z', 'C': 'B', 'D': 'R', 'E': 'G', 'F': 'I', 'G': 'T', 'H': 'Y', 'I': 'U', 'J': 'P', 'K': 'S', 'L': 'D', 'M': 'N', 'N': 'H', 'O': 'L', 'P': 'X', 'Q': 'A', 'R': 'W', 'S': 'M', 'T': 'J', 'U': 'Q', 'V': 'O', 'W': 'F', 'X': 'E', 'Y': 'C', 'Z': 'K'}
    VI = {'A': 'J', 'B': 'P', 'C': 'G', 'D': 'V', 'E': 'O', 'F': 'U', 'G': 'M', 'H': 'F', 'I': 'Y', 'J': 'Q', 'K': 'B', 'L': 'E', 'M': 'N', 'N': 'H', 'O': 'Z', 'P': 'R', 'Q': 'D', 'R': 'K', 'S': 'A', 'T': 'S', 'U': 'X', 'V': 'L', 'W': 'I', 'X': 'C', 'Y': 'T', 'Z': 'W'}
    VII = {'A': 'N', 'B': 'Z', 'C': 'J', 'D': 'H', 'E': 'G', 'F': 'R', 'G': 'C', 'H': 'X', 'I': 'M', 'J': 'Y', 'K': 'S', 'L': 'W', 'M': 'B', 'N': 'O', 'O': 'U', 'P': 'F', 'Q': 'A', 'R': 'I', 'S': 'V', 'T': 'L', 'U': 'P', 'V': 'E', 'W': 'K', 'X': 'Q', 'Y': 'D', 'Z': 'T'}
    VIII = {'A': 'F', 'B': 'K', 'C': 'Q', 'D': 'H', 'E': 'T', 'F': 'L', 'G': 'X', 'H': 'O', 'I': 'C', 'J': 'B', 'K': 'J', 'L': 'S', 'M': 'P', 'N': 'D', 'O': 'Z', 'P': 'R', 'Q': 'A', 'R': 'M', 'S': 'E', 'T': 'W', 'U': 'N', 'V': 'I', 'W': 'U', 'X': 'Y', 'Y': 'G', 'Z': 'V'}

    ROTOR_TYPE = {1:I, 2:II, 3:III, 4:IV, 5:V, 6:VI, 7:VII, 8:VIII}
    ROTOR_NOTCH = {1:'Q', 2:'E', 3:'V', 4:'J', 5:'Z', 6:'ZM', 7:'ZM', 8:'ZM'}

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
        f = 'Rotor Number: ' + str(self.getRotorNumber()) + ' Rotor Position: ' + str(self.getRotorPosition())
        return f

    def getRotorNumber(self):
        '''
        Get the rotor number 1-8
        '''
        return self.rotorNumber


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
        
class Reflector(Rotor):
    REFLECTOR_B = {'A':'Y', 'B':'R', 'C':'U', 'D':'H', 'E':'Q', 'F':'S', 'G':'L', 'H':'D', 'I':'P', 'J':'X', 'K':'N', 'L':'G', 'M':'O', 'N':'K', 'O':'M', 'P':'I', 'Q':'E', 'R':'B', 'S':'F', 'T':'Z', 'U':'C', 'V':'W', 'W':'V', 'X':'J', 'Y':'A', 'Z':'T'}
    REFLECTOR_C = {'A':'F', 'B':'V', 'C':'P', 'D':'J', 'E':'I', 'F':'A', 'G':'O', 'H':'Y', 'I':'E', 'J':'D', 'K':'R', 'L':'Z', 'M':'X', 'N':'W', 'O':'G', 'P':'C', 'Q':'T', 'R':'K', 'S':'U', 'T':'Q', 'U':'S', 'V':'B', 'W':'N', 'X':'M', 'Y':'H', 'Z':'L'}
    ROTOR_TYPE = {'REFLECTOR_B':REFLECTOR_B, 'REFLECTOR_C':REFLECTOR_C}
    ROTOR_NOTCH = {'REFLECTOR_B':None, 'REFLECTOR_C':None}
    def __init__(self, reflector):
        super().__init__(reflector, 'A', 'A')
    def __str__(self):
        f = 'Reflector: ' + str(self.getRotorNumber())
        return f

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

    def __str__(self):
        '''
        return information about the Enigma Machine's state
        '''
        f = ('Right Rotor: ' + str(self.rotorR)
            + '\nMiddle Rotor: ' + str(self.rotorM)
            + '\nLeft Rotor: ' + str(self.rotorL)
            + '\n' + str(self.reflector))
        return f

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
        if self.rotorR.position in self.rotorR.notch:
            rotorR_notch = True
        rotorM_notch = False
        if self.rotorM.position in self.rotorM.notch:
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
        assert letter in string.ascii_uppercase, 'must be an uppercase letter'
        rotor_s = string.ascii_uppercase.index(rotor.getRotorPosition())
        letter_s = string.ascii_uppercase.index(letter)
        shift = letter_s - rotor_s 
        if shift < 0:
            shift = shift % len(string.ascii_uppercase)

        return shift
    
    def positionToLetter(self, rotor, position):
        assert position <= (len(string.ascii_uppercase) - 1)
        rotor_i = string.ascii_uppercase.index(rotor.getRotorPosition())
        shift = rotor_i + position
        if shift > (len(string.ascii_uppercase) - 1):
            shift = shift % len(string.ascii_uppercase)
        return string.ascii_uppercase[shift] 
        

    def keyboardInput(self, key):
        '''
        Enter a plaintext character and return an ciphertext character
        '''
        self.stepRotors() # step the rotor before input

        # little board mapping transposition between rotors
        # forward path
        s = self.static.produceLetterOutput(key)
        s_i = string.ascii_uppercase.index(s)
        s_l = self.positionToLetter(self.rotorR, s_i)

        r = self.rotorR.produceLetterOutput(s_l)
        r_i = self.letterToPosition(self.rotorR, r)
        r_l = self.positionToLetter(self.rotorM, r_i)
       
        m = self.rotorM.produceLetterOutput(r_l)
        m_i = self.letterToPosition(self.rotorM, m)
        m_l = self.positionToLetter(self.rotorL, m_i)

        l = self.rotorL.produceLetterOutput(m_l)
        l_i = self.letterToPosition(self.rotorL, l)
        l_l = self.positionToLetter(self.reflector, l_i)

        # reflector
        e = self.reflector.produceLetterOutput(l_l)
        e_i = self.letterToPosition(self.reflector, e)
        e_l = self.positionToLetter(self.rotorL, e_i)

        # reverse path
        l2 = self.rotorL.produceReverseOutput(e_l)
        l2_i = self.letterToPosition(self.rotorL, l2)
        l2_l = self.positionToLetter(self.rotorM, l2_i)

        m2 = self.rotorM.produceReverseOutput(l2_l)
        m2_i = self.letterToPosition(self.rotorM, m2)
        m2_l = self.positionToLetter(self.rotorR, m2_i)
        
        r2 = self.rotorR.produceReverseOutput(m2_l)
        r2_i = self.letterToPosition(self.rotorR, r2)
        r2_l = string.ascii_uppercase[r2_i]
        
        s2 = self.static.produceLetterOutput(r2_l)
        return s2
        
       
        

