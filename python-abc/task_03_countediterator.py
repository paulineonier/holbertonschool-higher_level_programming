#!/usr/bin/python3
class CountedIterator:
    def __init__(self, iterable):
        self.iterator = iter(iterable)
        self.counter = 0

    def __next__(self):
        try:
            item = next(self.iterator)
            self.counter += 1
            return item
        except StopIteration:
            raise StopIteration("No more items in the iterator.")

    def get_count(self):
        return self.counter

# Testing the CountedIterator class
if __name__ == "__main__":
    # Instantiate a CountedIterator object with a list
    counted_iter = CountedIterator([1, 2, 3, 4, 5])

    # Iterate over items and print them
    for item in counted_iter:
        print(item)

    # Print the count of items iterated
    print("Count of items iterated:", counted_iter.get_count())
