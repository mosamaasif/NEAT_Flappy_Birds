# Flappy Birds AI

An AI that learns to play Flappy Bird using NEAT (NeuroEvolution of Augmenting Topologies).

## About

I built this as an AI course project at university. It uses the [NEAT algorithm](https://en.wikipedia.org/wiki/Neuroevolution_of_augmenting_topologies) to evolve neural networks that learn to play Flappy Bird through successive generations. Each bird in a generation is controlled by its own neural network, and the best performers are selected and mutated to produce the next generation. Within a few generations, the AI consistently clears pipes without human input.

## Demo

![AI Playing Flappy Bird](images/run.gif)

![Console Output](images/console.png)

## Built With

- [Python 3](https://www.python.org/)
- [NEAT-Python](https://neat-python.readthedocs.io/en/latest/) — neuroevolution library
- [Pygame](https://www.pygame.org/) — game rendering and input

## Getting Started

### Prerequisites

- [Python 3](https://www.python.org/downloads/)

### Installation & Running

```sh
git clone https://github.com/mosamaasif/NEAT_Flappy_Birds.git
cd NEAT_Flappy_Birds
pip3 install -r requirements.txt
python3 code/main.py
```

> **Note:** Use `python` instead of `python3` if that's how your system is aliased.

The NEAT configuration is in `code/config-feedforward.txt`. You can tweak population size, mutation rates, and other parameters there.
