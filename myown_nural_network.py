import numpy as np

class SimpleNeuralNetwork:
    def __init__(self, input_size=3, hidden_size=4, output_size=1):
        # Initialize weights and biases
        self.weights_input_to_hidden = np.random.randn(input_size, hidden_size)
        self.bias_hidden = np.random.randn(1, hidden_size)
        self.weights_hidden_to_output = np.random.randn(hidden_size, output_size)
        self.bias_output = np.random.randn(1, output_size)
    
    def sigmoid(self, x):
        """Activation function: Sigmoid"""
        return 1 / (1 + np.exp(-x))
    
    def forward(self, inputs):
        """Feedforward computation"""
        # Input to hidden layer
        self.hidden_layer_input = np.dot(inputs, self.weights_input_to_hidden) + self.bias_hidden
        self.hidden_layer_output = self.sigmoid(self.hidden_layer_input)
        
        # Hidden layer to output
        self.output_layer_input = np.dot(self.hidden_layer_output, self.weights_hidden_to_output) + self.bias_output
        self.output = self.sigmoid(self.output_layer_input)
        
        return self.output

# Example usage
if __name__ == "__main__":
    # Initialize the neural network
    nn = SimpleNeuralNetwork(input_size=3, hidden_size=4, output_size=1)
    
    # Sample input: 3 features
    inputs = np.array([[0.5, 0.2, 0.1]])
    
    # Perform a forward pass
    output = nn.forward(inputs)
    print("Predicted Output:", output) # This would be giving random output as inputs are all random in the input layers 
                                       # check code from line 6-9 it's all random hence the out puts are random .
