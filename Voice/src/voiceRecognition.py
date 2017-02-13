import subprocess

def runstring(text):
    print "RunString: " + text

proc = subprocess.Popen(['sh', '-c', 'pocketsphinx_continuous -adcdev hw:1,0  -nfft 2048 -samprate 48000 -lm 6363.lm -dict 6363.dic'],stdout=subprocess.PIPE)
    
while True:
    line = proc.stdout.readline()
    if line != '':
        output = line.rstrip()
        print output
        if (len(output.split("READY"))>1):
            runstring("Speak")
        if (len(output.split("please wait"))>1):
            runstring("Please wait")
        if (len(output.split(":"))>1):
            runstring(str(output.split(":")[1])+'.')
    else:
        break