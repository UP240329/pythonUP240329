from random import randint, choice, shuffle, sample
def list_of_hexa_colors():
    hex_colors = []
    for i in range(5):
        hex_color = '#'
        for j in range(6):
            hex_color += choice('0123456789abcdef')
        hex_colors.append(hex_color)
    return hex_colors
print(list_of_hexa_colors())

def list_of_rgb_colors():
    rgb_colors = []
    for i in range(10):
        rgb_color = rgb_color_gen()
        rgb_colors.append(rgb_color)
    return rgb_colors
print(list_of_rgb_colors())

def generate_colors(n):
    hex_colors = list_of_hexa_colors()  
    rgb_colors = list_of_rgb_colors()
    colors = []
    for i in range(n):
        colors.append((hex_colors[i], rgb_colors[i]))
    return colors   
print(generate_colors(5))