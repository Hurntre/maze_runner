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
    self._window = window

  def draw(self, x1, x2, y1, y2):
    if self._window is None:
      return
    self._x1 = x1
    self._x2 = x2
    self._y1 = y1
    self._y2 = y2
  
    if self.has_left_wall:
        left_wall = Line(Point(self._x1, self._y1), Point(self._x1,self._y2))
        self._window.draw_line(left_wall)
    else:
        left_wall = Line(Point(self._x1, self._y1), Point(self._x1,self._y2))
        self._window.draw_line(left_wall, 'white')
      
    if self.has_top_wall:
        top_wall = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
        self._window.draw_line(top_wall)
    else:
        top_wall = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
        self._window.draw_line(top_wall, 'white')

    if self.has_right_wall:
        right_wall = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
        self._window.draw_line(right_wall)
    else:
        right_wall = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
        self._window.draw_line(right_wall, 'white')

    if self.has_bottom_wall:
        bottom_wall = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))
        self._window.draw_line(bottom_wall)
    else:
        bottom_wall = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))
        self._window.draw_line(bottom_wall, 'white')
      

  def draw_move(self, to_cell, undo=False):
    # My implementation 
    # x_center = abs(self._x2 - self._x1) // 2 + self._x1
    # y_center = abs(self._y2 - self._y1) // 2 + self._y1

    # x_center2 = abs(to_cell._x2 - to_cell._x1) + to_cell._x1
    # y_center2 = abs(to_cell._y2 - to_cell._y1) + to_cell._y1

    # Tutors implementation
    half_length = abs(self._x2 - self._x1) // 2
    x_center = half_length + self._x1
    y_center = half_length + self._y1

    half_length2 = abs(to_cell._x2 - to_cell._x1) // 2
    x_center2 = half_length2 + to_cell._x1
    y_center2 = half_length2 + to_cell._y1

    fill_color = "red"
    if undo:
        fill_color = "gray"

    line = Line(Point(x_center, y_center), Point(x_center2, y_center2))
    self._window.draw_line(line, fill_color)
