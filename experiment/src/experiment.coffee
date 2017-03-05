###
experiment.coffee
Fred Callaway

Demonstrates the mouselab-mdp jspsych plugin

###
# coffeelint: disable=max_line_length, indentation

# Uncomment these to enforce a minimum window size
# $(window).resize -> checkWindowSize 920, 720, $('#jspsych-target')
# $(window).resize()

loadJson = (file) ->
  result = $.ajax
    dataType: 'json'
    url: file
    async: false
  return result.responseJSON

$(window).on 'load', ->
  trials = loadJson "static/json/trials.json"
  initializeExperiment trials

initializeExperiment = (trials) ->
  console.log 'INITIALIZE EXPERIMENT'

  #  ============================== #
  #  ========= EXPERIMENT ========= #
  #  ============================== #

  welcome =
    type: 'text'
    text: """
    <h1>Mouselab-MDP Demo</h1>

    This is a demonstration of the Mouselab-MDP plugin.
    <p>
    Press <b>space</b> to continue.

    """

  main =
    type: 'mouselab-mdp'
    timeline: trials

  experiment_timeline = [
    welcome
    main
  ]


  # ================================================ #
  # ========= START AND END THE EXPERIMENT ========= #
  # ================================================ #


  jsPsych.init
    display_element: $('#jspsych-target')
    timeline: experiment_timeline
    # show_progress_bar: true

    on_finish: ->
      jsPsych.data.displayData()

    on_data_update: (data) ->
      console.log 'data', data

