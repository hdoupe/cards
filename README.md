# Find the top hand from 7 random cards

The rules for the top hands can be found [here](https://www.cardplayer.com/rules-of-poker/hand-rankings).


### Example usage

```python
In [1]: import cards 
   ...: i = 0 
   ...: while True: 
   ...:     i += 1 
   ...:     hand = cards.gen_cards() 
   ...:     res = cards.choose_cards(hand) 
   ...:     if res and res[0] in ("straight", "flush", "straight_flush", "royal_flush"): 
   ...:         break 
   ...:                                                                                                                                                                                       

In [2]: i                                                                                                                                                                                     
Out[2]: 3

In [3]: res                                                                                                                                                                                   
Out[3]: 
('flush',
 [('spades', 10), ('spades', 8), ('spades', 6), ('spades', 3), ('spades', 2)])

```

### Run tests

```
$ py.test test.py -v
```

Possible TODOs:
- [ ] Fix the logic for finding a flush. This incorrectly returns royal flushes sometimes.
- [ ] Write a CLI
- [ ] Score more of the hands in the poker hand ranking website linked to above.
