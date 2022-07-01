"""
File: babygraphics.py
Name: Lina Chou
--------------------------------
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950,
         1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index where the current year is in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                            with the current year.
    """

    new_width = width - 2 * GRAPH_MARGIN_SIZE
    average_width = new_width/len(YEARS)
    x_coordinate = GRAPH_MARGIN_SIZE + year_index * average_width
    return x_coordinate


def draw_fixed_lines(canvas):
    """
    Draws the fixed background lines on the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # ----- Write your code below this line ----- #
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE)
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, CANVAS_WIDTH - GRAPH_MARGIN_SIZE,
                       CANVAS_HEIGHT-GRAPH_MARGIN_SIZE)
    for i in range(len(YEARS)):
        x_place = get_x_coordinate(CANVAS_WIDTH, i)
        canvas.create_line(x_place, 0, x_place, CANVAS_HEIGHT)
        canvas.create_text(x_place+TEXT_DX, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, text=YEARS[i], anchor=tkinter.NW)


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # ----- Write your code below this line ----- #
    j = -1
    y_range = (CANVAS_HEIGHT - 2*GRAPH_MARGIN_SIZE)/MAX_RANK  # 取畫布上,下方界線範圍與資料最低保留名次的比例
    for i in range(len(lookup_names)):
        j += 1
        if j == len(COLORS):  # 為避免當i的迴圈次數大於len(COLORS), 將j歸零重複指定顏色
            j -= len(COLORS)
        for k in range(len(YEARS)-1):
            if str(YEARS[k+1]) not in name_data[lookup_names[i]]:  # 指定'下一個年份' y的位置
                next_rank_y = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
            else:
                next_rank_y = int(name_data[lookup_names[i]][str(YEARS[k+1])])*y_range+GRAPH_MARGIN_SIZE
            if str(YEARS[k]) in name_data[lookup_names[i]]:  # 指定'此年分' y的位置,排行,畫線以及文字
                rank = int(name_data[lookup_names[i]][str(YEARS[k])])
                canvas.create_line(get_x_coordinate(CANVAS_WIDTH, k), rank*y_range+GRAPH_MARGIN_SIZE,
                                   get_x_coordinate(CANVAS_WIDTH, k+1), next_rank_y, width=LINE_WIDTH, fill=COLORS[j])
                canvas.create_text(get_x_coordinate(CANVAS_WIDTH, k)+TEXT_DX, rank*y_range+GRAPH_MARGIN_SIZE,
                                   text=lookup_names[i]+" "+str(rank), anchor=tkinter.SW, fill=COLORS[j])
                if k == len(YEARS)-2:  # 當k為最後一個年份
                    if str(YEARS[k+1]) in name_data[lookup_names[i]]:
                        canvas.create_text(get_x_coordinate(CANVAS_WIDTH, k+1), next_rank_y,
                                           text=lookup_names[i] + name_data[lookup_names[i]][str(YEARS[k + 1])],
                                           anchor=tkinter.SW, fill=COLORS[j])
                    else:
                        canvas.create_text(get_x_coordinate(CANVAS_WIDTH, k+1), next_rank_y,
                                           text=lookup_names[i] + '*',
                                           anchor=tkinter.SW, fill=COLORS[j])

            else:
                next_y_none = CANVAS_HEIGHT-GRAPH_MARGIN_SIZE
                canvas.create_line(get_x_coordinate(CANVAS_WIDTH, k), next_y_none, get_x_coordinate(CANVAS_WIDTH, k+1),
                                   next_rank_y, width=LINE_WIDTH, fill=COLORS[j])
                canvas.create_text(get_x_coordinate(CANVAS_WIDTH, k)+TEXT_DX, next_y_none, text=lookup_names[i] + "  *",
                                   anchor=tkinter.SW, fill=COLORS[j])
                if k == len(YEARS)-2:  # 當k為最後一個年份
                    canvas.create_text(get_x_coordinate(CANVAS_WIDTH, k+1), next_rank_y, text=lookup_names[i] + "  *",
                                       anchor=tkinter.SW, fill=COLORS[j])

# main() code is provided, feel free to read through it but DO NOT MODIFY


def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
