// neural_network.c

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define INPUT_SIZE 784
#define HIDDEN_LAYER_SIZE 128
#define OUTPUT_SIZE 10

// Function to initialize weights for neural network
void initialize_weights(float* weights, int size) {
    for (int i = 0; i < size; i++) {
        weights[i] = ((float)rand() / RAND_MAX) * 2 - 1; // Random weights between -1 and 1
    }
}

// Function to perform forward propagation in neural network
void forward_propagation(float* input, float* weights_input_hidden, float* weights_hidden_output, float* hidden_layer_output, float* output) {
    // Compute hidden layer output
    for (int i = 0; i < HIDDEN_LAYER_SIZE; i++) {
        float sum = 0;
        for (int j = 0; j < INPUT_SIZE; j++) {
            sum += input[j] * weights_input_hidden[j + i * INPUT_SIZE];
        }
        hidden_layer_output[i] = tanh(sum); // Hyperbolic tangent activation function
    }

    // Compute output layer output
    for (int i = 0; i < OUTPUT_SIZE; i++) {
        float sum = 0;
        for (int j = 0; j < HIDDEN_LAYER_SIZE; j++) {
            sum += hidden_layer_output[j] * weights_hidden_output[j + i * HIDDEN_LAYER_SIZE];
        }
        output[i] = sum; // Linear activation function for output layer
    }
}

int main() {
    // Allocate memory for weights and layers
    float* weights_input_hidden = (float*)malloc(INPUT_SIZE * HIDDEN_LAYER_SIZE * sizeof(float));
    float* weights_hidden_output = (float*)malloc(HIDDEN_LAYER_SIZE * OUTPUT_SIZE * sizeof(float));
    float* input = (float*)malloc(INPUT_SIZE * sizeof(float));
    float* hidden_layer_output = (float*)malloc(HIDDEN_LAYER_SIZE * sizeof(float));
    float* output = (float*)malloc(OUTPUT_SIZE * sizeof(float));

    // Initialize weights
    initialize_weights(weights_input_hidden, INPUT_SIZE * HIDDEN_LAYER_SIZE);
    initialize_weights(weights_hidden_output, HIDDEN_LAYER_SIZE * OUTPUT_SIZE);

    // Initialize input data (dummy data for demonstration)
    for (int i = 0; i < INPUT_SIZE; i++) {
        input[i] = ((float)rand() / RAND_MAX) * 2 - 1; // Random input between -1 and 1
    }

    // Perform forward propagation
    forward_propagation(input, weights_input_hidden, weights_hidden_output, hidden_layer_output, output);

    // Display output
    printf("Output: ");
    for (int i = 0; i < OUTPUT_SIZE; i++) {
        printf("%.2f ", output[i]);
    }
    printf("\n");

    // Free allocated memory
    free(weights_input_hidden);
    free(weights_hidden_output);
    free(input);
    free(hidden_layer_output);
    free(output);

    return 0;
}
