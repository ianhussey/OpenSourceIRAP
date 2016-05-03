# Implicit Relational Assessment Procedure (IRAP) written in PsychoPy

## License
Copyright (c) Ian Hussey 2015 (ian.hussey@ugent.be)

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
## Version
0.9.5 (17/04/2016)

Written in PsychoPy 1.82

*NB This code is still in beta - I haven't used this in an experiment yet or had someone else do a code review.*

## Notes
- This implimentation of the IRAP has high fidelity to the procedure described in Barnes-Holmes et al. (2010: a sketch of the IRAP and REC model), and to the IRAP 2010, 2012, and 2014 programs developed in Visual Basic 6 by Dermot Barnes-Holmes. See block layout below. 
- The included stimulus file employs pictures as category stimuli and words as attribute stimuli. However, this implimentation can display words or images for what are often referred to as the 'label' stimuli (top of screen) or 'target' stimuli (bottom of screen). To do this, edit stimuli.xlsx file: if using text stimuli, put "blank.png" in the img columns; if using image stimuli, put a single space character (i.e, " ") in the text stimuli columns. Failure to do either will cause Psychopy to throw an error message.
- All stimuli and instructions can be altered by editing the excel files. PsychoPy has unicode support, so tranlating the task into other languages only requires changes to these excel files.
- The escape key quits the task at any time. The return key ends the task properly once it’s complete.
- You can run either the psyexp file or the py file inside PsychoPy. The py file should have greater cross platform support; if you run into errors with the psyexp file use the py instead.
- psydat, csv and log files are produced for each participant. The csv file alone is sufficient to most analyses (e.g., calculation of D scores). An R script for this is in the works.
- Accuracies can be calculated by reverse scoring the feedback response variables. 
- Number of trials per block is equal to four times the number of rows in the stimuli.xlsx file.  
- Fixed or moving response options is determined via a variable in the task.xlsx file. Set this to "true" for moving.
- The order of presentation of the blocks (i.e., block order) is set for each participant in the dialogue box that appears after you press run. Set this to "b" for the alternate order.
- An autoresponse 'monkey' can be invoked by setting "UseMonkey" in the dialogue box to "y" or "yes". This will simulate keypresses throughout the task to that you can test your script with less labour. 
- ITI is set to 400 ms, as in the original publication.

## Block Layout
- Arbtrary number of maximum exposures to the practice block pairs. Default is max 4. 
- When participants meet the accuracy and latency criteria on both blocks in a pair they move on to test blocks. If criteria are not bet within the max the task skips the test blocks and goes to the end screen.
- Arbtrary number test blocks. Default is 3. 
- Arbitrary number of stimulus exemplars per category, but all must have the same number. 

## To do
1. R script for processing D scores and R script.
2. Calculate D scores within task? Pros: more user friendly to have the D scores in the output file. Cons: I don't know the pandas library very well.
3. Change timing from seconds to frames for higher accuracy, or provide a second version that does this.

## Known issues
1. If participants get 100% of trials correct on either blocks 1+2+3 or blocks 4+5 then the incorrect response RT column will not be created for that participant. This is a) unlikely, and b) not a problem if you process data files based on column header matching (e.g., most R methods). However, it can be problematic if your data processing workflow relies on column order rather than column header name, e.g., a SPSS script using a GET command.
2. Task requires equal numbers of label and target stimuli. This could be changes by splitting the stimuli files in two and sampling the labels with random but the targets with pop(). Indeed, this is how the original VB6 program works. However, assuming that there are equal number of label and target stimuli, the current implimentation is technically supperior as it results in an equal number of presentations of the label stimuli exemplars.
4. Needs a block length multiplier, given that many people will use only 3 or 4 stimulus exemplars. A simple multiplier variable in the task.xlsx file could make this easier.  

## Changelog
### 0.9.5
1. Added option for block order selection via the dialogue box.
2. Added autoresponse monkey
3. Added option for image stimuli.
4. Added Colored text for pre block rules.
5. Added option for moving response options.
6. Tidied up post block text and locations.
7. Added warning level logging
8. Separated the block layout and stimuli excel files. This allows for an arbitrary number of exemplars for each stimulus category.
9. Commented out the saving of median latency and % accuracy data to the csv file, as it was causing problems in reading the file into R.