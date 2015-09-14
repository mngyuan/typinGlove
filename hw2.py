from serial import Serial
import os

# I like never use right pinky (10) for alpha characters
# and I never use right thumb (6)
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
    # actually wordlist is filled from /usr/share/dict/words
]

keystroke_command = 'osascript -e \'tell application "System Events" to keystroke "%s"\''

def send_keystroke(c):
    os.system(keystroke_command % c)

def send_keys(word):
    for c in word:
        send_keystroke(c)
    send_keystroke(' ')
    print(word)

def build_mappings(words):
    fingers_to_words = {}
    for word in words:
        word = word.lower()
        if not word.isalpha():
            # skip weird word
            continue
        finger_key = ''
        for c in word:
            finger_key += str(alphabet_to_finger[c])
        if finger_key in fingers_to_words:
            fingers_to_words[finger_key].append(word)
        else:
            fingers_to_words[finger_key] = [word]
    return fingers_to_words

def build_wordlist():
    words = []
    with open('/usr/share/dict/words') as wordf:
        for line in wordf:
            words.append(line.strip())
    return words


def main():
    usbser = Serial('/dev/cu.usbmodem1422')
    fingers_to_words = build_mappings(build_wordlist())

    print('Ready to parse your input.')
    keysBuffer = []
    while True:
        line = usbser.readline().strip()
        if line[-1] == 'u':
            print(line[0])
            # depressed
            if line[0] == '1' or line[0] == '6':
                # word boundary (space)
                options = fingers_to_words[''.join(keysBuffer)]
                if len(options) > 1:
                    print('more than one option, picking first')
                    send_keys(options[0]) # TODO: pick for real
                else:
                    send_keys(options[0])
                keysBuffer = []
            else:
                keysBuffer.append(line[0])



if __name__ == '__main__':
    main()
