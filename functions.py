# -*- coding: utf-8 -*-



def isreacheble(hostname):
    import subprocess
    p = subprocess.Popen('ping ' + hostname + ' -n 1', stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    p.wait()
    if p.poll()==0:
        result = "Host "+hostname+" is up"
    else:
        result = "Host "+hostname+" is unreacheble"
    return result