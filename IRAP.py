#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.82.01), Mon Oct 19 01:09:06 2015
If you publish work using this script please cite the relevant PsychoPy publications
  Peirce, JW (2007) PsychoPy - Psychophysics software in Python. Journal of Neuroscience Methods, 162(1-2), 8-13.
  Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy. Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import division  # so that 1/3=0.333 instead of 1/3=0
from psychopy import visual, core, data, event, logging, sound, gui
from psychopy.constants import *  # things like STARTED, FINISHED
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'IRAP'  # from the Builder filename that created this script
expInfo = {u'Gender': u'', u'Age': u'', u'Participant': u''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False: core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data' + os.path.sep + '%s_%s' %(expInfo['Participant'], expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=None,
    savePickle=True, saveWideText=True,
    dataFileName=filename)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(size=(1366, 768), fullscr=True, screen=0, allowGUI=False, allowStencil=False,
    monitor='testMonitor', color='black', colorSpace='rgb',
    blendMode='avg', useFBO=True,
    units='norm')
# store frame rate of monitor if we can measure it successfully
expInfo['frameRate']=win.getActualFrameRate()
if expInfo['frameRate']!=None:
    frameDur = 1.0/round(expInfo['frameRate'])
else:
    frameDur = 1.0/60.0 # couldn't get a reliable measure so guess

# Initialize components for Routine "intro"
introClock = core.Clock()
introBox = visual.TextStim(win=win, ori=0, name='introBox',
    text='default text',    font='Arial',
    pos=[0, 0], height=0.08, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)
pressSpaceIntro = visual.TextStim(win=win, ori=0, name='pressSpaceIntro',
    text='default text',    font='Arial',
    pos=[0, -0.8], height=0.05, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0)

# Initialize components for Routine "instructPrac"
instructPracClock = core.Clock()
instrTextCon_3 = visual.TextStim(win=win, ori=0, name='instrTextCon_3',
    text='default text',    font='Arial',
    pos=[0, 0], height=0.08, wrapWidth=None,
    color=[-1,1,-1], colorSpace='rgb', opacity=1,
    depth=0.0)
text_28 = visual.TextStim(win=win, ori=0, name='text_28',
    text='default text',    font='Arial',
    pos=[0, -0.8], height=0.05, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0)

# Initialize components for Routine "block1Trials"
block1TrialsClock = core.Clock()
labelStimulusBlock1 = visual.TextStim(win=win, ori=0, name='labelStimulusBlock1',
    text='default text',    font='Arial',
    pos=[0, 0.5], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)
targetStimulus1 = visual.TextStim(win=win, ori=0, name='targetStimulus1',
    text='default text',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0)
responseOption1Con = visual.TextStim(win=win, ori=0, name='responseOption1Con',
    text='default text',    font='Arial',
    pos=[-0.5,-0.8], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-4.0)
responseOption2Con = visual.TextStim(win=win, ori=0, name='responseOption2Con',
    text='default text',    font='Arial',
    pos=[0.5,-0.8], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-5.0)
trialTypeCon = visual.TextStim(win=win, ori=0, name='trialTypeCon',
    text='default text',    font='Arial',
    pos=[0, -0.4], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=-6.0)
#msg variable just needs some value at start
msg=''
conAccuracyFeedback = visual.TextStim(win=win, ori=0, name='conAccuracyFeedback',
    text='default text',    font='Arial',
    pos=[0, -0.5], height=0.2, wrapWidth=None,
    color='red', colorSpace='rgb', opacity=1,
    depth=-8.0)

# Initialize components for Routine "feedbackBlock1Prac"
feedbackBlock1PracClock = core.Clock()
msg1='doh!'#if this comes up we forgot to update the msg!
endMsg='Finished Experiment'
text_30 = visual.TextStim(win=win, ori=0, name='text_30',
    text='default text',    font='Arial',
    pos=[0.2, 0], height=0.08, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0)
text_31 = visual.TextStim(win=win, ori=0, name='text_31',
    text='default text',    font='Arial',
    pos=[0, -0.8], height=0.05, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-3.0)
text_32 = visual.TextStim(win=win, ori=0, name='text_32',
    text='default text',    font='Arial',
    pos=[0.2, -0.1], height=0.08, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-4.0)
accuracyMessage_3 = visual.TextStim(win=win, ori=0, name='accuracyMessage_3',
    text='default text',    font='Arial',
    pos=[-0.2, 0], height=0.08, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-5.0)
speedMessage_3 = visual.TextStim(win=win, ori=0, name='speedMessage_3',
    text='default text',    font='Arial',
    pos=[-0.2, -0.1], height=0.08, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-6.0)
aimAccuracyAndLatency_3 = visual.TextStim(win=win, ori=0, name='aimAccuracyAndLatency_3',
    text='default text',    font='Arial',
    pos=[0, 0.3], height=0.08, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-7.0)

# Initialize components for Routine "instructPrac2"
instructPrac2Clock = core.Clock()
instrTextIncon_2 = visual.TextStim(win=win, ori=0, name='instrTextIncon_2',
    text='default text',    font='Arial',
    pos=[0, 0], height=0.08, wrapWidth=None,
    color=[-1,1,-1], colorSpace='rgb', opacity=1,
    depth=0.0)
text_11 = visual.TextStim(win=win, ori=0, name='text_11',
    text='default text',    font='Arial',
    pos=[0, -0.8], height=0.05, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0)

# Initialize components for Routine "block2Trials"
block2TrialsClock = core.Clock()
labelStimulusBlock2 = visual.TextStim(win=win, ori=0, name='labelStimulusBlock2',
    text='default text',    font='Arial',
    pos=[0, 0.5], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)
targetStimulus2 = visual.TextStim(win=win, ori=0, name='targetStimulus2',
    text='default text',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0)
responseOption1Incon = visual.TextStim(win=win, ori=0, name='responseOption1Incon',
    text='default text',    font='Arial',
    pos=[-0.5,-0.8], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-4.0)
responseOption2Incon = visual.TextStim(win=win, ori=0, name='responseOption2Incon',
    text='default text',    font='Arial',
    pos=[0.5,-0.8], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-5.0)
trialTypeIncon = visual.TextStim(win=win, ori=0, name='trialTypeIncon',
    text='default text',    font='Arial',
    pos=[0, -0.4], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=-6.0)
#msg variable just needs some value at start
msg2=""
inconAccuracyFeedback = visual.TextStim(win=win, ori=0, name='inconAccuracyFeedback',
    text='default text',    font='Arial',
    pos=[0, -0.5], height=0.2, wrapWidth=None,
    color='red', colorSpace='rgb', opacity=1,
    depth=-8.0)

# Initialize components for Routine "feedbackBlock2Prac"
feedbackBlock2PracClock = core.Clock()
msg2='doh!'#if this comes up we forgot to update the msg!
completeTestBlocks=0
text_10 = visual.TextStim(win=win, ori=0, name='text_10',
    text='default text',    font='Arial',
    pos=[0.2, 0], height=0.08, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0)
text_33 = visual.TextStim(win=win, ori=0, name='text_33',
    text='default text',    font='Arial',
    pos=[0, -0.8], height=0.05, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-3.0)
text_34 = visual.TextStim(win=win, ori=0, name='text_34',
    text='default text',    font='Arial',
    pos=[0.2, -0.1], height=0.08, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-4.0)
accuracyMessageIncon_2 = visual.TextStim(win=win, ori=0, name='accuracyMessageIncon_2',
    text='default text',    font='Arial',
    pos=[-0.2, 0], height=0.08, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-5.0)
speedMessageIncon_2 = visual.TextStim(win=win, ori=0, name='speedMessageIncon_2',
    text='default text',    font='Arial',
    pos=[-0.2, -0.1], height=0.08, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-6.0)
aimAccuracyAndLatencyIncon_2 = visual.TextStim(win=win, ori=0, name='aimAccuracyAndLatencyIncon_2',
    text='default text',    font='Arial',
    pos=[0, 0.3], height=0.08, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-7.0)

# Initialize components for Routine "instructTest"
instructTestClock = core.Clock()
instrTextCon_2 = visual.TextStim(win=win, ori=0, name='instrTextCon_2',
    text='default text',    font='Arial',
    pos=[0, 0], height=0.08, wrapWidth=None,
    color=[-1,1,-1], colorSpace='rgb', opacity=1,
    depth=0.0)
text_18 = visual.TextStim(win=win, ori=0, name='text_18',
    text='default text',    font='Arial',
    pos=[0, -0.8], height=0.05, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0)

# Initialize components for Routine "block1Trials"
block1TrialsClock = core.Clock()
labelStimulusBlock1 = visual.TextStim(win=win, ori=0, name='labelStimulusBlock1',
    text='default text',    font='Arial',
    pos=[0, 0.5], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)
targetStimulus1 = visual.TextStim(win=win, ori=0, name='targetStimulus1',
    text='default text',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0)
responseOption1Con = visual.TextStim(win=win, ori=0, name='responseOption1Con',
    text='default text',    font='Arial',
    pos=[-0.5,-0.8], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-4.0)
responseOption2Con = visual.TextStim(win=win, ori=0, name='responseOption2Con',
    text='default text',    font='Arial',
    pos=[0.5,-0.8], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-5.0)
trialTypeCon = visual.TextStim(win=win, ori=0, name='trialTypeCon',
    text='default text',    font='Arial',
    pos=[0, -0.4], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=-6.0)
#msg variable just needs some value at start
msg=''
conAccuracyFeedback = visual.TextStim(win=win, ori=0, name='conAccuracyFeedback',
    text='default text',    font='Arial',
    pos=[0, -0.5], height=0.2, wrapWidth=None,
    color='red', colorSpace='rgb', opacity=1,
    depth=-8.0)

# Initialize components for Routine "feedbackBlock1Test"
feedbackBlock1TestClock = core.Clock()
msg1='doh!'#if this comes up we forgot to update the msg!
endMsg='Finished Experiment'
text_25 = visual.TextStim(win=win, ori=0, name='text_25',
    text='default text',    font='Arial',
    pos=[0.2, 0], height=0.08, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0)
text_26 = visual.TextStim(win=win, ori=0, name='text_26',
    text='default text',    font='Arial',
    pos=[0, -0.8], height=0.05, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-3.0)
text_27 = visual.TextStim(win=win, ori=0, name='text_27',
    text='default text',    font='Arial',
    pos=[0.2, -0.1], height=0.08, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-4.0)
accuracyMessage_2 = visual.TextStim(win=win, ori=0, name='accuracyMessage_2',
    text='default text',    font='Arial',
    pos=[-0.2, 0], height=0.08, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-5.0)
speedMessage_2 = visual.TextStim(win=win, ori=0, name='speedMessage_2',
    text='default text',    font='Arial',
    pos=[-0.2, -0.1], height=0.08, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-6.0)
aimAccuracyAndLatency_2 = visual.TextStim(win=win, ori=0, name='aimAccuracyAndLatency_2',
    text='default text',    font='Arial',
    pos=[0, 0.3], height=0.08, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-7.0)

# Initialize components for Routine "instructTest2"
instructTest2Clock = core.Clock()
instrTextIncon_3 = visual.TextStim(win=win, ori=0, name='instrTextIncon_3',
    text='default text',    font='Arial',
    pos=[0, 0], height=0.08, wrapWidth=None,
    color=[-1,1,-1], colorSpace='rgb', opacity=1,
    depth=0.0)
text_13 = visual.TextStim(win=win, ori=0, name='text_13',
    text='default text',    font='Arial',
    pos=[0, -0.8], height=0.05, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0)

# Initialize components for Routine "block2Trials"
block2TrialsClock = core.Clock()
labelStimulusBlock2 = visual.TextStim(win=win, ori=0, name='labelStimulusBlock2',
    text='default text',    font='Arial',
    pos=[0, 0.5], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)
targetStimulus2 = visual.TextStim(win=win, ori=0, name='targetStimulus2',
    text='default text',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0)
responseOption1Incon = visual.TextStim(win=win, ori=0, name='responseOption1Incon',
    text='default text',    font='Arial',
    pos=[-0.5,-0.8], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-4.0)
responseOption2Incon = visual.TextStim(win=win, ori=0, name='responseOption2Incon',
    text='default text',    font='Arial',
    pos=[0.5,-0.8], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-5.0)
trialTypeIncon = visual.TextStim(win=win, ori=0, name='trialTypeIncon',
    text='default text',    font='Arial',
    pos=[0, -0.4], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=-6.0)
#msg variable just needs some value at start
msg2=""
inconAccuracyFeedback = visual.TextStim(win=win, ori=0, name='inconAccuracyFeedback',
    text='default text',    font='Arial',
    pos=[0, -0.5], height=0.2, wrapWidth=None,
    color='red', colorSpace='rgb', opacity=1,
    depth=-8.0)

# Initialize components for Routine "feedbackBlock2Test"
feedbackBlock2TestClock = core.Clock()

text_22 = visual.TextStim(win=win, ori=0, name='text_22',
    text='default text',    font='Arial',
    pos=[0.2, 0], height=0.08, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0)
text_23 = visual.TextStim(win=win, ori=0, name='text_23',
    text='default text',    font='Arial',
    pos=[0, -0.8], height=0.05, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-3.0)
text_24 = visual.TextStim(win=win, ori=0, name='text_24',
    text='default text',    font='Arial',
    pos=[0.2, -0.1], height=0.08, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-4.0)
accuracyMessageTestIncon_2 = visual.TextStim(win=win, ori=0, name='accuracyMessageTestIncon_2',
    text='default text',    font='Arial',
    pos=[-0.2, -0.0], height=0.08, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-5.0)
speedMessageInconTest_2 = visual.TextStim(win=win, ori=0, name='speedMessageInconTest_2',
    text='default text',    font='Arial',
    pos=[-0.2, -0.1], height=0.08, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-6.0)
aimAccuracyAndLatencyInconTest_2 = visual.TextStim(win=win, ori=0, name='aimAccuracyAndLatencyInconTest_2',
    text='default text',    font='Arial',
    pos=[0, 0.3], height=0.08, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-7.0)

# Initialize components for Routine "thanks"
thanksClock = core.Clock()
text = visual.TextStim(win=win, ori=0, name='text',
    text='default text',    font='Arial',
    pos=[0, -0.2], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)
endMsgLabel = visual.TextStim(win=win, ori=0, name='endMsgLabel',
    text='default text',    font='Arial',
    pos=[0, 0.1], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# set up handler to look after randomisation of conditions etc
getIntroStrings = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=None,
    trialList=data.importConditions('instructions.xlsx'),
    seed=None, name='getIntroStrings')
thisExp.addLoop(getIntroStrings)  # add the loop to the experiment
thisGetIntroString = getIntroStrings.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisGetIntroString.rgb)
if thisGetIntroString != None:
    for paramName in thisGetIntroString.keys():
        exec(paramName + '= thisGetIntroString.' + paramName)

for thisGetIntroString in getIntroStrings:
    currentLoop = getIntroStrings
    # abbreviate parameter names if possible (e.g. rgb = thisGetIntroString.rgb)
    if thisGetIntroString != None:
        for paramName in thisGetIntroString.keys():
            exec(paramName + '= thisGetIntroString.' + paramName)
    
    #------Prepare to start Routine "intro"-------
    t = 0
    introClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    introBox.setText(intro)
    keyResponseIntro = event.BuilderKeyResponse()  # create an object of type KeyResponse
    keyResponseIntro.status = NOT_STARTED
    pressSpaceIntro.setText(space)
    # keep track of which components have finished
    introComponents = []
    introComponents.append(introBox)
    introComponents.append(keyResponseIntro)
    introComponents.append(pressSpaceIntro)
    for thisComponent in introComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "intro"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = introClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *introBox* updates
        if t >= 0.4 and introBox.status == NOT_STARTED:
            # keep track of start time/frame for later
            introBox.tStart = t  # underestimates by a little under one frame
            introBox.frameNStart = frameN  # exact frame index
            introBox.setAutoDraw(True)
        
        # *keyResponseIntro* updates
        if t >= .4 and keyResponseIntro.status == NOT_STARTED:
            # keep track of start time/frame for later
            keyResponseIntro.tStart = t  # underestimates by a little under one frame
            keyResponseIntro.frameNStart = frameN  # exact frame index
            keyResponseIntro.status = STARTED
            # keyboard checking is just starting
            keyResponseIntro.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if keyResponseIntro.status == STARTED:
            theseKeys = event.getKeys(keyList=['d', 'k'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                if keyResponseIntro.keys == []:  # then this was the first keypress
                    keyResponseIntro.keys = theseKeys[0]  # just the first key pressed
                    keyResponseIntro.rt = keyResponseIntro.clock.getTime()
                    # a response ends the routine
                    continueRoutine = False
        
        # *pressSpaceIntro* updates
        if t >= .4 and pressSpaceIntro.status == NOT_STARTED:
            # keep track of start time/frame for later
            pressSpaceIntro.tStart = t  # underestimates by a little under one frame
            pressSpaceIntro.frameNStart = frameN  # exact frame index
            pressSpaceIntro.setAutoDraw(True)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in introComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "intro"-------
    for thisComponent in introComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if keyResponseIntro.keys in ['', [], None]:  # No response was made
       keyResponseIntro.keys=None
    # store data for getIntroStrings (TrialHandler)
    getIntroStrings.addData('keyResponseIntro.keys',keyResponseIntro.keys)
    if keyResponseIntro.keys != None:  # we had a response
        getIntroStrings.addData('keyResponseIntro.rt', keyResponseIntro.rt)
    # the Routine "intro" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed 1 repeats of 'getIntroStrings'


# set up handler to look after randomisation of conditions etc
pracBlocks = data.TrialHandler(nReps=3, method='sequential', 
    extraInfo=expInfo, originPath=None,
    trialList=data.importConditions('Blocks.xlsx'),
    seed=None, name='pracBlocks')
thisExp.addLoop(pracBlocks)  # add the loop to the experiment
thisPracBlock = pracBlocks.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisPracBlock.rgb)
if thisPracBlock != None:
    for paramName in thisPracBlock.keys():
        exec(paramName + '= thisPracBlock.' + paramName)

for thisPracBlock in pracBlocks:
    currentLoop = pracBlocks
    # abbreviate parameter names if possible (e.g. rgb = thisPracBlock.rgb)
    if thisPracBlock != None:
        for paramName in thisPracBlock.keys():
            exec(paramName + '= thisPracBlock.' + paramName)
    
    #------Prepare to start Routine "instructPrac"-------
    t = 0
    instructPracClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    instrTextCon_3.setText(rule1)
    ready_3 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    ready_3.status = NOT_STARTED
    text_28.setText(space)
    # keep track of which components have finished
    instructPracComponents = []
    instructPracComponents.append(instrTextCon_3)
    instructPracComponents.append(ready_3)
    instructPracComponents.append(text_28)
    for thisComponent in instructPracComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "instructPrac"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = instructPracClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instrTextCon_3* updates
        if t >= 0.4 and instrTextCon_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            instrTextCon_3.tStart = t  # underestimates by a little under one frame
            instrTextCon_3.frameNStart = frameN  # exact frame index
            instrTextCon_3.setAutoDraw(True)
        
        # *ready_3* updates
        if t >= .4 and ready_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            ready_3.tStart = t  # underestimates by a little under one frame
            ready_3.frameNStart = frameN  # exact frame index
            ready_3.status = STARTED
            # keyboard checking is just starting
            event.clearEvents(eventType='keyboard')
        if ready_3.status == STARTED:
            theseKeys = event.getKeys(keyList=['d', 'k'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                # a response ends the routine
                continueRoutine = False
        
        # *text_28* updates
        if t >= .4 and text_28.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_28.tStart = t  # underestimates by a little under one frame
            text_28.frameNStart = frameN  # exact frame index
            text_28.setAutoDraw(True)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instructPracComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "instructPrac"-------
    for thisComponent in instructPracComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "instructPrac" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trialsLoop1 = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=None,
        trialList=data.importConditions('stimuli.xlsx'),
        seed=None, name='trialsLoop1')
    thisExp.addLoop(trialsLoop1)  # add the loop to the experiment
    thisTrialsLoop1 = trialsLoop1.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb=thisTrialsLoop1.rgb)
    if thisTrialsLoop1 != None:
        for paramName in thisTrialsLoop1.keys():
            exec(paramName + '= thisTrialsLoop1.' + paramName)
    
    for thisTrialsLoop1 in trialsLoop1:
        currentLoop = trialsLoop1
        # abbreviate parameter names if possible (e.g. rgb = thisTrialsLoop1.rgb)
        if thisTrialsLoop1 != None:
            for paramName in thisTrialsLoop1.keys():
                exec(paramName + '= thisTrialsLoop1.' + paramName)
        
        #------Prepare to start Routine "block1Trials"-------
        t = 0
        block1TrialsClock.reset()  # clock 
        frameN = -1
        # update component parameters for each repeat
        labelStimulusBlock1.setText(label)
        targetStimulus1.setText(target)
        response1 = event.BuilderKeyResponse()  # create an object of type KeyResponse
        response1.status = NOT_STARTED
        incorrectResponse1 = event.BuilderKeyResponse()  # create an object of type KeyResponse
        incorrectResponse1.status = NOT_STARTED
        responseOption1Con.setText(responseOption1)
        responseOption2Con.setText(responseOption2)
        trialTypeCon.setText(trialType)
        
        # keep track of which components have finished
        block1TrialsComponents = []
        block1TrialsComponents.append(labelStimulusBlock1)
        block1TrialsComponents.append(targetStimulus1)
        block1TrialsComponents.append(response1)
        block1TrialsComponents.append(incorrectResponse1)
        block1TrialsComponents.append(responseOption1Con)
        block1TrialsComponents.append(responseOption2Con)
        block1TrialsComponents.append(trialTypeCon)
        block1TrialsComponents.append(conAccuracyFeedback)
        for thisComponent in block1TrialsComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        #-------Start Routine "block1Trials"-------
        continueRoutine = True
        while continueRoutine:
            # get current time
            t = block1TrialsClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *labelStimulusBlock1* updates
            if t >= 0.4 and labelStimulusBlock1.status == NOT_STARTED:
                # keep track of start time/frame for later
                labelStimulusBlock1.tStart = t  # underestimates by a little under one frame
                labelStimulusBlock1.frameNStart = frameN  # exact frame index
                labelStimulusBlock1.setAutoDraw(True)
            
            # *targetStimulus1* updates
            if t >= 0.4 and targetStimulus1.status == NOT_STARTED:
                # keep track of start time/frame for later
                targetStimulus1.tStart = t  # underestimates by a little under one frame
                targetStimulus1.frameNStart = frameN  # exact frame index
                targetStimulus1.setAutoDraw(True)
            
            # *response1* updates
            if t >= 0.4 and response1.status == NOT_STARTED:
                # keep track of start time/frame for later
                response1.tStart = t  # underestimates by a little under one frame
                response1.frameNStart = frameN  # exact frame index
                response1.status = STARTED
                # AllowedKeys looks like a variable named `allowAns1`
                if not 'allowAns1' in locals():
                    logging.error('AllowedKeys variable `allowAns1` is not defined.')
                    core.quit()
                if not type(allowAns1) in [list, tuple, np.ndarray]:
                    if not isinstance(allowAns1, basestring):
                        logging.error('AllowedKeys variable `allowAns1` is not string- or list-like.')
                        core.quit()
                    elif not ',' in allowAns1: allowAns1 = (allowAns1,)
                    else:  allowAns1 = eval(allowAns1)
                # keyboard checking is just starting
                response1.clock.reset()  # now t=0
                event.clearEvents(eventType='keyboard')
            if response1.status == STARTED:
                theseKeys = event.getKeys(keyList=list(allowAns1))
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    if response1.keys == []:  # then this was the first keypress
                        response1.keys = theseKeys[0]  # just the first key pressed
                        response1.rt = response1.clock.getTime()
                        # was this 'correct'?
                        if (response1.keys == str(correctAns1)) or (response1.keys == correctAns1):
                            response1.corr = 1
                        else:
                            response1.corr = 0
                        # a response ends the routine
                        continueRoutine = False
            
            # *incorrectResponse1* updates
            if t >= 0.4 and incorrectResponse1.status == NOT_STARTED:
                # keep track of start time/frame for later
                incorrectResponse1.tStart = t  # underestimates by a little under one frame
                incorrectResponse1.frameNStart = frameN  # exact frame index
                incorrectResponse1.status = STARTED
                # AllowedKeys looks like a variable named `allowAns2`
                if not 'allowAns2' in locals():
                    logging.error('AllowedKeys variable `allowAns2` is not defined.')
                    core.quit()
                if not type(allowAns2) in [list, tuple, np.ndarray]:
                    if not isinstance(allowAns2, basestring):
                        logging.error('AllowedKeys variable `allowAns2` is not string- or list-like.')
                        core.quit()
                    elif not ',' in allowAns2: allowAns2 = (allowAns2,)
                    else:  allowAns2 = eval(allowAns2)
                # keyboard checking is just starting
                incorrectResponse1.clock.reset()  # now t=0
                event.clearEvents(eventType='keyboard')
            if incorrectResponse1.status == STARTED:
                theseKeys = event.getKeys(keyList=list(allowAns2))
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    if incorrectResponse1.keys == []:  # then this was the first keypress
                        incorrectResponse1.keys = theseKeys[0]  # just the first key pressed
                        incorrectResponse1.rt = incorrectResponse1.clock.getTime()
                        # was this 'correct'?
                        if (incorrectResponse1.keys == str(correctAns2)) or (incorrectResponse1.keys == correctAns2):
                            incorrectResponse1.corr = 1
                        else:
                            incorrectResponse1.corr = 0
            
            # *responseOption1Con* updates
            if t >= 0 and responseOption1Con.status == NOT_STARTED:
                # keep track of start time/frame for later
                responseOption1Con.tStart = t  # underestimates by a little under one frame
                responseOption1Con.frameNStart = frameN  # exact frame index
                responseOption1Con.setAutoDraw(True)
            
            # *responseOption2Con* updates
            if t >= 0 and responseOption2Con.status == NOT_STARTED:
                # keep track of start time/frame for later
                responseOption2Con.tStart = t  # underestimates by a little under one frame
                responseOption2Con.frameNStart = frameN  # exact frame index
                responseOption2Con.setAutoDraw(True)
            
            # *trialTypeCon* updates
            if t >= 0.4 and trialTypeCon.status == NOT_STARTED:
                # keep track of start time/frame for later
                trialTypeCon.tStart = t  # underestimates by a little under one frame
                trialTypeCon.frameNStart = frameN  # exact frame index
                trialTypeCon.setAutoDraw(True)
            if trialTypeCon.status == STARTED and t >= (0.4 + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
                trialTypeCon.setAutoDraw(False)
            if len(incorrectResponse1.keys)<1:
                msg=""
            else:
                msg="X"
            
            # *conAccuracyFeedback* updates
            if t >= 0.4 and conAccuracyFeedback.status == NOT_STARTED:
                # keep track of start time/frame for later
                conAccuracyFeedback.tStart = t  # underestimates by a little under one frame
                conAccuracyFeedback.frameNStart = frameN  # exact frame index
                conAccuracyFeedback.setAutoDraw(True)
            if conAccuracyFeedback.status == STARTED:  # only update if being drawn
                conAccuracyFeedback.setText(msg, log=False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in block1TrialsComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        #-------Ending Routine "block1Trials"-------
        for thisComponent in block1TrialsComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if response1.keys in ['', [], None]:  # No response was made
           response1.keys=None
           # was no response the correct answer?!
           if str(correctAns1).lower() == 'none': response1.corr = 1  # correct non-response
           else: response1.corr = 0  # failed to respond (incorrectly)
        # store data for trialsLoop1 (TrialHandler)
        trialsLoop1.addData('response1.keys',response1.keys)
        trialsLoop1.addData('response1.corr', response1.corr)
        if response1.keys != None:  # we had a response
            trialsLoop1.addData('response1.rt', response1.rt)
        # check responses
        if incorrectResponse1.keys in ['', [], None]:  # No response was made
           incorrectResponse1.keys=None
           # was no response the correct answer?!
           if str(correctAns2).lower() == 'none': incorrectResponse1.corr = 1  # correct non-response
           else: incorrectResponse1.corr = 0  # failed to respond (incorrectly)
        # store data for trialsLoop1 (TrialHandler)
        trialsLoop1.addData('incorrectResponse1.keys',incorrectResponse1.keys)
        trialsLoop1.addData('incorrectResponse1.corr', incorrectResponse1.corr)
        if incorrectResponse1.keys != None:  # we had a response
            trialsLoop1.addData('incorrectResponse1.rt', incorrectResponse1.rt)
        
        # the Routine "block1Trials" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'trialsLoop1'
    
    
    #------Prepare to start Routine "feedbackBlock1Prac"-------
    t = 0
    feedbackBlock1PracClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    nCorrLoop1Prac = (float(trialsLoop1.data['response1.corr'].count()) - float(trialsLoop1.data['incorrectResponse1.corr'].sum())) /  float(trialsLoop1.data['response1.corr'].count()) * 100 #count the number of 'correct' correctIncon trials (which actually equals the number of trials, as all must be correct to progress). Take away the number of 'correct' incorrectIncon trials to find real proportion of truly correct trials. Divide by total number of trials and multiply by 100. 
    medianRtLoop1Prac = np.median(trialsLoop1.data['response1.rt'])
    msg1 = "%i %s" %(nCorrLoop1Prac, percentCorrect) #percentCorrect is a variable pulled from excel sheet 'blocks'
    msg1_2 = "%.2f %s" %(medianRtLoop1Prac, seconds) #same as above
    text_30.setText(msg1)
    key_resp_10 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    key_resp_10.status = NOT_STARTED
    text_31.setText(space)
    text_32.setText(msg1_2)
    accuracyMessage_3.setText(accuracy)
    speedMessage_3.setText(speed)
    aimAccuracyAndLatency_3.setText(aim)
    # keep track of which components have finished
    feedbackBlock1PracComponents = []
    feedbackBlock1PracComponents.append(text_30)
    feedbackBlock1PracComponents.append(key_resp_10)
    feedbackBlock1PracComponents.append(text_31)
    feedbackBlock1PracComponents.append(text_32)
    feedbackBlock1PracComponents.append(accuracyMessage_3)
    feedbackBlock1PracComponents.append(speedMessage_3)
    feedbackBlock1PracComponents.append(aimAccuracyAndLatency_3)
    for thisComponent in feedbackBlock1PracComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "feedbackBlock1Prac"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = feedbackBlock1PracClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # *text_30* updates
        if t >= 0.4 and text_30.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_30.tStart = t  # underestimates by a little under one frame
            text_30.frameNStart = frameN  # exact frame index
            text_30.setAutoDraw(True)
        
        # *key_resp_10* updates
        if t >= .4 and key_resp_10.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_10.tStart = t  # underestimates by a little under one frame
            key_resp_10.frameNStart = frameN  # exact frame index
            key_resp_10.status = STARTED
            # keyboard checking is just starting
            key_resp_10.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if key_resp_10.status == STARTED:
            theseKeys = event.getKeys(keyList=['d', 'k'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                key_resp_10.keys = theseKeys[-1]  # just the last key pressed
                key_resp_10.rt = key_resp_10.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        # *text_31* updates
        if t >= .4 and text_31.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_31.tStart = t  # underestimates by a little under one frame
            text_31.frameNStart = frameN  # exact frame index
            text_31.setAutoDraw(True)
        
        # *text_32* updates
        if t >= 0.4 and text_32.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_32.tStart = t  # underestimates by a little under one frame
            text_32.frameNStart = frameN  # exact frame index
            text_32.setAutoDraw(True)
        
        # *accuracyMessage_3* updates
        if t >= 0.4 and accuracyMessage_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            accuracyMessage_3.tStart = t  # underestimates by a little under one frame
            accuracyMessage_3.frameNStart = frameN  # exact frame index
            accuracyMessage_3.setAutoDraw(True)
        
        # *speedMessage_3* updates
        if t >= 0.4 and speedMessage_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            speedMessage_3.tStart = t  # underestimates by a little under one frame
            speedMessage_3.frameNStart = frameN  # exact frame index
            speedMessage_3.setAutoDraw(True)
        
        # *aimAccuracyAndLatency_3* updates
        if t >= 0.4 and aimAccuracyAndLatency_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            aimAccuracyAndLatency_3.tStart = t  # underestimates by a little under one frame
            aimAccuracyAndLatency_3.frameNStart = frameN  # exact frame index
            aimAccuracyAndLatency_3.setAutoDraw(True)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feedbackBlock1PracComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "feedbackBlock1Prac"-------
    for thisComponent in feedbackBlock1PracComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # check responses
    if key_resp_10.keys in ['', [], None]:  # No response was made
       key_resp_10.keys=None
    # store data for pracBlocks (TrialHandler)
    pracBlocks.addData('key_resp_10.keys',key_resp_10.keys)
    if key_resp_10.keys != None:  # we had a response
        pracBlocks.addData('key_resp_10.rt', key_resp_10.rt)
    # the Routine "feedbackBlock1Prac" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    #------Prepare to start Routine "instructPrac2"-------
    t = 0
    instructPrac2Clock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    instrTextIncon_2.setText(rule2)
    key_resp_3 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    key_resp_3.status = NOT_STARTED
    text_11.setText(space)
    # keep track of which components have finished
    instructPrac2Components = []
    instructPrac2Components.append(instrTextIncon_2)
    instructPrac2Components.append(key_resp_3)
    instructPrac2Components.append(text_11)
    for thisComponent in instructPrac2Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "instructPrac2"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = instructPrac2Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instrTextIncon_2* updates
        if t >= 0.4 and instrTextIncon_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            instrTextIncon_2.tStart = t  # underestimates by a little under one frame
            instrTextIncon_2.frameNStart = frameN  # exact frame index
            instrTextIncon_2.setAutoDraw(True)
        
        # *key_resp_3* updates
        if t >= .4 and key_resp_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_3.tStart = t  # underestimates by a little under one frame
            key_resp_3.frameNStart = frameN  # exact frame index
            key_resp_3.status = STARTED
            # keyboard checking is just starting
            key_resp_3.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if key_resp_3.status == STARTED:
            theseKeys = event.getKeys(keyList=['d', 'k'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                key_resp_3.keys = theseKeys[-1]  # just the last key pressed
                key_resp_3.rt = key_resp_3.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        # *text_11* updates
        if t >= .4 and text_11.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_11.tStart = t  # underestimates by a little under one frame
            text_11.frameNStart = frameN  # exact frame index
            text_11.setAutoDraw(True)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instructPrac2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "instructPrac2"-------
    for thisComponent in instructPrac2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_3.keys in ['', [], None]:  # No response was made
       key_resp_3.keys=None
    # store data for pracBlocks (TrialHandler)
    pracBlocks.addData('key_resp_3.keys',key_resp_3.keys)
    if key_resp_3.keys != None:  # we had a response
        pracBlocks.addData('key_resp_3.rt', key_resp_3.rt)
    # the Routine "instructPrac2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trialsLoop2 = data.TrialHandler(nReps=1, method='random', 
        extraInfo=expInfo, originPath=None,
        trialList=data.importConditions('stimuli.xlsx'),
        seed=None, name='trialsLoop2')
    thisExp.addLoop(trialsLoop2)  # add the loop to the experiment
    thisTrialsLoop2 = trialsLoop2.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb=thisTrialsLoop2.rgb)
    if thisTrialsLoop2 != None:
        for paramName in thisTrialsLoop2.keys():
            exec(paramName + '= thisTrialsLoop2.' + paramName)
    
    for thisTrialsLoop2 in trialsLoop2:
        currentLoop = trialsLoop2
        # abbreviate parameter names if possible (e.g. rgb = thisTrialsLoop2.rgb)
        if thisTrialsLoop2 != None:
            for paramName in thisTrialsLoop2.keys():
                exec(paramName + '= thisTrialsLoop2.' + paramName)
        
        #------Prepare to start Routine "block2Trials"-------
        t = 0
        block2TrialsClock.reset()  # clock 
        frameN = -1
        # update component parameters for each repeat
        labelStimulusBlock2.setText(label)
        targetStimulus2.setText(target)
        response2 = event.BuilderKeyResponse()  # create an object of type KeyResponse
        response2.status = NOT_STARTED
        incorrectResponse2 = event.BuilderKeyResponse()  # create an object of type KeyResponse
        incorrectResponse2.status = NOT_STARTED
        responseOption1Incon.setText(responseOption1)
        responseOption2Incon.setText(responseOption2)
        trialTypeIncon.setText(trialType)
        
        # keep track of which components have finished
        block2TrialsComponents = []
        block2TrialsComponents.append(labelStimulusBlock2)
        block2TrialsComponents.append(targetStimulus2)
        block2TrialsComponents.append(response2)
        block2TrialsComponents.append(incorrectResponse2)
        block2TrialsComponents.append(responseOption1Incon)
        block2TrialsComponents.append(responseOption2Incon)
        block2TrialsComponents.append(trialTypeIncon)
        block2TrialsComponents.append(inconAccuracyFeedback)
        for thisComponent in block2TrialsComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        #-------Start Routine "block2Trials"-------
        continueRoutine = True
        while continueRoutine:
            # get current time
            t = block2TrialsClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *labelStimulusBlock2* updates
            if t >= 0.4 and labelStimulusBlock2.status == NOT_STARTED:
                # keep track of start time/frame for later
                labelStimulusBlock2.tStart = t  # underestimates by a little under one frame
                labelStimulusBlock2.frameNStart = frameN  # exact frame index
                labelStimulusBlock2.setAutoDraw(True)
            
            # *targetStimulus2* updates
            if t >= 0.4 and targetStimulus2.status == NOT_STARTED:
                # keep track of start time/frame for later
                targetStimulus2.tStart = t  # underestimates by a little under one frame
                targetStimulus2.frameNStart = frameN  # exact frame index
                targetStimulus2.setAutoDraw(True)
            
            # *response2* updates
            if t >= 0.4 and response2.status == NOT_STARTED:
                # keep track of start time/frame for later
                response2.tStart = t  # underestimates by a little under one frame
                response2.frameNStart = frameN  # exact frame index
                response2.status = STARTED
                # AllowedKeys looks like a variable named `allowAns2`
                if not 'allowAns2' in locals():
                    logging.error('AllowedKeys variable `allowAns2` is not defined.')
                    core.quit()
                if not type(allowAns2) in [list, tuple, np.ndarray]:
                    if not isinstance(allowAns2, basestring):
                        logging.error('AllowedKeys variable `allowAns2` is not string- or list-like.')
                        core.quit()
                    elif not ',' in allowAns2: allowAns2 = (allowAns2,)
                    else:  allowAns2 = eval(allowAns2)
                # keyboard checking is just starting
                response2.clock.reset()  # now t=0
                event.clearEvents(eventType='keyboard')
            if response2.status == STARTED:
                theseKeys = event.getKeys(keyList=list(allowAns2))
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    if response2.keys == []:  # then this was the first keypress
                        response2.keys = theseKeys[0]  # just the first key pressed
                        response2.rt = response2.clock.getTime()
                        # was this 'correct'?
                        if (response2.keys == str(correctAns2)) or (response2.keys == correctAns2):
                            response2.corr = 1
                        else:
                            response2.corr = 0
                        # a response ends the routine
                        continueRoutine = False
            
            # *incorrectResponse2* updates
            if t >= 0.4 and incorrectResponse2.status == NOT_STARTED:
                # keep track of start time/frame for later
                incorrectResponse2.tStart = t  # underestimates by a little under one frame
                incorrectResponse2.frameNStart = frameN  # exact frame index
                incorrectResponse2.status = STARTED
                # AllowedKeys looks like a variable named `allowAns1`
                if not 'allowAns1' in locals():
                    logging.error('AllowedKeys variable `allowAns1` is not defined.')
                    core.quit()
                if not type(allowAns1) in [list, tuple, np.ndarray]:
                    if not isinstance(allowAns1, basestring):
                        logging.error('AllowedKeys variable `allowAns1` is not string- or list-like.')
                        core.quit()
                    elif not ',' in allowAns1: allowAns1 = (allowAns1,)
                    else:  allowAns1 = eval(allowAns1)
                # keyboard checking is just starting
                incorrectResponse2.clock.reset()  # now t=0
                event.clearEvents(eventType='keyboard')
            if incorrectResponse2.status == STARTED:
                theseKeys = event.getKeys(keyList=list(allowAns1))
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    if incorrectResponse2.keys == []:  # then this was the first keypress
                        incorrectResponse2.keys = theseKeys[0]  # just the first key pressed
                        incorrectResponse2.rt = incorrectResponse2.clock.getTime()
                        # was this 'correct'?
                        if (incorrectResponse2.keys == str(correctAns1)) or (incorrectResponse2.keys == correctAns1):
                            incorrectResponse2.corr = 1
                        else:
                            incorrectResponse2.corr = 0
            
            # *responseOption1Incon* updates
            if t >= 0 and responseOption1Incon.status == NOT_STARTED:
                # keep track of start time/frame for later
                responseOption1Incon.tStart = t  # underestimates by a little under one frame
                responseOption1Incon.frameNStart = frameN  # exact frame index
                responseOption1Incon.setAutoDraw(True)
            
            # *responseOption2Incon* updates
            if t >= 0 and responseOption2Incon.status == NOT_STARTED:
                # keep track of start time/frame for later
                responseOption2Incon.tStart = t  # underestimates by a little under one frame
                responseOption2Incon.frameNStart = frameN  # exact frame index
                responseOption2Incon.setAutoDraw(True)
            
            # *trialTypeIncon* updates
            if t >= 0.4 and trialTypeIncon.status == NOT_STARTED:
                # keep track of start time/frame for later
                trialTypeIncon.tStart = t  # underestimates by a little under one frame
                trialTypeIncon.frameNStart = frameN  # exact frame index
                trialTypeIncon.setAutoDraw(True)
            if trialTypeIncon.status == STARTED and t >= (0.4 + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
                trialTypeIncon.setAutoDraw(False)
            if len(incorrectResponse2.keys)<1:
                msg2=""
            else:
                msg2="X"
            
            # *inconAccuracyFeedback* updates
            if t >= 0.4 and inconAccuracyFeedback.status == NOT_STARTED:
                # keep track of start time/frame for later
                inconAccuracyFeedback.tStart = t  # underestimates by a little under one frame
                inconAccuracyFeedback.frameNStart = frameN  # exact frame index
                inconAccuracyFeedback.setAutoDraw(True)
            if inconAccuracyFeedback.status == STARTED:  # only update if being drawn
                inconAccuracyFeedback.setText(msg2, log=False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in block2TrialsComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        #-------Ending Routine "block2Trials"-------
        for thisComponent in block2TrialsComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if response2.keys in ['', [], None]:  # No response was made
           response2.keys=None
           # was no response the correct answer?!
           if str(correctAns2).lower() == 'none': response2.corr = 1  # correct non-response
           else: response2.corr = 0  # failed to respond (incorrectly)
        # store data for trialsLoop2 (TrialHandler)
        trialsLoop2.addData('response2.keys',response2.keys)
        trialsLoop2.addData('response2.corr', response2.corr)
        if response2.keys != None:  # we had a response
            trialsLoop2.addData('response2.rt', response2.rt)
        # check responses
        if incorrectResponse2.keys in ['', [], None]:  # No response was made
           incorrectResponse2.keys=None
           # was no response the correct answer?!
           if str(correctAns1).lower() == 'none': incorrectResponse2.corr = 1  # correct non-response
           else: incorrectResponse2.corr = 0  # failed to respond (incorrectly)
        # store data for trialsLoop2 (TrialHandler)
        trialsLoop2.addData('incorrectResponse2.keys',incorrectResponse2.keys)
        trialsLoop2.addData('incorrectResponse2.corr', incorrectResponse2.corr)
        if incorrectResponse2.keys != None:  # we had a response
            trialsLoop2.addData('incorrectResponse2.rt', incorrectResponse2.rt)
        
        # the Routine "block2Trials" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1 repeats of 'trialsLoop2'
    
    
    #------Prepare to start Routine "feedbackBlock2Prac"-------
    t = 0
    feedbackBlock2PracClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    nCorrLoop2Prac = (float(trialsLoop2.data['response2.corr'].count()) - float(trialsLoop2.data['incorrectResponse2.corr'].sum())) /  float(trialsLoop2.data['response2.corr'].count()) * 100 #count the number of 'correct' correctIncon trials (which actually equals the number of trials, as all must be correct to progress). Take away the number of 'correct' incorrectIncon trials to find real proportion of truly correct trials. Divide by total number of trials and multiply by 100. 
    medianRtLoop2Prac = np.median(trialsLoop2.data['response2.rt'])
    msg2 = "%i %s" %(nCorrLoop2Prac, percentCorrect) #percentCorrect is a variable pulled from excel sheet 'blocks'
    msg2_2 = "%.2f %s" %(medianRtLoop2Prac, seconds) #same as above
    text_10.setText(msg2)
    key_resp_11 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    key_resp_11.status = NOT_STARTED
    text_33.setText(space)
    text_34.setText(msg2_2)
    accuracyMessageIncon_2.setText(accuracy)
    speedMessageIncon_2.setText(speed)
    aimAccuracyAndLatencyIncon_2.setText(aim)
    # keep track of which components have finished
    feedbackBlock2PracComponents = []
    feedbackBlock2PracComponents.append(text_10)
    feedbackBlock2PracComponents.append(key_resp_11)
    feedbackBlock2PracComponents.append(text_33)
    feedbackBlock2PracComponents.append(text_34)
    feedbackBlock2PracComponents.append(accuracyMessageIncon_2)
    feedbackBlock2PracComponents.append(speedMessageIncon_2)
    feedbackBlock2PracComponents.append(aimAccuracyAndLatencyIncon_2)
    for thisComponent in feedbackBlock2PracComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "feedbackBlock2Prac"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = feedbackBlock2PracClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # *text_10* updates
        if t >= 0.4 and text_10.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_10.tStart = t  # underestimates by a little under one frame
            text_10.frameNStart = frameN  # exact frame index
            text_10.setAutoDraw(True)
        
        # *key_resp_11* updates
        if t >= .4 and key_resp_11.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_11.tStart = t  # underestimates by a little under one frame
            key_resp_11.frameNStart = frameN  # exact frame index
            key_resp_11.status = STARTED
            # keyboard checking is just starting
            key_resp_11.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if key_resp_11.status == STARTED:
            theseKeys = event.getKeys(keyList=['d', 'k'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                key_resp_11.keys = theseKeys[-1]  # just the last key pressed
                key_resp_11.rt = key_resp_11.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        # *text_33* updates
        if t >= .4 and text_33.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_33.tStart = t  # underestimates by a little under one frame
            text_33.frameNStart = frameN  # exact frame index
            text_33.setAutoDraw(True)
        
        # *text_34* updates
        if t >= 0.4 and text_34.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_34.tStart = t  # underestimates by a little under one frame
            text_34.frameNStart = frameN  # exact frame index
            text_34.setAutoDraw(True)
        
        # *accuracyMessageIncon_2* updates
        if t >= 0.4 and accuracyMessageIncon_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            accuracyMessageIncon_2.tStart = t  # underestimates by a little under one frame
            accuracyMessageIncon_2.frameNStart = frameN  # exact frame index
            accuracyMessageIncon_2.setAutoDraw(True)
        
        # *speedMessageIncon_2* updates
        if t >= 0.4 and speedMessageIncon_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            speedMessageIncon_2.tStart = t  # underestimates by a little under one frame
            speedMessageIncon_2.frameNStart = frameN  # exact frame index
            speedMessageIncon_2.setAutoDraw(True)
        
        # *aimAccuracyAndLatencyIncon_2* updates
        if t >= 0.4 and aimAccuracyAndLatencyIncon_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            aimAccuracyAndLatencyIncon_2.tStart = t  # underestimates by a little under one frame
            aimAccuracyAndLatencyIncon_2.frameNStart = frameN  # exact frame index
            aimAccuracyAndLatencyIncon_2.setAutoDraw(True)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feedbackBlock2PracComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "feedbackBlock2Prac"-------
    for thisComponent in feedbackBlock2PracComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    if nCorrLoop1Prac >= accuracyCriterion and nCorrLoop2Prac >= accuracyCriterion and medianRtLoop1Prac <= latencyCriterion and medianRtLoop2Prac <= latencyCriterion: #latencyCriterion and accuracyCriterion are variables pulled from the 'blocks' excel sheets
    #    endMsg='Finished Practice'
        pracBlocks.finished=True
        completeTestBlocks=1
    # check responses
    if key_resp_11.keys in ['', [], None]:  # No response was made
       key_resp_11.keys=None
    # store data for pracBlocks (TrialHandler)
    pracBlocks.addData('key_resp_11.keys',key_resp_11.keys)
    if key_resp_11.keys != None:  # we had a response
        pracBlocks.addData('key_resp_11.rt', key_resp_11.rt)
    # the Routine "feedbackBlock2Prac" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed 3 repeats of 'pracBlocks'


# set up handler to look after randomisation of conditions etc
completeTestBlocksConditional = data.TrialHandler(nReps=completeTestBlocks, method='sequential', 
    extraInfo=expInfo, originPath=None,
    trialList=[None],
    seed=None, name='completeTestBlocksConditional')
thisExp.addLoop(completeTestBlocksConditional)  # add the loop to the experiment
thisCompleteTestBlocksConditional = completeTestBlocksConditional.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisCompleteTestBlocksConditional.rgb)
if thisCompleteTestBlocksConditional != None:
    for paramName in thisCompleteTestBlocksConditional.keys():
        exec(paramName + '= thisCompleteTestBlocksConditional.' + paramName)

for thisCompleteTestBlocksConditional in completeTestBlocksConditional:
    currentLoop = completeTestBlocksConditional
    # abbreviate parameter names if possible (e.g. rgb = thisCompleteTestBlocksConditional.rgb)
    if thisCompleteTestBlocksConditional != None:
        for paramName in thisCompleteTestBlocksConditional.keys():
            exec(paramName + '= thisCompleteTestBlocksConditional.' + paramName)
    
    # set up handler to look after randomisation of conditions etc
    testBlocks = data.TrialHandler(nReps=3, method='sequential', 
        extraInfo=expInfo, originPath=None,
        trialList=data.importConditions('Blocks.xlsx'),
        seed=None, name='testBlocks')
    thisExp.addLoop(testBlocks)  # add the loop to the experiment
    thisTestBlock = testBlocks.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb=thisTestBlock.rgb)
    if thisTestBlock != None:
        for paramName in thisTestBlock.keys():
            exec(paramName + '= thisTestBlock.' + paramName)
    
    for thisTestBlock in testBlocks:
        currentLoop = testBlocks
        # abbreviate parameter names if possible (e.g. rgb = thisTestBlock.rgb)
        if thisTestBlock != None:
            for paramName in thisTestBlock.keys():
                exec(paramName + '= thisTestBlock.' + paramName)
        
        #------Prepare to start Routine "instructTest"-------
        t = 0
        instructTestClock.reset()  # clock 
        frameN = -1
        # update component parameters for each repeat
        instrTextCon_2.setText(rule1)
        ready_2 = event.BuilderKeyResponse()  # create an object of type KeyResponse
        ready_2.status = NOT_STARTED
        text_18.setText(space)
        # keep track of which components have finished
        instructTestComponents = []
        instructTestComponents.append(instrTextCon_2)
        instructTestComponents.append(ready_2)
        instructTestComponents.append(text_18)
        for thisComponent in instructTestComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        #-------Start Routine "instructTest"-------
        continueRoutine = True
        while continueRoutine:
            # get current time
            t = instructTestClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *instrTextCon_2* updates
            if t >= 0.4 and instrTextCon_2.status == NOT_STARTED:
                # keep track of start time/frame for later
                instrTextCon_2.tStart = t  # underestimates by a little under one frame
                instrTextCon_2.frameNStart = frameN  # exact frame index
                instrTextCon_2.setAutoDraw(True)
            
            # *ready_2* updates
            if t >= .4 and ready_2.status == NOT_STARTED:
                # keep track of start time/frame for later
                ready_2.tStart = t  # underestimates by a little under one frame
                ready_2.frameNStart = frameN  # exact frame index
                ready_2.status = STARTED
                # keyboard checking is just starting
                event.clearEvents(eventType='keyboard')
            if ready_2.status == STARTED:
                theseKeys = event.getKeys(keyList=['d', 'k'])
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    # a response ends the routine
                    continueRoutine = False
            
            # *text_18* updates
            if t >= .4 and text_18.status == NOT_STARTED:
                # keep track of start time/frame for later
                text_18.tStart = t  # underestimates by a little under one frame
                text_18.frameNStart = frameN  # exact frame index
                text_18.setAutoDraw(True)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in instructTestComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        #-------Ending Routine "instructTest"-------
        for thisComponent in instructTestComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "instructTest" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        trialsTestLoop1 = data.TrialHandler(nReps=1, method='random', 
            extraInfo=expInfo, originPath=None,
            trialList=data.importConditions('stimuli.xlsx'),
            seed=None, name='trialsTestLoop1')
        thisExp.addLoop(trialsTestLoop1)  # add the loop to the experiment
        thisTrialsTestLoop1 = trialsTestLoop1.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb=thisTrialsTestLoop1.rgb)
        if thisTrialsTestLoop1 != None:
            for paramName in thisTrialsTestLoop1.keys():
                exec(paramName + '= thisTrialsTestLoop1.' + paramName)
        
        for thisTrialsTestLoop1 in trialsTestLoop1:
            currentLoop = trialsTestLoop1
            # abbreviate parameter names if possible (e.g. rgb = thisTrialsTestLoop1.rgb)
            if thisTrialsTestLoop1 != None:
                for paramName in thisTrialsTestLoop1.keys():
                    exec(paramName + '= thisTrialsTestLoop1.' + paramName)
            
            #------Prepare to start Routine "block1Trials"-------
            t = 0
            block1TrialsClock.reset()  # clock 
            frameN = -1
            # update component parameters for each repeat
            labelStimulusBlock1.setText(label)
            targetStimulus1.setText(target)
            response1 = event.BuilderKeyResponse()  # create an object of type KeyResponse
            response1.status = NOT_STARTED
            incorrectResponse1 = event.BuilderKeyResponse()  # create an object of type KeyResponse
            incorrectResponse1.status = NOT_STARTED
            responseOption1Con.setText(responseOption1)
            responseOption2Con.setText(responseOption2)
            trialTypeCon.setText(trialType)
            
            # keep track of which components have finished
            block1TrialsComponents = []
            block1TrialsComponents.append(labelStimulusBlock1)
            block1TrialsComponents.append(targetStimulus1)
            block1TrialsComponents.append(response1)
            block1TrialsComponents.append(incorrectResponse1)
            block1TrialsComponents.append(responseOption1Con)
            block1TrialsComponents.append(responseOption2Con)
            block1TrialsComponents.append(trialTypeCon)
            block1TrialsComponents.append(conAccuracyFeedback)
            for thisComponent in block1TrialsComponents:
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            
            #-------Start Routine "block1Trials"-------
            continueRoutine = True
            while continueRoutine:
                # get current time
                t = block1TrialsClock.getTime()
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *labelStimulusBlock1* updates
                if t >= 0.4 and labelStimulusBlock1.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    labelStimulusBlock1.tStart = t  # underestimates by a little under one frame
                    labelStimulusBlock1.frameNStart = frameN  # exact frame index
                    labelStimulusBlock1.setAutoDraw(True)
                
                # *targetStimulus1* updates
                if t >= 0.4 and targetStimulus1.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    targetStimulus1.tStart = t  # underestimates by a little under one frame
                    targetStimulus1.frameNStart = frameN  # exact frame index
                    targetStimulus1.setAutoDraw(True)
                
                # *response1* updates
                if t >= 0.4 and response1.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    response1.tStart = t  # underestimates by a little under one frame
                    response1.frameNStart = frameN  # exact frame index
                    response1.status = STARTED
                    # AllowedKeys looks like a variable named `allowAns1`
                    if not 'allowAns1' in locals():
                        logging.error('AllowedKeys variable `allowAns1` is not defined.')
                        core.quit()
                    if not type(allowAns1) in [list, tuple, np.ndarray]:
                        if not isinstance(allowAns1, basestring):
                            logging.error('AllowedKeys variable `allowAns1` is not string- or list-like.')
                            core.quit()
                        elif not ',' in allowAns1: allowAns1 = (allowAns1,)
                        else:  allowAns1 = eval(allowAns1)
                    # keyboard checking is just starting
                    response1.clock.reset()  # now t=0
                    event.clearEvents(eventType='keyboard')
                if response1.status == STARTED:
                    theseKeys = event.getKeys(keyList=list(allowAns1))
                    
                    # check for quit:
                    if "escape" in theseKeys:
                        endExpNow = True
                    if len(theseKeys) > 0:  # at least one key was pressed
                        if response1.keys == []:  # then this was the first keypress
                            response1.keys = theseKeys[0]  # just the first key pressed
                            response1.rt = response1.clock.getTime()
                            # was this 'correct'?
                            if (response1.keys == str(correctAns1)) or (response1.keys == correctAns1):
                                response1.corr = 1
                            else:
                                response1.corr = 0
                            # a response ends the routine
                            continueRoutine = False
                
                # *incorrectResponse1* updates
                if t >= 0.4 and incorrectResponse1.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    incorrectResponse1.tStart = t  # underestimates by a little under one frame
                    incorrectResponse1.frameNStart = frameN  # exact frame index
                    incorrectResponse1.status = STARTED
                    # AllowedKeys looks like a variable named `allowAns2`
                    if not 'allowAns2' in locals():
                        logging.error('AllowedKeys variable `allowAns2` is not defined.')
                        core.quit()
                    if not type(allowAns2) in [list, tuple, np.ndarray]:
                        if not isinstance(allowAns2, basestring):
                            logging.error('AllowedKeys variable `allowAns2` is not string- or list-like.')
                            core.quit()
                        elif not ',' in allowAns2: allowAns2 = (allowAns2,)
                        else:  allowAns2 = eval(allowAns2)
                    # keyboard checking is just starting
                    incorrectResponse1.clock.reset()  # now t=0
                    event.clearEvents(eventType='keyboard')
                if incorrectResponse1.status == STARTED:
                    theseKeys = event.getKeys(keyList=list(allowAns2))
                    
                    # check for quit:
                    if "escape" in theseKeys:
                        endExpNow = True
                    if len(theseKeys) > 0:  # at least one key was pressed
                        if incorrectResponse1.keys == []:  # then this was the first keypress
                            incorrectResponse1.keys = theseKeys[0]  # just the first key pressed
                            incorrectResponse1.rt = incorrectResponse1.clock.getTime()
                            # was this 'correct'?
                            if (incorrectResponse1.keys == str(correctAns2)) or (incorrectResponse1.keys == correctAns2):
                                incorrectResponse1.corr = 1
                            else:
                                incorrectResponse1.corr = 0
                
                # *responseOption1Con* updates
                if t >= 0 and responseOption1Con.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    responseOption1Con.tStart = t  # underestimates by a little under one frame
                    responseOption1Con.frameNStart = frameN  # exact frame index
                    responseOption1Con.setAutoDraw(True)
                
                # *responseOption2Con* updates
                if t >= 0 and responseOption2Con.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    responseOption2Con.tStart = t  # underestimates by a little under one frame
                    responseOption2Con.frameNStart = frameN  # exact frame index
                    responseOption2Con.setAutoDraw(True)
                
                # *trialTypeCon* updates
                if t >= 0.4 and trialTypeCon.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    trialTypeCon.tStart = t  # underestimates by a little under one frame
                    trialTypeCon.frameNStart = frameN  # exact frame index
                    trialTypeCon.setAutoDraw(True)
                if trialTypeCon.status == STARTED and t >= (0.4 + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
                    trialTypeCon.setAutoDraw(False)
                if len(incorrectResponse1.keys)<1:
                    msg=""
                else:
                    msg="X"
                
                # *conAccuracyFeedback* updates
                if t >= 0.4 and conAccuracyFeedback.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    conAccuracyFeedback.tStart = t  # underestimates by a little under one frame
                    conAccuracyFeedback.frameNStart = frameN  # exact frame index
                    conAccuracyFeedback.setAutoDraw(True)
                if conAccuracyFeedback.status == STARTED:  # only update if being drawn
                    conAccuracyFeedback.setText(msg, log=False)
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in block1TrialsComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # check for quit (the Esc key)
                if endExpNow or event.getKeys(keyList=["escape"]):
                    core.quit()
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            #-------Ending Routine "block1Trials"-------
            for thisComponent in block1TrialsComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # check responses
            if response1.keys in ['', [], None]:  # No response was made
               response1.keys=None
               # was no response the correct answer?!
               if str(correctAns1).lower() == 'none': response1.corr = 1  # correct non-response
               else: response1.corr = 0  # failed to respond (incorrectly)
            # store data for trialsTestLoop1 (TrialHandler)
            trialsTestLoop1.addData('response1.keys',response1.keys)
            trialsTestLoop1.addData('response1.corr', response1.corr)
            if response1.keys != None:  # we had a response
                trialsTestLoop1.addData('response1.rt', response1.rt)
            # check responses
            if incorrectResponse1.keys in ['', [], None]:  # No response was made
               incorrectResponse1.keys=None
               # was no response the correct answer?!
               if str(correctAns2).lower() == 'none': incorrectResponse1.corr = 1  # correct non-response
               else: incorrectResponse1.corr = 0  # failed to respond (incorrectly)
            # store data for trialsTestLoop1 (TrialHandler)
            trialsTestLoop1.addData('incorrectResponse1.keys',incorrectResponse1.keys)
            trialsTestLoop1.addData('incorrectResponse1.corr', incorrectResponse1.corr)
            if incorrectResponse1.keys != None:  # we had a response
                trialsTestLoop1.addData('incorrectResponse1.rt', incorrectResponse1.rt)
            
            # the Routine "block1Trials" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed 1 repeats of 'trialsTestLoop1'
        
        
        #------Prepare to start Routine "feedbackBlock1Test"-------
        t = 0
        feedbackBlock1TestClock.reset()  # clock 
        frameN = -1
        # update component parameters for each repeat
        nCorrLoop1Test = (float(trialsTestLoop1.data['response1.corr'].count()) - float(trialsTestLoop1.data['incorrectResponse1.corr'].sum())) /  float(trialsTestLoop1.data['response1.corr'].count()) * 100 #count the number of 'correct' correctIncon trials (which actually equals the number of trials, as all must be correct to progress). Take away the number of 'correct' incorrectIncon trials to find real proportion of truly correct trials. Divide by total number of trials and multiply by 100. 
        medianRtLoop1Test = np.median(trialsTestLoop1.data['response1.rt'])
        msg1 = "%i %s" %(nCorrLoop1Test, percentCorrect) #percentCorrect is a variable pulled from excel sheet 'blocks'
        msg1_2 = "%.2f %s" %(medianRtLoop1Test, seconds) #same as above
        text_25.setText(msg1)
        key_resp_9 = event.BuilderKeyResponse()  # create an object of type KeyResponse
        key_resp_9.status = NOT_STARTED
        text_26.setText(space)
        text_27.setText(msg1_2)
        accuracyMessage_2.setText(accuracy)
        speedMessage_2.setText(speed)
        aimAccuracyAndLatency_2.setText(aim)
        # keep track of which components have finished
        feedbackBlock1TestComponents = []
        feedbackBlock1TestComponents.append(text_25)
        feedbackBlock1TestComponents.append(key_resp_9)
        feedbackBlock1TestComponents.append(text_26)
        feedbackBlock1TestComponents.append(text_27)
        feedbackBlock1TestComponents.append(accuracyMessage_2)
        feedbackBlock1TestComponents.append(speedMessage_2)
        feedbackBlock1TestComponents.append(aimAccuracyAndLatency_2)
        for thisComponent in feedbackBlock1TestComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        #-------Start Routine "feedbackBlock1Test"-------
        continueRoutine = True
        while continueRoutine:
            # get current time
            t = feedbackBlock1TestClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            
            # *text_25* updates
            if t >= 0.4 and text_25.status == NOT_STARTED:
                # keep track of start time/frame for later
                text_25.tStart = t  # underestimates by a little under one frame
                text_25.frameNStart = frameN  # exact frame index
                text_25.setAutoDraw(True)
            
            # *key_resp_9* updates
            if t >= .4 and key_resp_9.status == NOT_STARTED:
                # keep track of start time/frame for later
                key_resp_9.tStart = t  # underestimates by a little under one frame
                key_resp_9.frameNStart = frameN  # exact frame index
                key_resp_9.status = STARTED
                # keyboard checking is just starting
                key_resp_9.clock.reset()  # now t=0
                event.clearEvents(eventType='keyboard')
            if key_resp_9.status == STARTED:
                theseKeys = event.getKeys(keyList=['d', 'k'])
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    key_resp_9.keys = theseKeys[-1]  # just the last key pressed
                    key_resp_9.rt = key_resp_9.clock.getTime()
                    # a response ends the routine
                    continueRoutine = False
            
            # *text_26* updates
            if t >= .4 and text_26.status == NOT_STARTED:
                # keep track of start time/frame for later
                text_26.tStart = t  # underestimates by a little under one frame
                text_26.frameNStart = frameN  # exact frame index
                text_26.setAutoDraw(True)
            
            # *text_27* updates
            if t >= 0.4 and text_27.status == NOT_STARTED:
                # keep track of start time/frame for later
                text_27.tStart = t  # underestimates by a little under one frame
                text_27.frameNStart = frameN  # exact frame index
                text_27.setAutoDraw(True)
            
            # *accuracyMessage_2* updates
            if t >= 0.4 and accuracyMessage_2.status == NOT_STARTED:
                # keep track of start time/frame for later
                accuracyMessage_2.tStart = t  # underestimates by a little under one frame
                accuracyMessage_2.frameNStart = frameN  # exact frame index
                accuracyMessage_2.setAutoDraw(True)
            
            # *speedMessage_2* updates
            if t >= 0.4 and speedMessage_2.status == NOT_STARTED:
                # keep track of start time/frame for later
                speedMessage_2.tStart = t  # underestimates by a little under one frame
                speedMessage_2.frameNStart = frameN  # exact frame index
                speedMessage_2.setAutoDraw(True)
            
            # *aimAccuracyAndLatency_2* updates
            if t >= 0.4 and aimAccuracyAndLatency_2.status == NOT_STARTED:
                # keep track of start time/frame for later
                aimAccuracyAndLatency_2.tStart = t  # underestimates by a little under one frame
                aimAccuracyAndLatency_2.frameNStart = frameN  # exact frame index
                aimAccuracyAndLatency_2.setAutoDraw(True)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in feedbackBlock1TestComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        #-------Ending Routine "feedbackBlock1Test"-------
        for thisComponent in feedbackBlock1TestComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        # check responses
        if key_resp_9.keys in ['', [], None]:  # No response was made
           key_resp_9.keys=None
        # store data for testBlocks (TrialHandler)
        testBlocks.addData('key_resp_9.keys',key_resp_9.keys)
        if key_resp_9.keys != None:  # we had a response
            testBlocks.addData('key_resp_9.rt', key_resp_9.rt)
        # the Routine "feedbackBlock1Test" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        #------Prepare to start Routine "instructTest2"-------
        t = 0
        instructTest2Clock.reset()  # clock 
        frameN = -1
        # update component parameters for each repeat
        instrTextIncon_3.setText(rule2)
        key_resp_4 = event.BuilderKeyResponse()  # create an object of type KeyResponse
        key_resp_4.status = NOT_STARTED
        text_13.setText(space)
        # keep track of which components have finished
        instructTest2Components = []
        instructTest2Components.append(instrTextIncon_3)
        instructTest2Components.append(key_resp_4)
        instructTest2Components.append(text_13)
        for thisComponent in instructTest2Components:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        #-------Start Routine "instructTest2"-------
        continueRoutine = True
        while continueRoutine:
            # get current time
            t = instructTest2Clock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *instrTextIncon_3* updates
            if t >= 0.4 and instrTextIncon_3.status == NOT_STARTED:
                # keep track of start time/frame for later
                instrTextIncon_3.tStart = t  # underestimates by a little under one frame
                instrTextIncon_3.frameNStart = frameN  # exact frame index
                instrTextIncon_3.setAutoDraw(True)
            
            # *key_resp_4* updates
            if t >= .4 and key_resp_4.status == NOT_STARTED:
                # keep track of start time/frame for later
                key_resp_4.tStart = t  # underestimates by a little under one frame
                key_resp_4.frameNStart = frameN  # exact frame index
                key_resp_4.status = STARTED
                # keyboard checking is just starting
                key_resp_4.clock.reset()  # now t=0
                event.clearEvents(eventType='keyboard')
            if key_resp_4.status == STARTED:
                theseKeys = event.getKeys(keyList=['d', 'k'])
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    key_resp_4.keys = theseKeys[-1]  # just the last key pressed
                    key_resp_4.rt = key_resp_4.clock.getTime()
                    # a response ends the routine
                    continueRoutine = False
            
            # *text_13* updates
            if t >= .4 and text_13.status == NOT_STARTED:
                # keep track of start time/frame for later
                text_13.tStart = t  # underestimates by a little under one frame
                text_13.frameNStart = frameN  # exact frame index
                text_13.setAutoDraw(True)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in instructTest2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        #-------Ending Routine "instructTest2"-------
        for thisComponent in instructTest2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if key_resp_4.keys in ['', [], None]:  # No response was made
           key_resp_4.keys=None
        # store data for testBlocks (TrialHandler)
        testBlocks.addData('key_resp_4.keys',key_resp_4.keys)
        if key_resp_4.keys != None:  # we had a response
            testBlocks.addData('key_resp_4.rt', key_resp_4.rt)
        # the Routine "instructTest2" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        trialsTestLoop2 = data.TrialHandler(nReps=1, method='random', 
            extraInfo=expInfo, originPath=None,
            trialList=data.importConditions('stimuli.xlsx'),
            seed=None, name='trialsTestLoop2')
        thisExp.addLoop(trialsTestLoop2)  # add the loop to the experiment
        thisTrialsTestLoop2 = trialsTestLoop2.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb=thisTrialsTestLoop2.rgb)
        if thisTrialsTestLoop2 != None:
            for paramName in thisTrialsTestLoop2.keys():
                exec(paramName + '= thisTrialsTestLoop2.' + paramName)
        
        for thisTrialsTestLoop2 in trialsTestLoop2:
            currentLoop = trialsTestLoop2
            # abbreviate parameter names if possible (e.g. rgb = thisTrialsTestLoop2.rgb)
            if thisTrialsTestLoop2 != None:
                for paramName in thisTrialsTestLoop2.keys():
                    exec(paramName + '= thisTrialsTestLoop2.' + paramName)
            
            #------Prepare to start Routine "block2Trials"-------
            t = 0
            block2TrialsClock.reset()  # clock 
            frameN = -1
            # update component parameters for each repeat
            labelStimulusBlock2.setText(label)
            targetStimulus2.setText(target)
            response2 = event.BuilderKeyResponse()  # create an object of type KeyResponse
            response2.status = NOT_STARTED
            incorrectResponse2 = event.BuilderKeyResponse()  # create an object of type KeyResponse
            incorrectResponse2.status = NOT_STARTED
            responseOption1Incon.setText(responseOption1)
            responseOption2Incon.setText(responseOption2)
            trialTypeIncon.setText(trialType)
            
            # keep track of which components have finished
            block2TrialsComponents = []
            block2TrialsComponents.append(labelStimulusBlock2)
            block2TrialsComponents.append(targetStimulus2)
            block2TrialsComponents.append(response2)
            block2TrialsComponents.append(incorrectResponse2)
            block2TrialsComponents.append(responseOption1Incon)
            block2TrialsComponents.append(responseOption2Incon)
            block2TrialsComponents.append(trialTypeIncon)
            block2TrialsComponents.append(inconAccuracyFeedback)
            for thisComponent in block2TrialsComponents:
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            
            #-------Start Routine "block2Trials"-------
            continueRoutine = True
            while continueRoutine:
                # get current time
                t = block2TrialsClock.getTime()
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *labelStimulusBlock2* updates
                if t >= 0.4 and labelStimulusBlock2.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    labelStimulusBlock2.tStart = t  # underestimates by a little under one frame
                    labelStimulusBlock2.frameNStart = frameN  # exact frame index
                    labelStimulusBlock2.setAutoDraw(True)
                
                # *targetStimulus2* updates
                if t >= 0.4 and targetStimulus2.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    targetStimulus2.tStart = t  # underestimates by a little under one frame
                    targetStimulus2.frameNStart = frameN  # exact frame index
                    targetStimulus2.setAutoDraw(True)
                
                # *response2* updates
                if t >= 0.4 and response2.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    response2.tStart = t  # underestimates by a little under one frame
                    response2.frameNStart = frameN  # exact frame index
                    response2.status = STARTED
                    # AllowedKeys looks like a variable named `allowAns2`
                    if not 'allowAns2' in locals():
                        logging.error('AllowedKeys variable `allowAns2` is not defined.')
                        core.quit()
                    if not type(allowAns2) in [list, tuple, np.ndarray]:
                        if not isinstance(allowAns2, basestring):
                            logging.error('AllowedKeys variable `allowAns2` is not string- or list-like.')
                            core.quit()
                        elif not ',' in allowAns2: allowAns2 = (allowAns2,)
                        else:  allowAns2 = eval(allowAns2)
                    # keyboard checking is just starting
                    response2.clock.reset()  # now t=0
                    event.clearEvents(eventType='keyboard')
                if response2.status == STARTED:
                    theseKeys = event.getKeys(keyList=list(allowAns2))
                    
                    # check for quit:
                    if "escape" in theseKeys:
                        endExpNow = True
                    if len(theseKeys) > 0:  # at least one key was pressed
                        if response2.keys == []:  # then this was the first keypress
                            response2.keys = theseKeys[0]  # just the first key pressed
                            response2.rt = response2.clock.getTime()
                            # was this 'correct'?
                            if (response2.keys == str(correctAns2)) or (response2.keys == correctAns2):
                                response2.corr = 1
                            else:
                                response2.corr = 0
                            # a response ends the routine
                            continueRoutine = False
                
                # *incorrectResponse2* updates
                if t >= 0.4 and incorrectResponse2.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    incorrectResponse2.tStart = t  # underestimates by a little under one frame
                    incorrectResponse2.frameNStart = frameN  # exact frame index
                    incorrectResponse2.status = STARTED
                    # AllowedKeys looks like a variable named `allowAns1`
                    if not 'allowAns1' in locals():
                        logging.error('AllowedKeys variable `allowAns1` is not defined.')
                        core.quit()
                    if not type(allowAns1) in [list, tuple, np.ndarray]:
                        if not isinstance(allowAns1, basestring):
                            logging.error('AllowedKeys variable `allowAns1` is not string- or list-like.')
                            core.quit()
                        elif not ',' in allowAns1: allowAns1 = (allowAns1,)
                        else:  allowAns1 = eval(allowAns1)
                    # keyboard checking is just starting
                    incorrectResponse2.clock.reset()  # now t=0
                    event.clearEvents(eventType='keyboard')
                if incorrectResponse2.status == STARTED:
                    theseKeys = event.getKeys(keyList=list(allowAns1))
                    
                    # check for quit:
                    if "escape" in theseKeys:
                        endExpNow = True
                    if len(theseKeys) > 0:  # at least one key was pressed
                        if incorrectResponse2.keys == []:  # then this was the first keypress
                            incorrectResponse2.keys = theseKeys[0]  # just the first key pressed
                            incorrectResponse2.rt = incorrectResponse2.clock.getTime()
                            # was this 'correct'?
                            if (incorrectResponse2.keys == str(correctAns1)) or (incorrectResponse2.keys == correctAns1):
                                incorrectResponse2.corr = 1
                            else:
                                incorrectResponse2.corr = 0
                
                # *responseOption1Incon* updates
                if t >= 0 and responseOption1Incon.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    responseOption1Incon.tStart = t  # underestimates by a little under one frame
                    responseOption1Incon.frameNStart = frameN  # exact frame index
                    responseOption1Incon.setAutoDraw(True)
                
                # *responseOption2Incon* updates
                if t >= 0 and responseOption2Incon.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    responseOption2Incon.tStart = t  # underestimates by a little under one frame
                    responseOption2Incon.frameNStart = frameN  # exact frame index
                    responseOption2Incon.setAutoDraw(True)
                
                # *trialTypeIncon* updates
                if t >= 0.4 and trialTypeIncon.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    trialTypeIncon.tStart = t  # underestimates by a little under one frame
                    trialTypeIncon.frameNStart = frameN  # exact frame index
                    trialTypeIncon.setAutoDraw(True)
                if trialTypeIncon.status == STARTED and t >= (0.4 + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
                    trialTypeIncon.setAutoDraw(False)
                if len(incorrectResponse2.keys)<1:
                    msg2=""
                else:
                    msg2="X"
                
                # *inconAccuracyFeedback* updates
                if t >= 0.4 and inconAccuracyFeedback.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    inconAccuracyFeedback.tStart = t  # underestimates by a little under one frame
                    inconAccuracyFeedback.frameNStart = frameN  # exact frame index
                    inconAccuracyFeedback.setAutoDraw(True)
                if inconAccuracyFeedback.status == STARTED:  # only update if being drawn
                    inconAccuracyFeedback.setText(msg2, log=False)
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in block2TrialsComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # check for quit (the Esc key)
                if endExpNow or event.getKeys(keyList=["escape"]):
                    core.quit()
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            #-------Ending Routine "block2Trials"-------
            for thisComponent in block2TrialsComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # check responses
            if response2.keys in ['', [], None]:  # No response was made
               response2.keys=None
               # was no response the correct answer?!
               if str(correctAns2).lower() == 'none': response2.corr = 1  # correct non-response
               else: response2.corr = 0  # failed to respond (incorrectly)
            # store data for trialsTestLoop2 (TrialHandler)
            trialsTestLoop2.addData('response2.keys',response2.keys)
            trialsTestLoop2.addData('response2.corr', response2.corr)
            if response2.keys != None:  # we had a response
                trialsTestLoop2.addData('response2.rt', response2.rt)
            # check responses
            if incorrectResponse2.keys in ['', [], None]:  # No response was made
               incorrectResponse2.keys=None
               # was no response the correct answer?!
               if str(correctAns1).lower() == 'none': incorrectResponse2.corr = 1  # correct non-response
               else: incorrectResponse2.corr = 0  # failed to respond (incorrectly)
            # store data for trialsTestLoop2 (TrialHandler)
            trialsTestLoop2.addData('incorrectResponse2.keys',incorrectResponse2.keys)
            trialsTestLoop2.addData('incorrectResponse2.corr', incorrectResponse2.corr)
            if incorrectResponse2.keys != None:  # we had a response
                trialsTestLoop2.addData('incorrectResponse2.rt', incorrectResponse2.rt)
            
            # the Routine "block2Trials" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed 1 repeats of 'trialsTestLoop2'
        
        
        #------Prepare to start Routine "feedbackBlock2Test"-------
        t = 0
        feedbackBlock2TestClock.reset()  # clock 
        frameN = -1
        # update component parameters for each repeat
        nCorrLoop2Test = (float(trialsTestLoop2.data['response2.corr'].count()) - float(trialsTestLoop2.data['incorrectResponse2.corr'].sum())) /  float(trialsTestLoop2.data['response2.corr'].count()) * 100 #count the number of 'correct' correctIncon trials (which actually equals the number of trials, as all must be correct to progress). Take away the number of 'correct' incorrectIncon trials to find real proportion of truly correct trials. Divide by total number of trials and multiply by 100. 
        medianRtLoop2Test = np.median(trialsTestLoop2.data['response2.rt'])
        msg2 = "%i %s" %(nCorrLoop2Test, percentCorrect) #percentCorrect is a variable pulled from excel sheet 'blocks'
        msg2_2 = "%.2f %s" %(medianRtLoop2Test, seconds) #same as above
        text_22.setText(msg2)
        key_resp_8 = event.BuilderKeyResponse()  # create an object of type KeyResponse
        key_resp_8.status = NOT_STARTED
        text_23.setText(space)
        text_24.setText(msg2_2)
        accuracyMessageTestIncon_2.setText(accuracy)
        speedMessageInconTest_2.setText(speed)
        aimAccuracyAndLatencyInconTest_2.setText(aim)
        # keep track of which components have finished
        feedbackBlock2TestComponents = []
        feedbackBlock2TestComponents.append(text_22)
        feedbackBlock2TestComponents.append(key_resp_8)
        feedbackBlock2TestComponents.append(text_23)
        feedbackBlock2TestComponents.append(text_24)
        feedbackBlock2TestComponents.append(accuracyMessageTestIncon_2)
        feedbackBlock2TestComponents.append(speedMessageInconTest_2)
        feedbackBlock2TestComponents.append(aimAccuracyAndLatencyInconTest_2)
        for thisComponent in feedbackBlock2TestComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        #-------Start Routine "feedbackBlock2Test"-------
        continueRoutine = True
        while continueRoutine:
            # get current time
            t = feedbackBlock2TestClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            
            # *text_22* updates
            if t >= 0.4 and text_22.status == NOT_STARTED:
                # keep track of start time/frame for later
                text_22.tStart = t  # underestimates by a little under one frame
                text_22.frameNStart = frameN  # exact frame index
                text_22.setAutoDraw(True)
            
            # *key_resp_8* updates
            if t >= .4 and key_resp_8.status == NOT_STARTED:
                # keep track of start time/frame for later
                key_resp_8.tStart = t  # underestimates by a little under one frame
                key_resp_8.frameNStart = frameN  # exact frame index
                key_resp_8.status = STARTED
                # keyboard checking is just starting
                key_resp_8.clock.reset()  # now t=0
                event.clearEvents(eventType='keyboard')
            if key_resp_8.status == STARTED:
                theseKeys = event.getKeys(keyList=['d', 'k'])
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    key_resp_8.keys = theseKeys[-1]  # just the last key pressed
                    key_resp_8.rt = key_resp_8.clock.getTime()
                    # a response ends the routine
                    continueRoutine = False
            
            # *text_23* updates
            if t >= .4 and text_23.status == NOT_STARTED:
                # keep track of start time/frame for later
                text_23.tStart = t  # underestimates by a little under one frame
                text_23.frameNStart = frameN  # exact frame index
                text_23.setAutoDraw(True)
            
            # *text_24* updates
            if t >= 0.4 and text_24.status == NOT_STARTED:
                # keep track of start time/frame for later
                text_24.tStart = t  # underestimates by a little under one frame
                text_24.frameNStart = frameN  # exact frame index
                text_24.setAutoDraw(True)
            
            # *accuracyMessageTestIncon_2* updates
            if t >= 0.4 and accuracyMessageTestIncon_2.status == NOT_STARTED:
                # keep track of start time/frame for later
                accuracyMessageTestIncon_2.tStart = t  # underestimates by a little under one frame
                accuracyMessageTestIncon_2.frameNStart = frameN  # exact frame index
                accuracyMessageTestIncon_2.setAutoDraw(True)
            
            # *speedMessageInconTest_2* updates
            if t >= 0.4 and speedMessageInconTest_2.status == NOT_STARTED:
                # keep track of start time/frame for later
                speedMessageInconTest_2.tStart = t  # underestimates by a little under one frame
                speedMessageInconTest_2.frameNStart = frameN  # exact frame index
                speedMessageInconTest_2.setAutoDraw(True)
            
            # *aimAccuracyAndLatencyInconTest_2* updates
            if t >= 0.4 and aimAccuracyAndLatencyInconTest_2.status == NOT_STARTED:
                # keep track of start time/frame for later
                aimAccuracyAndLatencyInconTest_2.tStart = t  # underestimates by a little under one frame
                aimAccuracyAndLatencyInconTest_2.frameNStart = frameN  # exact frame index
                aimAccuracyAndLatencyInconTest_2.setAutoDraw(True)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in feedbackBlock2TestComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        #-------Ending Routine "feedbackBlock2Test"-------
        for thisComponent in feedbackBlock2TestComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        # check responses
        if key_resp_8.keys in ['', [], None]:  # No response was made
           key_resp_8.keys=None
        # store data for testBlocks (TrialHandler)
        testBlocks.addData('key_resp_8.keys',key_resp_8.keys)
        if key_resp_8.keys != None:  # we had a response
            testBlocks.addData('key_resp_8.rt', key_resp_8.rt)
        # the Routine "feedbackBlock2Test" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
    # completed 3 repeats of 'testBlocks'
    
# completed completeTestBlocks repeats of 'completeTestBlocksConditional'


# set up handler to look after randomisation of conditions etc
getThanksStrings = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=None,
    trialList=data.importConditions('instructions.xlsx'),
    seed=None, name='getThanksStrings')
thisExp.addLoop(getThanksStrings)  # add the loop to the experiment
thisGetThanksString = getThanksStrings.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisGetThanksString.rgb)
if thisGetThanksString != None:
    for paramName in thisGetThanksString.keys():
        exec(paramName + '= thisGetThanksString.' + paramName)

for thisGetThanksString in getThanksStrings:
    currentLoop = getThanksStrings
    # abbreviate parameter names if possible (e.g. rgb = thisGetThanksString.rgb)
    if thisGetThanksString != None:
        for paramName in thisGetThanksString.keys():
            exec(paramName + '= thisGetThanksString.' + paramName)
    
    #------Prepare to start Routine "thanks"-------
    t = 0
    thanksClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    text.setText(contactresearcher)
    endMsgLabel.setText(endMsg)
    key_resp_5 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    key_resp_5.status = NOT_STARTED
    # keep track of which components have finished
    thanksComponents = []
    thanksComponents.append(text)
    thanksComponents.append(endMsgLabel)
    thanksComponents.append(key_resp_5)
    for thisComponent in thanksComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "thanks"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = thanksClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        if t >= 0.4 and text.status == NOT_STARTED:
            # keep track of start time/frame for later
            text.tStart = t  # underestimates by a little under one frame
            text.frameNStart = frameN  # exact frame index
            text.setAutoDraw(True)
        
        # *endMsgLabel* updates
        if t >= 0.4 and endMsgLabel.status == NOT_STARTED:
            # keep track of start time/frame for later
            endMsgLabel.tStart = t  # underestimates by a little under one frame
            endMsgLabel.frameNStart = frameN  # exact frame index
            endMsgLabel.setAutoDraw(True)
        
        # *key_resp_5* updates
        if t >= .4 and key_resp_5.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_5.tStart = t  # underestimates by a little under one frame
            key_resp_5.frameNStart = frameN  # exact frame index
            key_resp_5.status = STARTED
            # keyboard checking is just starting
            key_resp_5.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if key_resp_5.status == STARTED:
            theseKeys = event.getKeys(keyList=['return'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                key_resp_5.keys = theseKeys[-1]  # just the last key pressed
                key_resp_5.rt = key_resp_5.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in thanksComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "thanks"-------
    for thisComponent in thanksComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_5.keys in ['', [], None]:  # No response was made
       key_resp_5.keys=None
    # store data for getThanksStrings (TrialHandler)
    getThanksStrings.addData('key_resp_5.keys',key_resp_5.keys)
    if key_resp_5.keys != None:  # we had a response
        getThanksStrings.addData('key_resp_5.rt', key_resp_5.rt)
    # the Routine "thanks" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed 1 repeats of 'getThanksStrings'









win.close()
core.quit()
