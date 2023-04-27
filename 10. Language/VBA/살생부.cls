' 한쪽 시트에 살생부를 만들고, 다른쪽에서 체크하며 붉게 만드는 매크로, 붉게 변할때 살생부의 오른쪽에 O를 표시해주자
Private Sub Worksheet_Change(ByBal tartget As Range)
  Dim victimList As Range
  Set victimList = WorkSheets("살생부").Range("살생부범위:살생부범위")

  Dim chkSheet As WorkSheets
  Set chkSheet = WorkSheets("글이 적힐 워크시트")

  Dim searchRange As Range
  Set searchRange = chkSheet.Range("글이 적히는 범위")

  ' 우선 검게 색칠
  Dim t As Range
  For Each t In Intersect(tartget, chkSheet.UsedRange)
    t.Font.ColorIndex = 1
  Next t

  ' 살생부 체크 : 글 속 단어는 붉게, 살생부 리스트 오른쪽에는 O
  Dim victimName As Range
  For Each victimName In victimList
    If Not searchRange.Find(what:=victimName, LookIn:=x|Values, lookat:=x|Part) Is Nothing Then
      ' 살생부 리스트 내용 포함시 리스트에 O 표시
      victimName.Offset(0,1).Value = "O"

      ' 글 속 포함 단어를 붉게
      Dim cell As Range
      For Each cell In Intersect(tartget, chkSheet.UsedRange)
        If InStr(cell.Value, victimName.Value) > 0 Then
          Dim startPos As Integer
          startPos = InStr(cell.Value, victimName.Value)
          Dim lenVal As Integer
          lenVal = Len(victimName.Value)
          cell.Characters(startPos, lenVal).Font.ColorIndex = 3
        End If
      Next cell
    Else
      victimName.Offset(0, 1).Value = ""
    End If
  Next victimName
End Sub