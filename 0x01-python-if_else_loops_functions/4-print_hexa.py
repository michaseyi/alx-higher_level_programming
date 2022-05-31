#!/usr/bin/python3
for i in range(0, 99):
    print("{} = 0x{}{}"
          .format(i,
                  "" if i // 16 == 0 else i // 16 if i // 16 < 10 else chr(
                      ord('a') + i // 16 - 10),
                  i % 16 if i % 16 < 10 else chr(ord('a') + i % 16 - 10)))
