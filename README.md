## Play

```
⋊> ~/tic-tac-toe on master ↑ python -m ttt                                                                    23:01:19
Welcome to a new game, enjoy!
P.S. you can always quit by typing 'quit'
How large of a game? (default=3)
>>
Enter name for player 1
>> Ms. First
Enter name for player 2
>> Mr. Second

 1 │ 2 │ 3
───┼───┼───
 4 │ 5 │ 6
───┼───┼───
 7 │ 8 │ 9

Ms. First, choose a box to place an 'x' into
>>

[some time later]

Ms. First, choose a box to place an 'x' into
>> 6

 o │ o │ x
───┼───┼───
   │ x │ x
───┼───┼───
 o │   │ x

Congratulations Ms. First, you won!
```

## Build

`python setup.py bdist_wheel`

## Test

`tox`
