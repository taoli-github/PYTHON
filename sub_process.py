# _*_ coding:utf-8 _*_
import subprocess


print('nslookup www.python.org')
r = subprocess.call(['nslookup', 'www.python.org'])
print('Exit code:', r)

print('nslookup')
p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, err = p.communicate(b'set q = mx \n python.org \n exit \n')
print(output.decode('gb2312'))
print('exit code:', p.returncode)
