import redis

class RedisAdapter:
    def __init__(self, host='localhost', port=6379, db=0):
        self.r = redis.Redis(host=host, port=port, db=db, decode_responses=True)

    def set_key(self, key, value):
        self.r.set(key, value)
        print(f"Set key {key} with value {value}")

    def get_key(self, key):
        value = self.r.get(key)
        print(f"Value of key {key} is {value}")
        return value

    def push_to_list(self, list_name, *values):
        self.r.rpush(list_name, *values)
        print(f"Pushed values {values} to list {list_name}")

    def get_list(self, list_name):
        values = self.r.lrange(list_name, 0, -1)
        print(f"Values in list {list_name} are {values}")
        return values

    def remove_key(self, key):
        self.r.delete(key)
        print(f"Removed key {key}")

# Example usage
if __name__ == "__main__":
    adapter = RedisAdapter()

    # Key-value operations
    adapter.set_key("QuantumOS", "1.0")
    adapter.get_key("QuantumOS")

    # List operations
    adapter.push_to_list("mylist", "a", "b", "c")
    adapter.get_list("mylist")

    # Removing a key
    adapter.remove_key("QuantumOS")
