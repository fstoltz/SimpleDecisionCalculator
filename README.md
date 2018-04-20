## SimpleDecisionCalculator  
**The aim for this program is to simplify decision-making  
by quantifying pros / cons in relation to a specified action.**  
  
**Background**  
Why I wish to build this program is because recently I've found  
myself weighing the pros / cons between various choices, but  
as the different sides become increasingly complex, I find myself losing track  
of the pros / cons when it's a non-trivial choice.

**Update 20/4-2018**  
I was thinking, this might be an interesting tool to continue building on.
It could be extended to persist entries to a database, so that each action
with its pros / cons are permanently stored. This might prove to be something interesting
if I continue adding records of the choices I'm making and my view of the pros / cons.
If I do that for say a few years, I could then use this database to look back at these choices
I was thinking about then and view a "snapshot" of how I viewed the pros / cons for that 
decision, which might 'now'(in the future) be full-fledged. And even further in the future, say 10-15 years
I suspect it might be interesting to get a glimpse of what I was pondering about at this point in time.
I'm thinking it might be similar to the sensation of going through really old photographs.
The one thing that might be difficult with this is where to store the data in order to maximize reliability
and mitigate the risk of somehow losing the data, because the idea will be to store it for a longer period of time.

Question then becomes if the data should be stored in the 'program folder' of the executable or if the
data should be written to a database that is stored on a different computer, and then each time an entry
is made, write this entry to the central database. Storing the database along with the executable program seems
like a risky choice, though I'm not entirely sure of how to setup the central database. Considering I might wanna make
the program available to others and not hard-code it to only fit/be available for use only by myself. I'd be interesting
to be able to have some server running, that keeps track of the database, and then distribute a program
that clients can run. 

**Core functionality**  
* Menu 
  * New action
    * Define action x
      * Add a pro to action x, assign a value (+1 ... +10)
      * Add a con to action x, assign a value (-1 ... -10)
      * Display summary of pros / cons for action x (preferably color-coded)
      * Go back to main menu
  * Exit
  

**Design**  
I think an OOP-approach might be suitable here.
 
![UML](http://huerty.com/content/umlSDC.png) 

pros & cons are dictionaries  
the key will be a string, value will be the quantifying value for the pro / con

Up next:
design for the menu(uml), sequence diagram(ish)