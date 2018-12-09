# solution to Advent of Code 2018, day 9 part one and two
# https://adventofcode.com/2018/day/9
#
# usage: marbles.py [inputfile]

from collections import defaultdict
import fileinput

class Marble:
    """Class representing a marble

    Init params:
      number - the marble's number
    """
    def __init__(self, number):
        self._number = number
        self.next = self
        self.prev = self

    def get_number(self):
        """Returns the marble's number"""
        return self._number

    def __str__(self):
        """Returns a string representation of the marble"""
        return str(self._number)


class MarbleCircle:
    """Class representing a circle of marbles"""
    def __init__(self):
        self._head = Marble(0)
        self._current_marble = self._head
        self._size = 1
        self._max_marble_seen = 0

    def take_turn(self):
        """Take a turn by adding a marble to the circle

        Returns the score produced by this turn
        """
        score = 0
        new_marble = Marble(self._max_marble_seen+1)
        if self._size == 1:
            # special case when only 1 marble in the circle
            self._current_marble.next = new_marble
            self._current_marble.prev = new_marble
            new_marble.next = self._current_marble
            new_marble.prev = self._current_marble
            self._current_marble = new_marble
        elif new_marble.get_number() % 23 == 0:
            # scoring play
            score = new_marble.get_number()
            seven_back = self.rewind(7)
            new_current = seven_back.next
            score += seven_back.get_number()
            self.remove(seven_back)
            self._current_marble = new_current
        else:
            # standard marble insert
            insert_after = self._current_marble.next
            insert_before = self.advance(2)
            insert_after.next = new_marble
            new_marble.prev = insert_after
            new_marble.next = insert_before
            insert_before.prev = new_marble
            self._current_marble = new_marble
        # increment counters
        self._max_marble_seen += 1
        self._size += 1
        return score

    def remove(self, marble):
        """Remove a marble from the circle

        Input:
          marble - marble to remove
        """
        prev_marble = marble.prev
        next_marble = marble.next
        prev_marble.next = next_marble
        next_marble.prev = prev_marble

    def advance(self, count):
        """Returns a marble after the current marble

        Input:
          count - number of marbles to go forward

        Returns a Marble object
        """
        tmp = self._current_marble
        for i in range(0, count):
            tmp = tmp.next
        return tmp

    def rewind(self, count):
        """Returns a marble previous to current marble

        Input:
          count - number of marbles to go back

        Returns a Marble object
        """
        tmp = self._current_marble
        for i in range(0, count):
            tmp = tmp.prev
        return tmp

    def get_current_marble_value(self):
        """Returns the current marble's value"""
        return self._current_marble.get_number()

    def __str__(self):
        """Returns a string representation of the marble circle"""
        marbles = []
        current = self._head
        for i in range(0, self._size):
            num = current.get_number()
            if current == self._current_marble:
                num = f"({num})"
            marbles.append(f"{num:<3}")
            current = current.next
        return f"{' '.join(marbles)}"


def main():
    inputline = next(fileinput.input()).split(' ')

    # parse puzzle input
    tmp = inputline
    player_count = int(tmp[0])
    last_marble_worth = int(tmp[6])

    # solve part one
    high_score = play_game(player_count, last_marble_worth)
    print(f"High score, part one: {high_score}")

    # solve part two
    high_score = play_game(player_count, last_marble_worth*100)
    print(f"High score, part two: {high_score}")


def play_game(player_count, until):
    """Play the marble game

    Input:
      player_count - number of players
      until - last marble value

    Returns highest score among all players
    """
    # init variables for storing game state
    player_scores = defaultdict(int)
    last_marble = False
    game = MarbleCircle()

    while not last_marble:
        for i in range(1, player_count+1):
            score = game.take_turn()
            if score > 0:
                player_scores[i] += score
            if game.get_current_marble_value() == until:
                last_marble = True
    return(max(player_scores.values()))


if __name__ == '__main__':
    main()
