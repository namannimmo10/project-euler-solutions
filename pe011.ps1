#region variables
$script:numbers = @(
"08", "02", "22", "97", "38", "15", "00", "40", "00", "75", "04", "05", "07", "78", "52", "12", "50", "77", "91", "08",
"49", "49", "99", "40", "17", "81", "18", "57", "60", "87", "17", "40", "98", "43", "69", "48", "04", "56", "62", "00",
"81", "49", "31", "73", "55", "79", "14", "29", "93", "71", "40", "67", "53", "88", "30", "03", "49", "13", "36", "65",
"52", "70", "95", "23", "04", "60", "11", "42", "69", "24", "68", "56", "01", "32", "56", "71", "37", "02", "36", "91",
"22", "31", "16", "71", "51", "67", "63", "89", "41", "92", "36", "54", "22", "40", "40", "28", "66", "33", "13", "80",
"24", "47", "32", "60", "99", "03", "45", "02", "44", "75", "33", "53", "78", "36", "84", "20", "35", "17", "12", "50",
"32", "98", "81", "28", "64", "23", "67", "10", "26", "38", "40", "67", "59", "54", "70", "66", "18", "38", "64", "70",
"67", "26", "20", "68", "02", "62", "12", "20", "95", "63", "94", "39", "63", "08", "40", "91", "66", "49", "94", "21",
"24", "55", "58", "05", "66", "73", "99", "26", "97", "17", "78", "78", "96", "83", "14", "88", "34", "89", "63", "72",
"21", "36", "23", "09", "75", "00", "76", "44", "20", "45", "35", "14", "00", "61", "33", "97", "34", "31", "33", "95",
"78", "17", "53", "28", "22", "75", "31", "67", "15", "94", "03", "80", "04", "62", "16", "14", "09", "53", "56", "92",
"16", "39", "05", "42", "96", "35", "31", "47", "55", "58", "88", "24", "00", "17", "54", "24", "36", "29", "85", "57",
"86", "56", "00", "48", "35", "71", "89", "07", "05", "44", "44", "37", "44", "60", "21", "58", "51", "54", "17", "58",
"19", "80", "81", "68", "05", "94", "47", "69", "28", "73", "92", "13", "86", "52", "17", "77", "04", "89", "55", "40",
"04", "52", "08", "83", "97", "35", "99", "16", "07", "97", "57", "32", "16", "26", "26", "79", "33", "27", "98", "66",
"88", "36", "68", "87", "57", "62", "20", "72", "03", "46", "33", "67", "46", "55", "12", "32", "63", "93", "53", "69",
"04", "42", "16", "73", "38", "25", "39", "11", "24", "94", "72", "18", "08", "46", "29", "32", "40", "62", "76", "36",
"20", "69", "36", "41", "72", "30", "23", "88", "34", "62", "99", "69", "82", "67", "59", "85", "74", "04", "36", "16",
"20", "73", "35", "29", "78", "31", "90", "01", "74", "31", "49", "71", "48", "86", "81", "16", "23", "57", "05", "54",
"01", "70", "54", "71", "83", "51", "54", "69", "16", "92", "33", "48", "61", "43", "52", "01", "89", "19", "67", "48"
)


[int]$script:result_product = 0
[int]$script:result_x = 0
[int]$script:result_y = 0
[int]$script:number1 = 0
[int]$script:number2 = 0
[int]$script:number3 = 0
[int]$script:number4 = 0
[string]$script:result_direction = ""

#param_list (direction_name, x_max, y_max, x_start, y_start, x_difference, y_difference)
$param_list = @(
    ("right", 16, 19, 0, 0, 1, 0),
    ("down", 19, 16, 0, 0, 0, 1),
    ("diagonal down right", 16, 16, 0, 0, 1, 1),
    ("diagonal down left", 19, 16, 3, 0, -1, 1)
    )
#end region

#region functions
function toint
(
    $number
)
{
    return [convert]::ToInt32($number, 10)
}


function result
(
$direction_name = $args[0],
$x_max = $args[1],
$y_max = $args[2],
$x_start = $args[3],
$y_start = $args[4],
$x_difference = $args[5],
$y_difference = $args[6]
)
{
    $difference = $y_difference * 20 + $x_difference 
    For ($y = $y_start; $y -lt ($y_max + 1); $y++)
        {
        For ($x = $x_start; $x -lt ($x_max + 1); $x++)
        {
            $number_pos = $y * 20 + $x
            $number1 = toint($script:numbers[$number_pos])
            $number2 = toint($script:numbers[$number_pos + $difference])
            $number3 = toint($script:numbers[$number_pos + 2 * $difference])
            $number4 = toint($script:numbers[$number_pos + 3 * $difference])

            $product = $number1 * $number2 * $number3 * $number4


            If ($product -gt $script:result_product)
            {
                $script:result_product = $product
                $script:result_x = $x
                $script:result_y = $y
                $script:result_direction = $direction_name
                $script:number1 = $number1
                $script:number2 = $number2
                $script:number3 = $number3
                $script:number4 = $number4

            }
        
        }
    }
}
#end region


#region run-program
Foreach ($i in $param_list){
    result $i[0] $i[1] $i[2] $i[3] $i[4] $i[5] $i[6]
}

Write-Host "Greatest product: $result_product"
Write-Host "Direction: $result_direction"
Write-Host "Start position: y = $result_y x = $result_x"
Write-Host "Numbers: $number1, $number2, $number3, $number4"
#end region