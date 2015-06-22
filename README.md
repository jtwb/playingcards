# Playing Cards

*"[E]very time you shuffle a deck of cards, you are almost certainly creating an arrangement which the universe has never before seen."*
--- http://nowiknow.com/shuffled/

This project explores that statement.

Questions include:

* (A) Is it possible to compute enough random decks that you get a duplicate deck?
  * How do we guarantee 122 bits of real entropy to ensure fully-random shuffles?
  * We have the Generalized Birthday Paradox on our side - only need to visit ~`10^33` decks before we start to see collisions
* (B) Is it possible to *know* when you have visited a duplicate deck? (There are `52!`=`8e67` possible decks)
* (C) What changes when we focus on Riffle Shuffles, which have much lower entropy than fully random shuffles?
  * Are we more likely to find non-unique states in this universe?

