import urllib.request as urlrequest
import sys
def getData(url):
    with open("dblp.xml", "w") as dblpf:
        with urlrequest.urlopen(url=url) as response:
            content_length = response.length
            block_size = 1024
            block_nums = content_length//block_size
            print("[response length]==>"+str(block_nums)+"kb")
            for i in range(block_nums):
                print("【总共"+str(block_nums)+"块，当前读取第"+str(i)+"块】")
                info = {"closed":response.closed,"chunked":response.chunked,"code":response.code,\
                        "msg":response.msg}
                print("【Http状态】："+str(info))
                content = response.read(block_size)
                content = str(content)
                # content = str(response.read(block_size))
                print(content[:100])
                dblpf.write(content)
                dblpf.flush()

if __name__ == "__main__":
    url = "https://hpi.de/fileadmin/user_upload/fachgebiete/naumann/projekte/repeatability/DBLP/dblp50000.xml"
    getData(url=url)
    print(sys.getdefaultencoding())