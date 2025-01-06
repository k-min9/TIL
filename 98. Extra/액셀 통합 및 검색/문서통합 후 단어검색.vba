' 매크로는 Alt + F11

'C3에 입력한 폴더아래에 있는 xlsx의 [본문] 워크시트를 전부 합친다.
Sub 합치기_매크로()
    Dim 폴더경로 As String
    Dim 파일이름 As String
    Dim 본문시트 As Worksheet
    Dim 합친시트 As Worksheet
    Dim 마지막행 As Long
    Dim 본문마지막행 As Long
    Dim i As Integer
    Dim j As Integer
    Dim 에러메시지 As String
    Dim 마지막열 As Long

    ' 사용자에게 확인 메시지 표시
    If MsgBox("엑셀 파일을 합치시겠습니까?", vbQuestion + vbYesNo, "확인") = vbNo Then Exit Sub

    ' 입력한 폴더 경로 가져오기
    폴더경로 = Sheets("Main").Range("C3").Value

    ' 기존의 '본문' 시트가 있는 경우 삭제
    On Error Resume Next
    Application.DisplayAlerts = False
    Sheets("본문").Delete
    Application.DisplayAlerts = True
    On Error GoTo 0

    ' 새로운 '본문' 시트 만들기
    Set 합친시트 = ThisWorkbook.Sheets.Add(After:=Sheets(Sheets.Count))
    합친시트.Name = "본문"

    ' 폴더 내의 모든 xlsx 파일에 대해 반복
    파일이름 = Dir(폴더경로 & "\*.xlsx")
    Do While 파일이름 <> ""
        ' 엑셀 파일 열기
        Workbooks.Open (폴더경로 & "\" & 파일이름)

        ' 본문 시트 가져오기
        On Error Resume Next
        Set 본문시트 = Workbooks(파일이름).Sheets("본문")
        On Error GoTo 0

        ' 본문 시트가 없는 경우 에러 메시지에 파일 이름 추가
        If 본문시트 Is Nothing Then
            에러메시지 = 에러메시지 & 파일이름 & vbCrLf
        Else
            ' 본문 시트의 마지막 행 가져오기
            본문마지막행 = 본문시트.Cells(본문시트.Rows.Count, "A").End(xlUp).Row

            ' 대상 시트의 마지막 행 가져오기
            마지막행 = 합친시트.Cells(합친시트.Rows.Count, "A").End(xlUp).Row

            ' 본문 시트의 내용을 대상 시트에 복사
            For i = 1 To 본문마지막행
                For j = 1 To 본문시트.Cells(i, Columns.Count).End(xlToLeft).Column
                    합친시트.Cells(마지막행 + i, j).Value = 본문시트.Cells(i, j).Value
                Next j
            Next i
        End If

        ' 엑셀 파일 닫기
        Workbooks(파일이름).Close False

        ' 다음 파일 이름 가져오기
        파일이름 = Dir
    Loop

    ' 중복 항목 제거 (애매함)
    ' 마지막행 = 합친시트.Cells(합친시트.Rows.Count, "A").End(xlUp).Row
    ' 마지막열 = 합친시트.Cells(1, 합친시트.Columns.Count).End(xlToLeft).Column
    ' 합친시트.Range(합친시트.Cells(1, 1), 합친시트.Cells(마지막행, 마지막열)).RemoveDuplicates Columns:=Application.WorksheetFunction.Transpose(Application.Evaluate("ROW(1:" & 마지막열 & ")")), Header:=xlYes

    ' 처리되지 않은 파일이 있는 경우 메시지 표시
    If 에러메시지 <> "" Then
        MsgBox "다음 파일에는 '본문' 시트가 없습니다:" & vbCrLf & 에러메시지, vbExclamation
    Else
        MsgBox "엑셀 파일을 성공적으로 합쳤습니다.", vbInformation
    End If
End Sub

' 검색열 이름을 표시하게 엑셀 함수 설정
' =INDEX(INDIRECT("본문!" & C3 & "2"), 1)

' 10행 이하에 "본문" 시트에서 검색된 결과를 가져와 수정
Sub 검색_매크로()
    Dim 검색어 As String
    Dim 검색열 As String
    Dim 검색열번호 As Long
    Dim 마지막행 As Long
    Dim i As Long
    Dim 대상시트 As Worksheet
    Dim 본문시트 As Worksheet
    Dim 복사행 As Long

    ' 검색어와 검색 열 가져오기
    검색어 = Sheets("Main").Range("C6").Value
    검색열 = Sheets("Main").Range("C3").Value
    
    ' 시트 참조
    Set 대상시트 = Sheets("Main")
    Set 본문시트 = Sheets("본문")
    
    ' 검색 열 번호로 변환
    검색열번호 = 본문시트.Range(검색열 & "1").Column
    
    ' 기존 7행 밑의 모든 행 삭제
    대상시트.Rows("10:" & 대상시트.Rows.Count).ClearContents
    
    ' 본문 시트의 마지막 행 가져오기
    마지막행 = 본문시트.Cells(본문시트.Rows.Count, 검색열번호).End(xlUp).Row
    
    ' 복사 시작 행 초기화
    복사행 = 10
    
    ' 본문 시트에서 검색어와 일치하는 행 찾기 및 복사
    For i = 1 To 마지막행
        If 본문시트.Cells(i, 검색열번호).Value = 검색어 Then
            본문시트.Rows(i).Copy Destination:=대상시트.Rows(복사행)
            복사행 = 복사행 + 1
        End If
    Next i
End Sub

' 검색어 칸이 변경시 검색하게 설정
Private Sub Worksheet_Change(ByVal Target As Range)
    ' C6 셀에서 변경이 발생한 경우
    If Not Intersect(Target, Me.Range("C6")) Is Nothing Then
        ' C6 셀 서식 설정
        With Me.Range("C6")
            ' 테두리 설정
            .Borders(xlEdgeLeft).LineStyle = xlContinuous
            .Borders(xlEdgeTop).LineStyle = xlContinuous
            .Borders(xlEdgeBottom).LineStyle = xlContinuous
            .Borders(xlEdgeRight).LineStyle = xlContinuous
            .Font.Size = 11
            .Font.Name = "맑은 고딕"
        End With
        
        ' 검색 매크로 호출
        Call 검색_매크로
    End If
End Sub
