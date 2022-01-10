import urequests
import os
import uasyncio
import time
import ujson
def package_installer(cmd_arr):
    if cmd_arr[2] == "test":
        """
        response = urequests.get("http://jsonplaceholder.typicode.com/posts")
        time.sleep(0.5)
        app = response.text
        os.chdir("/")
        os.mkdir("/app/test_pkg")
        f = open("/app/test_pkg/testapp.py",'w',encoding='utf-8')
        f.write(app)
        f.close()
        """
        os.chdir("/dev/pkginstaller")
        """
        commands_file = open("/dev/pkginstaller/pkgmanager.py","a+",encoding='utf-8')
        commands_file.write('\telif cmd_array[0] == "testpkg":\n\t\tprint("Hello from pkg installer")\n')
        """
        with open("/dev/pkginstaller/pkgmanager.py","a+",encoding='utf-8') as f:
            f.write('    elif cmd_arr[0] == "testpkg":\n        print("Hello from pkg installer")\n')
        print("Test success")
    else:
        url = "https://raw.githubusercontent.com/gooz-project/gooz_packages/main/"+cmd_arr[2]+".json"
        print(url)
        response_url = urequests.get(url)
        response_text = response_url.text
        print(response_text)
        time.sleep(0.5)
        response = ujson.loads(response_text)
        os.chdir("/")
        os.mkdir("/app/"+response["name"])
        for codes in response["codes"]:
            with open("/app/"+str(response["name"])+"/"+str(codes["filename"]),"w+",encoding='utf-8') as f:
                codes["code"] = codes["code"].replace("\\n","\n")
                f.write(str(codes["code"]))
        os.chdir("/dev/pkginstaller")
        with open("/dev/pkginstaller/pkgmanager.py","a+",encoding='utf-8') as f:
            response["managersnip"] = response["managersnip"].replace("\\n","\n")
            f.write(response["managersnip"])
        print("Package has been installed")

def package_uninstall(cmd_arr):
    try:
        os.chdir("/app/"+cmd_arr[2])
        files = os.listdir()
        for i in files:
            os.remove(i)
        os.rmdir("/app/"+cmd_arr[2])
        print("Package has been deleted")
        
    except:
        print("Package not found")