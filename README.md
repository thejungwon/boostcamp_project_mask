# 부스트캠프 마스크인식 웹사이트

## Getting Started
![image](demo.gif)
### Prerequisites
부스트캠프 마스크인식 모델이 있어야 합니다.
### Install

#### Server
현재 서버코드는 모델관련된 코드가 적용되어 있지 않습니다. 이 부분은 대회에서 사용하셨던 inference코드를 수정하여서 적용해주세요
```
pip install -r requirements.txt
python main.py
```

기본적으로 랜덤하게 18가지의 마스크 관련 클래스중 하나를 반환되도록 설정되었습니다.

#### Client
현재 서버사이드 렌더링을 사용하고 있으므로, 서버의 주소로 접근을 하시면됩니다.


### Trouble Shooting
- 바로 Ai Stages서버에 접근을 하시면 서버에 SSL인증서가 없어 https의 형태로 접근을 못하게되는데, 이 경우 크롬에서 카메라 접근을 차단하게됩니다 
  - 본인의 환경에서 시연하는 경우에는 크롬에서 `chrome://flags/#unsafely-treat-insecure-origin-as-secure` 에 현재 서버 주소를 입력하는 식으로 우회할 수 있습니다.
- 퍼블릭하게 오픈하려는 경우 SSL인증서를 제공하는 환경에서 서버를 구축하셔야합니다.
  - 이때 서버와 클라이언트를 분리해서, 클라이언트는 SSL인증서가 있는 곳에 호스팅을 하시고, 서버는 Ai Stages에서 돌리신다음 `fetch` 함수 부분에 주소를 바꿔주세요!
  - GPU가 필요 없는 경우에는 SSL 인증서가 있는 곳에서 그냥 서버사이드 렌더링을 진행하시면 됩니다.
- 개인 컴퓨터에서 작업할 경우 `localhost`로 접근을 하게되면 위의 이슈와 무관합니다.



