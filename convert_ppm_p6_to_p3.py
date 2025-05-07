def convert_p6_to_p3(input_path, output_path):
    with open(input_path, "rb") as f:
        magic_number = f.readline().strip()
        if magic_number != b'P6':
            raise ValueError("Not a P6 PPM file.")

        # Skip comments
        def read_non_comment_line(f):
            line = f.readline()
            while line.startswith(b'#'):
                line = f.readline()
            return line

        dimensions = read_non_comment_line(f)
        width, height = map(int, dimensions.strip().split())

        maxval = int(read_non_comment_line(f).strip())

        pixel_data = f.read()

    with open(output_path, "w") as out:
        out.write("P3\n")
        out.write(f"{width} {height}\n")
        out.write(f"{maxval}\n")

        for i in range(0, len(pixel_data), 3):
            r, g, b = pixel_data[i], pixel_data[i+1], pixel_data[i+2]
            out.write(f"{r} {g} {b}\n")

if __name__ == "__main__":
    convert_p6_to_p3("/home/data/colorP6File.ppm", "colorP3File.ppm")


