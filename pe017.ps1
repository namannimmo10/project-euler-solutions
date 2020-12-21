# region variables
$n_1_to_9 = @{"0"=0;"1"=3;"2"=3;"3"=5;"4"=4;"5"=4;"6"=3;"7"=5;"8"=5;"9"=4}
$n_10_to_19 = @{"10"=3;"11"=6;"12"=6;"13"=8;"14"=8;"15"=7;"16"=7;"17"=9;"18"=8;"19"=8}
$n_20_to_90 = @{"0"=0;"2"=6;"3"=6;"4"=5;"5"=5;"6"=5;"7"=7;"8"=6;"9"=6}
$n_hundred = @{"0"=0;"1"=10;"2"=10;"3"=12;"4"=11;"5"=11;"6"=10;"7"=12;"8"=12;"9"=11}
$n_thousand = @{"0"=0;"1"=11}
#end region

#region functions
function Get-Euler17($max_number){
    $counter = 0
    
    for($i = 1; $i -le $max_number; $i++){
        $n_string = $i.ToString()
        $n_length = $n_string.length
        $and = 0
        $10_to_19 = $false
        
        for($pos = 0; $pos -lt $n_length; $pos++){
            $number = $n_string.substring($pos, 1)
            switch($n_length - $pos){
                4 {$counter += $n_thousand[$number]}
                3 {$counter += $n_hundred[$number]}
                2 {
                    switch($number){
                        0 {
                            $and = $and
                        }
                        1 {
                            $counter += $n_10_to_19[$n_string.substring($pos, 2)]
                            if($n_length -gt 2){
                                $and = 3
                            }
                            $10_to_19 = $true
                        }
                        default {
                            $counter += $n_20_to_90[$number]
                            if($n_length -gt 2){
                               $and = 3
                            }
                        }
                    }

                }
                1 {
                    if(!($10_to_19)){
                        switch($number){
                            0 {
                                $and = $and
                            }
                            default {
                                $counter += $n_1_to_9[$number]
                                if($n_length -gt 2){
                                    $and = 3
                                }
                            }
                        }
                    }
                }
            }
        }
        $counter += $and
    }
    return $counter
}
#end region

Write-Host (Get-Euler17 -max_number 1000)
