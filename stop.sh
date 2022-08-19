ps -ef | grep "snap" | awk '{print $2}' | xargs sudo kill
ps -ef | grep "python3 snap.py" | awk '{print $2}' | xargs sudo kill
ps -ef | grep "python snap.py" | awk '{print $2}' | xargs sudo kill
kill $(pgrep -f 'python3 snap.py')
