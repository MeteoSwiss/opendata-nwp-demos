import os

def load_ncl_rgb_colors(name, base_path="plot_utils/colormaps"):
    path = os.path.join(base_path, f"{name}.rgb")
    if not os.path.exists(path):
        raise FileNotFoundError(f"Colormap file not found: {path}")

    colors = []
    levels = []

    with open(path) as f:
        lines = [line.strip() for line in f if line.strip() and not line.startswith("#")]


    # Second line: levels
    level_line = lines[1]
    levels = list(map(float, level_line.split()))

    # Remaining lines: RGB values
    for line in lines[2:]:
        parts = line.split()
        if len(parts) == 3:
            r, g, b = map(int, parts)
            colors.append((r / 255, g / 255, b / 255))

    return colors, levels
