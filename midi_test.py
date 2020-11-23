import mido
import pygame
import numpy as np
from time import time


# #play music
# pygame.init()
# pygame.mixer.music.load("dataset_sample.midi")
# pygame.mixer.music.play()
# while True:
#     print()

notes = []
unfinished_notes = {}
total_time = 0
index = 0

class Note():
    duration = -1
    stop_time = -1
    def __init__(self,type,channel,note,velocity,time,start_time):
        self.type = type
        self.channel = channel
        self.note = note
        self.velocity = velocity
        self.time = time
        self.start_time = start_time
    
    def to_numpy(self):
        v = np.zeros(129)
        v[self.note] = 1
        return v

print("Converting midi") #TIMING
timer_start = time()

mid = mido.MidiFile('dataset_sample.midi', clip=True)
print("Done reading file, dt=",time()-timer_start) #TIMING

tempo = -1

#extract notes from midi file
for track in mid.tracks:
    for msg in track:
        if msg.type == "set_tempo":
            tempo = msg.tempo
        if msg.type == "note_on":
            if msg.velocity > 0: #node_on
                note = Note(msg.type, msg.channel, msg.note, msg.velocity, msg.time, total_time)
                notes.append(note)
                unfinished_notes[msg.note] = (index,total_time)
                index += 1
            else: #node_off
                (unfinished_index,start_time) = unfinished_notes.pop(msg.note)
                notes[unfinished_index].duration = total_time - start_time
                notes[unfinished_index].stop_time = total_time
        total_time += msg.time

print("done making note objects, dt=",time()-timer_start) #TIMING

#make notes into an array
notes_num = np.zeros((total_time,129))
for note in notes:
    for i in range(note.duration):
        notes_num[note.start_time+i][note.note] = 1

print("done making numpy array, dt=",time()-timer_start) #TIMING

print("done making csv, dt=",time()-timer_start) #TIMING

durations = [note.duration for note in notes if note.duration]
print("min",min(durations))
print("max",max(durations))
print("avr",sum(durations)/len(durations))

# beat is a quarter note. There are 4 in a bar.
seconds_per_tick = (tempo/mid.ticks_per_beat)/1000000 #our res is 1 tick per vector.
song_length = seconds_per_tick*total_time# in seconds

print("total length of track: ", song_length, "s")
print("total length of track: ", song_length/60, "min")


# # draw notes like in garage band: USING NOTES OBJECTS
# pygame.init()
# screen = pygame.display.set_mode((800, 128*2))
# clock = pygame.time.Clock()

# done = False

# print("Entering loop")
# while not done:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             done = True
#     #draw first 2000
#     screen.fill((0, 0, 0))  
#     color = (255,0,0)

#     scale_x = 10
#     for note_obj in notes:
#         y = (128*2) - (note_obj.note * 2)
#         x1 = note_obj.start_time / scale_x
#         x2 = note_obj.stop_time / scale_x
#         pygame.draw.line(screen,color,(x1,y),(x2,y))

#     #for point in getLine((200,200),(mouse_x,mouse_y)):
#     #    pygame.draw.line(screen,(255,255,255),point,point)

#     pygame.display.flip()       
#     clock.tick(120)

#####################################################################

# # draw notes like in garage band: USING NUMPY ARRAY
# pygame.init()
# screen = pygame.display.set_mode((1600, 128*2))
# clock = pygame.time.Clock()

# done = False

# print("Entering loop")
# once = True
# while not done:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             done = True
#     if once:
#         #draw first 2000
#         screen.fill((0, 0, 0))  
#         color = (255,0,0)

#         scale_x = 10
#         for time, vector in enumerate(notes_num):
#             for note, is_active in enumerate(vector):
#                 if is_active:
#                     y = (128*2) - (note * 2)
#                     pygame.draw.line(screen,color,(time/scale_x,y),(time/scale_x,y))

#         #for point in getLine((200,200),(mouse_x,mouse_y)):
#         #    pygame.draw.line(screen,(255,255,255),point,point)
#         once = False

#     pygame.display.flip()       
#     clock.tick(120)




