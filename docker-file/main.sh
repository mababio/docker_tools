#!/bin/bash

function lsextt()
{
find . -type f -iname '*.'${1}'' -exec ls -l {} \; ;
}



function convert(){
   python convert.py '${1}'
   cat /tmp/output.mkv
}


