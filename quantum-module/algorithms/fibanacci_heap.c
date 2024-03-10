#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

typedef struct FibNode {
    int key;
    int degree;
    struct FibNode* parent;
    struct FibNode* child;
    struct FibNode* left;
    struct FibNode* right;
    int mark;
} FibNode;

typedef struct FibHeap {
    struct FibNode* min;
    int n;
} FibHeap;

FibHeap* createFibHeap() {
    FibHeap* H = (FibHeap*) malloc(sizeof(FibHeap));
    if (H == NULL) {
        fprintf(stderr, "Out of memory!\n");
        exit(EXIT_FAILURE);
    }
    H->min = NULL;
    H->n = 0;
    return H;
}

FibNode* createFibNode(int key) {
    FibNode* x = (FibNode*) malloc(sizeof(FibNode));
    if (x == NULL) {
        fprintf(stderr, "Out of memory!\n");
        exit(EXIT_FAILURE);
    }
    x->key = key;
    x->degree = 0;
    x->parent = NULL;
    x->child = NULL;
    x->left = x;
    x->right = x;
    x->mark = 0;
    return x;
}

void fibHeapInsert(FibHeap* H, FibNode* x) {
    if (H->min == NULL) {
        // Heap is empty, create a root list for H containing just x
        H->min = x;
    } else {
        // Insert x into H's root list
        x->left = H->min;
        x->right = H->min->right;
        H->min->right = x;
        x->right->left = x;
        if (x->key < H->min->key) {
            H->min = x;
        }
    }
    H->n = H->n + 1;
}

FibNode* fibHeapExtractMin(FibHeap* H) {
    FibNode* z = H->min;
    if (z != NULL) {
        // For each child of z, add it to the root list of H
        // This part of the code is omitted for brevity
        // ...

        // Remove z from the root list of H
        z->left->right = z->right;
        z->right->left = z->left;

        if (z == z->right) {
            H->min = NULL;
        } else {
            H->min = z->right;
            // Consolidate the heap
            // This part of the code is also omitted for brevity
            // ...
        }
        H->n = H->n - 1;
    }
    return z;
}

// This is a simplified implementation
// Many detailed operations like Consolidate, Link, Cut, CascadingCut,
// DecreaseKey, and actual memory management for node removal are omitted for brevity.

int main() {
    // Example usage
    FibHeap* H = createFibHeap();
    fibHeapInsert(H, createFibNode(3));
    fibHeapInsert(H, createFibNode(2));
    fibHeapInsert(H, createFibNode(15));

    FibNode* min = fibHeapExtractMin(H);
    printf("The minimum key is: %d\n", min->key);

    // Remember to free the heap and nodes after usage to avoid memory leaks
    // This is omitted here for brevity

    return 0;
}
