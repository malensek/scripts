#!/usr/bin/env bash

print_strip() {
    for ((color = ${1}; color < ${2}; ++color)); do
        inv=$(((color + 8) % 16))
        echo -ne "\x1b[48;5;${color}m \x1b[38;5;${inv}m${3} "
    done
    echo -e "\033[0m"
}

print_plain() {
    for ((color = ${1}; color < ${2}; ++color)); do
        echo -ne "\x1b[48;5;${color}m ${3} "
    done
    echo -e "\033[0m"
}

print_strip 0 8
print_strip 8 16
echo
print_strip 0 8 "     "
print_strip 0 8 "     "
print_strip 0 8 "     "
print_strip 8 16 "     "
print_strip 8 16 "     "
print_strip 8 16 "     "
echo
