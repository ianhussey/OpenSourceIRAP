#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.85.3),
    on Wed Nov 14 14:02:11 2018
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division
from psychopy import locale_setup, sound, gui, visual, core, data, event, logging
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'IRAP'  # from the Builder filename that created this script
expInfo = {u'gender': u'', u'age': u'', u'participant': u'', u'StartingBlock': u'a', u'UseMonkey': u'n'}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data' + os.path.sep + '%s_%s' %(expInfo['participant'], expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=None,
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.ERROR)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=(1600, 900), fullscr=True, screen=0,
    allowGUI=False, allowStencil=False,
    monitor='testMonitor', color='black', colorSpace='rgb',
    blendMode='avg', useFBO=True,
    units='norm')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "instructions"
instructionsClock = core.Clock()
# Dependencies

from psychopy.hardware.emulator import ResponseEmulator  #for response emulator
import itertools  # for flattening lists of lists into lists
import random  # for shuffling lists

# Functions

# Convert string to boolean.
# Take any likely input from the task.xlsx file and convert to a boolean. This helps to idiot-proof the excel files.
def string_to_booleanl(v):
  return v.lower() in ("yes", "true", "TRUE", "True", "t", "T", 1)

# Trial generation function
def generate_trials(trial_type_column, multiplier, shuffle_list):
    """Generate a shuffled list of stimuli exemplars from a column in an excel stimuli file""" 
    a = dict()  # declare a dict to be populated
    for i in range(len(exemplars)):
        a[i] = [exemplars[i][trial_type_column]] * multiplier  # populate the dict from vertical reads of the conditions
    a = a.values()  # extract only values (and not keys) from the list of dicts
    a = list(itertools.chain(*a))  # flatten the list of dicts into a list
    if shuffle_list == True:
        random.shuffle(a)  # shuffle this list, so that it can be drawn from by the trials
    return a


# Determine variables based on dialogue box

# auto response monkey
if str(expInfo['UseMonkey']) == 'y' or str(expInfo['UseMonkey']) == 'Y' or str(expInfo['UseMonkey']) == 'yes' or str(expInfo['UseMonkey']) == 't' or str(expInfo['UseMonkey']) == 'true' or str(expInfo['UseMonkey']) == 'True' or str(expInfo['UseMonkey']) == 'TRUE':
    Monkey = True
else:
    Monkey = False

# starting block
if str(expInfo['StartingBlock']) == 'a' or str(expInfo['StartingBlock']) == 'A':
    starting_block = 'a'
    Afirst_nReps = 1
    Asecond_nReps = 0
elif str(expInfo['StartingBlock']) == 'b' or str(expInfo['StartingBlock']) == 'B':
    starting_block = 'b'
    Afirst_nReps = 0
    Asecond_nReps = 1

intro_box = visual.TextStim(win=win, name='intro_box',
    text='default text',
    font='Arial',
    pos=[0, 0], height=0.08, wrapWidth=1.5, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);

# Initialize components for Routine "preblock_A"
preblock_AClock = core.Clock()
# msg variable just needs some value at start
accuracyFeedback=''

rule_box_A = visual.TextStim(win=win, name='rule_box_A',
    text='default text',
    font='Arial',
    pos=[0, 0], height=0.08, wrapWidth=1.5, ori=0, 
    color='orange', colorSpace='rgb', opacity=1,
    depth=-1.0);

# Initialize components for Routine "trial_A"
trial_AClock = core.Clock()

image_stimulus1_box_A = visual.ImageStim(
    win=win, name='image_stimulus1_box_A',
    image='sin', mask=None,
    ori=0, pos=[0,0], size=[0.5, 0.5],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
image_stimulus2_box_A = visual.ImageStim(
    win=win, name='image_stimulus2_box_A',
    image='sin', mask=None,
    ori=0, pos=[0,0], size=[0.5, 0.5],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
stimulus1_box_A = visual.TextStim(win=win, name='stimulus1_box_A',
    text='default text',
    font='Arial',
    pos=[0,0], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-3.0);
stimulus2_box_A = visual.TextStim(win=win, name='stimulus2_box_A',
    text='default text',
    font='Arial',
    pos=[0,0], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-4.0);
left_box_A = visual.TextStim(win=win, name='left_box_A',
    text='default text',
    font='Arial',
    pos=[0,0], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-7.0);
right_box_A = visual.TextStim(win=win, name='right_box_A',
    text='default text',
    font='Arial',
    pos=[0,0], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-8.0);
accuracy_feedback_box_A = visual.TextStim(win=win, name='accuracy_feedback_box_A',
    text='default text',
    font='Arial',
    pos=[0,0], height=0.2, wrapWidth=None, ori=0, 
    color='red', colorSpace='rgb', opacity=1,
    depth=-9.0);

# Initialize components for Routine "practice_postblock_A"
practice_postblock_AClock = core.Clock()

practice_aim_box_A = visual.TextStim(win=win, name='practice_aim_box_A',
    text='default text',
    font='Arial',
    pos=[0, 0.2], height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);
practice_accuracy_box_A = visual.TextStim(win=win, name='practice_accuracy_box_A',
    text='default text',
    font='Arial',
    pos=[0, 0], height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0);
practice_latency_box_A = visual.TextStim(win=win, name='practice_latency_box_A',
    text='default text',
    font='Arial',
    pos=[0, -0.2], height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-3.0);
press_box_prac_A = visual.TextStim(win=win, name='press_box_prac_A',
    text='default text',
    font='Arial',
    pos=[0, -0.5], height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-4.0);

# Initialize components for Routine "preblock_B"
preblock_BClock = core.Clock()

rule_box_B = visual.TextStim(win=win, name='rule_box_B',
    text='default text',
    font='Arial',
    pos=[0, 0], height=0.08, wrapWidth=1.5, ori=0, 
    color='cyan', colorSpace='rgb', opacity=1,
    depth=-1.0);

# Initialize components for Routine "trial_B"
trial_BClock = core.Clock()
#msg variable just needs some value at start
accuracyFeedback=''
image_stimulus1_box_B = visual.ImageStim(
    win=win, name='image_stimulus1_box_B',
    image='sin', mask=None,
    ori=0, pos=[0,0], size=[0.5, 0.5],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
image_stimulus2_box_B = visual.ImageStim(
    win=win, name='image_stimulus2_box_B',
    image='sin', mask=None,
    ori=0, pos=[0,0], size=[0.5, 0.5],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
stimulus1_box_B = visual.TextStim(win=win, name='stimulus1_box_B',
    text='default text',
    font='Arial',
    pos=[0,0], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-3.0);
stimulus2_box_B = visual.TextStim(win=win, name='stimulus2_box_B',
    text='default text',
    font='Arial',
    pos=[0,0], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-4.0);
left_box_B = visual.TextStim(win=win, name='left_box_B',
    text='default text',
    font='Arial',
    pos=[0,0], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-7.0);
right_box_B = visual.TextStim(win=win, name='right_box_B',
    text='default text',
    font='Arial',
    pos=[0,0], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-8.0);
accuracy_feedback_box_B = visual.TextStim(win=win, name='accuracy_feedback_box_B',
    text='default text',
    font='Arial',
    pos=[0,0], height=0.2, wrapWidth=None, ori=0, 
    color='red', colorSpace='rgb', opacity=1,
    depth=-9.0);

# Initialize components for Routine "practice_postblock_B"
practice_postblock_BClock = core.Clock()

practice_aim_box_B = visual.TextStim(win=win, name='practice_aim_box_B',
    text='default text',
    font='Arial',
    pos=[0, 0.2], height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);
practice_accuracy_box_B = visual.TextStim(win=win, name='practice_accuracy_box_B',
    text='default text',
    font='Arial',
    pos=[0, 0], height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0);
practice_latency_box_B = visual.TextStim(win=win, name='practice_latency_box_B',
    text='default text',
    font='Arial',
    pos=[0, -0.2], height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-3.0);
press_box_prac_B = visual.TextStim(win=win, name='press_box_prac_B',
    text='default text',
    font='Arial',
    pos=[0, -0.5], height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-4.0);

# Initialize components for Routine "preblock_A"
preblock_AClock = core.Clock()
# msg variable just needs some value at start
accuracyFeedback=''

rule_box_A = visual.TextStim(win=win, name='rule_box_A',
    text='default text',
    font='Arial',
    pos=[0, 0], height=0.08, wrapWidth=1.5, ori=0, 
    color='orange', colorSpace='rgb', opacity=1,
    depth=-1.0);

# Initialize components for Routine "trial_A"
trial_AClock = core.Clock()

image_stimulus1_box_A = visual.ImageStim(
    win=win, name='image_stimulus1_box_A',
    image='sin', mask=None,
    ori=0, pos=[0,0], size=[0.5, 0.5],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
image_stimulus2_box_A = visual.ImageStim(
    win=win, name='image_stimulus2_box_A',
    image='sin', mask=None,
    ori=0, pos=[0,0], size=[0.5, 0.5],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
stimulus1_box_A = visual.TextStim(win=win, name='stimulus1_box_A',
    text='default text',
    font='Arial',
    pos=[0,0], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-3.0);
stimulus2_box_A = visual.TextStim(win=win, name='stimulus2_box_A',
    text='default text',
    font='Arial',
    pos=[0,0], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-4.0);
left_box_A = visual.TextStim(win=win, name='left_box_A',
    text='default text',
    font='Arial',
    pos=[0,0], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-7.0);
right_box_A = visual.TextStim(win=win, name='right_box_A',
    text='default text',
    font='Arial',
    pos=[0,0], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-8.0);
accuracy_feedback_box_A = visual.TextStim(win=win, name='accuracy_feedback_box_A',
    text='default text',
    font='Arial',
    pos=[0,0], height=0.2, wrapWidth=None, ori=0, 
    color='red', colorSpace='rgb', opacity=1,
    depth=-9.0);

# Initialize components for Routine "practice_postblock_A"
practice_postblock_AClock = core.Clock()

practice_aim_box_A = visual.TextStim(win=win, name='practice_aim_box_A',
    text='default text',
    font='Arial',
    pos=[0, 0.2], height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);
practice_accuracy_box_A = visual.TextStim(win=win, name='practice_accuracy_box_A',
    text='default text',
    font='Arial',
    pos=[0, 0], height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0);
practice_latency_box_A = visual.TextStim(win=win, name='practice_latency_box_A',
    text='default text',
    font='Arial',
    pos=[0, -0.2], height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-3.0);
press_box_prac_A = visual.TextStim(win=win, name='press_box_prac_A',
    text='default text',
    font='Arial',
    pos=[0, -0.5], height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-4.0);

# Initialize components for Routine "end_practice_blocks"
end_practice_blocksClock = core.Clock()
# by default, don't do test blocks. Change elsewhere if mastery criteria are met.
complete_test_blocks = 0

# Initialize components for Routine "preblock_A"
preblock_AClock = core.Clock()
# msg variable just needs some value at start
accuracyFeedback=''

rule_box_A = visual.TextStim(win=win, name='rule_box_A',
    text='default text',
    font='Arial',
    pos=[0, 0], height=0.08, wrapWidth=1.5, ori=0, 
    color='orange', colorSpace='rgb', opacity=1,
    depth=-1.0);

# Initialize components for Routine "trial_A"
trial_AClock = core.Clock()

image_stimulus1_box_A = visual.ImageStim(
    win=win, name='image_stimulus1_box_A',
    image='sin', mask=None,
    ori=0, pos=[0,0], size=[0.5, 0.5],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
image_stimulus2_box_A = visual.ImageStim(
    win=win, name='image_stimulus2_box_A',
    image='sin', mask=None,
    ori=0, pos=[0,0], size=[0.5, 0.5],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
stimulus1_box_A = visual.TextStim(win=win, name='stimulus1_box_A',
    text='default text',
    font='Arial',
    pos=[0,0], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-3.0);
stimulus2_box_A = visual.TextStim(win=win, name='stimulus2_box_A',
    text='default text',
    font='Arial',
    pos=[0,0], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-4.0);
left_box_A = visual.TextStim(win=win, name='left_box_A',
    text='default text',
    font='Arial',
    pos=[0,0], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-7.0);
right_box_A = visual.TextStim(win=win, name='right_box_A',
    text='default text',
    font='Arial',
    pos=[0,0], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-8.0);
accuracy_feedback_box_A = visual.TextStim(win=win, name='accuracy_feedback_box_A',
    text='default text',
    font='Arial',
    pos=[0,0], height=0.2, wrapWidth=None, ori=0, 
    color='red', colorSpace='rgb', opacity=1,
    depth=-9.0);

# Initialize components for Routine "postblock_A"
postblock_AClock = core.Clock()

aim_box_A = visual.TextStim(win=win, name='aim_box_A',
    text='default text',
    font='Arial',
    pos=[0, 0.2], height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);
accuracy_box_A = visual.TextStim(win=win, name='accuracy_box_A',
    text='default text',
    font='Arial',
    pos=[0, 0], height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0);
latency_box_A = visual.TextStim(win=win, name='latency_box_A',
    text='default text',
    font='Arial',
    pos=[0, -0.2], height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-3.0);
press_box_A = visual.TextStim(win=win, name='press_box_A',
    text='default text',
    font='Arial',
    pos=[0, -0.5], height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-4.0);

# Initialize components for Routine "preblock_B"
preblock_BClock = core.Clock()

rule_box_B = visual.TextStim(win=win, name='rule_box_B',
    text='default text',
    font='Arial',
    pos=[0, 0], height=0.08, wrapWidth=1.5, ori=0, 
    color='cyan', colorSpace='rgb', opacity=1,
    depth=-1.0);

# Initialize components for Routine "trial_B"
trial_BClock = core.Clock()
#msg variable just needs some value at start
accuracyFeedback=''
image_stimulus1_box_B = visual.ImageStim(
    win=win, name='image_stimulus1_box_B',
    image='sin', mask=None,
    ori=0, pos=[0,0], size=[0.5, 0.5],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
image_stimulus2_box_B = visual.ImageStim(
    win=win, name='image_stimulus2_box_B',
    image='sin', mask=None,
    ori=0, pos=[0,0], size=[0.5, 0.5],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
stimulus1_box_B = visual.TextStim(win=win, name='stimulus1_box_B',
    text='default text',
    font='Arial',
    pos=[0,0], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-3.0);
stimulus2_box_B = visual.TextStim(win=win, name='stimulus2_box_B',
    text='default text',
    font='Arial',
    pos=[0,0], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-4.0);
left_box_B = visual.TextStim(win=win, name='left_box_B',
    text='default text',
    font='Arial',
    pos=[0,0], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-7.0);
right_box_B = visual.TextStim(win=win, name='right_box_B',
    text='default text',
    font='Arial',
    pos=[0,0], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-8.0);
accuracy_feedback_box_B = visual.TextStim(win=win, name='accuracy_feedback_box_B',
    text='default text',
    font='Arial',
    pos=[0,0], height=0.2, wrapWidth=None, ori=0, 
    color='red', colorSpace='rgb', opacity=1,
    depth=-9.0);

# Initialize components for Routine "postblock_B"
postblock_BClock = core.Clock()

aim_box_B = visual.TextStim(win=win, name='aim_box_B',
    text='default text',
    font='Arial',
    pos=[0, 0.2], height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);
accuracy_box_B = visual.TextStim(win=win, name='accuracy_box_B',
    text='default text',
    font='Arial',
    pos=[0, 0], height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0);
latency_box_B = visual.TextStim(win=win, name='latency_box_B',
    text='default text',
    font='Arial',
    pos=[0, -0.2], height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-3.0);
press_box_B = visual.TextStim(win=win, name='press_box_B',
    text='default text',
    font='Arial',
    pos=[0, -0.5], height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-4.0);

# Initialize components for Routine "preblock_A"
preblock_AClock = core.Clock()
# msg variable just needs some value at start
accuracyFeedback=''

rule_box_A = visual.TextStim(win=win, name='rule_box_A',
    text='default text',
    font='Arial',
    pos=[0, 0], height=0.08, wrapWidth=1.5, ori=0, 
    color='orange', colorSpace='rgb', opacity=1,
    depth=-1.0);

# Initialize components for Routine "trial_A"
trial_AClock = core.Clock()

image_stimulus1_box_A = visual.ImageStim(
    win=win, name='image_stimulus1_box_A',
    image='sin', mask=None,
    ori=0, pos=[0,0], size=[0.5, 0.5],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
image_stimulus2_box_A = visual.ImageStim(
    win=win, name='image_stimulus2_box_A',
    image='sin', mask=None,
    ori=0, pos=[0,0], size=[0.5, 0.5],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
stimulus1_box_A = visual.TextStim(win=win, name='stimulus1_box_A',
    text='default text',
    font='Arial',
    pos=[0,0], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-3.0);
stimulus2_box_A = visual.TextStim(win=win, name='stimulus2_box_A',
    text='default text',
    font='Arial',
    pos=[0,0], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-4.0);
left_box_A = visual.TextStim(win=win, name='left_box_A',
    text='default text',
    font='Arial',
    pos=[0,0], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-7.0);
right_box_A = visual.TextStim(win=win, name='right_box_A',
    text='default text',
    font='Arial',
    pos=[0,0], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-8.0);
accuracy_feedback_box_A = visual.TextStim(win=win, name='accuracy_feedback_box_A',
    text='default text',
    font='Arial',
    pos=[0,0], height=0.2, wrapWidth=None, ori=0, 
    color='red', colorSpace='rgb', opacity=1,
    depth=-9.0);

# Initialize components for Routine "postblock_A"
postblock_AClock = core.Clock()

aim_box_A = visual.TextStim(win=win, name='aim_box_A',
    text='default text',
    font='Arial',
    pos=[0, 0.2], height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);
accuracy_box_A = visual.TextStim(win=win, name='accuracy_box_A',
    text='default text',
    font='Arial',
    pos=[0, 0], height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0);
latency_box_A = visual.TextStim(win=win, name='latency_box_A',
    text='default text',
    font='Arial',
    pos=[0, -0.2], height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-3.0);
press_box_A = visual.TextStim(win=win, name='press_box_A',
    text='default text',
    font='Arial',
    pos=[0, -0.5], height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-4.0);

# Initialize components for Routine "end"
endClock = core.Clock()
end_box = visual.TextStim(win=win, name='end_box',
    text='default text',
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# set up handler to look after randomisation of conditions etc
task = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('task.xlsx'),
    seed=None, name='task')
thisExp.addLoop(task)  # add the loop to the experiment
thisTask = task.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTask.rgb)
if thisTask != None:
    for paramName in thisTask.keys():
        exec(paramName + '= thisTask.' + paramName)

for thisTask in task:
    currentLoop = task
    # abbreviate parameter names if possible (e.g. rgb = thisTask.rgb)
    if thisTask != None:
        for paramName in thisTask.keys():
            exec(paramName + '= thisTask.' + paramName)
    
    # ------Prepare to start Routine "instructions"-------
    t = 0
    instructionsClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    # ResponseEmulator
    if Monkey:
        simulated_responses = [(1.1, 'e'), (1.1, 'i')]  # simulated responses take the form (onsetTime, responseKey). You can simulate more than one.
        responder = ResponseEmulator(simulated_responses)
        responder.start()
    
    # Create sufficiently long lists of stimuli
    """
    This allows us to keep the stimuli in an excel file across multiple lines, and to present them based on the categories 
    set by the 'layout.xlsx' file. This allows for shuffled (counterbalanced pseudorandom) presentation of the stimuli examplars 
    as well as the categories. 
    
    The method to do this below is to first declare a dictionary to be populated from the exemplars conditions, but not in the usual way. 
    Usually, psychopy would read across columns. If the stimuli were entered as a list within the excel file (e.g., ['male', 'female']) 
    rather on seperate rows as they are now all we would have to do is multiply the length of the list to get enough exemplars. However, 
    I wanted the stimuli file to be as use friendly as possible, so instead the below code allows you to enter the exemplars on seperate
    rows, and then populates the dict vertically from the rows. 
    """
    # Import stimuli exemplars
    exemplars = data.importConditions(stimulus_file)  # Import stimuli exemplars. stimulus_file is defined in task.xlsx
    
    # Determine nReps of trials loop based on number of exemplars
    reptitions = len(exemplars)
    
    
    # Generate a first, unshuffled list of the stimuli exemplars for saving to output file
    
    # 1. generate: no shuffling, multiplier = 1.
    labelA_stimuli_for_output = generate_trials('labelA_stimuli', 1, False)  # function and variable determined at begin exp.
    labelB_stimuli_for_output = generate_trials('labelB_stimuli', 1, False)
    targetA_stimuli_for_output = generate_trials('targetA_stimuli', 1, False)
    targetB_stimuli_for_output = generate_trials('targetB_stimuli', 1, False)
    labelA_image_stimuli_for_output = generate_trials('labelA_image_stimuli', 1, False)
    labelB_image_stimuli_for_output = generate_trials('labelB_image_stimuli', 1, False)
    targetA_image_stimuli_for_output = generate_trials('targetA_image_stimuli', 1, False)
    targetB_image_stimuli_for_output = generate_trials('targetB_image_stimuli', 1, False)
    
    # 2. save these lists to the trial handler to be written to csv
    thisExp.addData('labelA_stimuli_for_output', labelA_stimuli_for_output)
    thisExp.addData('labelB_stimuli_for_output', labelB_stimuli_for_output)
    thisExp.addData('targetA_stimuli_for_output', targetA_stimuli_for_output)
    thisExp.addData('targetB_stimuli_for_output', targetB_stimuli_for_output)
    thisExp.addData('labelA_image_stimuli_for_output', labelA_image_stimuli_for_output)
    thisExp.addData('labelB_image_stimuli_for_output', labelB_image_stimuli_for_output)
    thisExp.addData('targetA_image_stimuli_for_output', targetA_image_stimuli_for_output)
    thisExp.addData('targetB_image_stimuli_for_output', targetB_image_stimuli_for_output)
    intro_box.setText(intro_message)
    intro_resp = event.BuilderKeyResponse()
    # keep track of which components have finished
    instructionsComponents = [intro_box, intro_resp]
    for thisComponent in instructionsComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "instructions"-------
    while continueRoutine:
        # get current time
        t = instructionsClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # *intro_box* updates
        if t >= 0.4 and intro_box.status == NOT_STARTED:
            # keep track of start time/frame for later
            intro_box.tStart = t
            intro_box.frameNStart = frameN  # exact frame index
            intro_box.setAutoDraw(True)
        
        # *intro_resp* updates
        if t >= 1 and intro_resp.status == NOT_STARTED:
            # keep track of start time/frame for later
            intro_resp.tStart = t
            intro_resp.frameNStart = frameN  # exact frame index
            intro_resp.status = STARTED
            # keyboard checking is just starting
            event.clearEvents(eventType='keyboard')
        if intro_resp.status == STARTED:
            theseKeys = event.getKeys(keyList=['e', 'i'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instructionsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "instructions"-------
    for thisComponent in instructionsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # the Routine "instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    practice_blocks = data.TrialHandler(nReps=max_pairs_practice_blocks, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='practice_blocks')
    thisExp.addLoop(practice_blocks)  # add the loop to the experiment
    thisPractice_block = practice_blocks.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisPractice_block.rgb)
    if thisPractice_block != None:
        for paramName in thisPractice_block.keys():
            exec(paramName + '= thisPractice_block.' + paramName)
    
    for thisPractice_block in practice_blocks:
        currentLoop = practice_blocks
        # abbreviate parameter names if possible (e.g. rgb = thisPractice_block.rgb)
        if thisPractice_block != None:
            for paramName in thisPractice_block.keys():
                exec(paramName + '= thisPractice_block.' + paramName)
        
        # set up handler to look after randomisation of conditions etc
        practice_Afirst = data.TrialHandler(nReps=Afirst_nReps, method='sequential', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
            seed=None, name='practice_Afirst')
        thisExp.addLoop(practice_Afirst)  # add the loop to the experiment
        thisPractice_Afirst = practice_Afirst.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisPractice_Afirst.rgb)
        if thisPractice_Afirst != None:
            for paramName in thisPractice_Afirst.keys():
                exec(paramName + '= thisPractice_Afirst.' + paramName)
        
        for thisPractice_Afirst in practice_Afirst:
            currentLoop = practice_Afirst
            # abbreviate parameter names if possible (e.g. rgb = thisPractice_Afirst.rgb)
            if thisPractice_Afirst != None:
                for paramName in thisPractice_Afirst.keys():
                    exec(paramName + '= thisPractice_Afirst.' + paramName)
            
            # ------Prepare to start Routine "preblock_A"-------
            t = 0
            preblock_AClock.reset()  # clock
            frameN = -1
            continueRoutine = True
            # update component parameters for each repeat
            # Option to simulates using ResponseEmulator:
            if Monkey:
                simulated_responses = [(1.1, 'e'), (1.1, 'i')]  # simulated responses take the form (onsetTime, responseKey). You can simulate more than one.
                responder = ResponseEmulator(simulated_responses)
                responder.start()
            
            # Generate list of stimuli for the block
            stim1_catA_stimuli_many = generate_trials('labelA_stimuli', 2, True)  # function and variable determined at begin exp.
            stim1_catB_stimuli_many = generate_trials('labelB_stimuli', 2, True)
            stim2_catA_stimuli_many = generate_trials('targetA_stimuli', 2, True)
            stim2_catB_stimuli_many = generate_trials('targetB_stimuli', 2, True)
            img_stim1_catA_stimuli_many = generate_trials('labelA_image_stimuli', 2, True)
            img_stim1_catB_stimuli_many = generate_trials('labelB_image_stimuli', 2, True)
            img_stim2_catA_stimuli_many = generate_trials('targetA_image_stimuli', 2, True)
            img_stim2_catB_stimuli_many = generate_trials('targetB_image_stimuli', 2, True)
            
            rule_box_A.setText(rule_A)
            preblock_response_A = event.BuilderKeyResponse()
            # keep track of which components have finished
            preblock_AComponents = [rule_box_A, preblock_response_A]
            for thisComponent in preblock_AComponents:
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            
            # -------Start Routine "preblock_A"-------
            while continueRoutine:
                # get current time
                t = preblock_AClock.getTime()
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                
                # *rule_box_A* updates
                if t >= 0.4 and rule_box_A.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    rule_box_A.tStart = t
                    rule_box_A.frameNStart = frameN  # exact frame index
                    rule_box_A.setAutoDraw(True)
                
                # *preblock_response_A* updates
                if t >= 1 and preblock_response_A.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    preblock_response_A.tStart = t
                    preblock_response_A.frameNStart = frameN  # exact frame index
                    preblock_response_A.status = STARTED
                    # keyboard checking is just starting
                    event.clearEvents(eventType='keyboard')
                if preblock_response_A.status == STARTED:
                    theseKeys = event.getKeys(keyList=['e', 'i'])
                    
                    # check for quit:
                    if "escape" in theseKeys:
                        endExpNow = True
                    if len(theseKeys) > 0:  # at least one key was pressed
                        # a response ends the routine
                        continueRoutine = False
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in preblock_AComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # check for quit (the Esc key)
                if endExpNow or event.getKeys(keyList=["escape"]):
                    core.quit()
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "preblock_A"-------
            for thisComponent in preblock_AComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            
            # the Routine "preblock_A" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # set up handler to look after randomisation of conditions etc
            practice_trials_Afirst = data.TrialHandler(nReps=reptitions, method='random', 
                extraInfo=expInfo, originPath=-1,
                trialList=data.importConditions('block_layout.xlsx'),
                seed=None, name='practice_trials_Afirst')
            thisExp.addLoop(practice_trials_Afirst)  # add the loop to the experiment
            thisPractice_trials_Afirst = practice_trials_Afirst.trialList[0]  # so we can initialise stimuli with some values
            # abbreviate parameter names if possible (e.g. rgb = thisPractice_trials_Afirst.rgb)
            if thisPractice_trials_Afirst != None:
                for paramName in thisPractice_trials_Afirst.keys():
                    exec(paramName + '= thisPractice_trials_Afirst.' + paramName)
            
            for thisPractice_trials_Afirst in practice_trials_Afirst:
                currentLoop = practice_trials_Afirst
                # abbreviate parameter names if possible (e.g. rgb = thisPractice_trials_Afirst.rgb)
                if thisPractice_trials_Afirst != None:
                    for paramName in thisPractice_trials_Afirst.keys():
                        exec(paramName + '= thisPractice_trials_Afirst.' + paramName)
                
                # ------Prepare to start Routine "trial_A"-------
                t = 0
                trial_AClock.reset()  # clock
                frameN = -1
                continueRoutine = True
                # update component parameters for each repeat
                # Option to simulates using ResponseEmulator:
                if Monkey:
                    simulated_responses = [(0.5, 'e'), (0.5, 'i')]  # simulated responses take the form (onsetTime, responseKey). You can simulate more than one.
                    responder = ResponseEmulator(simulated_responses)
                    responder.start()
                
                # For each stimlulus, choose a random exemplar from the appropriate list
                # word stimulus 1
                if stimulus1_category == 'a':
                    stimulus1 = stim1_catA_stimuli_many.pop()
                elif stimulus1_category == 'b':
                    stimulus1 = stim1_catB_stimuli_many.pop()
                
                # word stimulus 2
                if stimulus2_category == 'c':
                    stimulus2 = stim2_catA_stimuli_many.pop()
                elif stimulus2_category == 'd':
                    stimulus2 = stim2_catB_stimuli_many.pop()
                
                # image stimulus 1
                if stimulus1_category == 'a':
                    img_stimulus1 = img_stim1_catA_stimuli_many.pop()
                elif stimulus1_category == 'b':
                    img_stimulus1 = img_stim1_catB_stimuli_many.pop()
                
                # image stimulus 2
                if stimulus2_category == 'c':
                    img_stimulus2 = img_stim2_catA_stimuli_many.pop()
                elif stimulus2_category == 'd':
                    img_stimulus2 = img_stim2_catB_stimuli_many.pop()
                
                # set correct and incorrect responses
                if moving_response_options == False:
                    response_option_left = response_option_B  # i.e., the focal trial type is the right hand one, for hand dominance
                    response_option_right = response_option_A
                    response_option_onset = 0  # response options are onscreen constantly
                    if (trialType == 1) or (trialType == 4):
                        required_allowed = 'i'
                        required_correct = 'i'
                        feedback_allowed = 'e'
                        feedback_correct = 'e'
                    elif (trialType == 2) or (trialType == 3):
                        required_allowed = 'e'
                        required_correct = 'e'
                        feedback_allowed = 'i'
                        feedback_correct = 'i'
                elif moving_response_options == True:
                    rand_positions = randint(1, 3)
                    response_option_onset = 0.4  # response options appear with stimuli
                    if rand_positions == 1:
                        response_option_left = response_option_B
                        response_option_right = response_option_A
                        if (trialType == 1) or (trialType == 4):
                            required_allowed = 'i'
                            required_correct = 'i'
                            feedback_allowed = 'e'
                            feedback_correct = 'e'
                        elif (trialType == 2) or (trialType == 3):
                            required_allowed = 'e'
                            required_correct = 'e'
                            feedback_allowed = 'i'
                            feedback_correct = 'i'
                    elif rand_positions == 2:
                        response_option_left = response_option_A
                        response_option_right = response_option_B
                        if (trialType == 1) or (trialType == 4):
                            required_allowed = 'e'
                            required_correct = 'e'
                            feedback_allowed = 'i'
                            feedback_correct = 'i'
                        elif (trialType == 2) or (trialType == 3):
                            required_allowed = 'i'
                            required_correct = 'i'
                            feedback_allowed = 'e'
                            feedback_correct = 'e'
                image_stimulus1_box_A.setPos(image_stimulus1_location)
                image_stimulus1_box_A.setImage(img_stimulus1)
                image_stimulus2_box_A.setPos(image_stimulus2_location)
                image_stimulus2_box_A.setImage(img_stimulus2)
                stimulus1_box_A.setText(stimulus1)
                stimulus1_box_A.setPos(stimulus1_location)
                stimulus2_box_A.setText(stimulus2)
                stimulus2_box_A.setPos(stimulus2_location)
                required_response_A = event.BuilderKeyResponse()
                feedback_response_A = event.BuilderKeyResponse()
                left_box_A.setText(response_option_left)
                left_box_A.setPos(response_option_left_location)
                right_box_A.setText(response_option_right)
                right_box_A.setPos(response_option_right_location)
                accuracy_feedback_box_A.setPos(accuracy_feedback_location)
                # keep track of which components have finished
                trial_AComponents = [image_stimulus1_box_A, image_stimulus2_box_A, stimulus1_box_A, stimulus2_box_A, required_response_A, feedback_response_A, left_box_A, right_box_A, accuracy_feedback_box_A]
                for thisComponent in trial_AComponents:
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                
                # -------Start Routine "trial_A"-------
                while continueRoutine:
                    # get current time
                    t = trial_AClock.getTime()
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    # Accuracy feedback message
                    if len(feedback_response_A.keys)<1:
                        accuracyFeedback=""
                    else:
                        accuracyFeedback="X"
                    
                    # *image_stimulus1_box_A* updates
                    if t >= 0.4 and image_stimulus1_box_A.status == NOT_STARTED:
                        # keep track of start time/frame for later
                        image_stimulus1_box_A.tStart = t
                        image_stimulus1_box_A.frameNStart = frameN  # exact frame index
                        image_stimulus1_box_A.setAutoDraw(True)
                    
                    # *image_stimulus2_box_A* updates
                    if t >= 0.4 and image_stimulus2_box_A.status == NOT_STARTED:
                        # keep track of start time/frame for later
                        image_stimulus2_box_A.tStart = t
                        image_stimulus2_box_A.frameNStart = frameN  # exact frame index
                        image_stimulus2_box_A.setAutoDraw(True)
                    
                    # *stimulus1_box_A* updates
                    if t >= 0.4 and stimulus1_box_A.status == NOT_STARTED:
                        # keep track of start time/frame for later
                        stimulus1_box_A.tStart = t
                        stimulus1_box_A.frameNStart = frameN  # exact frame index
                        stimulus1_box_A.setAutoDraw(True)
                    
                    # *stimulus2_box_A* updates
                    if t >= 0.4 and stimulus2_box_A.status == NOT_STARTED:
                        # keep track of start time/frame for later
                        stimulus2_box_A.tStart = t
                        stimulus2_box_A.frameNStart = frameN  # exact frame index
                        stimulus2_box_A.setAutoDraw(True)
                    
                    # *required_response_A* updates
                    if t >= 0.4 and required_response_A.status == NOT_STARTED:
                        # keep track of start time/frame for later
                        required_response_A.tStart = t
                        required_response_A.frameNStart = frameN  # exact frame index
                        required_response_A.status = STARTED
                        # AllowedKeys looks like a variable named `required_allowed`
                        if not type(required_allowed) in [list, tuple, np.ndarray]:
                            if not isinstance(required_allowed, basestring):
                                logging.error('AllowedKeys variable `required_allowed` is not string- or list-like.')
                                core.quit()
                            elif not ',' in required_allowed: required_allowed = (required_allowed,)
                            else:  required_allowed = eval(required_allowed)
                        # keyboard checking is just starting
                        win.callOnFlip(required_response_A.clock.reset)  # t=0 on next screen flip
                        event.clearEvents(eventType='keyboard')
                    if required_response_A.status == STARTED:
                        theseKeys = event.getKeys(keyList=list(required_allowed))
                        
                        # check for quit:
                        if "escape" in theseKeys:
                            endExpNow = True
                        if len(theseKeys) > 0:  # at least one key was pressed
                            if required_response_A.keys == []:  # then this was the first keypress
                                required_response_A.keys = theseKeys[0]  # just the first key pressed
                                required_response_A.rt = required_response_A.clock.getTime()
                                # was this 'correct'?
                                if (required_response_A.keys == str(required_correct)) or (required_response_A.keys == required_correct):
                                    required_response_A.corr = 1
                                else:
                                    required_response_A.corr = 0
                                # a response ends the routine
                                continueRoutine = False
                    
                    # *feedback_response_A* updates
                    if t >= 0.4 and feedback_response_A.status == NOT_STARTED:
                        # keep track of start time/frame for later
                        feedback_response_A.tStart = t
                        feedback_response_A.frameNStart = frameN  # exact frame index
                        feedback_response_A.status = STARTED
                        # AllowedKeys looks like a variable named `feedback_allowed`
                        if not type(feedback_allowed) in [list, tuple, np.ndarray]:
                            if not isinstance(feedback_allowed, basestring):
                                logging.error('AllowedKeys variable `feedback_allowed` is not string- or list-like.')
                                core.quit()
                            elif not ',' in feedback_allowed: feedback_allowed = (feedback_allowed,)
                            else:  feedback_allowed = eval(feedback_allowed)
                        # keyboard checking is just starting
                        win.callOnFlip(feedback_response_A.clock.reset)  # t=0 on next screen flip
                        event.clearEvents(eventType='keyboard')
                    if feedback_response_A.status == STARTED:
                        theseKeys = event.getKeys(keyList=list(feedback_allowed))
                        
                        # check for quit:
                        if "escape" in theseKeys:
                            endExpNow = True
                        if len(theseKeys) > 0:  # at least one key was pressed
                            if feedback_response_A.keys == []:  # then this was the first keypress
                                feedback_response_A.keys = theseKeys[0]  # just the first key pressed
                                feedback_response_A.rt = feedback_response_A.clock.getTime()
                                # was this 'correct'?
                                if (feedback_response_A.keys == str(feedback_correct)) or (feedback_response_A.keys == feedback_correct):
                                    feedback_response_A.corr = 1
                                else:
                                    feedback_response_A.corr = 0
                    
                    # *left_box_A* updates
                    if t >= response_option_onset and left_box_A.status == NOT_STARTED:
                        # keep track of start time/frame for later
                        left_box_A.tStart = t
                        left_box_A.frameNStart = frameN  # exact frame index
                        left_box_A.setAutoDraw(True)
                    
                    # *right_box_A* updates
                    if t >= response_option_onset and right_box_A.status == NOT_STARTED:
                        # keep track of start time/frame for later
                        right_box_A.tStart = t
                        right_box_A.frameNStart = frameN  # exact frame index
                        right_box_A.setAutoDraw(True)
                    
                    # *accuracy_feedback_box_A* updates
                    if t >= 0.4 and accuracy_feedback_box_A.status == NOT_STARTED:
                        # keep track of start time/frame for later
                        accuracy_feedback_box_A.tStart = t
                        accuracy_feedback_box_A.frameNStart = frameN  # exact frame index
                        accuracy_feedback_box_A.setAutoDraw(True)
                    if accuracy_feedback_box_A.status == STARTED:  # only update if drawing
                        accuracy_feedback_box_A.setText(accuracyFeedback, log=False)
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in trial_AComponents:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # check for quit (the Esc key)
                    if endExpNow or event.getKeys(keyList=["escape"]):
                        core.quit()
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # -------Ending Routine "trial_A"-------
                for thisComponent in trial_AComponents:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                # save exemplars to experiment handler so they're written to the csv file
                thisExp.addData('stimulus1', stimulus1)
                thisExp.addData('stimulus2', stimulus2)
                thisExp.addData('img_stimulus1', img_stimulus1)
                thisExp.addData('img_stimulus2', img_stimulus2)
                thisExp.addData('response_option_left', response_option_left)
                thisExp.addData('response_option_right', response_option_right)
                # check responses
                if required_response_A.keys in ['', [], None]:  # No response was made
                    required_response_A.keys=None
                    # was no response the correct answer?!
                    if str(required_correct).lower() == 'none':
                       required_response_A.corr = 1  # correct non-response
                    else:
                       required_response_A.corr = 0  # failed to respond (incorrectly)
                # store data for practice_trials_Afirst (TrialHandler)
                practice_trials_Afirst.addData('required_response_A.keys',required_response_A.keys)
                practice_trials_Afirst.addData('required_response_A.corr', required_response_A.corr)
                if required_response_A.keys != None:  # we had a response
                    practice_trials_Afirst.addData('required_response_A.rt', required_response_A.rt)
                # check responses
                if feedback_response_A.keys in ['', [], None]:  # No response was made
                    feedback_response_A.keys=None
                    # was no response the correct answer?!
                    if str(feedback_correct).lower() == 'none':
                       feedback_response_A.corr = 1  # correct non-response
                    else:
                       feedback_response_A.corr = 0  # failed to respond (incorrectly)
                # store data for practice_trials_Afirst (TrialHandler)
                practice_trials_Afirst.addData('feedback_response_A.keys',feedback_response_A.keys)
                practice_trials_Afirst.addData('feedback_response_A.corr', feedback_response_A.corr)
                if feedback_response_A.keys != None:  # we had a response
                    practice_trials_Afirst.addData('feedback_response_A.rt', feedback_response_A.rt)
                # the Routine "trial_A" was not non-slip safe, so reset the non-slip timer
                routineTimer.reset()
                thisExp.nextEntry()
                
            # completed reptitions repeats of 'practice_trials_Afirst'
            
            
            # ------Prepare to start Routine "practice_postblock_A"-------
            t = 0
            practice_postblock_AClock.reset()  # clock
            frameN = -1
            continueRoutine = True
            # update component parameters for each repeat
            # Option to simulates using ResponseEmulator:
            if Monkey:
                simulated_responses = [(1.1, 'e'), (1.1, 'i')]  # simulated responses take the form (onsetTime, responseKey). You can simulate more than one.
                responder = ResponseEmulator(simulated_responses)
                responder.start()
            
            # calculate summary stats
            if(starting_block == 'a'):  
                prac_block_A_percentage_accuracy = (float(practice_trials_Afirst.data['required_response_A.corr'].count()) - float(practice_trials_Afirst.data['feedback_response_A.corr'].sum())) /  float(practice_trials_Afirst.data['required_response_A.corr'].count()) * 100 
                prac_block_A_median_latency = np.median(practice_trials_Afirst.data['required_response_A.rt'])
            
            if(starting_block == 'b'):  
                prac_block_A_percentage_accuracy = (float(practice_trials_Asecond.data['required_response_A.corr'].count()) - float(practice_trials_Asecond.data['feedback_response_A.corr'].sum())) /  float(practice_trials_Asecond.data['required_response_A.corr'].count()) * 100 
                prac_block_A_median_latency = np.median(practice_trials_Asecond.data['required_response_A.rt'])
            
            # set messages
            msg_accuracy = "%s %i %s" %(accuracy, prac_block_A_percentage_accuracy, percentCorrect) 
            msg_latency = "%s %.2f %s" %(speed, prac_block_A_median_latency, seconds)
            
            ### save summary stats to experiment handler so they're written to the csv file
            ##thisExp.addData('prac_block_A_percentage_accuracy', prac_block_A_percentage_accuracy)
            ##thisExp.addData('prac_block_A_median_latency', prac_block_A_median_latency)
            practice_aim_box_A.setText(aim)
            practice_accuracy_box_A.setText(msg_accuracy)
            practice_latency_box_A.setText(msg_latency)
            press_box_prac_A.setText(press_message)
            practice_postblock_response_A = event.BuilderKeyResponse()
            # keep track of which components have finished
            practice_postblock_AComponents = [practice_aim_box_A, practice_accuracy_box_A, practice_latency_box_A, press_box_prac_A, practice_postblock_response_A]
            for thisComponent in practice_postblock_AComponents:
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            
            # -------Start Routine "practice_postblock_A"-------
            while continueRoutine:
                # get current time
                t = practice_postblock_AClock.getTime()
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                
                # *practice_aim_box_A* updates
                if t >= 0.4 and practice_aim_box_A.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    practice_aim_box_A.tStart = t
                    practice_aim_box_A.frameNStart = frameN  # exact frame index
                    practice_aim_box_A.setAutoDraw(True)
                
                # *practice_accuracy_box_A* updates
                if t >= 0.4 and practice_accuracy_box_A.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    practice_accuracy_box_A.tStart = t
                    practice_accuracy_box_A.frameNStart = frameN  # exact frame index
                    practice_accuracy_box_A.setAutoDraw(True)
                
                # *practice_latency_box_A* updates
                if t >= 0.4 and practice_latency_box_A.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    practice_latency_box_A.tStart = t
                    practice_latency_box_A.frameNStart = frameN  # exact frame index
                    practice_latency_box_A.setAutoDraw(True)
                
                # *press_box_prac_A* updates
                if t >= 0.4 and press_box_prac_A.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    press_box_prac_A.tStart = t
                    press_box_prac_A.frameNStart = frameN  # exact frame index
                    press_box_prac_A.setAutoDraw(True)
                
                # *practice_postblock_response_A* updates
                if t >= 1 and practice_postblock_response_A.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    practice_postblock_response_A.tStart = t
                    practice_postblock_response_A.frameNStart = frameN  # exact frame index
                    practice_postblock_response_A.status = STARTED
                    # keyboard checking is just starting
                    event.clearEvents(eventType='keyboard')
                if practice_postblock_response_A.status == STARTED:
                    theseKeys = event.getKeys(keyList=['e', 'i'])
                    
                    # check for quit:
                    if "escape" in theseKeys:
                        endExpNow = True
                    if len(theseKeys) > 0:  # at least one key was pressed
                        # a response ends the routine
                        continueRoutine = False
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in practice_postblock_AComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # check for quit (the Esc key)
                if endExpNow or event.getKeys(keyList=["escape"]):
                    core.quit()
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "practice_postblock_A"-------
            for thisComponent in practice_postblock_AComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            
            # the Routine "practice_postblock_A" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
        # completed Afirst_nReps repeats of 'practice_Afirst'
        
        
        # ------Prepare to start Routine "preblock_B"-------
        t = 0
        preblock_BClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        # Option to simulates using ResponseEmulator:
        if Monkey:
            simulated_responses = [(1.1, 'e'), (1.1, 'i')]  # simulated responses take the form (onsetTime, responseKey). You can simulate more than one.
            responder = ResponseEmulator(simulated_responses)
            responder.start()
        
        # Generate list of stimuli for the block
        stim1_catA_stimuli_many = generate_trials('labelA_stimuli', 2, True)  # function and variable determined at begin exp.
        stim1_catB_stimuli_many = generate_trials('labelB_stimuli', 2, True)
        stim2_catA_stimuli_many = generate_trials('targetA_stimuli', 2, True)
        stim2_catB_stimuli_many = generate_trials('targetB_stimuli', 2, True)
        img_stim1_catA_stimuli_many = generate_trials('labelA_image_stimuli', 2, True)
        img_stim1_catB_stimuli_many = generate_trials('labelB_image_stimuli', 2, True)
        img_stim2_catA_stimuli_many = generate_trials('targetA_image_stimuli', 2, True)
        img_stim2_catB_stimuli_many = generate_trials('targetB_image_stimuli', 2, True)
        rule_box_B.setText(rule_B)
        preblock_response_B = event.BuilderKeyResponse()
        # keep track of which components have finished
        preblock_BComponents = [rule_box_B, preblock_response_B]
        for thisComponent in preblock_BComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "preblock_B"-------
        while continueRoutine:
            # get current time
            t = preblock_BClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            
            # *rule_box_B* updates
            if t >= 0.4 and rule_box_B.status == NOT_STARTED:
                # keep track of start time/frame for later
                rule_box_B.tStart = t
                rule_box_B.frameNStart = frameN  # exact frame index
                rule_box_B.setAutoDraw(True)
            
            # *preblock_response_B* updates
            if t >= 1 and preblock_response_B.status == NOT_STARTED:
                # keep track of start time/frame for later
                preblock_response_B.tStart = t
                preblock_response_B.frameNStart = frameN  # exact frame index
                preblock_response_B.status = STARTED
                # keyboard checking is just starting
                event.clearEvents(eventType='keyboard')
            if preblock_response_B.status == STARTED:
                theseKeys = event.getKeys(keyList=['e', 'i'])
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    # a response ends the routine
                    continueRoutine = False
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in preblock_BComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "preblock_B"-------
        for thisComponent in preblock_BComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        # the Routine "preblock_B" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        practice_trials_B = data.TrialHandler(nReps=reptitions, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions('block_layout.xlsx'),
            seed=None, name='practice_trials_B')
        thisExp.addLoop(practice_trials_B)  # add the loop to the experiment
        thisPractice_trials_B = practice_trials_B.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisPractice_trials_B.rgb)
        if thisPractice_trials_B != None:
            for paramName in thisPractice_trials_B.keys():
                exec(paramName + '= thisPractice_trials_B.' + paramName)
        
        for thisPractice_trials_B in practice_trials_B:
            currentLoop = practice_trials_B
            # abbreviate parameter names if possible (e.g. rgb = thisPractice_trials_B.rgb)
            if thisPractice_trials_B != None:
                for paramName in thisPractice_trials_B.keys():
                    exec(paramName + '= thisPractice_trials_B.' + paramName)
            
            # ------Prepare to start Routine "trial_B"-------
            t = 0
            trial_BClock.reset()  # clock
            frameN = -1
            continueRoutine = True
            # update component parameters for each repeat
            # Option to simulates using ResponseEmulator:
            if Monkey:
                simulated_responses = [(0.5, 'e'), (0.5, 'i')]  # simulated responses take the form (onsetTime, responseKey). You can simulate more than one.
                responder = ResponseEmulator(simulated_responses)
                responder.start()
            
            # For each stimlulus, choose a random exemplar from the appropriate list
            # word stimulus 1
            if stimulus1_category == 'a':
                stimulus1 = stim1_catA_stimuli_many.pop()
            elif stimulus1_category == 'b':
                stimulus1 = stim1_catB_stimuli_many.pop()
            
            # word stimulus 2
            if stimulus2_category == 'c':
                stimulus2 = stim2_catA_stimuli_many.pop()
            elif stimulus2_category == 'd':
                stimulus2 = stim2_catB_stimuli_many.pop()
            
            # image stimulus 1
            if stimulus1_category == 'a':
                img_stimulus1 = img_stim1_catA_stimuli_many.pop()
            elif stimulus1_category == 'b':
                img_stimulus1 = img_stim1_catB_stimuli_many.pop()
            
            # image stimulus 2
            if stimulus2_category == 'c':
                img_stimulus2 = img_stim2_catA_stimuli_many.pop()
            elif stimulus2_category == 'd':
                img_stimulus2 = img_stim2_catB_stimuli_many.pop()
            
            # set correct and incorrect responses
            if moving_response_options == False:
                response_option_left = response_option_B  # i.e., the focal trial type is the right hand one, for hand dominance
                response_option_right = response_option_A
                response_option_onset = 0  # response options are onscreen constantly
                if (trialType == 1) or (trialType == 4):
                    required_allowed = 'e'  # PATTERN REVERED FROM BLOCK A
                    required_correct = 'e'
                    feedback_allowed = 'i'
                    feedback_correct = 'i'
                elif (trialType == 2) or (trialType == 3):
                    required_allowed = 'i'  # PATTERN REVERED FROM BLOCK A
                    required_correct = 'i'
                    feedback_allowed = 'e'
                    feedback_correct = 'e'
            elif moving_response_options == True:
                rand_positions = randint(1, 3)
                response_option_onset = 0.4  # response options appear with stimuli
                if rand_positions == 1:
                    response_option_left = response_option_B
                    response_option_right = response_option_A
                    if (trialType == 1) or (trialType == 4):
                        required_allowed = 'e'  # PATTERN REVERED FROM BLOCK A
                        required_correct = 'e'
                        feedback_allowed = 'i'
                        feedback_correct = 'i'
                    elif (trialType == 2) or (trialType == 3):
                        required_allowed = 'i'  # PATTERN REVERED FROM BLOCK A
                        required_correct = 'i'
                        feedback_allowed = 'e'
                        feedback_correct = 'e'
                elif rand_positions == 2:
                    response_option_left = response_option_A
                    response_option_right = response_option_B
                    if (trialType == 1) or (trialType == 4):
                        required_allowed = 'i'  # PATTERN REVERED FROM BLOCK A
                        required_correct = 'i'
                        feedback_allowed = 'e'
                        feedback_correct = 'e'
                    elif (trialType == 2) or (trialType == 3):
                        required_allowed = 'e'  # PATTERN REVERED FROM BLOCK A
                        required_correct = 'e'
                        feedback_allowed = 'i'
                        feedback_correct = 'i'
            image_stimulus1_box_B.setPos(image_stimulus1_location)
            image_stimulus1_box_B.setImage(img_stimulus1)
            image_stimulus2_box_B.setPos(image_stimulus2_location)
            image_stimulus2_box_B.setImage(img_stimulus2)
            stimulus1_box_B.setText(stimulus1)
            stimulus1_box_B.setPos(stimulus1_location)
            stimulus2_box_B.setText(stimulus2)
            stimulus2_box_B.setPos(stimulus2_location)
            required_response_B = event.BuilderKeyResponse()
            feedback_response_B = event.BuilderKeyResponse()
            left_box_B.setText(response_option_left)
            left_box_B.setPos(response_option_left_location)
            right_box_B.setText(response_option_right)
            right_box_B.setPos(response_option_right_location)
            accuracy_feedback_box_B.setPos(accuracy_feedback_location)
            # keep track of which components have finished
            trial_BComponents = [image_stimulus1_box_B, image_stimulus2_box_B, stimulus1_box_B, stimulus2_box_B, required_response_B, feedback_response_B, left_box_B, right_box_B, accuracy_feedback_box_B]
            for thisComponent in trial_BComponents:
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            
            # -------Start Routine "trial_B"-------
            while continueRoutine:
                # get current time
                t = trial_BClock.getTime()
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                # Accuracy feedback message
                if len(feedback_response_B.keys)<1:
                    accuracyFeedback=""
                else:
                    accuracyFeedback="X"
                
                # *image_stimulus1_box_B* updates
                if t >= 0.4 and image_stimulus1_box_B.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    image_stimulus1_box_B.tStart = t
                    image_stimulus1_box_B.frameNStart = frameN  # exact frame index
                    image_stimulus1_box_B.setAutoDraw(True)
                
                # *image_stimulus2_box_B* updates
                if t >= 0.4 and image_stimulus2_box_B.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    image_stimulus2_box_B.tStart = t
                    image_stimulus2_box_B.frameNStart = frameN  # exact frame index
                    image_stimulus2_box_B.setAutoDraw(True)
                
                # *stimulus1_box_B* updates
                if t >= 0.4 and stimulus1_box_B.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    stimulus1_box_B.tStart = t
                    stimulus1_box_B.frameNStart = frameN  # exact frame index
                    stimulus1_box_B.setAutoDraw(True)
                
                # *stimulus2_box_B* updates
                if t >= 0.4 and stimulus2_box_B.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    stimulus2_box_B.tStart = t
                    stimulus2_box_B.frameNStart = frameN  # exact frame index
                    stimulus2_box_B.setAutoDraw(True)
                
                # *required_response_B* updates
                if t >= 0.4 and required_response_B.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    required_response_B.tStart = t
                    required_response_B.frameNStart = frameN  # exact frame index
                    required_response_B.status = STARTED
                    # AllowedKeys looks like a variable named `required_allowed`
                    if not type(required_allowed) in [list, tuple, np.ndarray]:
                        if not isinstance(required_allowed, basestring):
                            logging.error('AllowedKeys variable `required_allowed` is not string- or list-like.')
                            core.quit()
                        elif not ',' in required_allowed: required_allowed = (required_allowed,)
                        else:  required_allowed = eval(required_allowed)
                    # keyboard checking is just starting
                    win.callOnFlip(required_response_B.clock.reset)  # t=0 on next screen flip
                    event.clearEvents(eventType='keyboard')
                if required_response_B.status == STARTED:
                    theseKeys = event.getKeys(keyList=list(required_allowed))
                    
                    # check for quit:
                    if "escape" in theseKeys:
                        endExpNow = True
                    if len(theseKeys) > 0:  # at least one key was pressed
                        if required_response_B.keys == []:  # then this was the first keypress
                            required_response_B.keys = theseKeys[0]  # just the first key pressed
                            required_response_B.rt = required_response_B.clock.getTime()
                            # was this 'correct'?
                            if (required_response_B.keys == str(required_correct)) or (required_response_B.keys == required_correct):
                                required_response_B.corr = 1
                            else:
                                required_response_B.corr = 0
                            # a response ends the routine
                            continueRoutine = False
                
                # *feedback_response_B* updates
                if t >= 0.4 and feedback_response_B.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    feedback_response_B.tStart = t
                    feedback_response_B.frameNStart = frameN  # exact frame index
                    feedback_response_B.status = STARTED
                    # AllowedKeys looks like a variable named `feedback_allowed`
                    if not type(feedback_allowed) in [list, tuple, np.ndarray]:
                        if not isinstance(feedback_allowed, basestring):
                            logging.error('AllowedKeys variable `feedback_allowed` is not string- or list-like.')
                            core.quit()
                        elif not ',' in feedback_allowed: feedback_allowed = (feedback_allowed,)
                        else:  feedback_allowed = eval(feedback_allowed)
                    # keyboard checking is just starting
                    win.callOnFlip(feedback_response_B.clock.reset)  # t=0 on next screen flip
                    event.clearEvents(eventType='keyboard')
                if feedback_response_B.status == STARTED:
                    theseKeys = event.getKeys(keyList=list(feedback_allowed))
                    
                    # check for quit:
                    if "escape" in theseKeys:
                        endExpNow = True
                    if len(theseKeys) > 0:  # at least one key was pressed
                        if feedback_response_B.keys == []:  # then this was the first keypress
                            feedback_response_B.keys = theseKeys[0]  # just the first key pressed
                            feedback_response_B.rt = feedback_response_B.clock.getTime()
                            # was this 'correct'?
                            if (feedback_response_B.keys == str(feedback_correct)) or (feedback_response_B.keys == feedback_correct):
                                feedback_response_B.corr = 1
                            else:
                                feedback_response_B.corr = 0
                
                # *left_box_B* updates
                if t >= response_option_onset and left_box_B.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    left_box_B.tStart = t
                    left_box_B.frameNStart = frameN  # exact frame index
                    left_box_B.setAutoDraw(True)
                
                # *right_box_B* updates
                if t >= response_option_onset and right_box_B.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    right_box_B.tStart = t
                    right_box_B.frameNStart = frameN  # exact frame index
                    right_box_B.setAutoDraw(True)
                
                # *accuracy_feedback_box_B* updates
                if t >= 0.4 and accuracy_feedback_box_B.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    accuracy_feedback_box_B.tStart = t
                    accuracy_feedback_box_B.frameNStart = frameN  # exact frame index
                    accuracy_feedback_box_B.setAutoDraw(True)
                if accuracy_feedback_box_B.status == STARTED:  # only update if drawing
                    accuracy_feedback_box_B.setText(accuracyFeedback, log=False)
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in trial_BComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # check for quit (the Esc key)
                if endExpNow or event.getKeys(keyList=["escape"]):
                    core.quit()
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "trial_B"-------
            for thisComponent in trial_BComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # save exemplars to experiment handler so they're written to the csv file
            thisExp.addData('stimulus1', stimulus1)
            thisExp.addData('stimulus2', stimulus2)
            thisExp.addData('img_stimulus1', img_stimulus1)
            thisExp.addData('img_stimulus2', img_stimulus2)
            thisExp.addData('response_option_left', response_option_left)
            thisExp.addData('response_option_right', response_option_right)
            # check responses
            if required_response_B.keys in ['', [], None]:  # No response was made
                required_response_B.keys=None
                # was no response the correct answer?!
                if str(required_correct).lower() == 'none':
                   required_response_B.corr = 1  # correct non-response
                else:
                   required_response_B.corr = 0  # failed to respond (incorrectly)
            # store data for practice_trials_B (TrialHandler)
            practice_trials_B.addData('required_response_B.keys',required_response_B.keys)
            practice_trials_B.addData('required_response_B.corr', required_response_B.corr)
            if required_response_B.keys != None:  # we had a response
                practice_trials_B.addData('required_response_B.rt', required_response_B.rt)
            # check responses
            if feedback_response_B.keys in ['', [], None]:  # No response was made
                feedback_response_B.keys=None
                # was no response the correct answer?!
                if str(feedback_correct).lower() == 'none':
                   feedback_response_B.corr = 1  # correct non-response
                else:
                   feedback_response_B.corr = 0  # failed to respond (incorrectly)
            # store data for practice_trials_B (TrialHandler)
            practice_trials_B.addData('feedback_response_B.keys',feedback_response_B.keys)
            practice_trials_B.addData('feedback_response_B.corr', feedback_response_B.corr)
            if feedback_response_B.keys != None:  # we had a response
                practice_trials_B.addData('feedback_response_B.rt', feedback_response_B.rt)
            # the Routine "trial_B" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed reptitions repeats of 'practice_trials_B'
        
        
        # ------Prepare to start Routine "practice_postblock_B"-------
        t = 0
        practice_postblock_BClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        # Option to simulates using ResponseEmulator:
        if Monkey:
            simulated_responses = [(1.1, 'e'), (1.1, 'i')]  # simulated responses take the form (onsetTime, responseKey). You can simulate more than one.
            responder = ResponseEmulator(simulated_responses)
            responder.start()
        
        # calculate summary stats
        prac_block_B_percentage_accuracy = (float(practice_trials_B.data['required_response_B.corr'].count()) - float(practice_trials_B.data['feedback_response_B.corr'].sum())) /  float(practice_trials_B.data['required_response_B.corr'].count()) * 100 
        prac_block_B_median_latency = np.median(practice_trials_B.data['required_response_B.rt'])
        
        # set messages
        msg_accuracy = "%s %i %s" %(accuracy, prac_block_B_percentage_accuracy, percentCorrect) 
        msg_latency = "%s %.2f %s" %(speed, prac_block_B_median_latency, seconds)
        
        ### save summary stats to experiment handler so they're written to the csv file
        ##thisExp.addData('prac_block_B_percentage_accuracy', prac_block_B_percentage_accuracy)
        ##thisExp.addData('prac_block_B_median_latency', prac_block_B_median_latency)
        practice_aim_box_B.setText(aim)
        practice_accuracy_box_B.setText(msg_accuracy)
        practice_latency_box_B.setText(msg_latency)
        press_box_prac_B.setText(press_message)
        practice_postblock_response_B = event.BuilderKeyResponse()
        # keep track of which components have finished
        practice_postblock_BComponents = [practice_aim_box_B, practice_accuracy_box_B, practice_latency_box_B, press_box_prac_B, practice_postblock_response_B]
        for thisComponent in practice_postblock_BComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "practice_postblock_B"-------
        while continueRoutine:
            # get current time
            t = practice_postblock_BClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            
            # *practice_aim_box_B* updates
            if t >= 0.4 and practice_aim_box_B.status == NOT_STARTED:
                # keep track of start time/frame for later
                practice_aim_box_B.tStart = t
                practice_aim_box_B.frameNStart = frameN  # exact frame index
                practice_aim_box_B.setAutoDraw(True)
            
            # *practice_accuracy_box_B* updates
            if t >= 0.4 and practice_accuracy_box_B.status == NOT_STARTED:
                # keep track of start time/frame for later
                practice_accuracy_box_B.tStart = t
                practice_accuracy_box_B.frameNStart = frameN  # exact frame index
                practice_accuracy_box_B.setAutoDraw(True)
            
            # *practice_latency_box_B* updates
            if t >= 0.4 and practice_latency_box_B.status == NOT_STARTED:
                # keep track of start time/frame for later
                practice_latency_box_B.tStart = t
                practice_latency_box_B.frameNStart = frameN  # exact frame index
                practice_latency_box_B.setAutoDraw(True)
            
            # *press_box_prac_B* updates
            if t >= 0.4 and press_box_prac_B.status == NOT_STARTED:
                # keep track of start time/frame for later
                press_box_prac_B.tStart = t
                press_box_prac_B.frameNStart = frameN  # exact frame index
                press_box_prac_B.setAutoDraw(True)
            
            # *practice_postblock_response_B* updates
            if t >= 1 and practice_postblock_response_B.status == NOT_STARTED:
                # keep track of start time/frame for later
                practice_postblock_response_B.tStart = t
                practice_postblock_response_B.frameNStart = frameN  # exact frame index
                practice_postblock_response_B.status = STARTED
                # keyboard checking is just starting
                event.clearEvents(eventType='keyboard')
            if practice_postblock_response_B.status == STARTED:
                theseKeys = event.getKeys(keyList=['e', 'i'])
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    # a response ends the routine
                    continueRoutine = False
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in practice_postblock_BComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "practice_postblock_B"-------
        for thisComponent in practice_postblock_BComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        # the Routine "practice_postblock_B" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        practice_Asecond = data.TrialHandler(nReps=Asecond_nReps, method='sequential', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
            seed=None, name='practice_Asecond')
        thisExp.addLoop(practice_Asecond)  # add the loop to the experiment
        thisPractice_Asecond = practice_Asecond.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisPractice_Asecond.rgb)
        if thisPractice_Asecond != None:
            for paramName in thisPractice_Asecond.keys():
                exec(paramName + '= thisPractice_Asecond.' + paramName)
        
        for thisPractice_Asecond in practice_Asecond:
            currentLoop = practice_Asecond
            # abbreviate parameter names if possible (e.g. rgb = thisPractice_Asecond.rgb)
            if thisPractice_Asecond != None:
                for paramName in thisPractice_Asecond.keys():
                    exec(paramName + '= thisPractice_Asecond.' + paramName)
            
            # ------Prepare to start Routine "preblock_A"-------
            t = 0
            preblock_AClock.reset()  # clock
            frameN = -1
            continueRoutine = True
            # update component parameters for each repeat
            # Option to simulates using ResponseEmulator:
            if Monkey:
                simulated_responses = [(1.1, 'e'), (1.1, 'i')]  # simulated responses take the form (onsetTime, responseKey). You can simulate more than one.
                responder = ResponseEmulator(simulated_responses)
                responder.start()
            
            # Generate list of stimuli for the block
            stim1_catA_stimuli_many = generate_trials('labelA_stimuli', 2, True)  # function and variable determined at begin exp.
            stim1_catB_stimuli_many = generate_trials('labelB_stimuli', 2, True)
            stim2_catA_stimuli_many = generate_trials('targetA_stimuli', 2, True)
            stim2_catB_stimuli_many = generate_trials('targetB_stimuli', 2, True)
            img_stim1_catA_stimuli_many = generate_trials('labelA_image_stimuli', 2, True)
            img_stim1_catB_stimuli_many = generate_trials('labelB_image_stimuli', 2, True)
            img_stim2_catA_stimuli_many = generate_trials('targetA_image_stimuli', 2, True)
            img_stim2_catB_stimuli_many = generate_trials('targetB_image_stimuli', 2, True)
            
            rule_box_A.setText(rule_A)
            preblock_response_A = event.BuilderKeyResponse()
            # keep track of which components have finished
            preblock_AComponents = [rule_box_A, preblock_response_A]
            for thisComponent in preblock_AComponents:
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            
            # -------Start Routine "preblock_A"-------
            while continueRoutine:
                # get current time
                t = preblock_AClock.getTime()
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                
                # *rule_box_A* updates
                if t >= 0.4 and rule_box_A.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    rule_box_A.tStart = t
                    rule_box_A.frameNStart = frameN  # exact frame index
                    rule_box_A.setAutoDraw(True)
                
                # *preblock_response_A* updates
                if t >= 1 and preblock_response_A.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    preblock_response_A.tStart = t
                    preblock_response_A.frameNStart = frameN  # exact frame index
                    preblock_response_A.status = STARTED
                    # keyboard checking is just starting
                    event.clearEvents(eventType='keyboard')
                if preblock_response_A.status == STARTED:
                    theseKeys = event.getKeys(keyList=['e', 'i'])
                    
                    # check for quit:
                    if "escape" in theseKeys:
                        endExpNow = True
                    if len(theseKeys) > 0:  # at least one key was pressed
                        # a response ends the routine
                        continueRoutine = False
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in preblock_AComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # check for quit (the Esc key)
                if endExpNow or event.getKeys(keyList=["escape"]):
                    core.quit()
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "preblock_A"-------
            for thisComponent in preblock_AComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            
            # the Routine "preblock_A" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # set up handler to look after randomisation of conditions etc
            practice_trials_Asecond = data.TrialHandler(nReps=reptitions, method='random', 
                extraInfo=expInfo, originPath=-1,
                trialList=data.importConditions('block_layout.xlsx'),
                seed=None, name='practice_trials_Asecond')
            thisExp.addLoop(practice_trials_Asecond)  # add the loop to the experiment
            thisPractice_trials_Asecond = practice_trials_Asecond.trialList[0]  # so we can initialise stimuli with some values
            # abbreviate parameter names if possible (e.g. rgb = thisPractice_trials_Asecond.rgb)
            if thisPractice_trials_Asecond != None:
                for paramName in thisPractice_trials_Asecond.keys():
                    exec(paramName + '= thisPractice_trials_Asecond.' + paramName)
            
            for thisPractice_trials_Asecond in practice_trials_Asecond:
                currentLoop = practice_trials_Asecond
                # abbreviate parameter names if possible (e.g. rgb = thisPractice_trials_Asecond.rgb)
                if thisPractice_trials_Asecond != None:
                    for paramName in thisPractice_trials_Asecond.keys():
                        exec(paramName + '= thisPractice_trials_Asecond.' + paramName)
                
                # ------Prepare to start Routine "trial_A"-------
                t = 0
                trial_AClock.reset()  # clock
                frameN = -1
                continueRoutine = True
                # update component parameters for each repeat
                # Option to simulates using ResponseEmulator:
                if Monkey:
                    simulated_responses = [(0.5, 'e'), (0.5, 'i')]  # simulated responses take the form (onsetTime, responseKey). You can simulate more than one.
                    responder = ResponseEmulator(simulated_responses)
                    responder.start()
                
                # For each stimlulus, choose a random exemplar from the appropriate list
                # word stimulus 1
                if stimulus1_category == 'a':
                    stimulus1 = stim1_catA_stimuli_many.pop()
                elif stimulus1_category == 'b':
                    stimulus1 = stim1_catB_stimuli_many.pop()
                
                # word stimulus 2
                if stimulus2_category == 'c':
                    stimulus2 = stim2_catA_stimuli_many.pop()
                elif stimulus2_category == 'd':
                    stimulus2 = stim2_catB_stimuli_many.pop()
                
                # image stimulus 1
                if stimulus1_category == 'a':
                    img_stimulus1 = img_stim1_catA_stimuli_many.pop()
                elif stimulus1_category == 'b':
                    img_stimulus1 = img_stim1_catB_stimuli_many.pop()
                
                # image stimulus 2
                if stimulus2_category == 'c':
                    img_stimulus2 = img_stim2_catA_stimuli_many.pop()
                elif stimulus2_category == 'd':
                    img_stimulus2 = img_stim2_catB_stimuli_many.pop()
                
                # set correct and incorrect responses
                if moving_response_options == False:
                    response_option_left = response_option_B  # i.e., the focal trial type is the right hand one, for hand dominance
                    response_option_right = response_option_A
                    response_option_onset = 0  # response options are onscreen constantly
                    if (trialType == 1) or (trialType == 4):
                        required_allowed = 'i'
                        required_correct = 'i'
                        feedback_allowed = 'e'
                        feedback_correct = 'e'
                    elif (trialType == 2) or (trialType == 3):
                        required_allowed = 'e'
                        required_correct = 'e'
                        feedback_allowed = 'i'
                        feedback_correct = 'i'
                elif moving_response_options == True:
                    rand_positions = randint(1, 3)
                    response_option_onset = 0.4  # response options appear with stimuli
                    if rand_positions == 1:
                        response_option_left = response_option_B
                        response_option_right = response_option_A
                        if (trialType == 1) or (trialType == 4):
                            required_allowed = 'i'
                            required_correct = 'i'
                            feedback_allowed = 'e'
                            feedback_correct = 'e'
                        elif (trialType == 2) or (trialType == 3):
                            required_allowed = 'e'
                            required_correct = 'e'
                            feedback_allowed = 'i'
                            feedback_correct = 'i'
                    elif rand_positions == 2:
                        response_option_left = response_option_A
                        response_option_right = response_option_B
                        if (trialType == 1) or (trialType == 4):
                            required_allowed = 'e'
                            required_correct = 'e'
                            feedback_allowed = 'i'
                            feedback_correct = 'i'
                        elif (trialType == 2) or (trialType == 3):
                            required_allowed = 'i'
                            required_correct = 'i'
                            feedback_allowed = 'e'
                            feedback_correct = 'e'
                image_stimulus1_box_A.setPos(image_stimulus1_location)
                image_stimulus1_box_A.setImage(img_stimulus1)
                image_stimulus2_box_A.setPos(image_stimulus2_location)
                image_stimulus2_box_A.setImage(img_stimulus2)
                stimulus1_box_A.setText(stimulus1)
                stimulus1_box_A.setPos(stimulus1_location)
                stimulus2_box_A.setText(stimulus2)
                stimulus2_box_A.setPos(stimulus2_location)
                required_response_A = event.BuilderKeyResponse()
                feedback_response_A = event.BuilderKeyResponse()
                left_box_A.setText(response_option_left)
                left_box_A.setPos(response_option_left_location)
                right_box_A.setText(response_option_right)
                right_box_A.setPos(response_option_right_location)
                accuracy_feedback_box_A.setPos(accuracy_feedback_location)
                # keep track of which components have finished
                trial_AComponents = [image_stimulus1_box_A, image_stimulus2_box_A, stimulus1_box_A, stimulus2_box_A, required_response_A, feedback_response_A, left_box_A, right_box_A, accuracy_feedback_box_A]
                for thisComponent in trial_AComponents:
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                
                # -------Start Routine "trial_A"-------
                while continueRoutine:
                    # get current time
                    t = trial_AClock.getTime()
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    # Accuracy feedback message
                    if len(feedback_response_A.keys)<1:
                        accuracyFeedback=""
                    else:
                        accuracyFeedback="X"
                    
                    # *image_stimulus1_box_A* updates
                    if t >= 0.4 and image_stimulus1_box_A.status == NOT_STARTED:
                        # keep track of start time/frame for later
                        image_stimulus1_box_A.tStart = t
                        image_stimulus1_box_A.frameNStart = frameN  # exact frame index
                        image_stimulus1_box_A.setAutoDraw(True)
                    
                    # *image_stimulus2_box_A* updates
                    if t >= 0.4 and image_stimulus2_box_A.status == NOT_STARTED:
                        # keep track of start time/frame for later
                        image_stimulus2_box_A.tStart = t
                        image_stimulus2_box_A.frameNStart = frameN  # exact frame index
                        image_stimulus2_box_A.setAutoDraw(True)
                    
                    # *stimulus1_box_A* updates
                    if t >= 0.4 and stimulus1_box_A.status == NOT_STARTED:
                        # keep track of start time/frame for later
                        stimulus1_box_A.tStart = t
                        stimulus1_box_A.frameNStart = frameN  # exact frame index
                        stimulus1_box_A.setAutoDraw(True)
                    
                    # *stimulus2_box_A* updates
                    if t >= 0.4 and stimulus2_box_A.status == NOT_STARTED:
                        # keep track of start time/frame for later
                        stimulus2_box_A.tStart = t
                        stimulus2_box_A.frameNStart = frameN  # exact frame index
                        stimulus2_box_A.setAutoDraw(True)
                    
                    # *required_response_A* updates
                    if t >= 0.4 and required_response_A.status == NOT_STARTED:
                        # keep track of start time/frame for later
                        required_response_A.tStart = t
                        required_response_A.frameNStart = frameN  # exact frame index
                        required_response_A.status = STARTED
                        # AllowedKeys looks like a variable named `required_allowed`
                        if not type(required_allowed) in [list, tuple, np.ndarray]:
                            if not isinstance(required_allowed, basestring):
                                logging.error('AllowedKeys variable `required_allowed` is not string- or list-like.')
                                core.quit()
                            elif not ',' in required_allowed: required_allowed = (required_allowed,)
                            else:  required_allowed = eval(required_allowed)
                        # keyboard checking is just starting
                        win.callOnFlip(required_response_A.clock.reset)  # t=0 on next screen flip
                        event.clearEvents(eventType='keyboard')
                    if required_response_A.status == STARTED:
                        theseKeys = event.getKeys(keyList=list(required_allowed))
                        
                        # check for quit:
                        if "escape" in theseKeys:
                            endExpNow = True
                        if len(theseKeys) > 0:  # at least one key was pressed
                            if required_response_A.keys == []:  # then this was the first keypress
                                required_response_A.keys = theseKeys[0]  # just the first key pressed
                                required_response_A.rt = required_response_A.clock.getTime()
                                # was this 'correct'?
                                if (required_response_A.keys == str(required_correct)) or (required_response_A.keys == required_correct):
                                    required_response_A.corr = 1
                                else:
                                    required_response_A.corr = 0
                                # a response ends the routine
                                continueRoutine = False
                    
                    # *feedback_response_A* updates
                    if t >= 0.4 and feedback_response_A.status == NOT_STARTED:
                        # keep track of start time/frame for later
                        feedback_response_A.tStart = t
                        feedback_response_A.frameNStart = frameN  # exact frame index
                        feedback_response_A.status = STARTED
                        # AllowedKeys looks like a variable named `feedback_allowed`
                        if not type(feedback_allowed) in [list, tuple, np.ndarray]:
                            if not isinstance(feedback_allowed, basestring):
                                logging.error('AllowedKeys variable `feedback_allowed` is not string- or list-like.')
                                core.quit()
                            elif not ',' in feedback_allowed: feedback_allowed = (feedback_allowed,)
                            else:  feedback_allowed = eval(feedback_allowed)
                        # keyboard checking is just starting
                        win.callOnFlip(feedback_response_A.clock.reset)  # t=0 on next screen flip
                        event.clearEvents(eventType='keyboard')
                    if feedback_response_A.status == STARTED:
                        theseKeys = event.getKeys(keyList=list(feedback_allowed))
                        
                        # check for quit:
                        if "escape" in theseKeys:
                            endExpNow = True
                        if len(theseKeys) > 0:  # at least one key was pressed
                            if feedback_response_A.keys == []:  # then this was the first keypress
                                feedback_response_A.keys = theseKeys[0]  # just the first key pressed
                                feedback_response_A.rt = feedback_response_A.clock.getTime()
                                # was this 'correct'?
                                if (feedback_response_A.keys == str(feedback_correct)) or (feedback_response_A.keys == feedback_correct):
                                    feedback_response_A.corr = 1
                                else:
                                    feedback_response_A.corr = 0
                    
                    # *left_box_A* updates
                    if t >= response_option_onset and left_box_A.status == NOT_STARTED:
                        # keep track of start time/frame for later
                        left_box_A.tStart = t
                        left_box_A.frameNStart = frameN  # exact frame index
                        left_box_A.setAutoDraw(True)
                    
                    # *right_box_A* updates
                    if t >= response_option_onset and right_box_A.status == NOT_STARTED:
                        # keep track of start time/frame for later
                        right_box_A.tStart = t
                        right_box_A.frameNStart = frameN  # exact frame index
                        right_box_A.setAutoDraw(True)
                    
                    # *accuracy_feedback_box_A* updates
                    if t >= 0.4 and accuracy_feedback_box_A.status == NOT_STARTED:
                        # keep track of start time/frame for later
                        accuracy_feedback_box_A.tStart = t
                        accuracy_feedback_box_A.frameNStart = frameN  # exact frame index
                        accuracy_feedback_box_A.setAutoDraw(True)
                    if accuracy_feedback_box_A.status == STARTED:  # only update if drawing
                        accuracy_feedback_box_A.setText(accuracyFeedback, log=False)
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in trial_AComponents:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # check for quit (the Esc key)
                    if endExpNow or event.getKeys(keyList=["escape"]):
                        core.quit()
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # -------Ending Routine "trial_A"-------
                for thisComponent in trial_AComponents:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                # save exemplars to experiment handler so they're written to the csv file
                thisExp.addData('stimulus1', stimulus1)
                thisExp.addData('stimulus2', stimulus2)
                thisExp.addData('img_stimulus1', img_stimulus1)
                thisExp.addData('img_stimulus2', img_stimulus2)
                thisExp.addData('response_option_left', response_option_left)
                thisExp.addData('response_option_right', response_option_right)
                # check responses
                if required_response_A.keys in ['', [], None]:  # No response was made
                    required_response_A.keys=None
                    # was no response the correct answer?!
                    if str(required_correct).lower() == 'none':
                       required_response_A.corr = 1  # correct non-response
                    else:
                       required_response_A.corr = 0  # failed to respond (incorrectly)
                # store data for practice_trials_Asecond (TrialHandler)
                practice_trials_Asecond.addData('required_response_A.keys',required_response_A.keys)
                practice_trials_Asecond.addData('required_response_A.corr', required_response_A.corr)
                if required_response_A.keys != None:  # we had a response
                    practice_trials_Asecond.addData('required_response_A.rt', required_response_A.rt)
                # check responses
                if feedback_response_A.keys in ['', [], None]:  # No response was made
                    feedback_response_A.keys=None
                    # was no response the correct answer?!
                    if str(feedback_correct).lower() == 'none':
                       feedback_response_A.corr = 1  # correct non-response
                    else:
                       feedback_response_A.corr = 0  # failed to respond (incorrectly)
                # store data for practice_trials_Asecond (TrialHandler)
                practice_trials_Asecond.addData('feedback_response_A.keys',feedback_response_A.keys)
                practice_trials_Asecond.addData('feedback_response_A.corr', feedback_response_A.corr)
                if feedback_response_A.keys != None:  # we had a response
                    practice_trials_Asecond.addData('feedback_response_A.rt', feedback_response_A.rt)
                # the Routine "trial_A" was not non-slip safe, so reset the non-slip timer
                routineTimer.reset()
                thisExp.nextEntry()
                
            # completed reptitions repeats of 'practice_trials_Asecond'
            
            
            # ------Prepare to start Routine "practice_postblock_A"-------
            t = 0
            practice_postblock_AClock.reset()  # clock
            frameN = -1
            continueRoutine = True
            # update component parameters for each repeat
            # Option to simulates using ResponseEmulator:
            if Monkey:
                simulated_responses = [(1.1, 'e'), (1.1, 'i')]  # simulated responses take the form (onsetTime, responseKey). You can simulate more than one.
                responder = ResponseEmulator(simulated_responses)
                responder.start()
            
            # calculate summary stats
            if(starting_block == 'a'):  
                prac_block_A_percentage_accuracy = (float(practice_trials_Afirst.data['required_response_A.corr'].count()) - float(practice_trials_Afirst.data['feedback_response_A.corr'].sum())) /  float(practice_trials_Afirst.data['required_response_A.corr'].count()) * 100 
                prac_block_A_median_latency = np.median(practice_trials_Afirst.data['required_response_A.rt'])
            
            if(starting_block == 'b'):  
                prac_block_A_percentage_accuracy = (float(practice_trials_Asecond.data['required_response_A.corr'].count()) - float(practice_trials_Asecond.data['feedback_response_A.corr'].sum())) /  float(practice_trials_Asecond.data['required_response_A.corr'].count()) * 100 
                prac_block_A_median_latency = np.median(practice_trials_Asecond.data['required_response_A.rt'])
            
            # set messages
            msg_accuracy = "%s %i %s" %(accuracy, prac_block_A_percentage_accuracy, percentCorrect) 
            msg_latency = "%s %.2f %s" %(speed, prac_block_A_median_latency, seconds)
            
            ### save summary stats to experiment handler so they're written to the csv file
            ##thisExp.addData('prac_block_A_percentage_accuracy', prac_block_A_percentage_accuracy)
            ##thisExp.addData('prac_block_A_median_latency', prac_block_A_median_latency)
            practice_aim_box_A.setText(aim)
            practice_accuracy_box_A.setText(msg_accuracy)
            practice_latency_box_A.setText(msg_latency)
            press_box_prac_A.setText(press_message)
            practice_postblock_response_A = event.BuilderKeyResponse()
            # keep track of which components have finished
            practice_postblock_AComponents = [practice_aim_box_A, practice_accuracy_box_A, practice_latency_box_A, press_box_prac_A, practice_postblock_response_A]
            for thisComponent in practice_postblock_AComponents:
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            
            # -------Start Routine "practice_postblock_A"-------
            while continueRoutine:
                # get current time
                t = practice_postblock_AClock.getTime()
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                
                # *practice_aim_box_A* updates
                if t >= 0.4 and practice_aim_box_A.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    practice_aim_box_A.tStart = t
                    practice_aim_box_A.frameNStart = frameN  # exact frame index
                    practice_aim_box_A.setAutoDraw(True)
                
                # *practice_accuracy_box_A* updates
                if t >= 0.4 and practice_accuracy_box_A.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    practice_accuracy_box_A.tStart = t
                    practice_accuracy_box_A.frameNStart = frameN  # exact frame index
                    practice_accuracy_box_A.setAutoDraw(True)
                
                # *practice_latency_box_A* updates
                if t >= 0.4 and practice_latency_box_A.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    practice_latency_box_A.tStart = t
                    practice_latency_box_A.frameNStart = frameN  # exact frame index
                    practice_latency_box_A.setAutoDraw(True)
                
                # *press_box_prac_A* updates
                if t >= 0.4 and press_box_prac_A.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    press_box_prac_A.tStart = t
                    press_box_prac_A.frameNStart = frameN  # exact frame index
                    press_box_prac_A.setAutoDraw(True)
                
                # *practice_postblock_response_A* updates
                if t >= 1 and practice_postblock_response_A.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    practice_postblock_response_A.tStart = t
                    practice_postblock_response_A.frameNStart = frameN  # exact frame index
                    practice_postblock_response_A.status = STARTED
                    # keyboard checking is just starting
                    event.clearEvents(eventType='keyboard')
                if practice_postblock_response_A.status == STARTED:
                    theseKeys = event.getKeys(keyList=['e', 'i'])
                    
                    # check for quit:
                    if "escape" in theseKeys:
                        endExpNow = True
                    if len(theseKeys) > 0:  # at least one key was pressed
                        # a response ends the routine
                        continueRoutine = False
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in practice_postblock_AComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # check for quit (the Esc key)
                if endExpNow or event.getKeys(keyList=["escape"]):
                    core.quit()
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "practice_postblock_A"-------
            for thisComponent in practice_postblock_AComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            
            # the Routine "practice_postblock_A" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
        # completed Asecond_nReps repeats of 'practice_Asecond'
        
        
        # ------Prepare to start Routine "end_practice_blocks"-------
        t = 0
        end_practice_blocksClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        # Assess if acc and latency mastery criteria were met
        if (prac_block_A_percentage_accuracy >= accuracyCriterion) and (prac_block_B_percentage_accuracy >= accuracyCriterion) and (prac_block_A_median_latency <= latencyCriterion) and (prac_block_B_median_latency <= latencyCriterion):
            complete_test_blocks = n_pairs_test_blocks # latter from blocks.xlsx
            practice_blocks.finished = True
        # keep track of which components have finished
        end_practice_blocksComponents = []
        for thisComponent in end_practice_blocksComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "end_practice_blocks"-------
        while continueRoutine:
            # get current time
            t = end_practice_blocksClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in end_practice_blocksComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "end_practice_blocks"-------
        for thisComponent in end_practice_blocksComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        # the Routine "end_practice_blocks" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
    # completed max_pairs_practice_blocks repeats of 'practice_blocks'
    
    
    # set up handler to look after randomisation of conditions etc
    test_blocks = data.TrialHandler(nReps=complete_test_blocks, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='test_blocks')
    thisExp.addLoop(test_blocks)  # add the loop to the experiment
    thisTest_block = test_blocks.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTest_block.rgb)
    if thisTest_block != None:
        for paramName in thisTest_block.keys():
            exec(paramName + '= thisTest_block.' + paramName)
    
    for thisTest_block in test_blocks:
        currentLoop = test_blocks
        # abbreviate parameter names if possible (e.g. rgb = thisTest_block.rgb)
        if thisTest_block != None:
            for paramName in thisTest_block.keys():
                exec(paramName + '= thisTest_block.' + paramName)
        
        # set up handler to look after randomisation of conditions etc
        Afirst = data.TrialHandler(nReps=Afirst_nReps, method='sequential', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
            seed=None, name='Afirst')
        thisExp.addLoop(Afirst)  # add the loop to the experiment
        thisAfirst = Afirst.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisAfirst.rgb)
        if thisAfirst != None:
            for paramName in thisAfirst.keys():
                exec(paramName + '= thisAfirst.' + paramName)
        
        for thisAfirst in Afirst:
            currentLoop = Afirst
            # abbreviate parameter names if possible (e.g. rgb = thisAfirst.rgb)
            if thisAfirst != None:
                for paramName in thisAfirst.keys():
                    exec(paramName + '= thisAfirst.' + paramName)
            
            # ------Prepare to start Routine "preblock_A"-------
            t = 0
            preblock_AClock.reset()  # clock
            frameN = -1
            continueRoutine = True
            # update component parameters for each repeat
            # Option to simulates using ResponseEmulator:
            if Monkey:
                simulated_responses = [(1.1, 'e'), (1.1, 'i')]  # simulated responses take the form (onsetTime, responseKey). You can simulate more than one.
                responder = ResponseEmulator(simulated_responses)
                responder.start()
            
            # Generate list of stimuli for the block
            stim1_catA_stimuli_many = generate_trials('labelA_stimuli', 2, True)  # function and variable determined at begin exp.
            stim1_catB_stimuli_many = generate_trials('labelB_stimuli', 2, True)
            stim2_catA_stimuli_many = generate_trials('targetA_stimuli', 2, True)
            stim2_catB_stimuli_many = generate_trials('targetB_stimuli', 2, True)
            img_stim1_catA_stimuli_many = generate_trials('labelA_image_stimuli', 2, True)
            img_stim1_catB_stimuli_many = generate_trials('labelB_image_stimuli', 2, True)
            img_stim2_catA_stimuli_many = generate_trials('targetA_image_stimuli', 2, True)
            img_stim2_catB_stimuli_many = generate_trials('targetB_image_stimuli', 2, True)
            
            rule_box_A.setText(rule_A)
            preblock_response_A = event.BuilderKeyResponse()
            # keep track of which components have finished
            preblock_AComponents = [rule_box_A, preblock_response_A]
            for thisComponent in preblock_AComponents:
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            
            # -------Start Routine "preblock_A"-------
            while continueRoutine:
                # get current time
                t = preblock_AClock.getTime()
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                
                # *rule_box_A* updates
                if t >= 0.4 and rule_box_A.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    rule_box_A.tStart = t
                    rule_box_A.frameNStart = frameN  # exact frame index
                    rule_box_A.setAutoDraw(True)
                
                # *preblock_response_A* updates
                if t >= 1 and preblock_response_A.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    preblock_response_A.tStart = t
                    preblock_response_A.frameNStart = frameN  # exact frame index
                    preblock_response_A.status = STARTED
                    # keyboard checking is just starting
                    event.clearEvents(eventType='keyboard')
                if preblock_response_A.status == STARTED:
                    theseKeys = event.getKeys(keyList=['e', 'i'])
                    
                    # check for quit:
                    if "escape" in theseKeys:
                        endExpNow = True
                    if len(theseKeys) > 0:  # at least one key was pressed
                        # a response ends the routine
                        continueRoutine = False
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in preblock_AComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # check for quit (the Esc key)
                if endExpNow or event.getKeys(keyList=["escape"]):
                    core.quit()
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "preblock_A"-------
            for thisComponent in preblock_AComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            
            # the Routine "preblock_A" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # set up handler to look after randomisation of conditions etc
            trials_Afirst = data.TrialHandler(nReps=reptitions, method='random', 
                extraInfo=expInfo, originPath=-1,
                trialList=data.importConditions('block_layout.xlsx'),
                seed=None, name='trials_Afirst')
            thisExp.addLoop(trials_Afirst)  # add the loop to the experiment
            thisTrials_Afirst = trials_Afirst.trialList[0]  # so we can initialise stimuli with some values
            # abbreviate parameter names if possible (e.g. rgb = thisTrials_Afirst.rgb)
            if thisTrials_Afirst != None:
                for paramName in thisTrials_Afirst.keys():
                    exec(paramName + '= thisTrials_Afirst.' + paramName)
            
            for thisTrials_Afirst in trials_Afirst:
                currentLoop = trials_Afirst
                # abbreviate parameter names if possible (e.g. rgb = thisTrials_Afirst.rgb)
                if thisTrials_Afirst != None:
                    for paramName in thisTrials_Afirst.keys():
                        exec(paramName + '= thisTrials_Afirst.' + paramName)
                
                # ------Prepare to start Routine "trial_A"-------
                t = 0
                trial_AClock.reset()  # clock
                frameN = -1
                continueRoutine = True
                # update component parameters for each repeat
                # Option to simulates using ResponseEmulator:
                if Monkey:
                    simulated_responses = [(0.5, 'e'), (0.5, 'i')]  # simulated responses take the form (onsetTime, responseKey). You can simulate more than one.
                    responder = ResponseEmulator(simulated_responses)
                    responder.start()
                
                # For each stimlulus, choose a random exemplar from the appropriate list
                # word stimulus 1
                if stimulus1_category == 'a':
                    stimulus1 = stim1_catA_stimuli_many.pop()
                elif stimulus1_category == 'b':
                    stimulus1 = stim1_catB_stimuli_many.pop()
                
                # word stimulus 2
                if stimulus2_category == 'c':
                    stimulus2 = stim2_catA_stimuli_many.pop()
                elif stimulus2_category == 'd':
                    stimulus2 = stim2_catB_stimuli_many.pop()
                
                # image stimulus 1
                if stimulus1_category == 'a':
                    img_stimulus1 = img_stim1_catA_stimuli_many.pop()
                elif stimulus1_category == 'b':
                    img_stimulus1 = img_stim1_catB_stimuli_many.pop()
                
                # image stimulus 2
                if stimulus2_category == 'c':
                    img_stimulus2 = img_stim2_catA_stimuli_many.pop()
                elif stimulus2_category == 'd':
                    img_stimulus2 = img_stim2_catB_stimuli_many.pop()
                
                # set correct and incorrect responses
                if moving_response_options == False:
                    response_option_left = response_option_B  # i.e., the focal trial type is the right hand one, for hand dominance
                    response_option_right = response_option_A
                    response_option_onset = 0  # response options are onscreen constantly
                    if (trialType == 1) or (trialType == 4):
                        required_allowed = 'i'
                        required_correct = 'i'
                        feedback_allowed = 'e'
                        feedback_correct = 'e'
                    elif (trialType == 2) or (trialType == 3):
                        required_allowed = 'e'
                        required_correct = 'e'
                        feedback_allowed = 'i'
                        feedback_correct = 'i'
                elif moving_response_options == True:
                    rand_positions = randint(1, 3)
                    response_option_onset = 0.4  # response options appear with stimuli
                    if rand_positions == 1:
                        response_option_left = response_option_B
                        response_option_right = response_option_A
                        if (trialType == 1) or (trialType == 4):
                            required_allowed = 'i'
                            required_correct = 'i'
                            feedback_allowed = 'e'
                            feedback_correct = 'e'
                        elif (trialType == 2) or (trialType == 3):
                            required_allowed = 'e'
                            required_correct = 'e'
                            feedback_allowed = 'i'
                            feedback_correct = 'i'
                    elif rand_positions == 2:
                        response_option_left = response_option_A
                        response_option_right = response_option_B
                        if (trialType == 1) or (trialType == 4):
                            required_allowed = 'e'
                            required_correct = 'e'
                            feedback_allowed = 'i'
                            feedback_correct = 'i'
                        elif (trialType == 2) or (trialType == 3):
                            required_allowed = 'i'
                            required_correct = 'i'
                            feedback_allowed = 'e'
                            feedback_correct = 'e'
                image_stimulus1_box_A.setPos(image_stimulus1_location)
                image_stimulus1_box_A.setImage(img_stimulus1)
                image_stimulus2_box_A.setPos(image_stimulus2_location)
                image_stimulus2_box_A.setImage(img_stimulus2)
                stimulus1_box_A.setText(stimulus1)
                stimulus1_box_A.setPos(stimulus1_location)
                stimulus2_box_A.setText(stimulus2)
                stimulus2_box_A.setPos(stimulus2_location)
                required_response_A = event.BuilderKeyResponse()
                feedback_response_A = event.BuilderKeyResponse()
                left_box_A.setText(response_option_left)
                left_box_A.setPos(response_option_left_location)
                right_box_A.setText(response_option_right)
                right_box_A.setPos(response_option_right_location)
                accuracy_feedback_box_A.setPos(accuracy_feedback_location)
                # keep track of which components have finished
                trial_AComponents = [image_stimulus1_box_A, image_stimulus2_box_A, stimulus1_box_A, stimulus2_box_A, required_response_A, feedback_response_A, left_box_A, right_box_A, accuracy_feedback_box_A]
                for thisComponent in trial_AComponents:
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                
                # -------Start Routine "trial_A"-------
                while continueRoutine:
                    # get current time
                    t = trial_AClock.getTime()
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    # Accuracy feedback message
                    if len(feedback_response_A.keys)<1:
                        accuracyFeedback=""
                    else:
                        accuracyFeedback="X"
                    
                    # *image_stimulus1_box_A* updates
                    if t >= 0.4 and image_stimulus1_box_A.status == NOT_STARTED:
                        # keep track of start time/frame for later
                        image_stimulus1_box_A.tStart = t
                        image_stimulus1_box_A.frameNStart = frameN  # exact frame index
                        image_stimulus1_box_A.setAutoDraw(True)
                    
                    # *image_stimulus2_box_A* updates
                    if t >= 0.4 and image_stimulus2_box_A.status == NOT_STARTED:
                        # keep track of start time/frame for later
                        image_stimulus2_box_A.tStart = t
                        image_stimulus2_box_A.frameNStart = frameN  # exact frame index
                        image_stimulus2_box_A.setAutoDraw(True)
                    
                    # *stimulus1_box_A* updates
                    if t >= 0.4 and stimulus1_box_A.status == NOT_STARTED:
                        # keep track of start time/frame for later
                        stimulus1_box_A.tStart = t
                        stimulus1_box_A.frameNStart = frameN  # exact frame index
                        stimulus1_box_A.setAutoDraw(True)
                    
                    # *stimulus2_box_A* updates
                    if t >= 0.4 and stimulus2_box_A.status == NOT_STARTED:
                        # keep track of start time/frame for later
                        stimulus2_box_A.tStart = t
                        stimulus2_box_A.frameNStart = frameN  # exact frame index
                        stimulus2_box_A.setAutoDraw(True)
                    
                    # *required_response_A* updates
                    if t >= 0.4 and required_response_A.status == NOT_STARTED:
                        # keep track of start time/frame for later
                        required_response_A.tStart = t
                        required_response_A.frameNStart = frameN  # exact frame index
                        required_response_A.status = STARTED
                        # AllowedKeys looks like a variable named `required_allowed`
                        if not type(required_allowed) in [list, tuple, np.ndarray]:
                            if not isinstance(required_allowed, basestring):
                                logging.error('AllowedKeys variable `required_allowed` is not string- or list-like.')
                                core.quit()
                            elif not ',' in required_allowed: required_allowed = (required_allowed,)
                            else:  required_allowed = eval(required_allowed)
                        # keyboard checking is just starting
                        win.callOnFlip(required_response_A.clock.reset)  # t=0 on next screen flip
                        event.clearEvents(eventType='keyboard')
                    if required_response_A.status == STARTED:
                        theseKeys = event.getKeys(keyList=list(required_allowed))
                        
                        # check for quit:
                        if "escape" in theseKeys:
                            endExpNow = True
                        if len(theseKeys) > 0:  # at least one key was pressed
                            if required_response_A.keys == []:  # then this was the first keypress
                                required_response_A.keys = theseKeys[0]  # just the first key pressed
                                required_response_A.rt = required_response_A.clock.getTime()
                                # was this 'correct'?
                                if (required_response_A.keys == str(required_correct)) or (required_response_A.keys == required_correct):
                                    required_response_A.corr = 1
                                else:
                                    required_response_A.corr = 0
                                # a response ends the routine
                                continueRoutine = False
                    
                    # *feedback_response_A* updates
                    if t >= 0.4 and feedback_response_A.status == NOT_STARTED:
                        # keep track of start time/frame for later
                        feedback_response_A.tStart = t
                        feedback_response_A.frameNStart = frameN  # exact frame index
                        feedback_response_A.status = STARTED
                        # AllowedKeys looks like a variable named `feedback_allowed`
                        if not type(feedback_allowed) in [list, tuple, np.ndarray]:
                            if not isinstance(feedback_allowed, basestring):
                                logging.error('AllowedKeys variable `feedback_allowed` is not string- or list-like.')
                                core.quit()
                            elif not ',' in feedback_allowed: feedback_allowed = (feedback_allowed,)
                            else:  feedback_allowed = eval(feedback_allowed)
                        # keyboard checking is just starting
                        win.callOnFlip(feedback_response_A.clock.reset)  # t=0 on next screen flip
                        event.clearEvents(eventType='keyboard')
                    if feedback_response_A.status == STARTED:
                        theseKeys = event.getKeys(keyList=list(feedback_allowed))
                        
                        # check for quit:
                        if "escape" in theseKeys:
                            endExpNow = True
                        if len(theseKeys) > 0:  # at least one key was pressed
                            if feedback_response_A.keys == []:  # then this was the first keypress
                                feedback_response_A.keys = theseKeys[0]  # just the first key pressed
                                feedback_response_A.rt = feedback_response_A.clock.getTime()
                                # was this 'correct'?
                                if (feedback_response_A.keys == str(feedback_correct)) or (feedback_response_A.keys == feedback_correct):
                                    feedback_response_A.corr = 1
                                else:
                                    feedback_response_A.corr = 0
                    
                    # *left_box_A* updates
                    if t >= response_option_onset and left_box_A.status == NOT_STARTED:
                        # keep track of start time/frame for later
                        left_box_A.tStart = t
                        left_box_A.frameNStart = frameN  # exact frame index
                        left_box_A.setAutoDraw(True)
                    
                    # *right_box_A* updates
                    if t >= response_option_onset and right_box_A.status == NOT_STARTED:
                        # keep track of start time/frame for later
                        right_box_A.tStart = t
                        right_box_A.frameNStart = frameN  # exact frame index
                        right_box_A.setAutoDraw(True)
                    
                    # *accuracy_feedback_box_A* updates
                    if t >= 0.4 and accuracy_feedback_box_A.status == NOT_STARTED:
                        # keep track of start time/frame for later
                        accuracy_feedback_box_A.tStart = t
                        accuracy_feedback_box_A.frameNStart = frameN  # exact frame index
                        accuracy_feedback_box_A.setAutoDraw(True)
                    if accuracy_feedback_box_A.status == STARTED:  # only update if drawing
                        accuracy_feedback_box_A.setText(accuracyFeedback, log=False)
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in trial_AComponents:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # check for quit (the Esc key)
                    if endExpNow or event.getKeys(keyList=["escape"]):
                        core.quit()
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # -------Ending Routine "trial_A"-------
                for thisComponent in trial_AComponents:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                # save exemplars to experiment handler so they're written to the csv file
                thisExp.addData('stimulus1', stimulus1)
                thisExp.addData('stimulus2', stimulus2)
                thisExp.addData('img_stimulus1', img_stimulus1)
                thisExp.addData('img_stimulus2', img_stimulus2)
                thisExp.addData('response_option_left', response_option_left)
                thisExp.addData('response_option_right', response_option_right)
                # check responses
                if required_response_A.keys in ['', [], None]:  # No response was made
                    required_response_A.keys=None
                    # was no response the correct answer?!
                    if str(required_correct).lower() == 'none':
                       required_response_A.corr = 1  # correct non-response
                    else:
                       required_response_A.corr = 0  # failed to respond (incorrectly)
                # store data for trials_Afirst (TrialHandler)
                trials_Afirst.addData('required_response_A.keys',required_response_A.keys)
                trials_Afirst.addData('required_response_A.corr', required_response_A.corr)
                if required_response_A.keys != None:  # we had a response
                    trials_Afirst.addData('required_response_A.rt', required_response_A.rt)
                # check responses
                if feedback_response_A.keys in ['', [], None]:  # No response was made
                    feedback_response_A.keys=None
                    # was no response the correct answer?!
                    if str(feedback_correct).lower() == 'none':
                       feedback_response_A.corr = 1  # correct non-response
                    else:
                       feedback_response_A.corr = 0  # failed to respond (incorrectly)
                # store data for trials_Afirst (TrialHandler)
                trials_Afirst.addData('feedback_response_A.keys',feedback_response_A.keys)
                trials_Afirst.addData('feedback_response_A.corr', feedback_response_A.corr)
                if feedback_response_A.keys != None:  # we had a response
                    trials_Afirst.addData('feedback_response_A.rt', feedback_response_A.rt)
                # the Routine "trial_A" was not non-slip safe, so reset the non-slip timer
                routineTimer.reset()
                thisExp.nextEntry()
                
            # completed reptitions repeats of 'trials_Afirst'
            
            
            # ------Prepare to start Routine "postblock_A"-------
            t = 0
            postblock_AClock.reset()  # clock
            frameN = -1
            continueRoutine = True
            # update component parameters for each repeat
            # Option to simulates using ResponseEmulator:
            if Monkey:
                simulated_responses = [(1.1, 'e'), (1.1, 'i')]  # simulated responses take the form (onsetTime, responseKey). You can simulate more than one.
                responder = ResponseEmulator(simulated_responses)
                responder.start()
            
            # calculate summary stats
            if(starting_block == 'a'): 
                block_A_percentage_accuracy = (float(trials_Afirst.data['required_response_A.corr'].count()) - float(trials_Afirst.data['feedback_response_A.corr'].sum())) /  float(trials_Afirst.data['required_response_A.corr'].count()) * 100 
                block_A_median_latency = np.median(trials_Afirst.data['required_response_A.rt'])
            
            if(starting_block == 'b'): 
                block_A_percentage_accuracy = (float(trials_Asecond.data['required_response_A.corr'].count()) - float(trials_Asecond.data['feedback_response_A.corr'].sum())) /  float(trials_Asecond.data['required_response_A.corr'].count()) * 100 
                block_A_median_latency = np.median(trials_Asecond.data['required_response_A.rt'])
            
            # set messages
            msg_accuracy = "%s %i %s" %(accuracy, block_A_percentage_accuracy, percentCorrect) 
            msg_latency = "%s %.2f %s" %(speed, block_A_median_latency, seconds)
            
            ### save summary stats to experiment handler so they're written to the csv file
            ##thisExp.addData('block_A_percentage_accuracy', block_A_percentage_accuracy)
            ##thisExp.addData('block_A_median_latency', block_A_median_latency)
            aim_box_A.setText(aim)
            accuracy_box_A.setText(msg_accuracy)
            latency_box_A.setText(msg_latency)
            press_box_A.setText(press_message)
            postblock_response_A = event.BuilderKeyResponse()
            # keep track of which components have finished
            postblock_AComponents = [aim_box_A, accuracy_box_A, latency_box_A, press_box_A, postblock_response_A]
            for thisComponent in postblock_AComponents:
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            
            # -------Start Routine "postblock_A"-------
            while continueRoutine:
                # get current time
                t = postblock_AClock.getTime()
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                
                # *aim_box_A* updates
                if t >= 0.4 and aim_box_A.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    aim_box_A.tStart = t
                    aim_box_A.frameNStart = frameN  # exact frame index
                    aim_box_A.setAutoDraw(True)
                
                # *accuracy_box_A* updates
                if t >= 0.4 and accuracy_box_A.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    accuracy_box_A.tStart = t
                    accuracy_box_A.frameNStart = frameN  # exact frame index
                    accuracy_box_A.setAutoDraw(True)
                
                # *latency_box_A* updates
                if t >= 0.4 and latency_box_A.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    latency_box_A.tStart = t
                    latency_box_A.frameNStart = frameN  # exact frame index
                    latency_box_A.setAutoDraw(True)
                
                # *press_box_A* updates
                if t >= 0.4 and press_box_A.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    press_box_A.tStart = t
                    press_box_A.frameNStart = frameN  # exact frame index
                    press_box_A.setAutoDraw(True)
                
                # *postblock_response_A* updates
                if t >= 1 and postblock_response_A.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    postblock_response_A.tStart = t
                    postblock_response_A.frameNStart = frameN  # exact frame index
                    postblock_response_A.status = STARTED
                    # keyboard checking is just starting
                    event.clearEvents(eventType='keyboard')
                if postblock_response_A.status == STARTED:
                    theseKeys = event.getKeys(keyList=['e', 'i'])
                    
                    # check for quit:
                    if "escape" in theseKeys:
                        endExpNow = True
                    if len(theseKeys) > 0:  # at least one key was pressed
                        # a response ends the routine
                        continueRoutine = False
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in postblock_AComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # check for quit (the Esc key)
                if endExpNow or event.getKeys(keyList=["escape"]):
                    core.quit()
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "postblock_A"-------
            for thisComponent in postblock_AComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            
            # the Routine "postblock_A" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
        # completed Afirst_nReps repeats of 'Afirst'
        
        
        # ------Prepare to start Routine "preblock_B"-------
        t = 0
        preblock_BClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        # Option to simulates using ResponseEmulator:
        if Monkey:
            simulated_responses = [(1.1, 'e'), (1.1, 'i')]  # simulated responses take the form (onsetTime, responseKey). You can simulate more than one.
            responder = ResponseEmulator(simulated_responses)
            responder.start()
        
        # Generate list of stimuli for the block
        stim1_catA_stimuli_many = generate_trials('labelA_stimuli', 2, True)  # function and variable determined at begin exp.
        stim1_catB_stimuli_many = generate_trials('labelB_stimuli', 2, True)
        stim2_catA_stimuli_many = generate_trials('targetA_stimuli', 2, True)
        stim2_catB_stimuli_many = generate_trials('targetB_stimuli', 2, True)
        img_stim1_catA_stimuli_many = generate_trials('labelA_image_stimuli', 2, True)
        img_stim1_catB_stimuli_many = generate_trials('labelB_image_stimuli', 2, True)
        img_stim2_catA_stimuli_many = generate_trials('targetA_image_stimuli', 2, True)
        img_stim2_catB_stimuli_many = generate_trials('targetB_image_stimuli', 2, True)
        rule_box_B.setText(rule_B)
        preblock_response_B = event.BuilderKeyResponse()
        # keep track of which components have finished
        preblock_BComponents = [rule_box_B, preblock_response_B]
        for thisComponent in preblock_BComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "preblock_B"-------
        while continueRoutine:
            # get current time
            t = preblock_BClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            
            # *rule_box_B* updates
            if t >= 0.4 and rule_box_B.status == NOT_STARTED:
                # keep track of start time/frame for later
                rule_box_B.tStart = t
                rule_box_B.frameNStart = frameN  # exact frame index
                rule_box_B.setAutoDraw(True)
            
            # *preblock_response_B* updates
            if t >= 1 and preblock_response_B.status == NOT_STARTED:
                # keep track of start time/frame for later
                preblock_response_B.tStart = t
                preblock_response_B.frameNStart = frameN  # exact frame index
                preblock_response_B.status = STARTED
                # keyboard checking is just starting
                event.clearEvents(eventType='keyboard')
            if preblock_response_B.status == STARTED:
                theseKeys = event.getKeys(keyList=['e', 'i'])
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    # a response ends the routine
                    continueRoutine = False
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in preblock_BComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "preblock_B"-------
        for thisComponent in preblock_BComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        # the Routine "preblock_B" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        trials_B = data.TrialHandler(nReps=reptitions, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions('block_layout.xlsx'),
            seed=None, name='trials_B')
        thisExp.addLoop(trials_B)  # add the loop to the experiment
        thisTrials_B = trials_B.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisTrials_B.rgb)
        if thisTrials_B != None:
            for paramName in thisTrials_B.keys():
                exec(paramName + '= thisTrials_B.' + paramName)
        
        for thisTrials_B in trials_B:
            currentLoop = trials_B
            # abbreviate parameter names if possible (e.g. rgb = thisTrials_B.rgb)
            if thisTrials_B != None:
                for paramName in thisTrials_B.keys():
                    exec(paramName + '= thisTrials_B.' + paramName)
            
            # ------Prepare to start Routine "trial_B"-------
            t = 0
            trial_BClock.reset()  # clock
            frameN = -1
            continueRoutine = True
            # update component parameters for each repeat
            # Option to simulates using ResponseEmulator:
            if Monkey:
                simulated_responses = [(0.5, 'e'), (0.5, 'i')]  # simulated responses take the form (onsetTime, responseKey). You can simulate more than one.
                responder = ResponseEmulator(simulated_responses)
                responder.start()
            
            # For each stimlulus, choose a random exemplar from the appropriate list
            # word stimulus 1
            if stimulus1_category == 'a':
                stimulus1 = stim1_catA_stimuli_many.pop()
            elif stimulus1_category == 'b':
                stimulus1 = stim1_catB_stimuli_many.pop()
            
            # word stimulus 2
            if stimulus2_category == 'c':
                stimulus2 = stim2_catA_stimuli_many.pop()
            elif stimulus2_category == 'd':
                stimulus2 = stim2_catB_stimuli_many.pop()
            
            # image stimulus 1
            if stimulus1_category == 'a':
                img_stimulus1 = img_stim1_catA_stimuli_many.pop()
            elif stimulus1_category == 'b':
                img_stimulus1 = img_stim1_catB_stimuli_many.pop()
            
            # image stimulus 2
            if stimulus2_category == 'c':
                img_stimulus2 = img_stim2_catA_stimuli_many.pop()
            elif stimulus2_category == 'd':
                img_stimulus2 = img_stim2_catB_stimuli_many.pop()
            
            # set correct and incorrect responses
            if moving_response_options == False:
                response_option_left = response_option_B  # i.e., the focal trial type is the right hand one, for hand dominance
                response_option_right = response_option_A
                response_option_onset = 0  # response options are onscreen constantly
                if (trialType == 1) or (trialType == 4):
                    required_allowed = 'e'  # PATTERN REVERED FROM BLOCK A
                    required_correct = 'e'
                    feedback_allowed = 'i'
                    feedback_correct = 'i'
                elif (trialType == 2) or (trialType == 3):
                    required_allowed = 'i'  # PATTERN REVERED FROM BLOCK A
                    required_correct = 'i'
                    feedback_allowed = 'e'
                    feedback_correct = 'e'
            elif moving_response_options == True:
                rand_positions = randint(1, 3)
                response_option_onset = 0.4  # response options appear with stimuli
                if rand_positions == 1:
                    response_option_left = response_option_B
                    response_option_right = response_option_A
                    if (trialType == 1) or (trialType == 4):
                        required_allowed = 'e'  # PATTERN REVERED FROM BLOCK A
                        required_correct = 'e'
                        feedback_allowed = 'i'
                        feedback_correct = 'i'
                    elif (trialType == 2) or (trialType == 3):
                        required_allowed = 'i'  # PATTERN REVERED FROM BLOCK A
                        required_correct = 'i'
                        feedback_allowed = 'e'
                        feedback_correct = 'e'
                elif rand_positions == 2:
                    response_option_left = response_option_A
                    response_option_right = response_option_B
                    if (trialType == 1) or (trialType == 4):
                        required_allowed = 'i'  # PATTERN REVERED FROM BLOCK A
                        required_correct = 'i'
                        feedback_allowed = 'e'
                        feedback_correct = 'e'
                    elif (trialType == 2) or (trialType == 3):
                        required_allowed = 'e'  # PATTERN REVERED FROM BLOCK A
                        required_correct = 'e'
                        feedback_allowed = 'i'
                        feedback_correct = 'i'
            image_stimulus1_box_B.setPos(image_stimulus1_location)
            image_stimulus1_box_B.setImage(img_stimulus1)
            image_stimulus2_box_B.setPos(image_stimulus2_location)
            image_stimulus2_box_B.setImage(img_stimulus2)
            stimulus1_box_B.setText(stimulus1)
            stimulus1_box_B.setPos(stimulus1_location)
            stimulus2_box_B.setText(stimulus2)
            stimulus2_box_B.setPos(stimulus2_location)
            required_response_B = event.BuilderKeyResponse()
            feedback_response_B = event.BuilderKeyResponse()
            left_box_B.setText(response_option_left)
            left_box_B.setPos(response_option_left_location)
            right_box_B.setText(response_option_right)
            right_box_B.setPos(response_option_right_location)
            accuracy_feedback_box_B.setPos(accuracy_feedback_location)
            # keep track of which components have finished
            trial_BComponents = [image_stimulus1_box_B, image_stimulus2_box_B, stimulus1_box_B, stimulus2_box_B, required_response_B, feedback_response_B, left_box_B, right_box_B, accuracy_feedback_box_B]
            for thisComponent in trial_BComponents:
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            
            # -------Start Routine "trial_B"-------
            while continueRoutine:
                # get current time
                t = trial_BClock.getTime()
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                # Accuracy feedback message
                if len(feedback_response_B.keys)<1:
                    accuracyFeedback=""
                else:
                    accuracyFeedback="X"
                
                # *image_stimulus1_box_B* updates
                if t >= 0.4 and image_stimulus1_box_B.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    image_stimulus1_box_B.tStart = t
                    image_stimulus1_box_B.frameNStart = frameN  # exact frame index
                    image_stimulus1_box_B.setAutoDraw(True)
                
                # *image_stimulus2_box_B* updates
                if t >= 0.4 and image_stimulus2_box_B.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    image_stimulus2_box_B.tStart = t
                    image_stimulus2_box_B.frameNStart = frameN  # exact frame index
                    image_stimulus2_box_B.setAutoDraw(True)
                
                # *stimulus1_box_B* updates
                if t >= 0.4 and stimulus1_box_B.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    stimulus1_box_B.tStart = t
                    stimulus1_box_B.frameNStart = frameN  # exact frame index
                    stimulus1_box_B.setAutoDraw(True)
                
                # *stimulus2_box_B* updates
                if t >= 0.4 and stimulus2_box_B.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    stimulus2_box_B.tStart = t
                    stimulus2_box_B.frameNStart = frameN  # exact frame index
                    stimulus2_box_B.setAutoDraw(True)
                
                # *required_response_B* updates
                if t >= 0.4 and required_response_B.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    required_response_B.tStart = t
                    required_response_B.frameNStart = frameN  # exact frame index
                    required_response_B.status = STARTED
                    # AllowedKeys looks like a variable named `required_allowed`
                    if not type(required_allowed) in [list, tuple, np.ndarray]:
                        if not isinstance(required_allowed, basestring):
                            logging.error('AllowedKeys variable `required_allowed` is not string- or list-like.')
                            core.quit()
                        elif not ',' in required_allowed: required_allowed = (required_allowed,)
                        else:  required_allowed = eval(required_allowed)
                    # keyboard checking is just starting
                    win.callOnFlip(required_response_B.clock.reset)  # t=0 on next screen flip
                    event.clearEvents(eventType='keyboard')
                if required_response_B.status == STARTED:
                    theseKeys = event.getKeys(keyList=list(required_allowed))
                    
                    # check for quit:
                    if "escape" in theseKeys:
                        endExpNow = True
                    if len(theseKeys) > 0:  # at least one key was pressed
                        if required_response_B.keys == []:  # then this was the first keypress
                            required_response_B.keys = theseKeys[0]  # just the first key pressed
                            required_response_B.rt = required_response_B.clock.getTime()
                            # was this 'correct'?
                            if (required_response_B.keys == str(required_correct)) or (required_response_B.keys == required_correct):
                                required_response_B.corr = 1
                            else:
                                required_response_B.corr = 0
                            # a response ends the routine
                            continueRoutine = False
                
                # *feedback_response_B* updates
                if t >= 0.4 and feedback_response_B.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    feedback_response_B.tStart = t
                    feedback_response_B.frameNStart = frameN  # exact frame index
                    feedback_response_B.status = STARTED
                    # AllowedKeys looks like a variable named `feedback_allowed`
                    if not type(feedback_allowed) in [list, tuple, np.ndarray]:
                        if not isinstance(feedback_allowed, basestring):
                            logging.error('AllowedKeys variable `feedback_allowed` is not string- or list-like.')
                            core.quit()
                        elif not ',' in feedback_allowed: feedback_allowed = (feedback_allowed,)
                        else:  feedback_allowed = eval(feedback_allowed)
                    # keyboard checking is just starting
                    win.callOnFlip(feedback_response_B.clock.reset)  # t=0 on next screen flip
                    event.clearEvents(eventType='keyboard')
                if feedback_response_B.status == STARTED:
                    theseKeys = event.getKeys(keyList=list(feedback_allowed))
                    
                    # check for quit:
                    if "escape" in theseKeys:
                        endExpNow = True
                    if len(theseKeys) > 0:  # at least one key was pressed
                        if feedback_response_B.keys == []:  # then this was the first keypress
                            feedback_response_B.keys = theseKeys[0]  # just the first key pressed
                            feedback_response_B.rt = feedback_response_B.clock.getTime()
                            # was this 'correct'?
                            if (feedback_response_B.keys == str(feedback_correct)) or (feedback_response_B.keys == feedback_correct):
                                feedback_response_B.corr = 1
                            else:
                                feedback_response_B.corr = 0
                
                # *left_box_B* updates
                if t >= response_option_onset and left_box_B.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    left_box_B.tStart = t
                    left_box_B.frameNStart = frameN  # exact frame index
                    left_box_B.setAutoDraw(True)
                
                # *right_box_B* updates
                if t >= response_option_onset and right_box_B.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    right_box_B.tStart = t
                    right_box_B.frameNStart = frameN  # exact frame index
                    right_box_B.setAutoDraw(True)
                
                # *accuracy_feedback_box_B* updates
                if t >= 0.4 and accuracy_feedback_box_B.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    accuracy_feedback_box_B.tStart = t
                    accuracy_feedback_box_B.frameNStart = frameN  # exact frame index
                    accuracy_feedback_box_B.setAutoDraw(True)
                if accuracy_feedback_box_B.status == STARTED:  # only update if drawing
                    accuracy_feedback_box_B.setText(accuracyFeedback, log=False)
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in trial_BComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # check for quit (the Esc key)
                if endExpNow or event.getKeys(keyList=["escape"]):
                    core.quit()
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "trial_B"-------
            for thisComponent in trial_BComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # save exemplars to experiment handler so they're written to the csv file
            thisExp.addData('stimulus1', stimulus1)
            thisExp.addData('stimulus2', stimulus2)
            thisExp.addData('img_stimulus1', img_stimulus1)
            thisExp.addData('img_stimulus2', img_stimulus2)
            thisExp.addData('response_option_left', response_option_left)
            thisExp.addData('response_option_right', response_option_right)
            # check responses
            if required_response_B.keys in ['', [], None]:  # No response was made
                required_response_B.keys=None
                # was no response the correct answer?!
                if str(required_correct).lower() == 'none':
                   required_response_B.corr = 1  # correct non-response
                else:
                   required_response_B.corr = 0  # failed to respond (incorrectly)
            # store data for trials_B (TrialHandler)
            trials_B.addData('required_response_B.keys',required_response_B.keys)
            trials_B.addData('required_response_B.corr', required_response_B.corr)
            if required_response_B.keys != None:  # we had a response
                trials_B.addData('required_response_B.rt', required_response_B.rt)
            # check responses
            if feedback_response_B.keys in ['', [], None]:  # No response was made
                feedback_response_B.keys=None
                # was no response the correct answer?!
                if str(feedback_correct).lower() == 'none':
                   feedback_response_B.corr = 1  # correct non-response
                else:
                   feedback_response_B.corr = 0  # failed to respond (incorrectly)
            # store data for trials_B (TrialHandler)
            trials_B.addData('feedback_response_B.keys',feedback_response_B.keys)
            trials_B.addData('feedback_response_B.corr', feedback_response_B.corr)
            if feedback_response_B.keys != None:  # we had a response
                trials_B.addData('feedback_response_B.rt', feedback_response_B.rt)
            # the Routine "trial_B" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed reptitions repeats of 'trials_B'
        
        
        # ------Prepare to start Routine "postblock_B"-------
        t = 0
        postblock_BClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        # Option to simulates using ResponseEmulator:
        if Monkey:
            simulated_responses = [(1.1, 'e'), (1.1, 'i')]  # simulated responses take the form (onsetTime, responseKey). You can simulate more than one.
            responder = ResponseEmulator(simulated_responses)
            responder.start()
        
        # calculate summary stats
        block_B_percentage_accuracy = (float(trials_B.data['required_response_B.corr'].count()) - float(trials_B.data['feedback_response_B.corr'].sum())) /  float(trials_B.data['required_response_B.corr'].count()) * 100 
        block_B_median_latency = np.median(trials_B.data['required_response_B.rt'])
        
        # set messages
        msg_accuracy = "%s %i %s" %(accuracy, block_B_percentage_accuracy, percentCorrect) 
        msg_latency = "%s %.2f %s" %(speed, block_B_median_latency, seconds)
        
        ### save summary stats to experiment handler so they're written to the csv file
        ##thisExp.addData('block_B_percentage_accuracy', block_B_percentage_accuracy)
        ##thisExp.addData('block_B_median_latency', block_B_median_latency)
        aim_box_B.setText(aim)
        accuracy_box_B.setText(msg_accuracy)
        latency_box_B.setText(msg_latency)
        press_box_B.setText(press_message)
        postblock_response_B = event.BuilderKeyResponse()
        # keep track of which components have finished
        postblock_BComponents = [aim_box_B, accuracy_box_B, latency_box_B, press_box_B, postblock_response_B]
        for thisComponent in postblock_BComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "postblock_B"-------
        while continueRoutine:
            # get current time
            t = postblock_BClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            
            # *aim_box_B* updates
            if t >= 0.4 and aim_box_B.status == NOT_STARTED:
                # keep track of start time/frame for later
                aim_box_B.tStart = t
                aim_box_B.frameNStart = frameN  # exact frame index
                aim_box_B.setAutoDraw(True)
            
            # *accuracy_box_B* updates
            if t >= 0.4 and accuracy_box_B.status == NOT_STARTED:
                # keep track of start time/frame for later
                accuracy_box_B.tStart = t
                accuracy_box_B.frameNStart = frameN  # exact frame index
                accuracy_box_B.setAutoDraw(True)
            
            # *latency_box_B* updates
            if t >= 0.4 and latency_box_B.status == NOT_STARTED:
                # keep track of start time/frame for later
                latency_box_B.tStart = t
                latency_box_B.frameNStart = frameN  # exact frame index
                latency_box_B.setAutoDraw(True)
            
            # *press_box_B* updates
            if t >= 0.4 and press_box_B.status == NOT_STARTED:
                # keep track of start time/frame for later
                press_box_B.tStart = t
                press_box_B.frameNStart = frameN  # exact frame index
                press_box_B.setAutoDraw(True)
            
            # *postblock_response_B* updates
            if t >= 1 and postblock_response_B.status == NOT_STARTED:
                # keep track of start time/frame for later
                postblock_response_B.tStart = t
                postblock_response_B.frameNStart = frameN  # exact frame index
                postblock_response_B.status = STARTED
                # keyboard checking is just starting
                event.clearEvents(eventType='keyboard')
            if postblock_response_B.status == STARTED:
                theseKeys = event.getKeys(keyList=['e', 'i'])
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    # a response ends the routine
                    continueRoutine = False
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in postblock_BComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "postblock_B"-------
        for thisComponent in postblock_BComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        # the Routine "postblock_B" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        Asecond = data.TrialHandler(nReps=Asecond_nReps, method='sequential', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
            seed=None, name='Asecond')
        thisExp.addLoop(Asecond)  # add the loop to the experiment
        thisAsecond = Asecond.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisAsecond.rgb)
        if thisAsecond != None:
            for paramName in thisAsecond.keys():
                exec(paramName + '= thisAsecond.' + paramName)
        
        for thisAsecond in Asecond:
            currentLoop = Asecond
            # abbreviate parameter names if possible (e.g. rgb = thisAsecond.rgb)
            if thisAsecond != None:
                for paramName in thisAsecond.keys():
                    exec(paramName + '= thisAsecond.' + paramName)
            
            # ------Prepare to start Routine "preblock_A"-------
            t = 0
            preblock_AClock.reset()  # clock
            frameN = -1
            continueRoutine = True
            # update component parameters for each repeat
            # Option to simulates using ResponseEmulator:
            if Monkey:
                simulated_responses = [(1.1, 'e'), (1.1, 'i')]  # simulated responses take the form (onsetTime, responseKey). You can simulate more than one.
                responder = ResponseEmulator(simulated_responses)
                responder.start()
            
            # Generate list of stimuli for the block
            stim1_catA_stimuli_many = generate_trials('labelA_stimuli', 2, True)  # function and variable determined at begin exp.
            stim1_catB_stimuli_many = generate_trials('labelB_stimuli', 2, True)
            stim2_catA_stimuli_many = generate_trials('targetA_stimuli', 2, True)
            stim2_catB_stimuli_many = generate_trials('targetB_stimuli', 2, True)
            img_stim1_catA_stimuli_many = generate_trials('labelA_image_stimuli', 2, True)
            img_stim1_catB_stimuli_many = generate_trials('labelB_image_stimuli', 2, True)
            img_stim2_catA_stimuli_many = generate_trials('targetA_image_stimuli', 2, True)
            img_stim2_catB_stimuli_many = generate_trials('targetB_image_stimuli', 2, True)
            
            rule_box_A.setText(rule_A)
            preblock_response_A = event.BuilderKeyResponse()
            # keep track of which components have finished
            preblock_AComponents = [rule_box_A, preblock_response_A]
            for thisComponent in preblock_AComponents:
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            
            # -------Start Routine "preblock_A"-------
            while continueRoutine:
                # get current time
                t = preblock_AClock.getTime()
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                
                # *rule_box_A* updates
                if t >= 0.4 and rule_box_A.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    rule_box_A.tStart = t
                    rule_box_A.frameNStart = frameN  # exact frame index
                    rule_box_A.setAutoDraw(True)
                
                # *preblock_response_A* updates
                if t >= 1 and preblock_response_A.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    preblock_response_A.tStart = t
                    preblock_response_A.frameNStart = frameN  # exact frame index
                    preblock_response_A.status = STARTED
                    # keyboard checking is just starting
                    event.clearEvents(eventType='keyboard')
                if preblock_response_A.status == STARTED:
                    theseKeys = event.getKeys(keyList=['e', 'i'])
                    
                    # check for quit:
                    if "escape" in theseKeys:
                        endExpNow = True
                    if len(theseKeys) > 0:  # at least one key was pressed
                        # a response ends the routine
                        continueRoutine = False
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in preblock_AComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # check for quit (the Esc key)
                if endExpNow or event.getKeys(keyList=["escape"]):
                    core.quit()
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "preblock_A"-------
            for thisComponent in preblock_AComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            
            # the Routine "preblock_A" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # set up handler to look after randomisation of conditions etc
            trials_Asecond = data.TrialHandler(nReps=reptitions, method='random', 
                extraInfo=expInfo, originPath=-1,
                trialList=data.importConditions('block_layout.xlsx'),
                seed=None, name='trials_Asecond')
            thisExp.addLoop(trials_Asecond)  # add the loop to the experiment
            thisTrials_Asecond = trials_Asecond.trialList[0]  # so we can initialise stimuli with some values
            # abbreviate parameter names if possible (e.g. rgb = thisTrials_Asecond.rgb)
            if thisTrials_Asecond != None:
                for paramName in thisTrials_Asecond.keys():
                    exec(paramName + '= thisTrials_Asecond.' + paramName)
            
            for thisTrials_Asecond in trials_Asecond:
                currentLoop = trials_Asecond
                # abbreviate parameter names if possible (e.g. rgb = thisTrials_Asecond.rgb)
                if thisTrials_Asecond != None:
                    for paramName in thisTrials_Asecond.keys():
                        exec(paramName + '= thisTrials_Asecond.' + paramName)
                
                # ------Prepare to start Routine "trial_A"-------
                t = 0
                trial_AClock.reset()  # clock
                frameN = -1
                continueRoutine = True
                # update component parameters for each repeat
                # Option to simulates using ResponseEmulator:
                if Monkey:
                    simulated_responses = [(0.5, 'e'), (0.5, 'i')]  # simulated responses take the form (onsetTime, responseKey). You can simulate more than one.
                    responder = ResponseEmulator(simulated_responses)
                    responder.start()
                
                # For each stimlulus, choose a random exemplar from the appropriate list
                # word stimulus 1
                if stimulus1_category == 'a':
                    stimulus1 = stim1_catA_stimuli_many.pop()
                elif stimulus1_category == 'b':
                    stimulus1 = stim1_catB_stimuli_many.pop()
                
                # word stimulus 2
                if stimulus2_category == 'c':
                    stimulus2 = stim2_catA_stimuli_many.pop()
                elif stimulus2_category == 'd':
                    stimulus2 = stim2_catB_stimuli_many.pop()
                
                # image stimulus 1
                if stimulus1_category == 'a':
                    img_stimulus1 = img_stim1_catA_stimuli_many.pop()
                elif stimulus1_category == 'b':
                    img_stimulus1 = img_stim1_catB_stimuli_many.pop()
                
                # image stimulus 2
                if stimulus2_category == 'c':
                    img_stimulus2 = img_stim2_catA_stimuli_many.pop()
                elif stimulus2_category == 'd':
                    img_stimulus2 = img_stim2_catB_stimuli_many.pop()
                
                # set correct and incorrect responses
                if moving_response_options == False:
                    response_option_left = response_option_B  # i.e., the focal trial type is the right hand one, for hand dominance
                    response_option_right = response_option_A
                    response_option_onset = 0  # response options are onscreen constantly
                    if (trialType == 1) or (trialType == 4):
                        required_allowed = 'i'
                        required_correct = 'i'
                        feedback_allowed = 'e'
                        feedback_correct = 'e'
                    elif (trialType == 2) or (trialType == 3):
                        required_allowed = 'e'
                        required_correct = 'e'
                        feedback_allowed = 'i'
                        feedback_correct = 'i'
                elif moving_response_options == True:
                    rand_positions = randint(1, 3)
                    response_option_onset = 0.4  # response options appear with stimuli
                    if rand_positions == 1:
                        response_option_left = response_option_B
                        response_option_right = response_option_A
                        if (trialType == 1) or (trialType == 4):
                            required_allowed = 'i'
                            required_correct = 'i'
                            feedback_allowed = 'e'
                            feedback_correct = 'e'
                        elif (trialType == 2) or (trialType == 3):
                            required_allowed = 'e'
                            required_correct = 'e'
                            feedback_allowed = 'i'
                            feedback_correct = 'i'
                    elif rand_positions == 2:
                        response_option_left = response_option_A
                        response_option_right = response_option_B
                        if (trialType == 1) or (trialType == 4):
                            required_allowed = 'e'
                            required_correct = 'e'
                            feedback_allowed = 'i'
                            feedback_correct = 'i'
                        elif (trialType == 2) or (trialType == 3):
                            required_allowed = 'i'
                            required_correct = 'i'
                            feedback_allowed = 'e'
                            feedback_correct = 'e'
                image_stimulus1_box_A.setPos(image_stimulus1_location)
                image_stimulus1_box_A.setImage(img_stimulus1)
                image_stimulus2_box_A.setPos(image_stimulus2_location)
                image_stimulus2_box_A.setImage(img_stimulus2)
                stimulus1_box_A.setText(stimulus1)
                stimulus1_box_A.setPos(stimulus1_location)
                stimulus2_box_A.setText(stimulus2)
                stimulus2_box_A.setPos(stimulus2_location)
                required_response_A = event.BuilderKeyResponse()
                feedback_response_A = event.BuilderKeyResponse()
                left_box_A.setText(response_option_left)
                left_box_A.setPos(response_option_left_location)
                right_box_A.setText(response_option_right)
                right_box_A.setPos(response_option_right_location)
                accuracy_feedback_box_A.setPos(accuracy_feedback_location)
                # keep track of which components have finished
                trial_AComponents = [image_stimulus1_box_A, image_stimulus2_box_A, stimulus1_box_A, stimulus2_box_A, required_response_A, feedback_response_A, left_box_A, right_box_A, accuracy_feedback_box_A]
                for thisComponent in trial_AComponents:
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                
                # -------Start Routine "trial_A"-------
                while continueRoutine:
                    # get current time
                    t = trial_AClock.getTime()
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    # Accuracy feedback message
                    if len(feedback_response_A.keys)<1:
                        accuracyFeedback=""
                    else:
                        accuracyFeedback="X"
                    
                    # *image_stimulus1_box_A* updates
                    if t >= 0.4 and image_stimulus1_box_A.status == NOT_STARTED:
                        # keep track of start time/frame for later
                        image_stimulus1_box_A.tStart = t
                        image_stimulus1_box_A.frameNStart = frameN  # exact frame index
                        image_stimulus1_box_A.setAutoDraw(True)
                    
                    # *image_stimulus2_box_A* updates
                    if t >= 0.4 and image_stimulus2_box_A.status == NOT_STARTED:
                        # keep track of start time/frame for later
                        image_stimulus2_box_A.tStart = t
                        image_stimulus2_box_A.frameNStart = frameN  # exact frame index
                        image_stimulus2_box_A.setAutoDraw(True)
                    
                    # *stimulus1_box_A* updates
                    if t >= 0.4 and stimulus1_box_A.status == NOT_STARTED:
                        # keep track of start time/frame for later
                        stimulus1_box_A.tStart = t
                        stimulus1_box_A.frameNStart = frameN  # exact frame index
                        stimulus1_box_A.setAutoDraw(True)
                    
                    # *stimulus2_box_A* updates
                    if t >= 0.4 and stimulus2_box_A.status == NOT_STARTED:
                        # keep track of start time/frame for later
                        stimulus2_box_A.tStart = t
                        stimulus2_box_A.frameNStart = frameN  # exact frame index
                        stimulus2_box_A.setAutoDraw(True)
                    
                    # *required_response_A* updates
                    if t >= 0.4 and required_response_A.status == NOT_STARTED:
                        # keep track of start time/frame for later
                        required_response_A.tStart = t
                        required_response_A.frameNStart = frameN  # exact frame index
                        required_response_A.status = STARTED
                        # AllowedKeys looks like a variable named `required_allowed`
                        if not type(required_allowed) in [list, tuple, np.ndarray]:
                            if not isinstance(required_allowed, basestring):
                                logging.error('AllowedKeys variable `required_allowed` is not string- or list-like.')
                                core.quit()
                            elif not ',' in required_allowed: required_allowed = (required_allowed,)
                            else:  required_allowed = eval(required_allowed)
                        # keyboard checking is just starting
                        win.callOnFlip(required_response_A.clock.reset)  # t=0 on next screen flip
                        event.clearEvents(eventType='keyboard')
                    if required_response_A.status == STARTED:
                        theseKeys = event.getKeys(keyList=list(required_allowed))
                        
                        # check for quit:
                        if "escape" in theseKeys:
                            endExpNow = True
                        if len(theseKeys) > 0:  # at least one key was pressed
                            if required_response_A.keys == []:  # then this was the first keypress
                                required_response_A.keys = theseKeys[0]  # just the first key pressed
                                required_response_A.rt = required_response_A.clock.getTime()
                                # was this 'correct'?
                                if (required_response_A.keys == str(required_correct)) or (required_response_A.keys == required_correct):
                                    required_response_A.corr = 1
                                else:
                                    required_response_A.corr = 0
                                # a response ends the routine
                                continueRoutine = False
                    
                    # *feedback_response_A* updates
                    if t >= 0.4 and feedback_response_A.status == NOT_STARTED:
                        # keep track of start time/frame for later
                        feedback_response_A.tStart = t
                        feedback_response_A.frameNStart = frameN  # exact frame index
                        feedback_response_A.status = STARTED
                        # AllowedKeys looks like a variable named `feedback_allowed`
                        if not type(feedback_allowed) in [list, tuple, np.ndarray]:
                            if not isinstance(feedback_allowed, basestring):
                                logging.error('AllowedKeys variable `feedback_allowed` is not string- or list-like.')
                                core.quit()
                            elif not ',' in feedback_allowed: feedback_allowed = (feedback_allowed,)
                            else:  feedback_allowed = eval(feedback_allowed)
                        # keyboard checking is just starting
                        win.callOnFlip(feedback_response_A.clock.reset)  # t=0 on next screen flip
                        event.clearEvents(eventType='keyboard')
                    if feedback_response_A.status == STARTED:
                        theseKeys = event.getKeys(keyList=list(feedback_allowed))
                        
                        # check for quit:
                        if "escape" in theseKeys:
                            endExpNow = True
                        if len(theseKeys) > 0:  # at least one key was pressed
                            if feedback_response_A.keys == []:  # then this was the first keypress
                                feedback_response_A.keys = theseKeys[0]  # just the first key pressed
                                feedback_response_A.rt = feedback_response_A.clock.getTime()
                                # was this 'correct'?
                                if (feedback_response_A.keys == str(feedback_correct)) or (feedback_response_A.keys == feedback_correct):
                                    feedback_response_A.corr = 1
                                else:
                                    feedback_response_A.corr = 0
                    
                    # *left_box_A* updates
                    if t >= response_option_onset and left_box_A.status == NOT_STARTED:
                        # keep track of start time/frame for later
                        left_box_A.tStart = t
                        left_box_A.frameNStart = frameN  # exact frame index
                        left_box_A.setAutoDraw(True)
                    
                    # *right_box_A* updates
                    if t >= response_option_onset and right_box_A.status == NOT_STARTED:
                        # keep track of start time/frame for later
                        right_box_A.tStart = t
                        right_box_A.frameNStart = frameN  # exact frame index
                        right_box_A.setAutoDraw(True)
                    
                    # *accuracy_feedback_box_A* updates
                    if t >= 0.4 and accuracy_feedback_box_A.status == NOT_STARTED:
                        # keep track of start time/frame for later
                        accuracy_feedback_box_A.tStart = t
                        accuracy_feedback_box_A.frameNStart = frameN  # exact frame index
                        accuracy_feedback_box_A.setAutoDraw(True)
                    if accuracy_feedback_box_A.status == STARTED:  # only update if drawing
                        accuracy_feedback_box_A.setText(accuracyFeedback, log=False)
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in trial_AComponents:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # check for quit (the Esc key)
                    if endExpNow or event.getKeys(keyList=["escape"]):
                        core.quit()
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # -------Ending Routine "trial_A"-------
                for thisComponent in trial_AComponents:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                # save exemplars to experiment handler so they're written to the csv file
                thisExp.addData('stimulus1', stimulus1)
                thisExp.addData('stimulus2', stimulus2)
                thisExp.addData('img_stimulus1', img_stimulus1)
                thisExp.addData('img_stimulus2', img_stimulus2)
                thisExp.addData('response_option_left', response_option_left)
                thisExp.addData('response_option_right', response_option_right)
                # check responses
                if required_response_A.keys in ['', [], None]:  # No response was made
                    required_response_A.keys=None
                    # was no response the correct answer?!
                    if str(required_correct).lower() == 'none':
                       required_response_A.corr = 1  # correct non-response
                    else:
                       required_response_A.corr = 0  # failed to respond (incorrectly)
                # store data for trials_Asecond (TrialHandler)
                trials_Asecond.addData('required_response_A.keys',required_response_A.keys)
                trials_Asecond.addData('required_response_A.corr', required_response_A.corr)
                if required_response_A.keys != None:  # we had a response
                    trials_Asecond.addData('required_response_A.rt', required_response_A.rt)
                # check responses
                if feedback_response_A.keys in ['', [], None]:  # No response was made
                    feedback_response_A.keys=None
                    # was no response the correct answer?!
                    if str(feedback_correct).lower() == 'none':
                       feedback_response_A.corr = 1  # correct non-response
                    else:
                       feedback_response_A.corr = 0  # failed to respond (incorrectly)
                # store data for trials_Asecond (TrialHandler)
                trials_Asecond.addData('feedback_response_A.keys',feedback_response_A.keys)
                trials_Asecond.addData('feedback_response_A.corr', feedback_response_A.corr)
                if feedback_response_A.keys != None:  # we had a response
                    trials_Asecond.addData('feedback_response_A.rt', feedback_response_A.rt)
                # the Routine "trial_A" was not non-slip safe, so reset the non-slip timer
                routineTimer.reset()
                thisExp.nextEntry()
                
            # completed reptitions repeats of 'trials_Asecond'
            
            
            # ------Prepare to start Routine "postblock_A"-------
            t = 0
            postblock_AClock.reset()  # clock
            frameN = -1
            continueRoutine = True
            # update component parameters for each repeat
            # Option to simulates using ResponseEmulator:
            if Monkey:
                simulated_responses = [(1.1, 'e'), (1.1, 'i')]  # simulated responses take the form (onsetTime, responseKey). You can simulate more than one.
                responder = ResponseEmulator(simulated_responses)
                responder.start()
            
            # calculate summary stats
            if(starting_block == 'a'): 
                block_A_percentage_accuracy = (float(trials_Afirst.data['required_response_A.corr'].count()) - float(trials_Afirst.data['feedback_response_A.corr'].sum())) /  float(trials_Afirst.data['required_response_A.corr'].count()) * 100 
                block_A_median_latency = np.median(trials_Afirst.data['required_response_A.rt'])
            
            if(starting_block == 'b'): 
                block_A_percentage_accuracy = (float(trials_Asecond.data['required_response_A.corr'].count()) - float(trials_Asecond.data['feedback_response_A.corr'].sum())) /  float(trials_Asecond.data['required_response_A.corr'].count()) * 100 
                block_A_median_latency = np.median(trials_Asecond.data['required_response_A.rt'])
            
            # set messages
            msg_accuracy = "%s %i %s" %(accuracy, block_A_percentage_accuracy, percentCorrect) 
            msg_latency = "%s %.2f %s" %(speed, block_A_median_latency, seconds)
            
            ### save summary stats to experiment handler so they're written to the csv file
            ##thisExp.addData('block_A_percentage_accuracy', block_A_percentage_accuracy)
            ##thisExp.addData('block_A_median_latency', block_A_median_latency)
            aim_box_A.setText(aim)
            accuracy_box_A.setText(msg_accuracy)
            latency_box_A.setText(msg_latency)
            press_box_A.setText(press_message)
            postblock_response_A = event.BuilderKeyResponse()
            # keep track of which components have finished
            postblock_AComponents = [aim_box_A, accuracy_box_A, latency_box_A, press_box_A, postblock_response_A]
            for thisComponent in postblock_AComponents:
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            
            # -------Start Routine "postblock_A"-------
            while continueRoutine:
                # get current time
                t = postblock_AClock.getTime()
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                
                # *aim_box_A* updates
                if t >= 0.4 and aim_box_A.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    aim_box_A.tStart = t
                    aim_box_A.frameNStart = frameN  # exact frame index
                    aim_box_A.setAutoDraw(True)
                
                # *accuracy_box_A* updates
                if t >= 0.4 and accuracy_box_A.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    accuracy_box_A.tStart = t
                    accuracy_box_A.frameNStart = frameN  # exact frame index
                    accuracy_box_A.setAutoDraw(True)
                
                # *latency_box_A* updates
                if t >= 0.4 and latency_box_A.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    latency_box_A.tStart = t
                    latency_box_A.frameNStart = frameN  # exact frame index
                    latency_box_A.setAutoDraw(True)
                
                # *press_box_A* updates
                if t >= 0.4 and press_box_A.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    press_box_A.tStart = t
                    press_box_A.frameNStart = frameN  # exact frame index
                    press_box_A.setAutoDraw(True)
                
                # *postblock_response_A* updates
                if t >= 1 and postblock_response_A.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    postblock_response_A.tStart = t
                    postblock_response_A.frameNStart = frameN  # exact frame index
                    postblock_response_A.status = STARTED
                    # keyboard checking is just starting
                    event.clearEvents(eventType='keyboard')
                if postblock_response_A.status == STARTED:
                    theseKeys = event.getKeys(keyList=['e', 'i'])
                    
                    # check for quit:
                    if "escape" in theseKeys:
                        endExpNow = True
                    if len(theseKeys) > 0:  # at least one key was pressed
                        # a response ends the routine
                        continueRoutine = False
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in postblock_AComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # check for quit (the Esc key)
                if endExpNow or event.getKeys(keyList=["escape"]):
                    core.quit()
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "postblock_A"-------
            for thisComponent in postblock_AComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            
            # the Routine "postblock_A" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
        # completed Asecond_nReps repeats of 'Asecond'
        
    # completed complete_test_blocks repeats of 'test_blocks'
    
    
    # ------Prepare to start Routine "end"-------
    t = 0
    endClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    end_box.setText(end_message)
    end_response = event.BuilderKeyResponse()
    # keep track of which components have finished
    endComponents = [end_box, end_response]
    for thisComponent in endComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "end"-------
    while continueRoutine:
        # get current time
        t = endClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *end_box* updates
        if t >= 0.4 and end_box.status == NOT_STARTED:
            # keep track of start time/frame for later
            end_box.tStart = t
            end_box.frameNStart = frameN  # exact frame index
            end_box.setAutoDraw(True)
        
        # *end_response* updates
        if t >= .4 and end_response.status == NOT_STARTED:
            # keep track of start time/frame for later
            end_response.tStart = t
            end_response.frameNStart = frameN  # exact frame index
            end_response.status = STARTED
            # keyboard checking is just starting
            event.clearEvents(eventType='keyboard')
        if end_response.status == STARTED:
            theseKeys = event.getKeys(keyList=['return'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in endComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "end"-------
    for thisComponent in endComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "end" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed 1 repeats of 'task'





















# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
