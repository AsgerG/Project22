import mido
import numpy as np
from midi_note import Note 

def convert_midi_to_numpy(path, downscale=1, ticks_per_beat = 0):
    notes = []
    unfinished_notes = {}
    total_time = 0
    index = 0


    mid = mido.MidiFile(path, clip=True)
    if ticks_per_beat > 0:
        resolution = int(mid.ticks_per_beat / ticks_per_beat)
    else: resolution = downscale

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
                elif msg.note in unfinished_notes:  # to avoid key errors, check that it does exist
                    (unfinished_index, start_time) = unfinished_notes.pop(msg.note)
                    notes[unfinished_index].duration = total_time - start_time
                    notes[unfinished_index].stop_time = total_time
            total_time += msg.time

    # make notes into an array
    # notes_np = np.zeros((total_time,129)) #using numbers
    # using booleans for better memory
    notes_np = np.zeros((total_time, 129))
    for note in notes:
        for i in range(note.duration):
            notes_np[note.start_time+i][note.note] = 1

    if resolution > 1:
        downscaled_x = int(total_time/resolution)
        downscaled_notes = np.zeros((downscaled_x, 129))
        for x_new in range(downscaled_x):
            v_new = np.zeros(129)
            for i in range(resolution):
                v_new = v_new + notes_np[(x_new*resolution)+i]
            for i in range(len(v_new)):
                if v_new[i] > 0: v_new[i] = 1
            downscaled_notes[x_new] = v_new
        notes_np = downscaled_notes

    return notes_np
    # done. notes_num contains the whole song


def convert_matrix_to_word_seq(notes_np, resolution = 1):
    is_playing = [False for _ in range(129)]

    note_seq = ["x"]
    
    for tick, v in enumerate(notes_np):
        for note, is_on in enumerate(v):
            note_started = not is_playing[note] and is_on
            note_stopped = is_playing[note] and not is_on
            note_playing = is_playing[note] and is_on

            if note_started:
                is_playing[note] = True
                note_seq.append("p"+str(note))
            elif note_stopped:
                is_playing[note] = False
                note_seq.append("s"+str(note))
            #elif note_playing: #not used yet
        if note_seq[-1][0] == "w":
            c = int(note_seq[-1][1:])+1
            note_seq.pop()
            note_seq.append("w"+str(c))
        else: note_seq.append("w1")
  
    return note_seq[1:]

def convert_to_number_seq(note_seq):
    #lower half is start, upper half is stop, top is tick_end
    num_seq = []
    for word in note_seq:
        num_seq.append(convert_word_to_num(word))
    return num_seq

def convert_word_to_num(word):
    node_range = 129
    letter = word[0]
    note = int(word[1:])
    if letter == "p": return note
    elif letter == "s": return note+node_range
    elif letter == "w": 
        if note > 200: note = 200 # WAIT CAP
        return note+2*node_range

# def convert_num_to_word(num): Yet to implement



# print("hey")
# temp = convert_midi_to_numpy("dataset_sample.midi", 100)  # EXAMPLE

# print(len(temp))


def convert_numpy_to_midi(notes_np, output_name = "exported_midi_from_numpy", upscale = 1, tempo = 500000):
    subset = np.array([v for v in notes_np for _ in range(upscale)])
    mid_new = mido.MidiFile(ticks_per_beat=384)
    track_meta = mido.MidiTrack()
    track_notes = mido.MidiTrack()

    track_meta.append(mido.MetaMessage("set_tempo", tempo=tempo))
    track_meta.append(mido.MetaMessage("time_signature", clocks_per_click = 24, denominator = 4, numerator = 4, time = 0, notated_32nd_notes_per_beat = 8))
    track_meta.append(mido.MetaMessage("end_of_track", time = 1))

    is_on_list = [False for _ in range(129)]
    time = 0
    #to_append = (note,velo)
    to_append = (0,0)

    for v in subset:
        is_on_list_old = is_on_list #get a copy
        for note, is_on in enumerate(v):
            cond1 = is_on and not is_on_list[note] 
            cond2 = not is_on and is_on_list[note]

            if cond1 or cond2:
                #save prev note with correct time
                note_prev, velo_prev = to_append
                track_notes.append(mido.Message('note_on', note=note_prev, velocity=velo_prev, time=time))
                time = 0
            if cond1:
                #note just activated
                is_on_list[note] = True
                to_append = (note, 64)
            elif cond2:
                #note just deactivated
                is_on_list[note] = False
                to_append = (note,0)
            #if note is playing and it has been noted in the list, then ignore
        time += 1

    mid_new.tracks.append(track_meta)
    mid_new.tracks.append(track_notes)
    mid_new.save(output_name)
