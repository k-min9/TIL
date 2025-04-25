#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.

;create a txt file to store the coordinates in
FileDelete, %A_WorkingDir%\coords.txt
FileAppend, Coordinates for the Toilets are`n, %A_WorkingDir%\coords.txt

;setup where we move the mouse in the right places and save the Positions
MsgBox,
(
Move the cursor to the Top of the black circle inside the Toilet
Top Row Far Left Toilet
Press Enter if you did it
)
click
sleep, 50
;Store the coordinates in the txt file, repeat this a bunch of times
MouseGetPos, MouseX, MouseY
FileAppend, %MouseX%`n, %A_WorkingDir%\coords.txt
FileAppend, %MouseY%`n, %A_WorkingDir%\coords.txt


MsgBox,
(
Move the cursor to the Top of the black circle inside the Toilet
Middle Row Second Toilet from the Left
Press Enter if you did it
)
click
sleep, 50
MouseGetPos, MouseX, MouseY
FileAppend, %MouseX%`n, %A_WorkingDir%\coords.txt
FileAppend, %MouseY%`n, %A_WorkingDir%\coords.txt

MsgBox,
(
Move the cursor to the Top of the black circle inside the Toilet
Bottom Row Middle Toilet
Press Enter if you did it
)
click
sleep, 50
MouseGetPos, MouseX, MouseY
FileAppend, %MouseX%`n, %A_WorkingDir%\coords.txt
FileAppend, %MouseY%`n, %A_WorkingDir%\coords.txt

MsgBox,
(
Move the cursor to the Top of the black circle inside the Toilet
Top Row Second Toilet from the Right
Press Enter if you did it
)
click
sleep, 50
MouseGetPos, MouseX, MouseY
FileAppend, %MouseX%`n, %A_WorkingDir%\coords.txt

MsgBox,
(
Move the cursor to the Top of the black circle inside the Toilet
Top Row Far Right Toilet
Press Enter if you did it
)
click
sleep, 50
MouseGetPos, MouseX, MouseY
FileAppend, %MouseX%`n, %A_WorkingDir%\coords.txt

Missedit:
MsgBox,
(
Move the Cursor over the white Part of the second "s" in "Press Start"
Press Enter if you did it
)
click
sleep, 50
MouseGetPos, MouseX, MouseY
	PixelGetColor, color, MouseX, MouseY
	if (color != 0xFFFFFF)
	{
	goto, Missedit
	}
FileAppend, %MouseX%`n, %A_WorkingDir%\coords.txt
FileAppend, %MouseY%`n, %A_WorkingDir%\coords.txt

MsgBox,
(
Move the Cursor over the Start Button
Press Enter if you did it
)
MouseMove, 0, -200, 0, R
sleep, 50
click
sleep, 50
MouseMove, 0, 200, 0, R
sleep, 50
MouseGetPos, MouseX, MouseY
FileAppend, %MouseX%`n, %A_WorkingDir%\coords.txt
FileAppend, %MouseY%`n, %A_WorkingDir%\coords.txt

ExitApp 

;Pause button
F11::
Pause
Suspend
return