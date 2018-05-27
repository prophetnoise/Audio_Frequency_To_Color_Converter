# Audio_Frequency_To_Color_Converter

Instructions for two different versions below. 
First is a real time converter of MIDI note to its octave color. 
Second is a manual version where you assign a variable to a note name.

========================================================================================================

1
Real Time Converter: ColorOctaveConverter.py
Real Time Converter MIDI Note to audio frequency, to its literal octave frequency in the visible light spectrum and displays color.

1- On a Mac open Audio MIDI Setup.
2-In Audio Midi Setup go to Window > Show MIDI Studio
3-In the MIDI Studio, enable on your IAC Driver (Device on checked, add port Bus 1, MIDI in 1, MIDI out 1)

4- Open Ableton Live
5- Ableton preferences > Link MIDI > MIDI Ports > Output: IAC Driver (Bus 1) Track: ON, Sync: ON, Remote:ON
6-Create a new MIDI track and populate clips with MIDI notes and add an Ableton Instrument > External Instrument to this track.
7-On External Instrument set MIDI To dropdown menu to IAC Driver (Bus 1), Ch. 1 (All other parameters ignored)

8- Run Python Script 
$ python3 ColorOctaveConverter.py

9-Script will display MIDI port is open. 
10- Press play in Ableton. 


=================================================================================================================

2
Manual Conversion by updating variable with note name
display_color.py
frq_to_rgb.py
octaver.py

Converts musical note to corresponding frequency in visible spectrum and displays color

Select the musical note you want in octaver.py where commented to do so and save. (A through GSharp)
Run display_color.py:
  $ python3 display_color.py

octaver.py calculates all octaves of that note. It prints the frequencies of those octaves in the human hearing range, all frequencies above the human hearing range, and the frequency of the octave within the visible spectrum.

frq_to_rgb.py imports the visible freqency octave from octaver.py, converts it to wavelength, and then converts the wavelength to an RGB value. 

display_color.py imports the RGB value from frq_to_rgb.py and displays that color in a window on the screen.
