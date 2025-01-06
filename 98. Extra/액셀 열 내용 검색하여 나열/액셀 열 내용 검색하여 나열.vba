Sub FillResults()
    Dim wsInput As Worksheet, wsOutput As Worksheet
    Dim lastRowA As Long, lastRowK As Long
    Dim i As Long, j As Long
    Dim lastKeyWord As String
    Dim searchKey As String
    Dim resultRow As Long
    Dim colCount As Long
    Dim inputColumn As String, searchColumn As String, outputColumn As String
    Dim uniqueKeys As Object
    Dim substringKey As String
    Dim targetColumn As String
    Dim inputSheetName As String, outputSheetName As String

    ' 시트 이름 초기화
    inputSheetName = "sample1"  ' 입력 시트 이름
    outputSheetName = "output" ' 출력 시트 이름
    
    ' 초기 변수 변경
    inputColumn = "A" ' 검색할 내용
    searchColumn = "K" ' 검색될 내용
    copyColumn = "L" ' 검색될 내용+1칸부터 오른쪽끝까지 복사함
    outputColumn = "C" ' 복사 시작열
    
    ' 컬렉션 초기화 (목록 저장용)
    Set uniqueKeys = CreateObject("Scripting.Dictionary")
    
    ' 입력 시트와 출력 시트 설정
    Set wsInput = ThisWorkbook.Sheets(inputSheetName)
    
    ' "output" 시트 생성 또는 초기화
    On Error Resume Next
    Set wsOutput = ThisWorkbook.Sheets(outputSheetName)
    On Error GoTo 0
    If wsOutput Is Nothing Then
        Set wsOutput = ThisWorkbook.Sheets.Add(After:=wsInput)
        wsOutput.Name = "output"
    Else
        wsOutput.Cells.Clear ' 기존 데이터를 초기화
        wsOutput.Move After:=wsInput ' sample1 뒤로 이동
    End If
    
    ' sample1 시트의 데이터를 output 시트로 복사
    wsInput.Cells.Copy Destination:=wsOutput.Cells

    
    ' A열과 K열의 마지막 행 찾기
    lastRowA = wsOutput.Cells(wsOutput.Rows.Count, inputColumn).End(xlUp).Row
    lastRowK = wsOutput.Cells(wsOutput.Rows.Count, searchColumn).End(xlUp).Row
    
    ' A열 전체 순회
    For i = 1 To lastRowA
        searchKey = wsOutput.Cells(i, inputColumn).Value ' A열에서 검색 내용
        
        ' A열이 비어 있지 않고, uniqueKeys에 없으면 추가
        If searchKey <> "" And Not uniqueKeys.Exists(searchKey) Then
            lastKeyWord = searchKey ' lastKeyWord 갱신
            uniqueKeys.Add searchKey, True ' 목록에 키 추가
            
            'resultRow = wsOutput.Cells(wsOutput.Rows.Count, outputColumn).End(xlUp).Row + 1 ' 결과 입력 시작 위치
            resultRow = i
            
            ' K열에서 검색 (앞 7글자만 비교)
            For j = 1 To lastRowK
                substringKey = Left(wsOutput.Cells(j, searchColumn).Value, 7) ' 최대 7글자까지 substring
                If substringKey = Left(searchKey, 7) Then
                    ' searchColumn 한 칸 오른쪽부터 오른쪽 끝까지 복사
                    targetColumn = wsOutput.Cells(j, searchColumn).Offset(0, 1).Column
                    colCount = wsOutput.Cells(j, wsOutput.Columns.Count).End(xlToLeft).Column ' 오른쪽 끝 열 찾기
                    wsOutput.Range(wsOutput.Cells(j, copyColumn), wsOutput.Cells(j, colCount)).Copy
                    
                    ' 결과 출력
                    wsOutput.Cells(resultRow, outputColumn).PasteSpecial Paste:=xlPasteAll
                    ' 이때 A열 값이 비어 있으면 lastKeyWord로 채움
                    If wsOutput.Cells(resultRow, inputColumn).Value = "" Then
                        wsOutput.Cells(resultRow, inputColumn).Value = lastKeyWord
                    End If
                    resultRow = resultRow + 1 ' 다음 결과는 다음 줄에 기록
                End If
            Next j
        End If
    Next i
    
    ' 클립보드 해제
    Application.CutCopyMode = False
    
    ' 작업 완료 후 output 시트 선택하고 A1로 이동
    wsOutput.Activate
    wsOutput.Cells(1, 1).Select
End Sub
