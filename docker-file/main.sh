#!/bin/bash

function lsextt()
{
find . -type f -iname '*.'${1}'' -exec ls -l {} \; ;
}



function convertma(){
   python convert.py ${1}

}
