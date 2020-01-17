# Sound to text

## 1. mp3 to 16kHz wav
```
sudo apt-get install ffmpeg
ffmpeg -i in.mp3 -acodec pcm_s16le -ac 1 -ar 16000 out.wav
```


## 2. Sound to text (stt.py)
```
#-*- coding:utf-8 -*-
import urllib3
import json
import base64
openApiURL="http://aiopen.etri.re.kr:8000/WiseASR/Recognition"
accessKey="6e5ae159-2c10-4383-b8dc-a2c62f33afec"
audioFilePath="./out.wav"
languageCode="korean"

file=open(audioFilePath, "rb")
audioContents=base64.b64encode(file.read()).decode("utf8")
file.close()

requestJson = {
    "access_key": accessKey,
    "argument": {
        "language_code": languageCode,
        "audio": audioContents
    }
}

http=urllib3.PoolManager()
response=http.request(
    "POST",
    openApiURL,
    headers={"Content-Type": "application/json; charset=UTF-8"},
    body=json.dumps(requestJson)
)

print("[responseCode] " + str(response.status))
print("[responBody]")
print(response.data)
```
