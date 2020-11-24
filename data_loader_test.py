import numpy as np
import mido
import midi_conversion
import os
from time import time, sleep
import numpy as np
import matplotlib.pyplot as plt

# lists for saving data
all_midi_2017_np = []
timings = []

path = "/Users/sebastian/projects/Project22/maestro-v2.0.0"
directory = r"/Users/sebastian/projects/Project22/maestro-v2.0.0"
for folder in os.listdir(directory):
    folder_path = path+"/"+folder
    print(folder_path, "is dir:", os.path.isdir(folder_path))
    if os.path.isdir(folder_path):
        for filename in os.listdir(folder_path):
            if filename.endswith(".midi"):
                t0 = time()  # timing

                # convert
                full_path = folder_path+"/"+filename
                all_midi_2017_np.append(
                    midi_conversion.convert_midi_to_numpy(full_path, 100))

                # get timings
                timing = time()-t0
                timings.append(timing)
                print(folder, ":", "Loading", filename, "took", timing, "s")
            else:
                continue


# Data for plotting
fig, ax = plt.subplots()
ax.plot([s for s in range(len(timings))], timings)
ax.set(xlabel='nr. song', ylabel='timings (s)',
       title='benchmark')
ax.grid()
plt.show()
