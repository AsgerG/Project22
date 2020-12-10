import numpy as np
import pandas as pd
import os
from midi_conversion import convert_midi_to_numpy

#from PIL import Image, ImageOps
from skimage.io import imread
from skimage.transform import resize
from sklearn.model_selection import StratifiedShuffleSplit
import warnings

with warnings.catch_warnings():
    warnings.filterwarnings("ignore", category=DeprecationWarning)


class load_data():
    # data_train, data_test and le are public
    def __init__(self, resolution=1):
        track_paths = self._generate_paths()
        self.resolution = resolution

        self._load(track_paths)

    def _generate_paths(self):
        paths = []
        maestro_dir = "./maestro-v2.0.0/"
        for maestro_folder in os.listdir(maestro_dir):
            if maestro_folder == "2004":
                # print(maestro_folder)
                # if len(maestro_folder) == 4:
                for track_path in os.listdir(maestro_dir + maestro_folder):
                    paths.append(maestro_dir + maestro_folder +
                                 "/" + track_path)
        return paths

    def _load(self, track_paths):
        #train_data = []
        #test_data = []
        self.ts = []
        train_data = np.zeros((1, 129))
        test_data = np.zeros((1, 129))
        for idx, path in enumerate(track_paths):
            if idx % 5 == 0:
                test_data = np.concatenate(
                    (test_data, convert_midi_to_numpy(path, 100)))
                #train_data.append(convert_midi_to_numpy(path, 100))
            else:
                train_data = np.concatenate(
                    (train_data, convert_midi_to_numpy(path, 100)))
            print(idx)
            if idx >= 5:
                break

        self.train = self.chop_data(train_data)
        self.test = self.chop_data(test_data)

    def chop_data(self, uncut_data, cut_length=1024):
        chop = 0
        index = 0

        cutted_data = np.zeros(
            (int(uncut_data.shape[0]/cut_length), cut_length, 129))

        for node in uncut_data:
            if index >= cut_length:
                index = 0
                chop += 1

            if chop >= cutted_data.shape[0]:
                break
            # print(index)
            cutted_data[chop][index] = node
            index += 1

        return cutted_data


class batch_generator():
    def __init__(self, data, batch_size=64, num_classes=1024,
                 num_iterations=5e3, num_features=129, seed=42, val_size=0.1):
        self._train = data.train
        self._test = data.test
        self._batch_size = batch_size
        self._num_classes = num_classes
        self._num_iterations = num_iterations
        self._num_features = num_features
        self._seed = seed
        self._val_size = val_size
        self._valid_split()

    def _valid_split(self):
        sss = StratifiedShuffleSplit(
            n_splits=1,
            test_size=self._val_size,
            random_state=self._seed
        ).split(
            # Needed in StratifiedShuffleSplit for nothing...
            np.zeros((self._train.shape[0])),
            np.zeros((self._train.shape[0]))
        )
        self._idcs_train, self._idcs_valid = next(iter(sss))

    def _shuffle_train(self):
        np.random.shuffle(self._idcs_train)

    def _batch_init(self, purpose):
        assert purpose in ['train', 'valid', 'test']
        batch_holder = np.zeros(
            (self._batch_size, self._num_classes, self._num_features), dtype='int32')
        return batch_holder

    def gen_valid(self):
        batch = self._batch_init(purpose='valid')
        i = 0
        for idx in self._idcs_valid:
            batch[i] = self._train[idx]
            i += 1
            if i >= self._batch_size:
                yield batch, i
                batch = self._batch_init(purpose='valid')
                i = 0
        if i != 0:
            batch = batch[:i]
            yield batch, i

    def gen_test(self):
        batch = self._batch_init(purpose='test')
        i = 0
        for idx in range(len(self._test)):
            batch[i] = self._test[idx]
            i += 1
            if i >= self._batch_size:
                yield batch, i
                batch = self._batch_init(purpose='test')
                i = 0
        if i != 0:
            yield batch, i

    def gen_train(self):
        batch = self._batch_init(purpose='train')
        iteration = 0
        i = 0
        while True:
            # shuffling all batches
            self._shuffle_train()
            for idx in self._idcs_train:
                # extract data from dict
                batch[i] = self._train[idx]
                i += 1
                if i >= self._batch_size:
                    yield batch
                    batch = self._batch_init(purpose='train')
                    i = 0
                    iteration += 1
                    if iteration >= self._num_iterations:
                        break


#max_iterations = 50000
#data = load_data()
#batch_gen = batch_generator(data)
#eval_every = 1000

# for i, batch_train in enumerate(batch_gen.gen_train()):
#    if i % eval_every == 0:
#        print("training...")

    # Train network

#    if max_iterations < i:
#        break
# print(data)
