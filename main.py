import sys

def read_input_file(file_path):
    try:
        with open(file_path, 'r') as file:
            data = []
            for line in file:
                try:
                    data.append(float(line.strip()))
                except ValueError:
                    continue  # Skips invalid values
        return data
    except FileNotFoundError:
        print("Error: File not found.")
        sys.exit(1)

def perform_calculations(data):
    total = sum(data)
    average = total / len(data) if data else 0
    return total, average

def write_output_file(output_path, total, average):
    try:
        with open(output_path, 'w') as file:
            file.write(f"Sum: {total}\n")
            file.write(f"Average: {average}\n")
        print(f"Results saved to {output_path}")
    except IOError:
        print("Error: Unable to write to output file.")
        sys.exit(1)

def main():
    input_file = "input.txt"  # Change this to match your file
    output_file = "output.txt"

    data = read_input_file(input_file)
    total, average = perform_calculations(data)
    write_output_file(output_file, total, average)

if __name__ == "__main__":
    main()
