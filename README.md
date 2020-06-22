# Find the top hand from 7 random cards

The rules for the top hands can be found [here](https://www.cardplayer.com/rules-of-poker/hand-rankings).

Run the script:

```
$ python cards.py 
('royal_flush', [('diamonds', 'Jack'), ('diamonds', 'Queen'), ('diamonds', 'Ace'), ('diamonds', 10), ('diamonds', 'King')])
('straight', [('hearts', 'Ace'), ('clubs', 'Ace'), ('diamonds', 'King'), ('diamonds', 'Queen'), ('diamonds', 'Jack'), ('diamonds', 10), ('spades', 2)])
('straight_flush', [('diamonds', 'King'), ('diamonds', 'Queen'), ('diamonds', 'Jack'), ('diamonds', 10), ('diamonds', 9)])
('straight_flush', [('diamonds', 'King'), ('diamonds', 'Queen'), ('diamonds', 'Jack'), ('diamonds', 10), ('diamonds', 9), ('diamonds', 8)])
```

Possible TODOs:
- [ ] Fix the logic for finding a flush. This incorrectly returns royal flushes sometimes.
- [ ] Write a CLI
- [ ] Score more of the hands in the poker hand ranking website linked to above.
