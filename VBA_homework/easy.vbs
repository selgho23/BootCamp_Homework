Sub easy()
    
    ' Cycle through all worksheets
    For Each ws In Worksheets
        
        ' Grab the last row and last column indices of each ws
        lastRow = ws.Range("A1").CurrentRegion.Rows.Count
        lastColumn = ws.Range("A1").CurrentRegion.Columns.Count
        
        ' Grab the index of the volume column
        Dim volColumn
        For i = 1 To lastColumn
            If ws.Cells(1, i).Value = "<vol>" Then
                volColumn = i
            End If
        Next
        
        ' Variable to mark the first instance of a given ticker
        Dim firstTicker
        ' firstTicker for "A"
        firstTicker = 2
        
        ' Variable to specify the row in which total stock volume and ticker
        ' will be inserted
        Dim entryRow
        entryRow = 2
        
        ' Iterate through all rows in current worksheet
        For i = 2 To lastRow
        
            ' Variables to store the ticker at the current iteration and next iteration
            Dim currentTicker
            currentTicker = ws.Cells(i, 1).Value
            Dim nextTicker
            nextTicker = ws.Cells(i + 1, 1).Value

            ' Compare the value of the current and next ticker
            ' If they are not equal then ...
            If currentTicker <> nextTicker Then
            
                ' Sum the stock volume over the interval defined by firstTicker and
                ' current i value
                Dim totalVolume
                totalVolume = Excel.WorksheetFunction.Sum(ws.Range( _
                              ws.Cells(firstTicker, volColumn), ws.Cells(i, volColumn)))

                ' Update firstTicker
                ' e.g. firstTicker for "A" is updated by setting it equal to the row
                ' number at which ticker equals "AA"
                firstTicker = i + 1
                
                ' Label the headers for the results columns
                ws.Cells(1, volColumn + 2).Value = "Ticker"
                ws.Cells(1, volColumn + 3).Value = "Total Stock Volume"
                
                ' Insert appropriate values into results columns
                ws.Cells(entryRow, volColumn + 2).Value = currentTicker
                ws.Cells(entryRow, volColumn + 3).Value = totalVolume
                
                ' Autofit the results columns for aesthetic purposes
                ws.Range("I1:J1").Columns.AutoFit
                
                ' Update entryRow for the next ticker entry
                entryRow = entryRow + 1
            End If
        Next
    Next
End Sub


