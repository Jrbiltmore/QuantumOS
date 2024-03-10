// decision_tree.c

#include <stdio.h>
#include <stdlib.h>

#define NUM_FEATURES 5
#define NUM_SAMPLES 1000

// Structure to represent a node in the decision tree
typedef struct Node {
    int feature_index;  // Index of feature to split on
    float split_value;  // Value to split the feature on
    struct Node* left;  // Pointer to left child node
    struct Node* right; // Pointer to right child node
    int class_label;    // Class label for leaf nodes
} Node;

// Function to create a new node
Node* create_node(int feature_index, float split_value, Node* left, Node* right, int class_label) {
    Node* node = (Node*)malloc(sizeof(Node));
    if (node == NULL) {
        fprintf(stderr, "Memory allocation failed\n");
        exit(1);
    }
    node->feature_index = feature_index;
    node->split_value = split_value;
    node->left = left;
    node->right = right;
    node->class_label = class_label;
    return node;
}

// Function to perform decision tree training (dummy implementation for demonstration)
Node* train_decision_tree(float** data, int* labels) {
    // Dummy implementation
    // Assume a binary tree with a single decision node
    return create_node(0, 0.5, create_node(-1, -1, NULL, NULL, 0), create_node(-1, -1, NULL, NULL, 1), -1);
}

// Function to perform prediction using the trained decision tree
int predict(Node* root, float* sample) {
    while (root->class_label == -1) {
        if (sample[root->feature_index] <= root->split_value) {
            root = root->left;
        } else {
            root = root->right;
        }
    }
    return root->class_label;
}

int main() {
    // Dummy data for demonstration
    float** data = (float**)malloc(NUM_SAMPLES * sizeof(float*));
    for (int i = 0; i < NUM_SAMPLES; i++) {
        data[i] = (float*)malloc(NUM_FEATURES * sizeof(float));
        // Initialize data with random values between 0 and 1
        for (int j = 0; j < NUM_FEATURES; j++) {
            data[i][j] = ((float)rand() / RAND_MAX);
        }
    }
    int* labels = (int*)malloc(NUM_SAMPLES * sizeof(int));
    // Initialize labels with random binary values
    for (int i = 0; i < NUM_SAMPLES; i++) {
        labels[i] = rand() % 2;
    }

    // Train decision tree
    Node* decision_tree = train_decision_tree(data, labels);

    // Dummy sample for prediction
    float* sample = (float*)malloc(NUM_FEATURES * sizeof(float));
    // Initialize sample with random values between 0 and 1
    for (int j = 0; j < NUM_FEATURES; j++) {
        sample[j] = ((float)rand() / RAND_MAX);
    }

    // Perform prediction
    int prediction = predict(decision_tree, sample);
    printf("Predicted class label: %d\n", prediction);

    // Free allocated memory
    for (int i = 0; i < NUM_SAMPLES; i++) {
        free(data[i]);
    }
    free(data);
    free(labels);
    free(sample);

    return 0;
}
