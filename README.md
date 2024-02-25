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

FastAPI 를 이용하여 

## 사진을 등록하는 페이지 ( Home )
![image](https://github.com/djy2211/AI-X_miniproject/assets/131187694/1567a68d-c361-4232-a1df-ba02ba551329)

## 캠을 이용하여 사진을 저장하는 페이지 ( Search )
![image](https://github.com/djy2211/AI-X_miniproject/assets/131187694/2918ec0d-b2d2-4821-a37b-be102cea5787)

## 등록된 얼굴을 인식하는 페이지 ( detect )
![image](https://github.com/djy2211/AI-X_miniproject/assets/131187694/18957c45-3a4c-44e3-b74b-1d74255b6050)



# Home
## 사진을 등록한 후, Add를 클릭하면 Static 폴더에 등록한 사진이 저장

## DB에 index 생성 
> User name 과 img 파일 경로가 DB에 저장
> Delete 시, DB에 저장된 정보와 Static에 저장된 사진이 같이 삭제
> ![image](https://github.com/djy2211/AI-X_miniproject/assets/131187694/c520c990-50ad-4ce2-a7b9-9ede9f4228b7)




# Search
## 웹 캠을 통하여 입력받은 이미지를 화면에 출력

## "캡쳐하기"를 클릭하면 "저장히기" 클릭 시, 저장될 이미지 파일을 확인할 수 있음.
> ![image](https://github.com/djy2211/AI-X_miniproject/assets/131187694/dcacc5da-d0ae-4879-9c16-f2a45cd7cce4)


# detect

## Home 에 등록된 사진을 기반으로 detect 기능 수행

## DB에 저장된 경로를 확인하여 사진 파일 read, 사진의 얼굴인 경우 'access' 표시
> ![image](https://github.com/djy2211/AI-X_miniproject/assets/131187694/be158d0d-56b4-473d-b6ca-799432e4f451)
