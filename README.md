# FRC-2017 Notes

## Launching scripts

* Shell scripts are found in *~pi/git/FRC-2017/bin*. All changes to these scripts
should be pushed to github and not done as a one-off edit on the Raspi. The goal 
is provision a Raspi with `git` and minimize the amount of configuration 
on the Raspi. 

* Shell script stdout and stderr are redirected to *~pi/git/FRC-2017/logs*.

* Shell scripts are launched from */etc/rc.local* during startup.
The shell script calls are added just before the call to `exit 0` and are executed as user *pi*:
````bash
su - pi -c ~pi/git/FRC-2017/bin/object-tracker.sh
su - pi -c ~pi/git/FRC-2017/bin/gear-front-publisher.sh

exit 0
````

* Shell scripts running Python code using OpenCV need to first setup a *cv2* environment:
```bash
source ~pi/.profile
workon py2cv3
```

* *$PYTHONPATH* must be set appropriately to include dependent packages:
```bash
export PYTHONPATH=${PYTHONPATH}:~pi/git/common-robotics:~pi/git/object-tracking
```

* The *stdout* and *stderr* are included in the log file by using `&>`. It is critical that each shell script
be forked with a trailing `&`:
```bash
python2 ~pi/git/object-tracking/object_tracker.py --bgr "174, 56, 5" --width 400 --flip &> ~pi/git/FRC-2017/logs/object-tracker.out &
```