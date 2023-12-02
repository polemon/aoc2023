#!/bin/zsh
s=0

for l in "${(@f)"$(<./day01.in.utf8)"}"
{
    [[ $l =~ '^[^0-9]*([0-9]).*([0-9])[^0-9]*$' ]] && {
        s=$((s + "${match[1]}${match[2]}" ))
    }

    [[ $l =~ '^[^0-9]*([0-9])[^0-9]*$' ]] && {
        s=$((s + "${match[1]}${match[1]}" ))
    }
}

echo "${s}"
