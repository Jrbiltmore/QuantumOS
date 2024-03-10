import os
import uuid

# Path to the file where active sessions are stored
SESSIONS_FILE = "active_sessions.txt"

# Ensure the sessions file exists
if not os.path.exists(SESSIONS_FILE):
    open(SESSIONS_FILE, 'w').close()

def create_session(username):
    """Create a new session for a username."""
    session_id = str(uuid.uuid4())
    with open(SESSIONS_FILE, 'a') as file:
        file.write(f"{session_id},{username}\n")
    print(f"Session created for {username}. Session ID: {session_id}")
    return session_id

def verify_session(session_id):
    """Verify if a session ID is valid."""
    with open(SESSIONS_FILE, 'r') as file:
        for line in file:
            stored_session_id, _ = line.strip().split(',')
            if stored_session_id == session_id:
                print("Session is valid.")
                return True
    print("Session is invalid.")
    return False

def destroy_session(session_id):
    """Destroy an active session."""
    lines_to_keep = []
    with open(SESSIONS_FILE, 'r') as file:
        for line in file:
            stored_session_id, _ = line.strip().split(',')
            if stored_session_id != session_id:
                lines_to_keep.append(line)
    with open(SESSIONS_FILE, 'w') as file:
        file.writelines(lines_to_keep)
    print(f"Session {session_id} destroyed.")

# Example usage
if __name__ == "__main__":
    # For demonstration purposes, automatically creating and then verifying a session
    username = "example_user"
    session_id = create_session(username)
    verify_session(session_id)
    destroy_session(session_id)
