from tkinter import Tk, BOTH, Canvas

class Window:
  def __init__(self, width, height):
    self.__root = Tk()
    self.__root.title('Maze Solver')
    self.__root.protocol("WM_DELETE_WINDOW", self.close)
    self.__canvas = Canvas(self.__root, bg="white", height=height, width=width)
    self.__canvas.pack(fill=BOTH, expand=1)
    self.window_running = False

  def redraw(self):
    self.__root.update_idletasks()
    self.__root.update()

  def wait_for_close(self):
    self.window_running = True
    while self.window_running:
      self.redraw()
    print("window closed...")

  def draw_line(self, line, fill_color='black'):
    line.draw(self.__canvas, fill_color)

  def close(self):
    self.window_running = False



class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y

class Line:
  def __init__(self, p1, p2):
    self.p1 = p1
    self.p2 = p2

  def draw(self, canvas, fill_color='black'):
    canvas.create_line(self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fill_color, width=2)

class Cell:
  def __init__(
      self,
      x1,
      x2,
      y1,
      y2,
      window,
      has_left_wall=True,
      has_right_wall=True,
      has_top_wall=True,
      has_bottom_wall=True):
    
    self.has_left_wall = has_left_wall
    self.has_right_wall = has_right_wall
    self.has_top_wall = has_top_wall
    self.has_bottom_wall = has_bottom_wall
    self._x1 = x1
    self._x2 = x2
    self._y1 = y1
    self._y2 = y2
    self._win = window