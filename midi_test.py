import midi_conversion
from midi_plotter import plot_midi, play_midi, plot_num_seq
from midi_note import Note
import numpy as np

notes_np = midi_conversion.convert_midi_to_numpy("maestro-v2.0.0/2008/MIDI-Unprocessed_04_R1_2008_01-04_ORIG_MID--AUDIO_04_R1_2008_wav--4.midi", ticks_per_beat=12) #convert midi to numpy
note_seq = midi_conversion.convert_matrix_to_word_seq(notes_np)
num_seq = midi_conversion.convert_to_number_seq(note_seq)
midi_conversion.convert_num_seq_to_midi(num_seq,output_name="NUM SEQ2")
#note_seq_alt = midi_conversion.convert_matrix_to_word_seq_alt(notes_np)
#print(note_seq[:20])
#print(note_seq_alt[:20])

print(np.unique(num_seq))

print()
"""
plot_midi(notes_np, seq_length=100, filename="vector")
plot_num_seq(num_seq, 100, filename="num_seq")


#plot_midi(notes_np,seq_length = 100,show_plot = True)
print()

"""

rem = "n33 d0 n110 d103 n0 d80 n126 xxnscls d39 xxnscls d85 n16 d74 n108 d105 n80 d103 dummy1 dummy1 d84 n60 d32 xxmask d109 n18 d92 n91 xxpad n1 dummy1 dummy1 dummy1 d62 n110 d97 n37 xxnscls d158 n40 d12 n45 d85 n63 dummy1 d160 n41 d44 dummy1 d152 n28 d103 n74 d85 n8 d27 n69 d97 n34 d100 n1 d0 n121 d0 n114 d115 n28 d97 n19 d160 n96 d109 n63 d121 n24 d57 n14 d151 n28 d83 n126 d56 dummy1 d109 n126 d32 n110 d103 n110 d115 n34 d109 n48 d86 n18 d78 n91 d85 n12 d74 n108"
rem = rem.split(" ")



#12 times per quarter note


#subset = notes_np[:1024]

t = np.array([[[str(d)+","+str(i)+str(e) for i in range(65,69)] for e in range(3)] for d in range(5)])
print("shape",t.shape)
print("FUCK")
t = np.reshape(t,(5,3,-1))
print("final")
print(t)


#print(subset)

#plot_midi(notes_np, filename="midi_plot")

#midi_conversion.convert_numpy_to_midi(notes_np, output_name = "midi_exported.midi", upscale = 1) #convert np to midi
# play_midi("midi_exported.midi")


