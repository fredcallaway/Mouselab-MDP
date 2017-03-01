# Mouselab-MDP

A Mouselab-MDP environment has four essential components:

#. `graph` is a function $s \mapsto \{(a_1, r_1, s'_1), (a_2, r_2, s'_2) \dots}$ that specifies the actions $a$ available in state $s$ along with their associated rewards $r$ and resultant states $s'$.
#. `initial` is the state in which the participant begins the trial. Along with `graph`, this defines a deterministic MDP.
#. `layout` is a function $s \mapsto (x, y$) that specifies the location of each state on the screen.
#. `click` is a function $s \mapsto (r, \ell)$ that specifies the reward $r$and label $\ell$ that is displayed when a state is clicked on.

If `click` is left unspecified, the environment reduces to a standard MDP. In a given trial, the MDP is first displayed on the screen as a graph (see Figure \ref{fig:screenshots}. States are positioned acording to `layout` and directed edges automatically drawn to indicate available actions. Optionally, the reward associated with each action may be displayed. The participant finds her character in the intial state and navigates through the MDP using the keyboard (the arrow keys by default). The trial ends when the participant reaches a final state (i.e. one with no available actions).

When click is specified, the participant can click on a state in order to gain information about it. This could be the reward associated with traveling to that state, the value of the state (i.e. the sum of future rewards), or anything else the experimenter can imagine. By default, this information is displayed on the state for the remainder of the trial. Optionally, a reward---or more likely, a penalty---is added to the participant's score. The times of every action and click are recorded.

This novel paradigm offers three advantages that we'd like to highlight:

#. Participants make their planning process explicit through their information-seeking clicks. This allows an experimenter to test hypotheses that do not make strong predictions about surface-level actions.
#. A wide variety of state-transition and reward structures can be displayed automatically. This allows an experimenter to create a large number of highly variable stimuli (potentially with a computer program) in relatively little time (compared to using an image-editing software).
#. The paradigm is packaged as a JsPsych plugin with concise, yet flexible specifications of stimuli. This allows experimenters with only basic knowledge of javascript to use the paradigm to run qualitatively new expermients.