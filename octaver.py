#Lowest frequencies of musical notes within human hearing (20Hz minimum)
E = ['E',20.6]
F = ['F',21.83]
FSharp = ['F Sharp',23.12]
GFlat = ['G Flat',23.12]
G = ['G',24.5]
GSharp = ['G Sharp',25.96]
AFlat = ['A Flat',25.96]
A = ['A',27.5]
ASharp = ['A Sharp',29.14]
BFlat = ['B Flat',29.14]
B = ['B',30.87]
C = ['C',32.7]
CSharp = ['C Sharp',34.65]
DFlat = ['D Flat',34.65]
D = ['D',36.71]
DSharp = ['D Sharp',38.89]
EFlat = ['E Flat',38.89]


#Audio frequencies in Hz
frq = E  #Replace with note of choice
min_aud = 20
max_aud = 20000

#Frequency range of visible light in Hz
min_vis = 4 * 10**14
max_vis = 7.89 * 10**14

# Double audible frequency until it's in the visible light range
octaves = [frq[1]]
while octaves[-1] < min_vis:
    octaves.append(octaves[-1]*2)

# List all octaves of note in audible range
audible = []
audible.append([i for i in octaves if i <= max_aud])

# List all octaves of note above audible and below visible
supersonic = []
supersonic.append([i for i in octaves if max_aud < i < min_vis])

# Frequency of note in visible spectrum
color = int(octaves[-1])

print("Audible octaves of %s in Hz:" % frq[0])
print(audible)
print("")
print("Octaves of %s above human hearing and below visible spectrum in Hz:" % frq[0])
print(supersonic)
print("")
print("Octave of %s in visible spectrum, aka the color of note %s in Hz:" % (frq[0],frq[0]))
print(color)
print("")
