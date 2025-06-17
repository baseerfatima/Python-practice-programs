def binary_addition(a, b, chunk_size):
    """Perform binary addition with carry and wrap-around handling."""
    carry = 0
    result = ""

    a, b = a.zfill(chunk_size), b.zfill(chunk_size)

    for i in range(chunk_size - 1, -1, -1):
        total = int(a[i]) + int(b[i]) + carry
        result = str(total % 2) + result
        carry = total // 2

    if carry:
        result = binary_addition(result, '1'.zfill(chunk_size), chunk_size)

    return result[-chunk_size:]


def calculate_checksum(chunks, chunk_size):
    total_sum = "0" * chunk_size
    for chunk in chunks:
        total_sum = binary_addition(total_sum, chunk, chunk_size)

    checksum = ''.join('1' if bit == '0' else '0' for bit in total_sum)  # One's complement
    return total_sum, checksum


def detect_errors(original_data, received_data):
    """Detect errors and show flipped bit positions."""
    error_positions = [i for i in range(len(original_data)) if original_data[i] != received_data[i]]
    return error_positions


def main():
    chunk_size = int(input("Enter chunk size: "))
    data = input("Enter binary data: ").zfill(chunk_size)

    chunks = [data[i:i+chunk_size] for i in range(0, len(data), chunk_size)]
    sender_sum, sender_checksum = calculate_checksum(chunks, chunk_size)

    print(f"Sender Chunks: {chunks}")
    print(f"Sender Sum: {sender_sum}")
    print(f"Sender Checksum: {sender_checksum}")

    # Append checksum to the transmitted data
    transmitted_data = ''.join(chunks) + sender_checksum
    print(f"Transmitted Data (including Checksum): {transmitted_data}")

    # Transmission (Manual Entry of Received Data)
    received_data = input("Enter received binary data (including checksum): ").zfill(len(transmitted_data))

    received_chunks = [received_data[i:i+chunk_size] for i in range(0, len(received_data) - chunk_size, chunk_size)]
    received_checksum = received_data[-chunk_size:]

    print(f"Received Chunks: {received_chunks}")
    print(f"Received Checksum: {received_checksum}")

    receiver_sum, receiver_checksum = calculate_checksum(received_chunks + [received_checksum], chunk_size)

    print(f"Receiver Sum: {receiver_sum}")
    print(f"Receiver Checksum: {receiver_checksum}")

    if '0' in receiver_sum:
        print("Error detected!")
        error_positions = detect_errors(''.join(chunks) + sender_checksum, received_data)
        print(f"Error Positions: {error_positions}")
    else:
        print("No error detected! Transmission successful.")


if __name__ == "__main__":
    main()