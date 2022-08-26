#!/bin/bash
# prints the input
function pillowdrift() {
    if [[ $1 == '--start' ]] 
    then
        echo 'Starting pillowdrift monitoring interface ...' 
    elif [[ $1 == '--stop' ]] 
    then
        echo 'Stopping pillowdrift monitoring interface ...' 
        echo '                Thanks !!!                   ' 
    else 
        echo 'Enter a valid command line please.'
        echo 'Example: pillowdrift [--start|--stop] '
    fi

}