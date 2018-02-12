# Josh had to install http://prolificusa.com/pl-2303hx-drivers/
#
import serial
import time

def blink(s, morse_code):
    if morse_code == " ":
        time.sleep(1.0)
    if morse_code == ".":
        s.setDTR(True) # Turns light on
        time.sleep(0.25)
        s.setDTR(False) # Turns light off
    if morse_code == "-":
        s.setDTR(True) # Turns light on
        time.sleep(0.50)
        s.setDTR(False) # Turns light off

def blink_arduino(s,morse_code):
    if morse_code == " ":
        time.sleep(1.0)
    if morse_code == ".":
        s.write(b"1") # Turns light on
        time.sleep(0.25)
        s.write(b"0") # Turns light off
    if morse_code == "-":
        s.write(b"1") # Turns light on
        time.sleep(0.50)
        s.write(b"0") # Turns light off

morsetab = {
        'A': '.-',              'a': '.-',
        'B': '-...',            'b': '-...',
        'C': '-.-.',            'c': '-.-.',
        'D': '-..',             'd': '-..',
        'E': '.',               'e': '.',
        'F': '..-.',            'f': '..-.',
        'G': '--.',             'g': '--.',
        'H': '....',            'h': '....',
        'I': '..',              'i': '..',
        'J': '.---',            'j': '.---',
        'K': '-.-',             'k': '-.-',
        'L': '.-..',            'l': '.-..',
        'M': '--',              'm': '--',
        'N': '-.',              'n': '-.',
        'O': '---',             'o': '---',
        'P': '.--.',            'p': '.--.',
        'Q': '--.-',            'q': '--.-',
        'R': '.-.',             'r': '.-.',
        'S': '...',             's': '...',
        'T': '-',               't': '-',
        'U': '..-',             'u': '..-',
        'V': '...-',            'v': '...-',
        'W': '.--',             'w': '.--',
        'X': '-..-',            'x': '-..-',
        'Y': '-.--',            'y': '-.--',
        'Z': '--..',            'z': '--..',
        '0': '-----',           ',': '--..--',
        '1': '.----',           '.': '.-.-.-',
        '2': '..---',           '?': '..--..',
        '3': '...--',           ';': '-.-.-.',
        '4': '....-',           ':': '---...',
        '5': '.....',           "'": '.----.',
        '6': '-....',           '-': '-....-',
        '7': '--...',           '/': '-..-.',
        '8': '---..',           '(': '-.--.-',
        '9': '----.',           ')': '-.--.-',
        ' ': ' ',               '_': '..--.-',
}

print("Please enter message to transmit.")
msg = input()
byte_length = len(msg)

serial_dev = "/dev/cu.usbmodem1421" # /dev/tty.usbserial-A6008cMI

arduino = True
if arduino:
    s = serial.Serial(serial_dev)  # use this line to connect to an arduino or microbit
else:
    s = serial.Serial('/dev/tty.usbserial')

s.write(b"0");

start_time = time.time()
for c in msg:
    m_code = "!"
    try:
        m_code = morsetab[c]
    except KeyError:
        print(c, "has no morse code translation, skipping.")
    if m_code != "!":
        print(c, m_code)
        for elem in m_code:
            if not arduino:
                blink(s, elem)
            else:
                blink_arduino(s,elem)
            time.sleep(0.10)
end_time = time.time()
s.close()
transmission_time = end_time - start_time
print("Message transmission time:", round(transmission_time, 2), "seconds.")
print("Data rate:", round(byte_length/transmission_time, 2), "bytes/sec.")
