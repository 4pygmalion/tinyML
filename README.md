# tinyML
Arduino tinyML

### IDE for vscode
- install Arduino IDE 1.x (the vscode extention supports only 1.x not 2.x)
- open setting.json and write as follow:
```
{
    "arduino.path": "C:\\Program Files (x86)\\Arduino",
    "arduino.useArduinoCli": true,
    "arduino.logLevel": "info",
    "arduino.allowPDEFiletype": false,
    "arduino.enableUSBDetection": true,
    "arduino.disableTestingOpen": false,
    "arduino.skipHeaderProvider": false,
    "arduino.additionalUrls": [
        "https://raw.githubusercontent.com/VSChina/azureiotdevkit_tools/master/package_azureboard_index.json",
        "http://arduino.esp8266.com/stable/package_esp8266com_index.json"
    ],
    "arduino.defaultBaudRate": 9600,
    "arduino.useArduinoCli": false,
}
```
- Select environment including Arduino device and port
![env](/images/environ.png)


### PinMap
- 핀맵(PinMap)을 회로내 장치가 몇 번 핀에 연결되어있는지 확인할 수 있는 지도이다.
- P0. 13은 프로그래밍번호, 13은 핀번호라고 함.
- 예를 들어, 빌트인LED(BUILT_IN LED)은 13번 핀을 의미합니다.
- P1.13과 같이 이런 핀은 논리적으로 PIN을 그룹화한것을 의미합니다.
예제)![pinmap](/images/pinmap.png)


### Contents
```
C:.
├─.vscode
├─images
└─projects
    ├─ledblink  : LED PIN 입출력 예제
    └─sin_wave  : 사인파 예측 예제
```