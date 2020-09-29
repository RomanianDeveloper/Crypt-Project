import subprocess, requests, time, os



from tqdm import tqdm
loop = tqdm(total = 10000, position=0, leave=False)
for k in range(10000):
    loop.set_description("Checking your HWID...".format(k))
    loop.update(1)

loop.close()





hwid = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()
r = requests.get('github link')

try:
    if hwid in r.text:
        pass
    else:
        print('██████████████████████████████████████████████████████████████')
        print('██                                                          ██')
        print('██                      Acces Denied.                       ██')
        print('██                                                          ██')
        print('██'                    f'HWID: {hwid}         '                     '       ██')
        print('██                                                          ██')
        print('██████████████████████████████████████████████████████████████')
        time.sleep(2000)

except:
    time.sleep(5)
    os._exit()
print("█████████████████████████████████████████████████")
print("██                                             ██")
print("██           Successfully logged in.           ██")
print("██                                             ██")
print("█████████████████████████████████████████████████")
