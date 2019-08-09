import enigma

machine = enigma.Enigma(
    enigma.Plugboard.STATIC_WIRING,
    enigma.Rotor(1, 'A', 'A'),
    enigma.Rotor(2, 'A', 'A'),
    enigma.Rotor(3, 'A', 'A'),
    enigma.Reflector('REFLECTOR_A'))

print(machine.keyboardInput('A'))
print(machine.keyboardInput('A'))
print(machine.keyboardInput('A'))
print(machine.keyboardInput('A'))
print(machine.keyboardInput('A'))
