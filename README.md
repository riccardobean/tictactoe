# Welcome to Tic Tac Toe! 
***A game developed by Riccardo Bean***

# How to download the latest release
1. [Download the file **(Windows only)**.](https://github.com/riccardobean/tictactoe/releases/download/win3.1/setup.exe)
2. Extract the zip file.
3. Run Tic Tac Toe.exe and the program should run.
4. If the program does not run see below.

# License
**License: Copyright © 2024 Riccardo Bean. All Rights Reserved.**

***See [LICENSE.txt](LICENSE.txt) for more information***

# Credits
***At the time of development, all the icons used were available without the need of attribution to the author.***

***The logo was created by the developer of this repository, Riccardo Bean.***

# The game
There are three game modes:
- Multiplayer
- Easy AI
- Impossible AI
*Note: there is no use of AI in this project. The solution is hard-coded, but saying "AI" looked better nowadays!*

### Easy AI 
Easy AI is built so that your computer will pick a random move without any algorithm behind. Thus, it will be beatable most of the times.

### Impossible AI 
Impossible AI (it should really be impossible to beat!) is built using a hard coded solution that explores in order of priority the next best move. The logic of this mode was solely thought by the author of this repository, Riccardo Bean.

#### How Impossible AI works
*If you want to play the game, don't look at it! (You won't be able to win anyways though!)*

In order of priority, the AI will (if possible):
1. Win vertically
2. Win horizontally
3. Win obliquely
4. Block vertically
5. Block horizontally
6. Block obliquely
7. Pick the center
8. Create a fork
9. Pick a corner
10. Do a random move

If you happen to beat impossible AI, please take a screenshot of how you cheated and submit it (along with a brief explanation) using [this form](https://bit.ly/3O72Rpa).

# Bugs
If you find any bugs, please take a screenshot of the bug you encountered and submit it (along with a brief explanation) using [this form](https://bit.ly/3O72Rpa).

# Troubleshooting
***Pick the best description of your situation from below. If nothing works for you, please submit a reply to the form found in the section "Bugs".***
### If your browser shows an orange triangle
1. Hover the setup download
2. Click on the three dots that appear
3. Click on "Keep" and a menu will pop up
4. Click "Show more"
5. Click "Keep anyway"
6. The download should finish
### If your browser doesn't let you download the file ("Couldn't download - virus detected")
1. Try using a different browser
2. If the previous option still does not work, install "Free Download Manager"
3. Copy the download link from above and paste it into the "+" in "Free Download Manager"
4. The download should start
### If your antivirus opens and marks setup.exe or Tic Tac Toe.exe as a malicious file
1. Click on "Show more"
2. Click on "Run anyway"
3. The program should run 
### If your notepad opens and says "Your program could not be executed"
1. Your program is in the right folder but your images are not
2. Check correct order section below
### If a grey window with a red triangle opens
1. Your program is not in the right folder or your subfolders do not exist
2. Check correct order section below
### If the setup concluded successfully but nothing happens
1. Wait for a few minutes
2. If nothing pops up, press the Windows icon
3. Type "Tic Tac Toe.exe" and press enter
4. Wait until the game opens

# Correct Order
Folder Name

\-- assets

----- home.png 

----- logo.png

----- logo.ico

----- undo-arrow.png

\-- log

----- feedback.txt

----- LICENSE.txt

\-- ReadMe.txt

\-- Tic Tac Toe.exe
 
