import torch
from torch.autograd import Variable
import torch.nn as nn
import torch.optim as optim
from torch.nn import Linear, GRU, Conv2d, Dropout, MaxPool2d, BatchNorm1d, BatchNorm2d, ReLU
from torch.nn.functional import relu, elu, relu6, sigmoid, tanh, softmax

lstm_hidden = 4
out_hidden = 64
num_classes = 1024
num_features = 129

# Keep track of features to output layer #(20*20*128)//64
# <-- Number of features concatenated before output layer
features_cat_size = lstm_hidden


class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()

        # Exercise: Add a recurrent unit like and RNN or GRU
        # >> YOUR CODE HERE <<
        self.lstm_1 = nn.LSTM(input_size=1,
                              hidden_size=lstm_hidden,
                              num_layers=1,
                              bidirectional=False)

        self.bn_2 = nn.BatchNorm2d(32)

        self.l_hidden_last = Linear(in_features=features_cat_size,
                                    out_features=out_hidden,
                                    bias=False)

        self.l_out = Linear(in_features=out_hidden,
                            out_features=num_classes,
                            bias=False)

        self.dropout = Dropout(0.7)
        self.max_pool = MaxPool2d(kernel_size=2, stride=1)

    def forward(self, x):
        features = []
        out = {}

        ## Convolutional layer ##
        # - Change dimensions to fit the convolutional layer
        # - Apply Conv2d
        # - Use an activation function
        # - Change dimensions s.t. the features can be used in the final FFNN output layer

        # Shape data processing
        x = x.T
        x = x[:, :, None]

        x, (h, c) = self.lstm_1(x)
        h = h.view(h.shape[1], -1)
        features.append(h)

        # Append features to the list "features"

        ## Use concatenated leaf features for RNN ##
        # - Chage dimensions to fit GRU
        # - Apply GRU
        # - Change dimensions s.t. the features can be used in the final FFNN output layer

        # >> YOUR CODE HERE <<

        # Append features to the list "features"
        # features.append(features_rnn)

        ## Output layer where all features are in use ##

        # Final concatenated data processing
        features_final = torch.cat(features, dim=1)
        features_final = relu(self.l_hidden_last(features_final))
        features_final = self.dropout(features_final)
        out['out'] = self.l_out(features_final)
        return out


net = Net()
print(net)
