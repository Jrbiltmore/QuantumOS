// logistic_regression.c

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define NUM_FEATURES 5
#define LEARNING_RATE 0.01
#define MAX_ITERATIONS 1000
#define TOLERANCE 0.0001

// Function to perform sigmoid activation
float sigmoid(float x) {
    return 1.0 / (1.0 + exp(-x));
}

// Function to perform logistic regression training
void train_logistic_regression(float** data, int* labels, int num_samples, int num_features, float* weights) {
    float gradient[num_features]; // Gradient for each feature
    float prev_loss = INFINITY;
    float current_loss;
    int iteration = 0;

    while (iteration < MAX_ITERATIONS) {
        // Compute gradient
        for (int i = 0; i < num_features; ++i) {
            gradient[i] = 0.0;
            for (int j = 0; j < num_samples; ++j) {
                float predicted = sigmoid(weights[0] * data[j][0] + weights[1] * data[j][1] + weights[2] * data[j][2] + weights[3] * data[j][3] + weights[4] * data[j][4]);
                gradient[i] += (predicted - labels[j]) * data[j][i];
            }
            gradient[i] /= num_samples;
        }

        // Update weights
        for (int i = 0; i < num_features; ++i) {
            weights[i] -= LEARNING_RATE * gradient[i];
        }

        // Compute loss
        current_loss = 0.0;
        for (int j = 0; j < num_samples; ++j) {
            float predicted = sigmoid(weights[0] * data[j][0] + weights[1] * data[j][1] + weights[2] * data[j][2] + weights[3] * data[j][3] + weights[4] * data[j][4]);
            current_loss += labels[j] * log(predicted) + (1 - labels[j]) * log(1 - predicted);
        }
        current_loss = -current_loss / num_samples;

        // Check convergence
        if (fabs(current_loss - prev_loss) < TOLERANCE) {
            break;
        }
        prev_loss = current_loss;
        iteration++;
    }

    printf("Training complete.\n");
}

// Function to perform logistic regression prediction
int predict_logistic_regression(float* sample, float* weights) {
    float output = weights[0] * sample[0] + weights[1] * sample[1] + weights[2] * sample[2] + weights[3] * sample[3] + weights[4] * sample[4];
    float probability = sigmoid(output);
    return (probability >= 0.5) ? 1 : 0;
}

int main() {
    // Dummy data for demonstration
    float** data = (float**)malloc(3 * sizeof(float*));
    for (int i = 0; i < 3; i++) {
        data[i] = (float*)malloc(NUM_FEATURES * sizeof(float));
    }
    data[0][0] = 0.2; data[0][1] = 0.3; data[0][2] = 0.4; data[0][3] = 0.5; data[0][4] = 0.6;
    data[1][0] = 0.3; data[1][1] = 0.4; data[1][2] = 0.5; data[1][3] = 0.6; data[1][4] = 0.7;
    data[2][0] = 0.4; data[2][1] = 0.5; data[2][2] = 0.6; data[2][3] = 0.7; data[2][4] = 0.8;

    int labels[3] = {0, 1, 0};

    float weights[NUM_FEATURES] = {0};

    // Train logistic regression model
    train_logistic_regression(data, labels, 3, NUM_FEATURES, weights);

    // Dummy sample for prediction
    float sample[NUM_FEATURES] = {0.1, 0.2, 0.3, 0.4, 0.5};

    // Perform prediction using logistic regression model
    int prediction = predict_logistic_regression(sample, weights);
    printf("Predicted class label: %d\n", prediction);

    // Free allocated memory
    for (int i = 0; i < 3; i++) {
        free(data[i]);
    }
    free(data);

    return 0;
}
