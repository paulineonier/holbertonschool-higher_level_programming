#!/usr/bin/python3
class VerboseList(list):
    
    def append(self, item):
        super().append(item)
        print(f"Added {item} to the list.")
    
    def extend(self, items):
        super().extend(items)
        print(f"Extended the list with {len(items)} items.")
    
    def remove(self, item):
        if item in self:
            super().remove(item)
            print(f"Removed {item} from the list.")
        else:
            print(f"Item {item} not found in the list.")
    
    def pop(self, index=None):
        if index is None:
            item = super().pop()
            print(f"Popped {item} from the list.")
        else:
            item = super().pop(index)
            print(f"Popped {item} from index {index} of the list.")
        return item

# Testing the VerboseList class
if __name__ == "__main__":
    vlist = VerboseList()
    
    # Test append method
    vlist.append(1)
    vlist.append(2)
    
    # Test extend method
    vlist.extend([3, 4, 5])
    
    # Test remove method
    vlist.remove(3)
    vlist.remove(10)  # Trying to remove an item not in the list
    
    # Test pop method
    vlist.pop()
    vlist.pop(0)
