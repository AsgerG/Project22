import midi_conversion
from midi_plotter import plot_midi, play_midi
from midi_note import Note

notes_np = midi_conversion.convert_midi_to_numpy("midi_dataset_sample.midi", downscale = 100)
midi_conversion.convert_numpy_to_midi(notes_np, output_name = "midi_exported.midi", upscale = 100)
play_midi("midi_exported.midi")

#notes_downscaled_100 = midi_conversion.convert_midi_to_numpy("dataset_sample.midi",100)