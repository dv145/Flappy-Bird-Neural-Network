# Flappy-Bird-Neural-Network

I used PyGame to host the game.

A genetic algorithm is used which essentially assigns a fitness rating to each bird. Every iteration 60 birds were spawned. The fitness rating was determined by time alive and distance from center of the pipes. 2 unfit birds were not able to reproduce (i.e. their weights were discarded) and a random element of merging the weights of the remaining birds was used to simulate evolution.

<img width="960" alt="Screenshot 2021-07-03 at 2 02 44 PM" src="https://user-images.githubusercontent.com/82046907/124348403-627a5c00-dc07-11eb-86c7-d41695db287e.png">


The game design was inspired by Bluefever Software (https://www.youtube.com/channel/UCFkfibjxPzrP0e2WIa8aJCg)

