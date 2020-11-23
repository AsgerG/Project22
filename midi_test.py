import mido
import pygame

mid = mido.MidiFile('dataset_sample.midi', clip=True)

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

#extract notes from midi file
for track in mid.tracks:
    for msg in track:
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

# open notes list to see all notes

# draw notes like in garage band
pygame.init()
screen = pygame.display.set_mode((800, 128*2))
clock = pygame.time.Clock()

done = False

print("Entering loop")
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    #draw first 2000
    screen.fill((0, 0, 0))  
    color = (255,0,0)

    scale_x = 10
    for note_obj in notes:
        y = (128*2) - (note_obj.note * 2)
        x1 = note_obj.start_time / scale_x
        x2 = note_obj.stop_time / scale_x
        pygame.draw.line(screen,color,(x1,y),(x2,y))

    #for point in getLine((200,200),(mouse_x,mouse_y)):
    #    pygame.draw.line(screen,(255,255,255),point,point)

    pygame.display.flip()       
    clock.tick(120)



