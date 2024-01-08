Set ws = CreateObject("WScript.shell")
Wscript.Echo "Start"

Do

WScript.Sleep 60000

ws.SendKeys "{SCROLLLOCK}{SCROLLLOCK}"

Wscript.Echo "Act"

Loop