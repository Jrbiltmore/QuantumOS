# Placeholder content for role_based_access_control.py
class Role:
    def __init__(self, name):
        self.name = name
        self.permissions = set()

    def add_permission(self, permission):
        self.permissions.add(permission)

    def has_permission(self, permission):
        return permission in self.permissions


class User:
    def __init__(self, username):
        self.username = username
        self.roles = []

    def add_role(self, role):
        self.roles.append(role)

    def has_permission(self, permission):
        return any(role.has_permission(permission) for role in self.roles)


# Example usage
def main():
    # Define roles
    admin_role = Role('admin')
    admin_role.add_permission('create_user')
    admin_role.add_permission('delete_user')

    editor_role = Role('editor')
    editor_role.add_permission('create_post')
    editor_role.add_permission('edit_post')

    # Define users
    admin_user = User('admin_user')
    admin_user.add_role(admin_role)

    editor_user = User('editor_user')
    editor_user.add_role(editor_role)

    # Check permissions
    print(f"Admin has permission to create user: {admin_user.has_permission('create_user')}")
    print(f"Editor has permission to edit post: {editor_user.has_permission('edit_post')}")
    print(f"Editor has permission to delete user: {editor_user.has_permission('delete_user')}")

if __name__ == "__main__":
    main()
