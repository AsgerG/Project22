import matplotlib
import matplotlib.pyplot as plt
import numpy as np

## DRAW NOTES USING MATPLOTLIB

def plot_midi(midi_np, seq_length = 1024, filename = "temp_midi_file", show_plot = False):
    """
    Exports an image showing the midi track. Can be configured to show the plot. 
    """

    #FAIL SAFE
    if len(midi_np) < seq_length: seq_length = len(midi_np)

    ss_l = seq_length
    v_l = 129
    ss = midi_np[:ss_l]
    y = [i if ss[e][i] else float("nan") for e in range(ss_l) for i in range(v_l)]
    fig, ax = plt.subplots(figsize = (40,10))
    t = [x for x in range(ss_l)]*v_l
    t.sort()
    ax.plot(t, y, 'ko', markersize=2)

    ax.set(xlabel='time (tick)', ylabel='note',
        title='')
    ax.grid()

    filename_full = filename+".png"
    plt.savefig(filename_full, dpi=500)
    if show_plot:
        plt.show()


def plot_num_seq(num_seq, seq_length, show_plot = True, filename = ""):
    active = [False for _ in range(129)]
    midi_np = []
    for num in num_seq:
        if num < 129: active[num] = True #start
        elif num < 129*2: active[num-129] = False #stop
        else: # wait call
            number_of_waits = (num-129*2)
            for _ in range(number_of_waits):
                v = [i for i in active] #copy active
                midi_np.append(v)
    
    ss_l = seq_length
    v_l = 129
    ss = midi_np[:ss_l]
    y = [i if ss[e][i] else float("nan") for e in range(ss_l) for i in range(v_l)]
    fig, ax = plt.subplots(figsize = (40,10))
    t = [x for x in range(ss_l)]*v_l
    t.sort()
    ax.plot(t, y, 'ko', markersize=2)

    ax.set(xlabel='time (tick)', ylabel='note',
        title='')
    ax.grid()

    if len(filename) > 0:
        filename_full = filename+".png"
        plt.savefig(filename_full, dpi=500)
    if show_plot:
        plt.show()



def play_midi(filename):
    import pygame
    #play music
    pygame.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()
    print("PLAYING MUSIC")
    while pygame.mixer.music.get_busy(): #TODO make a better solution
        print()