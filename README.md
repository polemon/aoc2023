# aoc2023
My solutions to [Advent of Code 2023][1]

  [1]: https://adventofcode.com/2023

----

* Per day, each file is named: `dayNN.EXT`, where `NN` is a two-digit number (01 to 24), and `EXT` is any file extension applicable.
* Input is in the form of a UTF-8 encoded file following this naming scheme: `dayNN.in.utf8` (`NN` as above).
* Output is written directly to the shell.
* In case the question is a two-parter, only the second solution is tracked, however usually the first part is completed using a shellscript, etc.
* A Markdown file (scheme: `dayNN.md`) contains notes for that day's puzzle.

## Assignments

### Day 1
* input consists of alphanumeric lines like: `xxxeight4two1nothing`
* varying in length, but never empty.

#### Part 1
* loop over all lines
* take alphanumeric string, ex: `xxxeight4two1nothing`
* find first **and** last digit
* concatenate first and last digit: `4` and `1`, become `41`
* sum up all those numeric values created by each line

##### Expected result
`55123`

#### Part 2
Same as Part 1, but this time words describing a digit (like `one`, `two`, `three`, etc.) also have to be considered.

> [!NOTE]
> Parsing actually has to be done in reverse to find the last item.
> An item like `xnineightx` would actually parse as `98`, since `nine` is detected when parsing from left to right (first item),
> and `eight` is detected when parsing backwards (last item).

##### Expected result
`55260`

### Day 2
* input consists of lines with the following structure:
`Game <N1>:{[ <N2> blue,][ <N3> red,][ <N4> green,]; }`
* first number (`<N1>`), is the "game ID", each game consists of rounds separated by `;`
* each round consists of a number of "red", "green", and "blue" values, at most one of each.
* empty rounds have not been seen, but are technically possible, so a `Game <N>: ; 0 blue, 0 red, 0 green` is technically a valid game

#### Part 1
* observe global maximum: `12` red, `13` green, `14` blue
* loop over all lines
* if in any round of a game the maximum is surpassed, the game is invalid: ex: `Game <N>: 13 red, 8 green; ...` ⇒ game `<N>` invalid.
* sum up ids of all valid games

##### Expected result
`2512`

#### Part 2
* find maximum of each game
* loop over all lines
* in each line find sets of values separated by `;`
* each set contains a value for `red`, `green`, `blue`, find maximum of each of those per line
* compute combined product (maxred × maxgreen × maxblue)
* sum all products of every line

##### Expected result
`67335`
