# # A DUMP OF UNUSED CODE

# mid = mido.MidiFile('dataset_sample.midi', clip=True)
# tempo = -1
# #extract notes from midi file
# for track in mid.tracks:
#     for msg in track:
#         if msg.type == "set_tempo":
#             tempo = msg.tempo
#         if msg.type == "note_on":
#             if msg.velocity > 0: #node_on
#                 note = Note(msg.type, msg.channel, msg.note, msg.velocity, msg.time, total_time)
#                 notes.append(note)
#                 unfinished_notes[msg.note] = (index,total_time)
#                 index += 1
#             else: #node_off
#                 (unfinished_index,start_time) = unfinished_notes.pop(msg.note)
#                 notes[unfinished_index].duration = total_time - start_time
#                 notes[unfinished_index].stop_time = total_time
#         total_time += msg.time


# #MISC
# def get_length(mid):
#     # beat is a quarter note. There are 4 in a bar.
#     seconds_per_tick = (tempo/mid.ticks_per_beat)/1000000 #our res is 1 tick per vector.
#     song_length_total = seconds_per_tick*total_time# total length in seconds
#     h = 60*60
#     m = 60
#     song_length_temp = song_length_total
#     song_length_hours = floor(song_length_temp/h) #get hours
#     song_length_temp = song_length_temp-song_length_hours*h
#     song_length_minutes = floor((song_length_temp)/m) #get remaining minutes
#     song_length_temp = song_length_temp-song_length_minutes*m
#     song_length_seconds = song_length_temp #get remaining seconds

#     return (song_length_total, (song_length_hours, "h", song_length_minutes, "m", song_length_seconds, "s"))
