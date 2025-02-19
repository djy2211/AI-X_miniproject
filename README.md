# 27CM_miniProject

# 가상환경 python 버전
- python=3.10

# 설치한 패키지
- pip install fastapi
- pip install "uvicorn[standard]"
- pip install sqlalchemy
- pip install numpy
- pip install jinja2
- pip install opencv-python
- pip install face_recognition
- pip install python-multipart

### pip 이후, 터미널에서 "uvicorn main:app" 으로 실행



# 구현 기능

## Face_recognition 을 이용하여 등록한 얼굴을 인식하는 시스템 구현

Face_recognition / https://github.com/ageitgey/face_recognition

위 모델을 이용하여, 출입관련 통제에 사용할 수 있는 일부 기능 구현


웹캠을 통하여 실시간으로 영상을 입력 받아서, 
그 입력받은 영상에 DB에 등록된 사람 얼굴이 있으면 통과, 없으면 거부

위 기능을 구현하기 위해서, 크게 아래의 3가지 기능들이 필요함
1. 실시간으로 웹캠을 통하여 영상을 입력받는 기능
2. 통과할 수 있는 권한을 부여할 수 있도록 유저를 등록하는 기능
3. 등록된 유저가 웹캠에 등장할 경우, 인식하여 통과를 출력하는 기능


위 기능들을 FastAPI를 통하여 로컬서버를 통한 웹페이지에서 구현되도록 코드 작성


# 페이지 관련 내용

## 1 사진을 등록하는 페이지 ( Home )
<img src="https://github.com/djy2211/AI-X_miniproject/assets/131187694/1567a68d-c361-4232-a1df-ba02ba551329" width="400" height="320"/>

위에서 설명한 2번 기능(유저를 등록하는 기능)을 구현하기 위하여 작성한 페이지

위 페이지에서 유저의 사진을 db로 보내서 등록하거나 등록된 유저의 사진을 지우는 기능을 위 페이지에서 사용 가능

#

## 2 캠을 이용하여 사진을 저장하는 페이지 ( Search )
<img src="https://github.com/djy2211/AI-X_miniproject/assets/131187694/2918ec0d-b2d2-4821-a37b-be102cea5787" width="400" height="320"/>

꼭 필요한 기능은 아니지만, 웹캠을 통하여 사진을 찍기위하여 만든 페이지

위 페이지에서 웹캠을 통하여 입력받은 이미지를 저장할 수 있음

위 페이지에서 저장한 이미지를 Home 기능을 통하여 db에 저장할 수 있음.

#

## 3 등록된 얼굴을 인식하는 페이지 ( detect )
<img src="https://github.com/djy2211/AI-X_miniproject/assets/131187694/18957c45-3a4c-44e3-b74b-1d74255b6050" width="400" height="320"/>

1번 기능과 3번 기능을 구현하기 위한 페이지

위 페이지에서는 실시간으로 웹캠을 통하여 이미지를 입력받고, 입력받은 이미지에 db에 저장된 유저가 있는 경우 인식

#

## DB에 저장된 정보를 확인하여 'access' 표시
<img src="https://github.com/djy2211/AI-X_miniproject/assets/131187694/be158d0d-56b4-473d-b6ca-799432e4f451" width="400" height="320"/>
