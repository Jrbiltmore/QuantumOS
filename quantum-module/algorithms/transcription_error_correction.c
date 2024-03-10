// transcription_error_correction.c

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_SEQ_LENGTH 100

// Function to correct transcription errors in DNA sequence
char* correct_transcription_error(const char* sequence) {
    int len = strlen(sequence);
    char* corrected_sequence = (char*)malloc((len + 1) * sizeof(char));
    if (corrected_sequence == NULL) {
        perror("Memory allocation failed");
        exit(EXIT_FAILURE);
    }
    
    // Iterate through the sequence and correct errors
    for (int i = 0; i < len; i++) {
        switch (sequence[i]) {
            case 'T':
                corrected_sequence[i] = 'U'; // Replace Thymine with Uracil
                break;
            default:
                corrected_sequence[i] = sequence[i]; // No correction needed
                break;
        }
    }
    corrected_sequence[len] = '\0'; // Null-terminate the corrected sequence
    return corrected_sequence;
}

int main() {
    const char* dna_sequence = "ATCGATCGTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGC";
    char* corrected_sequence = correct_transcription_error(dna_sequence);
    
    printf("Original DNA Sequence: %s\n", dna_sequence);
    printf("Corrected RNA Sequence: %s\n", corrected_sequence);
    
    free(corrected_sequence); // Free allocated memory
    return 0;
}
