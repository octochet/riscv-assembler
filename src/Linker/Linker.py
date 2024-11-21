import struct
import os

def combine_binaries(input_files, output_file):
    with open(output_file, 'wb') as exec_file:
        offsets = []
        current_offset = 4 + (8 * len(input_files))  # Header + metadata
        exec_file.write(struct.pack("I", len(input_files)))  # Number of files

        # Reserve space for offsets and sizes
        exec_file.seek(current_offset)

        for file in input_files:
            with open(file, 'rb') as f:
                data = f.read()
                exec_file.write(data)
                offsets.append((current_offset, len(data)))
                current_offset += len(data)

        # Write offsets and sizes in the header
        exec_file.seek(4)  # Skip number of files
        for offset, size in offsets:
            exec_file.write(struct.pack("II", offset, size))


def extract_binaries(exec_file_path, output_dir):
    with open(exec_file_path, 'rb') as f:
        num_files = struct.unpack("I", f.read(4))[0]
        offsets = [struct.unpack("II", f.read(8)) for _ in range(num_files)]

        for i, (offset, size) in enumerate(offsets):
            f.seek(offset)
            data = f.read(size)
            with open(os.path.join(output_dir, f"file_{i}.bin"), 'wb') as out_file:
                out_file.write(data)


if __name__ == "__main__":
    import tempfile

    with tempfile.TemporaryDirectory() as temp_dir:
        # Create test files
        input_files = []
        for i in range(3):
            input_file = os.path.join(temp_dir, f"input_{i}.bin")
            with open(input_file, 'wb') as f:
                f.write(bytes([i] * (10 + i)))  # Write test data
            input_files.append(input_file)

        # Define combined binary file path
        combined_exec_file = os.path.join(temp_dir, "combined_exec.bin")

        # Combine binaries into a single executable file
        combine_binaries(input_files, combined_exec_file)

        # Extract binaries from the combined file
        extracted_dir = os.path.join(temp_dir, "extracted")
        os.makedirs(extracted_dir, exist_ok=True)
        extract_binaries(combined_exec_file, extracted_dir)

        # Compare extracted files with the original files
        for i, input_file in enumerate(input_files):
            extracted_file = os.path.join(extracted_dir, f"file_{i}.bin")
            with open(input_file, 'rb') as original, open(extracted_file, 'rb') as extracted:
                original_data = original.read()
                extracted_data = extracted.read()
                assert original_data == extracted_data, f"Mismatch in file {i}"

        print("All test cases passed successfully!")
