class SortingRobot:
    def __init__(self, l):
        """
        SortingRobot takes a list and sorts it.
        """
        self._list = l   # The list the robot is tasked with sorting
        self._item = None   # The item the robot is holding
        self._position = 0    # The list position the robot is at
        self._light = "OFF"    # The state of the robot's light
        self._time = 0   # A time counter (stretch)

    def can_move_right(self):
        """
        Returns True if the robot can move right or False if it's
        at the end of the list.
        """
        return self._position < len(self._list) - 1

    def can_move_left(self):
        """
        Returns True if the robot can move left or False if it's
        at the start of the list.
        """
        return self._position > 0

    def move_right(self):
        """
        If the robot can move to the right, it moves to the right and
        returns True. Otherwise, it stays in place and returns False.

        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position < len(self._list) - 1:
            self._position += 1
            return True
        else:
            return False

    def move_left(self):
        """
        If the robot can move to the left, it moves to the left and
        returns True. Otherwise, it stays in place and returns False.

        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position > 0:
            self._position -= 1
            return True
        else:
            return False

    def swap_item(self):
        """
        The robot swaps its currently held item with the list item in front
        of it.

        This will increment the time counter by 1.
        """
        self._time += 1
        # Swap the held item with the list item at the robot's position
        self._item, self._list[self._position] = self._list[self._position], self._item

    def compare_item(self):
        """
        Compare the held item with the item in front of the robot:

        If the held item's value is greater, return 1.
        If the held item's value is less, return -1.
        If the held item's value is equal, return 0.
        If either item is None, return None.
        """
        if self._item is None or self._list[self._position] is None:
            return None
        elif self._item > self._list[self._position]:
            return 1
        elif self._item < self._list[self._position]:
            return -1
        else:
            return 0
    

    def set_light_on(self):
        """
        Turn on the robot's light
        """
        self._light = "ON"
    def set_light_off(self):
        """
        Turn off the robot's light
        """
        self._light = "OFF"
    def light_is_on(self):
        """
        Returns True if the robot's light is on and False otherwise.
        """
        return self._light == "ON"

    def sort(self):
        """
        Sort the robot's list.
        """
        # First Attempt
        # compare item and the item at list[position]
        # if item is gretater than list[position] and you can move right
        #       swap them and move right
        # if item is less than list[position] and you can move left 
        #       move left until item is greater thsn list[position] then swap
        #
        # looping through the steps above and will give you a sorted list
        # 
        # [4, 3, 2, 1] position: 0 value: None
        # [None, 3, 2 ,1] position: 1 value: 4
        # [None, 4, 2, 1] position: 0 value: 3
        # [3, 4, 2, 1] position: 0 value: None
        # [3, None, 2, 1] position: 1 value: 4
        # [3, None, 2, 1] position: 2 value: 4
        # [3, 4, None, 1] position: 2 value: 2
        # [3, 4, None, 1] position: 1 value: 2
        # [3, 4, None, 1] position: 0 value: 2
        # [2, 4, None, 1] position: 1 value: 3
        # [2, 3, None, 1] position: 2 value: 4
        # [2, 3, 4, 1] position: 2 value: None
        # [2, 3, 4, 1] position: 3 value: None
        # [2, 3, 4, None] position: 2 value: 1
        # [2, 3, 4, None] position: 1 value: 1
        # [2, 3, 4, None] position: 0 value: 1
        # [1, 3, 4, None] position: 0 value: 2
        # [1, 2, 4, None] position: 0 value: 3
        # [1, 2, 3, None] position: 0 value: 4
        # [1, 2, 3, 4] position: 0 value: None
        #

        # Working attempt
        # start with light off
        # while light is not on
            # set the light on
            # while the robot can move right
                # swap item
                # move right
                # if compare value is 0
                    # swap item
                    # set light off
                    # move left
                    #swap item
                    # move right
                # if light is on break
            # turn light on

        # start with light off
        while self.light_is_on() == False:
            # set light on
            self.set_light_on()

            # while not at the end of list
            while self.can_move_right():
                # pick up item
                self.swap_item()
                self.move_right()

                # if current item is > then item at position
                if self.compare_item() == 1:
                    # switch light off because list is not fully sorted
                    self.set_light_off()
                    # swap both numbers and go back to holding nothing
                    self.swap_item()
                    self.move_left()
                    self.swap_item()
                    self.move_right()

                else:
                    # if item is sorted
                    # get rid of None in list and move forward
                    self.move_left()
                    self.swap_item()
                    self.move_right()

            # go back to the begining and try to sort again
            if self.light_is_on() == False:
                while self.can_move_left():
                    self.move_left()
            



robot = SortingRobot([5, 4, 3, 2, 1])
robot.sort()
print(robot._list)
    
# if __name__ == "__main__":
#     # Test our your implementation from the command line
#     # with `python robot_sort.py`

#     l = [15, 41, 58, 49, 26, 4, 28, 8, 61, 60, 65, 21, 78, 14, 35, 90, 54, 5, 0, 87, 82, 96, 43, 92, 62, 97, 69, 94, 99, 93, 76, 47, 2, 88, 51, 40, 95, 6, 23, 81, 30, 19, 25, 91, 18, 68, 71, 9, 66, 1, 45, 33, 3, 72, 16, 85, 27, 59, 64, 39, 32, 24, 38, 84, 44, 80, 11, 73, 42, 20, 10, 29, 22, 98, 17, 48, 52, 67, 53, 74, 77, 37, 63, 31, 7, 75, 36, 89, 70, 34, 79, 83, 13, 57, 86, 12, 56, 50, 55, 46]

#     robot = SortingRobot(l)

#     robot.sort()
#     print(robot._list)




