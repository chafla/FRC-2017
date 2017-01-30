# FRC-2017 Notes

## Launching scripts

* Shell scripts are found in *~pi/git/FRC-2017/bin*.

* Shell script stdout and stderr are directed to *~pi/git/FRC-2017/logs*.

* Shell scripts are launched from */etc/rc.local* during startup 
by adding these lines above the call to `exit 0`.
Notice the script is executed as user *pi*:
````bash
su - pi -c ~pi/git/FRC-2017/bin/object-tracker.sh
su - pi -c ~pi/git/FRC-2017/bin/gear-front-publisher.sh
exit 0
````

* Scripts running Python code using OpenCV need to first setup a *cv2* environment:
```bash
source /home/pi/.profile
workon py2cv3
```

* Scripts need to adjust *$PYTHONPATH* appropriately:
```bash
export PYTHONPATH=${PYTHONPATH}:~pi/git/common-robotics:~pi/git/object-tracking
```

* The *stdout* and *stderr* are included in the log file by using `&>`. It is critical that each shell script
be forked with a trailing `&`:
```bash
~pi/git/object-tracking/object_tracker.py --bgr "174, 56, 5" --width 400 --flip &> ~pi/git/FRC-2017/logs/object-tracker.out &
```