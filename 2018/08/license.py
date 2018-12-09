# solution to Advent of Code 2018, day 8 part one and two
# https://adventofcode.com/2018/day/8
#
# assumes puzzle input is in a file called input.txt

import fileinput
from collections import deque

class LicenseNode():
    """Class representing a tree of LicenseNodes

    Init Params:
      child_count - number of child nodes
      metadata_count - number of metadata entries
    """
    def __init__(self, child_count, metadata_count):
        self._child_count = child_count
        self._metadata_count = metadata_count
        self._children = []
        self._metadata = []
        pass

    def __str__(self):
        """Returns a string representation of the LicenseNode"""
        children = [c for c in self._children]
        return f"<{self._child_count} {self._metadata_count} {children} {self._metadata}>"

    def add_child(self, child):
        """Add a child to the LicenseNode"""
        self._children = self._children + [child]

    def add_metadata(self, meta):
        """Add a metadata entry to the LicenseNode"""
        self._metadata = self._metadata + [meta]

    def sum_all_metadata(self):
        """Return the sum of the LicenseNode's metadata plus all child metadata"""
        return sum(self._metadata) + sum([child.sum_all_metadata() for child in self._children])

    def value(self):
        """Return the value of the LicenseNode"""
        if not self._children:
            return sum(self._metadata)
        else:
            return sum([self._children[meta-1].value() for meta in self._metadata if (meta-1) in range(0, len(self._children))])


def extract(nums):
    """Given a list of numbers, recursively construct a LicenseNode
    object that represents the tree

    Input:
      nums - list of numbers in license file

    Returns a LicenseNode object
    """
    child_count = nums.popleft()
    metadata_count = nums.popleft()
    node = LicenseNode(child_count, metadata_count)

    if child_count == 0:
        for i in range(0, metadata_count):
            node.add_metadata(nums.popleft())
        return node

    for child in range(0,child_count):
        node.add_child(extract(nums))
    for i in range(0, metadata_count):
        node.add_metadata(nums.popleft())
    return node


def main():
    inputline = next(fileinput.input()).strip()

    # convert puzzle input to list of numbers
    nums = deque([int(n) for n in inputline.split(' ')])

    # extract license tree
    license = extract(nums)

    # solve part one
    print('metadata sum:', license.sum_all_metadata())

    # solve part two
    print('root value:', license.value())


if __name__ == '__main__':
    main()
