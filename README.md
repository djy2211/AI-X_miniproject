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

# 구현 기능
face_recognaition 모델을 이용하여 얼굴 인식 기능을 활용한 출입통제시스템 구현

FastAPI를 이용하여 서버를 구현

사진을 등록하면, 그 사진과 유사한 얼굴을 인식

등록 시, 로컬에 사진이 다운로드되고 데이터베이스에 이름과 사진 경로가 저장

데이터베이스의 경로에 저장된 사진들과 Cam으로 입력받은 이미지를 비교하여 얼굴인식
