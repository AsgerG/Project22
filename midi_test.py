import midi_conversion
from midi_plotter import plot_midi, play_midi, plot_num_seq
from midi_note import Note
import numpy as np

notes_np = midi_conversion.convert_midi_to_numpy("maestro-v2.0.0/2008/MIDI-Unprocessed_04_R1_2008_01-04_ORIG_MID--AUDIO_04_R1_2008_wav--4.midi", ticks_per_beat=12) #convert midi to numpy
note_seq = midi_conversion.convert_matrix_to_word_seq(notes_np)
num_seq = midi_conversion.convert_to_number_seq(note_seq)

plot_midi(notes_np, seq_length=100, filename="vector")
plot_num_seq(num_seq, 100, filename="num_seq")


#plot_midi(notes_np,seq_length = 100,show_plot = True)
print()





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


