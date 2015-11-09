# Implicit Relational Assessment Procedure (IRAP) written in PsychoPy

## LicenceCopyright Ian Hussey (ian.hussey@ugent.be)

Distributed under the MIT licence
## Version
0.9 (19/10/2015)

*This is still in beta - I have not had this code reviewed to guarantee that it functions as intended.*

## Notes
- The escape key quits the task at any time. The return key ends the task properly once it’s complete.

- You can run either the psyexp file or the py file inside PsychoPy. The py file should have greater cross platform support; if you run into errors with the psyexp file use the py instead.

- psydat and csv files are produced for each participant. csv file alone is sufficient to most analyses (e.g., calculation of D scores).

- All stimuli and instructions can be altered by editing the excel files. Indeed, all strings presented within the task are variables, so tranlating the task into other languages only requires changes to the stimuli and instructions files.

- The Traditional IRAP does not randomly sample Label stimuli separately from Target stimuli. I.e., each trial presents stimuli from a single row in the stimuli.xlsx file. As such, one can only present 1) a single Label exemplar per category and multiple Target exemplars, 2) or visa versa, 3) or have specific label exemplars tied to specific target exemplars. This differs from the 2012 and 2014 versions of the Visual Basic IRAP which allowed for multiple exemplars and randomisation of both. Changing this is not easy within the confines of the PsychoPy builder. It could be done with manual editing of the .py file code, but I haven't attempted this.

- Two versions of the IRAP can be easily deployed: the Traditional IRAP (Barnes-Holmes et al., 2006, 2010) or the Natural Language IRAP (Kavanagh, Hussey, et al., submitted). The former presents label and target stimuli (e.g., "I am" and "positive"), the latter presents a compound target stimulus in the form of a proposition (e.g., "I am positive"). The NL IRAP is therefore very similar to the Relational Responding Task (De Houwer et al., 2015). Indeed, the only differences being that 1) the NL IRAP requires participants to practice to criterion, whereas the RRT has a fixed single practice block before each test block; 2) the RRT uses inducer trials to establish and maintain the true and false response options, whereas the NL IRAP does not (moving response options could do this, but introduce a lot of noise. inducer trials actually seem to be a superior option); and 3) the NL IRAP practices pairs of the two rule blocks and then tests those pairs, whereas the RRT practices and tests one rule block and then practices and tests the other.  

- The location of the response options is fixed rather than moving/alternating in this version. Changing this is not easy within the confines of the PsychoPy builder. It could be done with manual editing of the .py file code, but I haven't attempted this.

- The order of presentation of the blocks is the same for all participants here. If you want to counterbalance this, create a copy of this entire folder and alter the stimuli.xlsx file to swap the Ds for Ks so that the correct and incorrect responses across blocks are swapped.

- ITI is set to 400 ms, as in the original publication.

## Block Layout
- [up to 3 practice block pairs. When participants meet the accuracy and latency criteria on both blocks in a pair they move on to test blocks. If criteria are not bet within 3 pairs of blocks the tast skips the test blocks and goes to the end screen]
  - practice block - Rule A - 24 trials (6 exemplars, 4 trials-types)
  - practice block - Rule B - 24 trials (6 exemplars, 4 trials-types)
- [3 test block pairs.]
  - practice block - Rule A - 24 trials (6 exemplars, 4 trials-types)
  - practice block - Rule B - 24 trials (6 exemplars, 4 trials-types)

## Known issues
1. If duplicate stimuli are entered in the stimuli file then participants can be presented with two identical exemplars one after another. This is not easy to overcome within the confines of the Psychopy builder. However, the included stimulus file does not repeat stimuli, thus if a similar pattern is followed this issue will not arise.

2. If participants get 100% of trials correct on either blocks 1+2+3 or blocks 4+5 then the incorrect response RT column will not be created for that participant. This is a) unlikely, and b) not a problem if you merge files across participants based on column header matching (e.g., using dplyr’s `rbind_list()` command). However, it can be problematic if your data processing workflow relies on column ORDER rather than column header NAME, e.g., a SPSS script using a GET command.

3. The names of many components outside of trial routines are unsystematic and need tidying if the .py file is to be intelligible.
