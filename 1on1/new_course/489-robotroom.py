# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
# class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """


class Solution:
    def __init__(self):
        self.turn_cnt = 0
        self.cur_x, self.cur_y = 0, 0
        self.map = {}
        self.x_, self.y_ = [-1, 0, 1, 0], [0, 1, 0, -1]
        self.opp = {0: 2, 1: 3, 2: 0, 3: 1}

    def cleanRoom(self, robot):
        cur_cnt = self.turn_cnt
        self.map[(self.cur_x, self.cur_y)] = 1
        robot.clean()
        moved = 0
        while robot.move():
            moved += 1
            self.cur_x = self.cur_x + self.x_[cur_cnt]
            self.cur_y = self.cur_y + self.y_[cur_cnt]
            self.map[(self.cur_x, self.cur_y)] = 1
            robot.clean()
        self.blk_x = self.cur_x + self.x_[cur_cnt]
        self.blk_y = self.cur_y + self.y_[cur_cnt]
        self.map[(self.blk_x, self.blk_y)] = 0

        # try all nxt_directions(x4)  dfs()
        for i in range(4):
            if i != cur_cnt:
                nxt_x, nxt_y = self.cur_x+self.x_[i], self.cur_y+self.y_[i]
                if (nxt_x, nxt_y) not in self.map:
                    left, right = 0, 0
                    if i - self.turn_cnt > 0:
                        for k in range(i-self.turn_cnt):
                            robot.turnRight()
                    else:
                        for k in range(self.turn_cnt-i):
                            robot.turnLeft()
                    self.turn_cnt = i
                    self.cleanRoom(robot)
        # robot 还需要开回到dfs()启动前的状态    通过moved和i 两个属性来操作
        back_cnt = self.opp[cur_cnt]
        if back_cnt - self.turn_cnt > 0:
            for k in range(back_cnt - self.turn_cnt):
                robot.turnRight()
        else:
            for k in range(self.turn_cnt - back_cnt):
                robot.turnLeft()
        while moved:
            moved -= 1
            robot.move()
        for k in range(2):
            robot.turnRight()
        self.turn_cnt = cur_cnt
