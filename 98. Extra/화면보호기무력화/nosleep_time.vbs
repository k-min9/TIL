' 근무시간(09:00~11:30/13:00~18:00)에만 작동하게 해보자.
Set ws = CreateObject("WScript.shell")
Wscript.Echo "Start"

Do
    currentTime = Time

    If (currentTime >= #9:00:00 AM# And currentTime <= #11:30:00 AM#) Or (currentTime >= #1:00:00 PM# And currentTime <= #6:00:00 PM#) Then
        ws.SendKeys "{SCROLLLOCK}{SCROLLLOCK}"
        Wscript.Echo "Act"
    Else
        Wscript.Echo "Resting"
    End If

    WScript.Sleep 60000
Loop
