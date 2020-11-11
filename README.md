DESCRIPTION
For guitar players, transposing songs from one key to another - to better suit vocals, for example - can be
a time-consuming complicated process. This software solves that problem.

SPECIAL INSTRUCTIONS
None! Nothing needed other than a python engine.
Instructions on how to use the interface will print upon execution.

ASSUMPTIONS
This application is actually written with someone who has some musical knowledge. That is where its main value rests.
However, instructions are written such that anyone can use it, even if they don't know anything about music.

FEATURES
  1.  Master Loop.  
      - located in master_loop.py
  2.  Create class, create an instance, and populate it
      - there are numerous examples, but the Song class in the song.py file is one. It's used in the Master Loop
  3.  Create a dictionary or list, populate it, retrieve at least one value and use it
      - In notes.py I create NOTES as a list. 
      - In chords.IChord, in the convert_note method, I retrieve a NOTE items, then use them to compute the number 
        of halfsteps between the current note and the newly desired note
  4.  Create and call at least 3 functions, at least one of which returns a value that gets used
      - From the Song class, I call insert_chord_progression() and transpose()
      - In class Factory, I created get_chord() which returns the proper chord (major, minor, etc). It is called
        in the Song.insert_chord_progression() method to populate the Song's chord progression 
      - there's other examples which I think are pretty noticeable
  5.  Implement a regular expression to ensure data is stored and displayed in same format
      - Regular expressions are used in the master loop to parse the input string into distinct chord types. 
        Those types are then converted and stored as Chord objects. Eventually those chord objects get printed
        out again.  This is a loose interpretation of the requirement but it at least demonstrates some skill
        in using RE to accomplish certain tasks.
  6.  Build a conversion tool that converts user input to another type and displays it
      - As mentioned in (5), user input is converted to a list of Chord objects that is stored in class Song.
      - That list of chord objects is eventually iterated over and printed, after it has been transposed to the
        desired key
  7.  (Bonus feature not actually required)  Implemented Factory Method Design pattern
      - A Factory class was created that creates the appropriate chord type (major, minor, etc) 
      - The Factory object is 'injected' into the Song object
      - This pattern allows the Factory class to be updated to handle other chord types as time and need dictate.
      - Admittedly it's not a perfect implementation, but it's a decent approximation.
        


Users can enter a chord progression, what key they'd like it transposed to, and get back the new progression
in the desired key.

The Factory Method Design Pattern was used to create the distinct chords in the chord progression.
    - This will allow adding the ability to handle different chord types in the future.

    
