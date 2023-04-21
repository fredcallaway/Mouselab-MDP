# Mouselab-MDP
Mouselab-MDP is a [JsPsych](https://github.com/jodeleeuw/jsPsych/) plugin that renders Markov decision processes (MDP) for participants to navigate through. Optionally, information about the environment can be presented only when the participant asks for it, thus creating a record of the information considered. Try out the live demo mouselab-demo [here](http://cocosci.dreamhosters.com/webexpt/mouselab-demo/).

# Usage

To view the experiment, you must use an http server. You can start one by running `python -m http.server` in the experiment/ directory. Then visit http://localhost:8000/ in your browser.

A basic description of how to use the plugin can be found in our RLDM [paper](https://www.researchgate.net/publication/314258117_Mouselab-MDP_A_new_paradigm_for_tracing_how_people_plan) . There is also a limited amount of inline documentation in the source coffeescript. Pay special attention to the constructor of `MouselabMDP`, beginning at [line 90](https://github.com/fredcallaway/Mouselab-MDP/blob/master/jspsych-mouselab-mdp.coffee#L90).

Note that we have included the javascript which compiles from coffeescript. You only need to link to the javascript in your own code (I just include the coffeescript for reference).

## Example
Documentation is sparse, thus it is probably best to learn by example. The code for the demo can be found in [experiment/](/experiment/). Here is an [excerpt](https://github.com/fredcallaway/Mouselab-MDP/blob/master/experiment/src/experiment.coffee#L57) from the main experiment file, the definition of a simple Mouselab-MDP trial.

```coffee
trial =
  type: 'mouselab-mdp'  # use the jspsych plugin
  # ---------- MANDATORY PARAMETERS ---------- #
  graph:  # defines transition and reward functions
    A:  # for each state, an object mapping actions to [reward, nextState]
      right: [5, 'B']  # states may be strings or numbers (be consistent!)
      left: [-5, 'C']
    B: {}
    C: {}
  layout:  # defines position of states
    A: [1, 1]
    B: [2, 1]
    C: [0, 1]
  initial: 'A'  # initial state of player
  # ---------- OPTIONAL PARAMETERS ---------- #
  stateLabels:  # object mapping from state names to displayed labels
    A: 'A'
    B: 'B'
    C: 'C'
  stateDisplay: 'always'  # one of 'never', 'hover', 'click', 'always'
  stateClickCost: 0  # subtracted from score every time a state is clicked
  edgeLabels: 'reward'  # object mapping from edge names (s0 + '__' + s1) to labels
  edgeDisplay: 'hover'  # one of 'never', 'hover', 'click', 'always'
  edgeClickCost: 0  # subtracted from score every time an edge is clicked
  stimId:1994  # for your own data-keeping
  playerImage: 'static/images/plane.png'
  playerImageScale: 0.5
  size: 200  # determines the size of states, text, etc...
  leftMessage: 'Left Message'
  centerMessage: 'Center Message'
```

## Running Locally
To run the code locally, install [psiturk](https://psiturk.readthedocs.io/en/latest/quickstart.html) and then navigate to the `experiment` directory and run locally:

```psiturk server start```

When done, you should run:

```psiturk server stop```