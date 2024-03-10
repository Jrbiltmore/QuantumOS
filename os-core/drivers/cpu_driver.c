// os-core/kernel/drivers/cpu_driver.c

#define _GNU_SOURCE
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>
#include <string.h>
#include <sched.h>

typedef struct {
    unsigned int core_count;
    float frequency; // in GHz
    char model_name[256];
} CPUInfo;

// Declare static functions for internal use
static void read_cpu_model_name(char* model_name, size_t len);
static unsigned int count_cpu_cores(void);
static float read_cpu_max_frequency(unsigned int core);

// Public API functions
void initialize_cpu_driver(void);
void fetch_cpu_info(CPUInfo* info);
void display_cpu_info(const CPUInfo* info);
void adjust_cpu_frequency(unsigned int core, float newFrequency);

void initialize_cpu_driver(void) {
    printf("CPU driver initialization complete.\n");
}

void read_cpu_model_name(char* model_name, size_t len) {
    FILE* fp = fopen("/proc/cpuinfo", "r");
    if (!fp) {
        perror("Failed to open /proc/cpuinfo");
        return;
    }

    char* line = NULL;
    size_t n = 0;
    while (getline(&line, &n, fp) != -1) {
        if (strncmp(line, "model name", 10) == 0) {
            char* colon = strchr(line, ':');
            if (colon && strlen(colon) > 2) {
                strncpy(model_name, colon + 2, len);
                size_t model_len = strlen(model_name);
                if (model_len > 0 && model_name[model_len - 1] == '\n') {
                    model_name[model_len - 1] = '\0'; // Remove newline
                }
                break;
            }
        }
    }
    free(line);
    fclose(fp);
}

unsigned int count_cpu_cores(void) {
    return sysconf(_SC_NPROCESSORS_ONLN);
}

float read_cpu_max_frequency(unsigned int core) {
    char path[256];
    snprintf(path, sizeof(path), "/sys/devices/system/cpu/cpu%d/cpufreq/scaling_max_freq", core);

    FILE* fp = fopen(path, "r");
    if (!fp) {
        perror("Failed to read CPU frequency");
        return 0.0;
    }

    unsigned long max_freq = 0;
    fscanf(fp, "%lu", &max_freq);
    fclose(fp);

    return max_freq / 1e6; // Convert kHz to GHz
}

void fetch_cpu_info(CPUInfo* info) {
    if (!info) return;

    info->core_count = count_cpu_cores();
    read_cpu_model_name(info->model_name, sizeof(info->model_name));
    // Assuming all cores have the same max frequency for simplicity
    info->frequency = read_cpu_max_frequency(0);
}

void display_cpu_info(const CPUInfo* info) {
    if (!info) return;

    printf("CPU Model: %s\n", info->model_name);
    printf("Core Count: %u\n", info->core_count);
    printf("Max Frequency: %.2f GHz\n", info->frequency);
}

void adjust_cpu_frequency(unsigned int core, float newFrequency) {
    // This function is a placeholder.
    // Adjusting CPU frequency requires privileged access and is platform-dependent.
    printf("Adjusting frequency for core %u to %.2f GHz (Not implemented).\n", core, newFrequency);
}

int main() {
    CPUInfo cpuInfo;
    
    initialize_cpu_driver();
    fetch_cpu_info(&cpuInfo);
    display_cpu_info(&cpuInfo);
    
    // Example: Attempt to adjust the frequency of core 0 (not implemented)
    adjust_cpu_frequency(0, 3.8);

    return 0;
}
