def solution(brown, yellow):
    for y_width in range(1, yellow+1):
        if yellow % y_width == 0:
            y_height = yellow // y_width
            if y_height > y_width:
                temp = y_height
                y_height = y_width
                y_width = temp
            if brown == ((y_width+2)*(y_height+2) - yellow):
                return [y_width+2, y_height+2]