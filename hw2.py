from serial import Serial

alphabet_to_finger = {
    'a': 5,
    'b': 2,
    'c': 3,
    'd': 3,
    'e': 3,
    'f': 2,
    'g': 2,
    'h': 7,
    'i': 8,
    'j': 7,
    'k': 8,
    'l': 9,
    'm': 7,
    'n': 7,
    'o': 9,
    'p': 9,
    'q': 5,
    'r': 2,
    's': 4,
    't': 2,
    'u': 7,
    'v': 2,
    'w': 4,
    'x': 4,
    'y': 7,
    'z': 5
}

words = [
    'hello',
    'world'
]


def build_mappings():
    fingers_to_words = {}
    for word in words:
        finger_key = ''
        for c in word:
            finger_key += str(alphabet_to_finger[c])
        if finger_key in fingers_to_words:
            fingers_to_words[finger_key].append(word)
        else:
            fingers_to_words[finger_key] = [word]
    return fingers_to_words


def main():
    usbser = Serial('/dev/cu.usbmodem1412')
    fingers_to_words = build_mappings()

    keysBuffer = []
    while True:
        line = usbser.readline().strip()
        if line[-1] == 'u':
            print(line[0])
            # depressed
            if line[0] == '1':
                # word boundary (space)
                print(fingers_to_words[''.join(keysBuffer)])
                keysBuffer = []
            else:
                keysBuffer.append(line[0])



if __name__ == '__main__':
    main()
