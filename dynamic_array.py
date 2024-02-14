from static_array import StaticArray

class Dynamic_Array:
    def __init__(self, start_array=None):
        """
        Initialize new dynamic array
        """
        self.size = 0
        self.capacity = 10
        self.data = StaticArray(self.capacity)

        # populate dynamic array with initial values (if provided)
        if start_array is not None:
            for value in start_array:
                self.append(value)

    def __str__(self):
        return str(self.data)

    # Will need to be amended to check if there is room and call function to expand array when necessary
    def append(self, val):
      if self._size < self._capacity:
          self._data[self._size] =  val
          self._size = self._size + 1
      else:
        self.resize(self._capacity * 2)
        self.append(val)

    # Add a function that will create an expanded array with twice the size with the same elements
    def resize(self, new_capacity: int) -> None:
        new_array = StaticArray(new_capacity)
        for i in range(self.size):
            new_array[i] = self.data[i]
        self.data = new_array
        self.capacity = new_array.length()


# Create new instance of Dynamic_Array
my_list = Dynamic_Array()

# Build list with 10 items
for i in range(10):
  my_list.append(i)


for i in range(11):
  my_list.append(i)
# Output list
print(my_list)