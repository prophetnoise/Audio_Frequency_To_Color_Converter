# Audio_Frequency_To_Color_Converter
Converts musical note to corresponding frequency in visible spectrum and displays color

Select the musical note you want in octaver.py where commented to do so and save. (A through GSharp)
Run display_color.py:
  $ python3 display_color.py

octaver.py calculates all octaves of that note. It prints the frequencies of those octaves in the human hearing range, all frequencies above the human hearing range, and the frequency of the octave within the visible spectrum.

frq_to_rgb.py imports the visible freqency octave from octaver.py, converts it to wavelength, and then converts the wavelength to an RGB value. 

display_color.py imports the RGB value from frq_to_rgb.py and displays that color in a window on the screen.
