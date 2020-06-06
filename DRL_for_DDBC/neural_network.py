""" the neural network embeded in the DQN agent """

from keras import Sequential
from keras.layers import Dense
from config import Config


class NeuralNetwork:

    def __init__(self, input_ports=11*Config().U+7,
                 output_ports=Config().n_actions,
                 num_neurons=(64, 32),
                 activation_function='relu'):

        self.input_ports = input_ports
        self.output_ports = output_ports
        self.num_neurons = num_neurons
        self.activation_function = activation_function

    def get_model(self):

        model = Sequential()
        model.add(Dense(self.num_neurons[0], input_shape=(self.input_ports,), activation=self.activation_function))
        for j in range(1, len(self.num_neurons)):
            model.add(Dense(self.num_neurons[j], activation=self.activation_function))
        model.add(Dense(self.output_ports))
        return model
