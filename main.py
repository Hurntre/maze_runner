from graphics import Window
from cell import Cell


def main():

  win = Window(800, 600)

  c = Cell(win)
  c.has_left_wall = False
  c.draw(30, 60, 60, 120)

  c = Cell(win)
  c.has_right_wall = False
  c.draw(65, 95, 125, 185)

  c = Cell(win)
  c.has_bottom_wall = False
  c.draw(100, 130, 190, 250)

  c = Cell(win)
  c.has_top_wall = False
  c.draw(135, 165, 255, 315)

  win.wait_for_close()

main()