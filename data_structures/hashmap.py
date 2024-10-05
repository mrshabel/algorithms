class Pair:
    """
    This represents a key-value pair of a hashmap
    """
    def __init__(self, key, val):
        self.key= key
        self.val = val


class HashMap:
    """
    An implementation that uses array under the hood and resolves collisions.
    The array stores the key and value of the hashmap entry.
    """
    def __init__(self) -> None:
        """
        Initialize a hashmap by keeping track of its size and capacity. default size 0 and capacity 2
        """
        self._size = 0
        self._capacity = 2
        self._map: list[Pair | None] = [None, None]
    
    def _hash(self, key) -> int:
        """
        Computes the hash of a provided key using its ASCII value representation and return its position
        """
        hash_code = 0

        for character in key:
            hash_code += ord(character)
        
        return hash_code % self._capacity
    
    def get(self, key):
        """
        Retrieve the value associated with the provided key
        """
        # recompute the hash again to determine the position
        position = self._hash(key)

        # to accurately find the element, if a different pair is linked to its position, iterate over the internal array to locate its new position
        # this is as a result of that position being openly addressed
        while self._map[position] != None:
            if self._map[position].key == key:
                return self._map[position].val
            
            # use an incremental approach to find the new position. position can be out of bounds hence the need to pick the modulus
            position  = (position + 1) % self._capacity

        return None
    
    def put(self, key, val):
        """
        Store a key-pair entry in the hashmap
        """
        # compute the position of the key
        position = self._hash(key)

        # incrementally iterate through the internal map to find the next available address until the conditions have been met
        while True:
            # replace value if key already exists
            if self._map[position] and self._map[position].key == key:
                self._map[position].val = val
                return
            
            # create a new pair when the position is available
            if self._map[position] == None:
                self._map[position] = Pair(key=key, val=val)
                # increment size
                self._size += 1

                # increase capacity and rehash only when over half of it is used
                if self._size >= self._capacity // 2:
                    self._rehash()
                
                return
                
            # increment position to find next available address incase it is occupied
            position = (position + 1) % self._capacity

    
    def _rehash(self):
        """
        Increase the capacity of the hashmap and rehash
        """
        # double capacity. the next available prime number can be computed to reduce collisions
        self._capacity *= 2

        # create empty entries for the new map with the same capacity as the old map
        new_map: list[Pair | None] = [None for _ in range(self._capacity)]

        # save current map in a temporal buffer
        temp_map = self._map

        # assign internal map to new map and reset the size. the put function increments the size hence the reset
        self._map = new_map
        self._size = 0

        # now place the old entries in the new map
        for entry in temp_map:
            self.put(key=entry.key, val=entry.val)

