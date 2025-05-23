import os

# Return list of colors instead of a colormap object
def load_ncl_rgb_colors(name, base_path="plot_utils/colormaps"):
    path = os.path.join(base_path, f"{name}.rgb")
    if not os.path.exists(path):
        raise FileNotFoundError(f"Colormap file not found: {path}")

    colors = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#") or "ncolors" in line:
                continue
            parts = line.split()
            if len(parts) == 3:
                r, g, b = map(int, parts)
                colors.append((r / 255, g / 255, b / 255))

    return colors
