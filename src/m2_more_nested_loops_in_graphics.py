"""
This project demonstrates NESTED LOOPS (i.e., loops within loops)
in the context of TWO-DIMENSIONAL GRAPHICS.

Authors: David Mutchler, Valerie Galluzzi, Mark Hays, Amanda Stouder,
         their colleagues and Kathi Munoz.
"""  # Done: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


def main():
    """ Calls the other functions to test them. """
    run_test_draw_upside_down_wall()


def run_test_draw_upside_down_wall():
    """ Tests the    draw_upside_down_wall    function. """
    # Tests 1 and 2 are ALREADY DONE (here).
    window = rg.RoseWindow(550, 300, 'Upside-down wall, Tests 1 and 2')

    rectangle = rg.Rectangle(rg.Point(125, 230), rg.Point(155, 250))
    draw_upside_down_wall(rectangle, 8, window)

    rectangle = rg.Rectangle(rg.Point(375, 175), rg.Point(425, 225))
    draw_upside_down_wall(rectangle, 4, window)

    window.close_on_mouse_click()


def draw_upside_down_wall(rectangle, n, window):
    """
    See   MoreWalls.pdf   in this project for pictures that may
    help you better understand the following specification:

    Draws an "upside-down wall" on the given window, where:
      -- The BOTTOM of the wall is a single "brick"
            that is the given rg.Rectangle.
      -- There are n rows in the wall.
      -- Each row is a row of "bricks" that are the same size
            as the given rg.Rectangle.
      -- Each row has one more brick than the row below it.
      -- Each row is centered on the bottom row.

    Preconditions:
      :type rectangle: rg.Rectangle
      :type n: int
      :type window: rg.RoseWindow
    and n is nonnegative.
    """
    # ------------------------------------------------------------------
    # done: 2. Implement and test this function.
    #     Some tests are already written for you (above).
    # ------------------------------------------------------------------
    og_rect_ul = rectangle.get_upper_left_corner()
    og_rect_lr = rectangle.get_lower_right_corner()
    ul = rg.Point(og_rect_ul.x, og_rect_ul.y)
    lr = rg.Point(og_rect_lr.x, og_rect_lr.y)
    for k in range(n):
        remember_ulx = ul.x
        remember_lrx = lr.x
        for l in range(k+1):
            new_rect = rg.Rectangle(ul, lr)
            new_rect.attach_to(window)
            window.render(0.2)
            ul.x = ul.x + rectangle.get_width()
            lr.x = lr.x + rectangle.get_width()
        ul.x = remember_ulx - 0.5*rectangle.get_width()
        lr.x = remember_lrx - 0.5*rectangle.get_width()
        ul.y = ul.y - rectangle.get_height()
        lr.y = lr.y - rectangle.get_height()


        # ul.x = ul.x - 0.5*rectangle.get_width()
        # ul.y = ul.y - rectangle.get_height()
        # lr.x = lr.x - 0.5*rectangle.get_width()
        # lr.y = lr.y - rectangle.get_height()





# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
