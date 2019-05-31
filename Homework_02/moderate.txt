Sub moderate()
    
    ' Cycle through all worksheets
    For Each ws In Worksheets
        
        ' Grab the last row and last column indices of each ws
        lastRow = ws.Range("A1").CurrentRegion.Rows.Count
        lastColumn = ws.Range("A1").CurrentRegion.Columns.Count
        
        ' Grab the index of the volume column, the opening price column and the closing
        ' price column
        Dim volCol
        Dim openCol
        Dim closeCol
        For i = 1 To lastColumn
            If ws.Cells(1, i).Value = "<vol>" Then
                volCol = i
            ElseIf ws.Cells(1, i).Value = "<open>" Then
                openCol = i
            ElseIf ws.Cells(1, i).Value = "<close>" Then
                closeCol = i
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
            
                ' COMPUTE YEARLY CHANGE FROM OPENING PRICE TO CLOSING PRICE
                ''' Extract opening price
                Dim openPrice
                openPrice = ws.Cells(firstTicker, openCol).Value
                If openPrice = 0 Then
                    MsgBox (Str(firstTicker) + " " + Str(openCol) + " " + Str(openPrice))
                End If
                
                ''' Extract closing price
                Dim closePrice
                closePrice = ws.Cells(i, closeCol).Value
                ''' Subtract opening price from closing price
                Dim yearlyChange
                yearlyChange = closePrice - openPrice
                
                ' COMPUTE PERCENT CHANGE FROM OPENING TO CLOSING PRICE
                Dim percentChange
                ' Account for possible division by 0
                If openPrice = 0 Then
                    percentChange = yearlyChange
                Else
                    percentChange = yearlyChange / openPrice
                End If
                
                ' COMPUTE TOTAL STOCK VOLUME
                ''' Sum the stock volume over the interval defined by firstTicker and
                ''' current i value
                Dim totalVolume
                totalVolume = Excel.WorksheetFunction.Sum(ws.Range( _
                              ws.Cells(firstTicker, volCol), ws.Cells(i, volCol)))

                ' Update firstTicker
                ' e.g. firstTicker for "A" is updated by setting it equal to the row
                ' number at which ticker equals "AA"
                firstTicker = i + 1
                
                ' Label the headers for the results columns
                ws.Cells(1, volCol + 2).Value = "Ticker"
                ws.Cells(1, volCol + 3).Value = "Yearly Change"
                ws.Cells(1, volCol + 4).Value = "Percent Change"
                ws.Cells(1, volCol + 5).Value = "Total Stock Volume"
                
                ' Insert appropriate values into results columns
                ws.Cells(entryRow, volCol + 2).Value = currentTicker
                ws.Cells(entryRow, volCol + 3).Value = yearlyChange
                ws.Cells(entryRow, volCol + 4).Value = percentChange
                ws.Cells(entryRow, volCol + 4).NumberFormat = "0.00%"
                ws.Cells(entryRow, volCol + 5).Value = totalVolume
                
                ' Conditional formatting for yearly change column
                If yearlyChange < 0 Then
                    ws.Cells(entryRow, volCol + 3).Interior.Color = RGB(255, 0, 0)
                Else
                    ws.Cells(entryRow, volCol + 3).Interior.Color = RGB(0, 255, 0)
                End If
                
                ' Autofit the results columns for aesthetic purposes
                ws.Range("I1:L1").Columns.AutoFit
                
                ' Update entryRow for the next ticker entry
                entryRow = entryRow + 1
            End If
        Next
    Next
End Sub






