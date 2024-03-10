#include <stdio.h>
#include <string.h>

#define MAX_PERMISSIONS 5
#define MAX_ROLES 2
#define MAX_USERS 2

typedef struct {
    char name[20];
    char permissions[MAX_PERMISSIONS][20];
    int permCount;
} Role;

typedef struct {
    char username[20];
    Role roles[MAX_ROLES];
    int roleCount;
} User;

void addPermission(Role *role, const char *permission) {
    if (role->permCount < MAX_PERMISSIONS) {
        strcpy(role->permissions[role->permCount++], permission);
    }
}

void addRole(User *user, Role role) {
    if (user->roleCount < MAX_ROLES) {
        user->roles[user->roleCount++] = role;
    }
}

int hasPermission(User user, const char *permission) {
    for (int i = 0; i < user.roleCount; i++) {
        for (int j = 0; j < user.roles[i].permCount; j++) {
            if (strcmp(user.roles[i].permissions[j], permission) == 0) {
                return 1;
            }
        }
    }
    return 0;
}

int main() {
    Role adminRole = {.permCount = 0};
    strcpy(adminRole.name, "admin");

    addPermission(&adminRole, "create_user");
    addPermission(&adminRole, "delete_user");

    User adminUser = {.roleCount = 0};
    strcpy(adminUser.username, "admin");

    addRole(&adminUser, adminRole);

    printf("Does admin have permission to 'create_user'? %s\n", hasPermission(adminUser, "create_user") ? "Yes" : "No");
    printf("Does admin have permission to 'edit_post'? %s\n", hasPermission(adminUser, "edit_post") ? "Yes" : "No");

    return 0;
}
