#!/bin/zsh
s=0
for l in "${(@f)"$(<./day01.in.utf8)"}"
{
    echo " »   line: ${l}"
    l=${l//zero/0}
    l=${l//one/1}
    l=${l//two/2}
    l=${l//three/3}
    l=${l//four/4}
    l=${l//five/5}
    l=${l//six/6}
    l=${l//seven/7}
    l=${l//eight/8}
    l=${l//nine/9}
    echo "  »  line: ${l}"

    [[ $l =~ '^[^0-9]*([0-9]).*([0-9])[^0-9]*$' ]] && {
        s=$((s + "${match[1]}${match[2]}" ))
        echo "   » ${match[1]}${match[2]}"
    }

    [[ $l =~ '^[^0-9]*([0-9])[^0-9]*$' ]] && {
        s=$((s + "${match[1]}${match[1]}" ))
        echo "   » ${match[1]}${match[1]}"
    }

    echo "${s}" > ./day01.out.utf8
}
