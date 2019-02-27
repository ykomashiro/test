import pickle
import numpy as np


class DataLoader():
    def __init__(self):
        self.data = None
        self.labels = None

    def next_batch(self, batch_size=256):
        mask = np.random.choice(
            self.data.shape[0], size=batch_size, replace=True)
        batch_data = self.data[mask]
        batch_labels = self.labels[mask]
        return batch_data, batch_labels


class Data(object):
    def __init__(self):
        self.Xtrain, self.Ytrain, self.Xtest, self.Ytest = \
            None, None, None, None

    def __load_data_batch(self, filename):
        with open(filename, 'rb') as fn:
            data_dict = pickle.load(fn, encoding='iso-8859-1')
            X = data_dict['data'].astype("float")
            y = np.array(data_dict['labels'])
        return X, y

    def load_data(self, root, quantify=6):
        xs = []
        ys = []
        for num in range(1, quantify):
            fn = root + 'data_batch_{}'.format(num)
            x, y = self.__load_data_batch(fn)
            xs.append(x)
            ys.append(y)
        self.Xtrain = np.concatenate(xs)
        self.Ytrain = np.concatenate(ys)
        del x, y
        self.Xtest, self.Ytest = self.__load_data_batch(root + 'test_batch')
        return self.Xtrain, self.Ytrain, self.Xtest, self.Ytest


def load_data_batch(filename):
    with open(filename, 'rb') as fn:
        data_dict = pickle.load(fn, encoding='iso-8859-1')
        X = data_dict['data'].astype("float")
        y = np.array(data_dict['labels'])
    return X, y


def load_cifar10(root=r'dataset/cifar10/'):
    xs = []
    ys = []
    for num in range(1, 6):
        fn = root + 'data_batch_{}'.format(num)
        x, y = load_data_batch(fn)
        xs.append(x)
        ys.append(y)
    Xtrain = np.concatenate(xs)
    Ytrain = np.concatenate(ys)
    del x, y
    Xtest, Ytest = load_data_batch(root + 'test_batch')
    return Xtrain, Ytrain, Xtest, Ytest
