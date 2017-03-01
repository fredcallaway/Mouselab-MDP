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
  # Load data and test connection to server.
  expData = loadJson "/static/json/condition_0_0.json"
  console.log 'expData', expData
  initializeExperiment expData.blocks

createStartButton = ->
  document.getElementById("loader").style.display = "none"
  document.getElementById("successLoad").style.display = "block"
  document.getElementById("failLoad").style.display = "none"
  $('#load-btn').click initializeExperiment


initializeExperiment = (blocks) ->
  console.log 'INITIALIZE EXPERIMENT'

  #  ============================== #
  #  ========= EXPERIMENT ========= #
  #  ============================== #

  welcome =
    type: 'text'
    text: """
    <h1>Graph-MDP Demo</h1>

    This is a demonstration of the Graph-MDP plugin.
    <p>
    Press <b>space</b> to continue.

    """

  main =
    type: 'graph'
    centerMessage: 'A simple cross'
    timeline: blocks.grid

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

