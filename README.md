# Mouselab-MDP
Mouselab-MDP is a [JsPsych](https://github.com/jodeleeuw/jsPsych/) plugin that renders Markov decision processes (MDP) for participants to navigate through. Optionally, information about the environment can be presented only when the participant asks for it, thus creating a record of the information considered. Try out the live demo mouselab-demo [here](http://cocosci.dreamhosters.com/webexpt/mouselab-demo/).

# Usage
Documentation is sparse, thus it is best to learn by example. The code for the demo can be found in [demo/](/demo/). 

src/experiment.coffee is the master experiment script. It contains 
src/jspsych-mouselab-mdp.coffee

The stimulus specifications are in [demo/static/json/trials.json](/demo/json/trials.json)

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

A basic description of how to use the plugin can be found in our RLDM paper. If you don't have access to the paper, email fredcallaway@berkeley.edu and ask for a copy. There is also a limited amount of inline documentation in [jspsych-mouselab-mdp.coffee](/jspsych-mouselab-mdp.coffee). Pay special attention to the constructor of `MouselabMDP`, around line 90.



@graph  # defines transition and reward functions
@layout  # defines position of states
@initial  # initial state of player

@stateLabels=null  # object mapping from state names to labels
@stateDisplay='never'  # one of 'never', 'hover', 'click', 'always'
@stateClickCost=0  # subtracted from score every time a state is clicked
@edgeLabels='reward'  # object mapping from edge names (s0 + '__' + s1) to labels
@edgeDisplay='always'  # one of 'never', 'hover', 'click', 'always'
@edgeClickCost=0  # subtracted from score every time an edge is clicked


@keys=KEYS  # mapping from actions to keycodes
@trialIndex=TRIAL_INDEX  # number of trial (starts from 1)
@playerImage='static/images/plane.png'
SIZE=120  # determines the size of states, text, etc...

leftMessage='&nbsp;'
centerMessage='&nbsp;'
rightMessage='Score: <span id=mouselab-score/>'
lowerMessage=KEY_DESCRIPTION

# Example experiment
The code for the demo can be found in [experiment/](/experiment/). The stimulus specifications are in [experiment/static/json/trials.json](/experiment/json/trials.json)

# RLDM Abstract
Below is the abstract for our submission to Reinforcement learning and decision making: "Mouselab-MDP: A new paradigm for tracing how people plan".

Planning is a latent cognitive process that cannot be observed directly. This makes it difficult to study how people plan. To address this problem, we propose a new paradigm for studying planning that provides experimenters with a timecourse of participant attention to information in the task environment. This paradigm employs the information-acquisition mechanism of the Mouselab paradigm, in which participants click on options to reveal the outcome of choosing those options. However, in contrast to the original Mouselab paradigm, our paradigm is a sequential decision process, in which participants must plan multiple steps ahead to achieve high scores. We release Mouselab-MDP open-source as a plugin for the JsPsych online Psychology experiment library. The plugin displays a Markov decision process as a directed graph, which the participant navigates to maximize reward. To trace the the process of planning, the rewards associated with states or actions are initially occluded; the participant has to click on a transition to reveal its reward. Thus, the participant makes explicit the states she considers in her information gathering behavior. We illustrate the utility of the Mouselab-MDP paradigm with a proof-of-concept experiment in which we trace the temporal dynamics of planning in a simple environment. Our data shed new light on people’s approximate planning strategies and on how people prune decision trees. We hope that the release of Mouselab-MDP will facilitate future research on human planning strategies. In particular, we hope that the fine-grained time course data the paradigm generates will be instrumental in specifying algorithms, tracking learning trajectories, and characterizing individual differences in human planning