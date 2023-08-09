class Colors:
    dark_grey = (26, 31, 40)
    green = (47, 230, 23)
    red = (26, 31, 18)
    orange = (44, 116, 17)
    yellow = (99, 115, 4)
    purple = (165, 126, 220)
    cyan = (195, 207, 215)
    blue = (112, 165, 233)


    @classmethod
    def get_cell_colors(cls):
        return [cls.dark_grey, cls.green, cls.red, cls.orange, cls.yellow, cls.purple, cls.cyan, cls.blue]
    
