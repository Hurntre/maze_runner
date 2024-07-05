from graphics import Point, Line

class Cell:
  def __init__(self, window=None):
    self.has_left_wall = True
    self.has_right_wall = True
    self.has_top_wall = True
    self.has_bottom_wall = True
    self.visited = False
    self._x1 = None #top_left_corner
    self._x2 = None #bottom_right_corner
    self._y1 = None #top_left_corner
    self._y2 = None #bottom_right_corner
    self._win = window

  def draw(self, x1, x2, y1, y2):
    self._x1 = x1
    self._x2 = x2
    self._y1 = y1
    self._y2 = y2
  
    if self.has_left_wall:
      left_wall = Line(Point(self._x1, self._y1), Point(self._x1,self._y2))
      self._win.draw_line(left_wall)

    if self.has_right_wall:
      right_wall = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
      self._win.draw_line(right_wall)

    if self.has_top_wall:
      top_wall = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
      self._win.draw_line(top_wall)

    if self.has_bottom_wall:
      bottom_wall = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))
      self._win.draw_line(bottom_wall)

  def draw_move(self, to_cell, undo=False):
    x_center = abs(self._x2 - self._x1) // 2 + self._x1
    y_center = abs(self._y2 - self._y1) // 2 + self._y1

    x_center2 = abs(to_cell._x2 - to_cell._x1) + to_cell._x1
    y_center2 = abs(to_cell._y2 - to_cell._y1) + to_cell._y1

    fill_color = "red"
    if undo:
        fill_color = "gray"

    line = Line(Point(x_center, y_center), Point(x_center2, y_center2))
    self._win.draw_line(line, fill_color)
