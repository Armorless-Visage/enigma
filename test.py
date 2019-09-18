import enigma

machine = enigma.Enigma(
    enigma.Plugboard.STATIC_WIRING,
    enigma.Rotor(1, 'A', 'A'),
    enigma.Rotor(2, 'A', 'A'),
    enigma.Rotor(3, 'A', 'A'),
    enigma.Reflector('REFLECTOR_B'))

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
        print('Test for letterToPosition PASS')
    else:
        print('Test for letterToPosition FAIL')
        print('## CORRECT OUTPUT\n' + str(good_out) + '\n## ACTUAL OUTPUT')
        print(t)

def test_positionToLetter(rotor, position, good_out):
    t = machine.positionToLetter(rotor, position) 
    if t == good_out:
        print('Test for positionToLetter PASS')
    else:
        print('Test for positionToLetter FAIL')
        print('## CORRECT OUTPUT\n' + str(good_out) + '\n## ACTUAL OUTPUT')
        print(t)

# std output test
test_RotorWiring(1, 'A', 'A', 'A', 'A', 'E', 'U') 

# rotor w/ ringsetting
test_RotorWiring(1, 'B', 'A', 'A', 'A', 'F', 'W') 

# test for ringsetting modulo 
test_RotorWiring(1, 'Z', 'A', 'A', 'A', 'E', 'J')

# std orientation test
test_letterToPosition(enigma.Rotor(1, 'A', 'A'), 'A', 0)
test_letterToPosition(enigma.Rotor(1, 'A', 'B'), 'A', 25)
test_letterToPosition(enigma.Rotor(1, 'A', 'Z'), 'A', 1)
test_letterToPosition(enigma.Rotor(1, 'A', 'A'), 'C', 2)
test_letterToPosition(enigma.Rotor(1, 'A', 'B'), 'C', 1)
test_letterToPosition(enigma.Rotor(1, 'A', 'Z'), 'C', 3)
# alt orientation test
test_positionToLetter(enigma.Rotor(1, 'A', 'A'), 0, 'A')
test_positionToLetter(enigma.Rotor(1, 'A', 'B'), 25, 'A')
test_positionToLetter(enigma.Rotor(1, 'A', 'Z'), 1, 'A')
test_positionToLetter(enigma.Rotor(1, 'A', 'A'), 2, 'C')
test_positionToLetter(enigma.Rotor(1, 'A', 'B'), 1, 'C')
test_positionToLetter(enigma.Rotor(1, 'A', 'Z'), 3, 'C')

test_positionToLetter(enigma.Rotor(1, 'A', 'B'), 0, 'B')
test_positionToLetter(enigma.Rotor(1, 'A', 'Z'), 1, 'A')


machine = enigma.Enigma(
    enigma.Plugboard.STATIC_WIRING,
    enigma.Rotor(1, 'A', 'A'),
    enigma.Rotor(2, 'A', 'A'),
    enigma.Rotor(3, 'A', 'A'),
    enigma.Reflector('REFLECTOR_B'))
print(machine)

a1 = machine.keyboardInput('A')
a2 = machine.keyboardInput('A')
a3 = machine.keyboardInput('A')

print('ENCRYPT')
print(a1)
print(a2)
print(a3)

machine = enigma.Enigma(
    enigma.Plugboard.STATIC_WIRING,
    enigma.Rotor(1, 'A', 'A'),
    enigma.Rotor(2, 'A', 'A'),
    enigma.Rotor(3, 'A', 'A'),
    enigma.Reflector('REFLECTOR_B'))

a1 = machine.keyboardInput(a1)
a2 = machine.keyboardInput(a2)
a3 = machine.keyboardInput(a3)

print('DECRYPT')
print(a1)
print(a2)
print(a3)
