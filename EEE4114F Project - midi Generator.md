---
date: 2024/04/15 - 21:03
status: active
type: note
subtype: rubric
world: Real
tags: EEE4114F, 4114, DSP, Signals
---

# EEE4114F Project - midi Generator

## Idea Description

- Pick up audio (music)
- Compare this to .wav files of different notes
- Detect the notes being played in the song
- Choose the smallest number of notes which still sound close to the original audio
- Generate a .midi file of the song
- Play this .midi file back (using the .wav files of the different notes) and compare to the original audio

## Development Stages (Milestones)

### Milestone 1:

#### Preparation
1) collect .wav files for each note of an instrument (a soundfont)
2) using .midi files, create chords
	- Chords played for full duration of the note .wav files)
	- Chords played at t=0
3) using .midi files and .wav files, generate .wav files for each chord
	- this combines the .wav files of several notes into a single .wav file

#### Deliverable
1) Play chord .wav files
2) Process these .wav files to find the notes present
	- by comparing to the soundfont
	- correlation functions?
	- may be beneficial to limit the number of notes that can be picked
3) Generate a .midi file from this
	- Remember: every note plays for a fixed duration
4) Compare this .midi to the original chord
	- Can be done by comparing both midi files
	- OR by playing both .midi files using the soundfont
	- The latter is superior, since changes to a chord may still be close enough

### Milestone 2:

#### Preparation
1) Prepare .midi files of songs/sound snippets
	- Notes/chords can be played at any time
	- And can have varying durations
2) Using the soundfont, generate .wav files of the song snippets

#### Deliverable
1) Play song snippet .wav files
2) Process these .wav files in short sample intervals
	- $t_{sample} < 1/T\ |\ T =$ shortest permissible note
	- in each sample, pick the most likely notes being played
	- weight notes that were played in the previous sample more heavily (this may help prevent back and forth switches between notes which have similar correlations)
3) Generate .midi file for the entire song
	- Remember: each note has a length that can be measured in number of samples
4) Compare the .midi to the original song snippet
	- Same process as Milestone 1
5) CONSIDERATION WHEN DOING STEP 2, ABOVE:
	- a .wav file of a note varies with time
	- we are allowing notes less than the full duration of the note .wav
	- a note may end and be played again
	- therefore, we MAY need to compare:
		- the start of each note .wav, $0< t <t_{sample}$
		- AND the middle of the note .wav at $n*t_{sample}< t <(n+1)*t_{sample}$ where n is the number of consecutive samples that the note has already been playing.
		- HOWEVER, it may be possible to simply compare the entire .wav

\* *NOTE: milestone 2 may already be a suitable submission for the course project, depending on the amount of work necessary.*

### Milestone 3:

#### Preparation
1) Play a real instrument and record the audio
	- This means the notes will sound different, but close to the soundfont
	- Note timing will be more variable
	- Dynamics will be variable (loudness of a note)
	- Reverb, microphone noise, background noise etc. will affect the audio being recorded

#### Deliverable
1) Perform the same analysis as in Milestone 2
2) If performance is unacceptable, consider ML
3) If performance exceeds expectations
	- Add more noise
	- Use a instrument that is less similar to the soundfont
	- Use real songs comprising multiple instruments (and human voice)
	- Measure effectiveness under these circumstances