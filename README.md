# Simple Nim Game solved by Minimax algorithm
## Author: Dhruv Joshi

This is a very simple application of the minimax algorithm to play an adversarial zero-sum game against the computer. It is based on concepts learned when I took the class CS221 (Artificial Intelligence) taught by Prof. Percy Liang at Stanford.

## Objective of the game
The last player to move the "rock" into the end position wins the game. This can be modelled as a subtraction game - assume we start with a number 25 and either player can subtract 1,2 or 3. Turn by turn, each player chooses how much to subtract. The person to subtract the last number and reach 0 wins. 

## Demo
Access the demo [here](http://nim.derbedhruv.webfactional.com/)

In the web demo of the game, a "rock" is moved from start to end, along a tabular grid - in this case represented by the blue coloured cell. The player making the last move to make it reach the end state wins.

## References
* [Nim games](https://en.wikipedia.org/wiki/Nim)
* [Minimax algorithm](https://en.wikipedia.org/wiki/Minimax#Minimax_algorithm_with_alternate_moves)