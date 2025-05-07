def read_header(f):
    """Read PPM header and return magic number, width, height, maxval"""
    def read_token():
        while True:
            line = f.readline()
            if not line:
                raise ValueError("Unexpected EOF in header.")
            line = line.strip()
            if line.startswith(b'#') or len(line) == 0:
                continue
            for token in line.split():
                yield token

    token_gen = read_token()
    magic = next(token_gen)
    width = int(next(token_gen))
    height = int(next(token_gen))
    maxval = int(next(token_gen))
    return magic, width, height, maxval


def convert_p6_to_p3(input_path, output_path):
    with open(input_path, 'rb') as f:
        magic, width, height, max_val = read_header(f)

        if magic != b'P6':
            raise ValueError("Not a valid P6 PPM file.")

        # Read the rest (pixel data)
        pixel_data = f.read()
        expected = width * height * 3
        if len(pixel_data) < expected:
            raise ValueError(f"Pixel data too short. Expected {expected}, got {len(pixel_data)}")

    with open(output_path, 'w') as out:
        out.write("P3\n")
        out.write(f"{width} {height}\n")
        out.write(f"{max_val}\n")

        for i in range(0, expected, 3):
            r = pixel_data[i]
            g = pixel_data[i + 1]
            b = pixel_data[i + 2]
            out.write(f"{r} {g} {b}\n")
