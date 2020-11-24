import mido
import numpy as np


class Note():
    duration = -1
    stop_time = -1

    def __init__(self, type, channel, note, velocity, time, start_time):
        self.type = type
        self.channel = channel
        self.note = note
        self.velocity = velocity
        self.time = time
        self.start_time = start_time


def convert_midi_to_numpy(path):
    notes = []
    unfinished_notes = {}
    total_time = 0
    index = 0

    mid = mido.MidiFile(path, clip=True)

    # extract notes from midi file
    for track in mid.tracks:
        for msg in track:
            if msg.type == "note_on":
                if msg.velocity > 0:  # node_on
                    note = Note(msg.type, msg.channel, msg.note,
                                msg.velocity, msg.time, total_time)
                    notes.append(note)
                    unfinished_notes[msg.note] = (index, total_time)
                    index += 1
                else:  # node_off
                    (unfinished_index, start_time) = unfinished_notes.pop(msg.note)
                    notes[unfinished_index].duration = total_time - start_time
                    notes[unfinished_index].stop_time = total_time
            total_time += msg.time

    # make notes into an array
    notes_num = np.zeros((total_time, 129))
    for note in notes:
        for i in range(note.duration):
            notes_num[note.start_time+i][note.note] = 1

    return notes_num
    # done. notes_num contains the whole song
