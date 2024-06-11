def color_invert(rgb: tuple) -> tuple:
    r, g, b = rgb
    return (255 - r, 255 - g, 255 - b)

if __name__ == '__main__':
    print(color_invert((165, 170, 221)))

    