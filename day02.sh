#!/bin/zsh
s=0

r_max=12
g_max=13
b_max=14

for l in "${(@f)"$(<./day02.in.utf8)"}"
{
    game=0
    [[ $l =~ '([0-9]+):' ]] && {
        game=$(("${match[1]}"))
    }
    rounds_str="${l##*: }"
    rounds=("${(@s/; /)rounds_str}")

    for round in "${rounds[@]}"
    {
        r=0
        g=0
        b=0

        [[ $round =~ '([0-9]+) red' ]] && {
            r=$(("${match[1]}"))
        }
        [[ $round =~ '([0-9]+) green' ]] && {
            g=$(("${match[1]}"))
        }
        [[ $round =~ '([0-9]+) blue' ]] && {
            b=$(("${match[1]}"))
        }

        if (( ${r} > ${r_max} )); then
            game=0
        fi
        if (( ${g} > ${g_max} )); then
            game=0
        fi
        if (( ${b} > ${b_max} )); then
            game=0
        fi
    }

    s=$((s + "${game}"))
}

echo "${s}" > ./day02.out.utf8
