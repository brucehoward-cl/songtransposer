# Song Transposer
### DESCRIPTION
For guitar players, transposing songs from one key to another - to better suit vocals, for example - can be
a time-consuming complicated process. This software solves that problem.

### SPECIAL INSTRUCTIONS
None! Nothing needed other than a python engine.
Instructions on how to use the interface will print upon execution.
Disclaimer: I didn't spend a lot of time on making the user interface robust. But it'll work for what it's supposed to do.

### TO EXECUTE APP:   python master_loop.py

### ASSUMPTIONS
This application is actually written with someone who has some musical knowledge. That is where its main value rests.
However, instructions are written such that anyone can use it, even if they don't know anything about music.

### FEATURES
  ###### 1.  Master Loop.  
      - located in **master_loop.py**
  ###### 2.  Create class, create an instance, and populate it
      - there are numerous examples, but in **Master Loop** the **Song class** from **song.py** is an example. 
  ###### 3.  Create a dictionary or list, populate it, retrieve at least one value and use it
      - In **notes.py** >> **SCALE** is a list. 
      - In **song.py** >> **song class** >> **chord_progression** is a list of Chord classes
  ###### 4.  Create and call at least 3 functions, at least one of which returns a value that gets used
      - In **song.py** >> **Song class** I call ***insert_chord_progression()*** and ***transpose()***
      - In **factory.py** >> **Factory class**, I created ***get_chord()*** which returns the proper chord 
        (major, minor, etc). It is called in the Song.insert_chord_progression() method to populate the Song's
        chord progression 
      - there's other examples which I think are pretty noticeable
  ###### 5.  Implement a regular expression to ensure data is stored and displayed in same format
      - In **master_loop.py** REs are used to parse the input string into distinct chord types. 
        Those types are then converted and stored as Chord objects. Eventually those chord objects get printed
        out again.  *This is a loose interpretation of the requirement but it at least demonstrates some skill
        in using RE to accomplish certain tasks.*
  ###### 6.  Build a conversion tool that converts user input to another type and displays it
      - As mentioned in (5), user input is converted to a list of Chord objects that is stored in class Song.
      - That list of chord objects is eventually iterated over and printed, after it has been transposed to 
        the desired key
      - *The conversion tool can be considered as the collaboration of these classes:* 
             **Song, Factory, IChord** 
  ###### 7.  (Bonus feature not actually required)  Implemented Factory Method Design pattern
      - A Factory class was created that creates the appropriate chord type (major, minor, etc) 
      - The Factory object is 'injected' into the Song object. Even though Factory has to have knowledge of
         the Chord classes, Song does not.
      - This pattern allows the Factory class to be updated to handle other chord types as time and need 
        dictate.
      - Admittedly it's not a perfect implementation, but I think it's a decent approximation.
        


    
