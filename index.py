def to_bin_8bit(val: int) -> str:
    """Helper to display values as clean 8-bit binary strings."""
    return format(val & 0xFF, "08b")


def count_set_bits(val: int) -> int:
    """Counts the number of set bits (1s) in a number."""
    # Alternatively, you can use val.bit_count() in Python 3.10+
    count = 0
    while val > 0:
        count += val & 1
        val >>= 1
    return count


def bit_scanner():
    print("=" * 45)
    print("      MY SECRET CODE BIT SCANNER      ")
    print("=" * 45)

    # 1. Input Values
    try:
        secret_code = int(input("Enter Secret Code (0-255): "))
        access_key = int(input("Enter Access Key (0-255):  "))
    except ValueError:
        print("Please enter valid integers.")
        return

    print("\n--- 1. Binary Representations ---")
    print(f"Secret Code : {secret_code:>3}  ->  [0b{to_bin_8bit(secret_code)}]")
    print(f"Access Key  : {access_key:>3}  ->  [0b{to_bin_8bit(access_key)}]")

    print("\n--- 2. Bitwise Comparisons ---")
    and_result = secret_code & access_key
    or_result = secret_code | access_key
    xor_result = secret_code ^ access_key

    print(
        f"AND  (Code & Key) : {and_result:>3}  ->  [0b{to_bin_8bit(and_result)}]  (Matching active bits)"
    )
    print(
        f"OR   (Code | Key) : {or_result:>3}  ->  [0b{to_bin_8bit(or_result)}]  (Combined active bits)"
    )
    print(
        f"XOR  (Code ^ Key) : {xor_result:>3}  ->  [0b{to_bin_8bit(xor_result)}]  (Differing bits)"
    )

    print("\n--- 3. Bit Inversion / Flipping ---")
    # Masking with 0xFF keeps the display focused on an 8-bit byte representation
    flipped_code = ~secret_code & 0xFF
    print(f"NOT  (~Code)      : {flipped_code:>3}  ->  [0b{to_bin_8bit(flipped_code)}]")

    print("\n--- 4. Bit Shifting (Secret Code) ---")
    left_shift = (secret_code << 1) & 0xFF
    right_shift = secret_code >> 1
    print(f"Left Shift  (<< 1): {left_shift:>3}  ->  [0b{to_bin_8bit(left_shift)}]")
    print(f"Right Shift (>> 1): {right_shift:>3}  ->  [0b{to_bin_8bit(right_shift)}]")

    print("\n--- 5. Bit Counter ---")
    print(f"Set bits (1s) in Secret Code : {count_set_bits(secret_code)}")
    print(f"Set bits (1s) in Access Key  : {count_set_bits(access_key)}")
    print(f"Mismatched bits (Hamming Dist): {count_set_bits(xor_result)}")


if __name__ == "__main__":
    bit_scanner()