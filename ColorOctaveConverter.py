import rtmidi
import frq_to_rgb
import cv2
import numpy as np

#Lowest frequencies of musical notes within human hearing (20Hz minimum)
d = {
"E" : ['E',20.6],
"F" : ['F',21.83],
"F#" : ['F Sharp',23.12],
"G" : ['G',24.5],
"G#" : ['G Sharp',25.96],
"A" : ['A',27.5],
"A#" : ['A Sharp',29.14],
"B" : ['B',30.87],
"C" : ['C',32.7],
"C#" : ['C Sharp',34.65],
"D" : ['D',36.71],
"D#" : ['D Sharp',38.89]
}

#Audio frequencies in Hz
min_aud = 20
max_aud = 20000

#Frequency range of visible light in Hz
min_vis = 4 * 10**14
max_vis = 7.89 * 10**14

midiin = rtmidi.RtMidiIn()

def get_midi_note(midi):
    if midi.isNoteOn():
        return midi.getMidiNoteName(midi.getNoteNumber())
    elif midi.isNoteOff():
        return midi.getMidiNoteName(midi.getNoteNumber())
    elif midi.isController():
        return None

def grab_midi(m):
    note = get_midi_note(m)
    if note != None:
        note = note[:-1]
        frq = d[note]

        # Double audible frequency until it's in the visible light range
        octaves = [frq[1]]
        while octaves[-1] < min_vis:
            octaves.append(octaves[-1]*2)
        # Frequency of note in visible spectrum
        color = int(octaves[-1])
        # print(color)
        return color

def freq_to_wavelength(frq):
    c = 299792458 #speed of light
    wv = c/frq  # wavelength in meters
    wv = wv/(10**-9) # convert wavelenght to nanometers (nm)
    return wv

# code derived from:
# http://www.noah.org/wiki/Wavelength_to_RGB_in_Python
# http://www.physics.sfasu.edu/astro/color/spectra.html
def wavelength_to_rgb(wavelength, gamma=0.8):
    wavelength = float(wavelength)
    if wavelength >= 380 and wavelength <= 440:
        attenuation = 0.3 + 0.7 * (wavelength - 380) / (440 - 380)
        R = ((-(wavelength - 440) / (440 - 380)) * attenuation) ** gamma
        G = 0.0
        B = (1.0 * attenuation) ** gamma
    elif wavelength >= 440 and wavelength <= 490:
        R = 0.0
        G = ((wavelength - 440) / (490 - 440)) ** gamma
        B = 1.0
    elif wavelength >= 490 and wavelength <= 510:
        R = 0.0
        G = 1.0
        B = (-(wavelength - 510) / (510 - 490)) ** gamma
    elif wavelength >= 510 and wavelength <= 580:
        R = ((wavelength - 510) / (580 - 510)) ** gamma
        G = 1.0
        B = 0.0
    elif wavelength >= 580 and wavelength <= 645:
        R = 1.0
        G = (-(wavelength - 645) / (645 - 580)) ** gamma
        B = 0.0
    elif wavelength >= 645 and wavelength <= 750:
        attenuation = 0.3 + 0.7 * (750 - wavelength) / (750 - 645)
        R = (1.0 * attenuation) ** gamma
        G = 0.0
        B = 0.0
    else:
        R = 0.0
        G = 0.0
        B = 0.0
    R *= 255
    G *= 255
    B *= 255
    return (int(R), int(G), int(B))

# cv2 uses BGR instead of RGB
# Convert RGB to BGR
def rgb_to_bgr(RGB):
    BGR = (RGB[::-1])
    return BGR

def create_image(BGR):
    image = np.zeros((1000,1000,3), np.uint8)
    image[::] = BGR
    return image


ports = range(midiin.getPortCount())
if ports:
    for i in ports:
        print(midiin.getPortName(i))
    print("Opening port 0!")
    midiin.openPort(0)
    while True:
        m = midiin.getMessage(250)
        if m:
            color = grab_midi(m)
            if color != None:
                wavelength = freq_to_wavelength(color)
                RGB = wavelength_to_rgb(wavelength)
                BGR = rgb_to_bgr(RGB)
                image = create_image(BGR)
                cv2.imshow('Color Octave',image)
                cv2.waitKey(1)
                # cv2.destroyAllWindows()
else:
    print("NO MIDI INPUT PORTS!")
