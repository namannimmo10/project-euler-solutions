$sundays = 0

for($year = 1901; $year -le 2000; $year++){
    for($month = 1; $month -le 12; $month++){
        if((Get-Date -Date "$month/01/$year").DayOfWeek -eq "Sunday"){
            $sundays += 1
        }
    }
}

Write-Host $sundays
