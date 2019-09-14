import enigma

machine = enigma.Enigma(
    enigma.Plugboard.STATIC_WIRING,
    enigma.Rotor(1, 'C', 'A'),
    enigma.Rotor(2, 'A', 'A'),
    enigma.Rotor(3, 'A', 'A'),
    enigma.Reflector('REFLECTOR_A'))

#print(machine.keyboardInput('A'))
#print(machine.keyboardInput('A'))
#print(machine.keyboardInput('A'))
#print(machine.keyboardInput('A'))
#print(machine.keyboardInput('A')

def test_RotorWiring(rotor_n, rings, pos, fwd_in, rev_in, fwd_out, rev_out):
    rotor = enigma.Rotor(rotor_n, rings, pos)
    if rotor.produceLetterOutput(fwd_in) == fwd_out and rotor.produceReverseOutput(rev_in) == rev_out:
        print('Test for rotor PASS')
    else:
        print('Test for rotor FAIL')
        print('## CORRECT OUTPUT\n' + fwd_out + '\n' + rev_out + '\n## ACTUAL OUTPUT')
        print(rotor.produceLetterOutput(fwd_in))
        print(rotor.produceReverseOutput(fwd_out))

def test_letterToPosition(rotor, letter, good_out):
    t = machine.letterToPosition(rotor, letter) 
    if t == good_out:
        print('Test for wiring orientation PASS')
    else:
        print('Test for wiring orientation FAIL')
        print('## CORRECT OUTPUT\n' + str(good_out) + '\n## ACTUAL OUTPUT')
        print(t)

# std output test
test_RotorWiring(1, 'A', 'A', 'A', 'A', 'E', 'U') 

# rotor w/ ringsetting
test_RotorWiring(1, 'B', 'A', 'A', 'A', 'F', 'W') 

# test for ringsetting modulo 
test_RotorWiring(1, 'Z', 'B', 'A', 'A', 'E', 'J')

# std orientation test
test_letterToPosition(enigma.Rotor(1, 'A', 'A'), 'A', 0)
test_letterToPosition(enigma.Rotor(1, 'A', 'B'), 'A', 25)
test_letterToPosition(enigma.Rotor(1, 'A', 'Z'), 'A', 1)
test_letterToPosition(enigma.Rotor(1, 'A', 'A'), 'C', 2)
test_letterToPosition(enigma.Rotor(1, 'A', 'B'), 'C', 1)
test_letterToPosition(enigma.Rotor(1, 'A', 'Z'), 'C', 3)
