class Mapper:
    def setup(self):
        # This method is executed once at the beginning of the task.
        # You can perform setup or configuration here.
        pass

    def map(self, key, value):
        # This method implements the logic to process the input data.
        # In this example, we split each line into words and emit a key-value pair for each word.
        for word in value.split():
            self.emit(word, 1)

    def cleanup(self):
        # This method is executed once at the end of the map task.
        # You can close resources or perform any final computations here.
        pass

    def emit(self, key, value):
        # Helper method to emit a key-value pair using the context or collector.
        # The actual implementation may vary based on the MapReduce framework used.
        print(f"{key}, {value}")

# Example usage:
# Create an instance of the Mapper class
mapper = Mapper()

# Call the setup method (usually executed once at the beginning)
mapper.setup()

# Example input data
input_key = 1  # For illustration purposes, the key is not used in this example
input_value = "Hello World Hello MapReduce"

# Call the map method with the input key-value pair
mapper.map(input_key, input_value)

# Call the cleanup method (usually executed once at the end)
mapper.cleanup()
