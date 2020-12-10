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

def play_midi(filename):
    import pygame
    #play music
    pygame.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()
    print("PLAYING MUSIC")
    while pygame.mixer.music.get_busy(): #TODO make a better solution
        print()