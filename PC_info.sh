#!/bin/bash


line="-----------------------------------------------------";echo

echo "-- Opened at : $(date)"; echo

echo "-- [UPTIME]" $line; uptime; echo


echo "-- [FREE]" $line; free; echo
 

echo "-- [WHO]" $line; who; echo


echo "-- Closed at : $(date)"; echo
