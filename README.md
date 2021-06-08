# brownian
Tools and simulations for Brownian motions and other stochastic processes. 

## The Framework
The basic split is we want some tools that do math, and other tools that make plots. 

### MarkovProcess
This class represents a generic Markov process. Subclasses must implement the step() function which computes the next state of the process. 

The state space may be discrete or continuous. For now, time is discrete.

Optionally, this class keeps a record of all previous states (mainly for plotting purposes). 

### DiscreteMarkovProcess
Subclass of MarkovProcess which accepts a state-transition matrix. The step() function then samples from this matrix. 

### Functions

Generate stuff (brownian motions, etc.)
- brownian motion (1D, 2D,...?)
- skorohod
- bridges
- time change
- other martingales?

### Plotting

Maybe use seaborn?
