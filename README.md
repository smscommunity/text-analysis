# SMS Text Analysis

*(Made by Jpep and Toburr)*

## Any% Text Length
*(in quarter-frames)*  
Italian: **7326.0**  
Japanese: **8168.0** (+7.02s)  
French: **8700.0**  
English: **8703.0**  
Spanish: **8765.0**  
German: **8932.0**  

Numbers are still not 100% certain for Japanese.

## Theory

If we have a textbox that is *l* lines long and contains *n* characters, how long does it take to scroll through and close it?

### Character Mechanics

**Non-Japanese**  
Assuming fast text and textbox mashing are both frame perfect:
1. The first 2 characters in a textbox appear in **1QF**.
2. The 3rd and 4th characters in a textbox take **1F** = **4QF** to appear each.
3. The 5th character takes **3QF** to appear.
4. The first 2 characters of lines 2 and 3 take **1QF** to appear. They both
appear on the same QF, not one after the other.
5. Every other character takes **2QF** to appear.

*Example: Airstrip character appearances per frame (rows) and quarterframe (columns)*

![](https://cdn.discordapp.com/attachments/529145099003887618/934195613950681149/AirstripScrollExample.png)

**Japanese**  
Japanese uses another set of mechanics (presumably to account for the wider characters). Unlike the above these were derived manually, going frame by frame on TAS text.

Assuming fast text and textbox mashing are both frame perfect:
1. The first character in a textbox appear in **1QF**.
2. The 2nd character takes **10QF** to appear.
3. The 3rd character takes **8QF** to appear.
4. The 4th character takes **4QF** to appear.
5. The first 2 characters of lines 2 and 3 take **1QF** to appear. They both
appear on the same QF, not one after the other.
6. Every other character takes **3QF** to appear.

### Blue Bands
The textbox can be closed once 2 conditions are met:
1) The last character of the last line has appeared.
2) The blue band behind the last line of text has fully appeared.

Every blue band has a timer which starts at the line number (1, 2 or 3) and counts down by 0.04 every QF. Once it goes below -0.109, the line is considered to have fully appeared.  
However, the timer cannot go below 1 while the last character of the previous line hasn’t appeared. This mechanic comes into play on the last line of text.  
Because of it it is
not always possible to close a textbox once the last character has appeared.

### Timing Methodology
We can time how long it takes for every line but the last one to appear using a formula derived from the rules outlined in the ”Mechanics” paragraph.  
For the last line, we also need to compute how long it takes for the blue band to appear, compare this number to how long it takes for the characters of the line to appear, and keep the biggest.

Finally, note that a textbox can only be closed at the beginning of
a frame. This means that in-game, mashing perfectly through the same
textbox twice can lead to different results.  
For instance, a textbox that is 3QF long and starts on Frame 1, QF 1 will end on Frame 1, QF 3. So it can be closed at the beginning of Frame 2. But
if it starts on QF3 instead, then it can only be closed starting on Frame 3.
The average timeloss due to this is 1.5QF.
