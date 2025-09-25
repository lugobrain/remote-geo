import laspy
import io

def run(uploaded_file, z_min=0.0, z_max=10.0):
    # Read LAS/LAZ file
    with uploaded_file as f:
        las = laspy.read(f)

    # Filter points by Z range
    mask = (las.z >= z_min) & (las.z <= z_max)
    filtered = las.points[mask]

    # Create new LAS file
    new_las = laspy.LasData(las.header)
    new_las.points = filtered

    # Save to buffer
    buf = io.BytesIO()
    new_las.write(buf)
    buf.seek(0)
    return buf
