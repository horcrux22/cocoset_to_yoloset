# CONVERT_COCO_TO_YOLO

COCO format convert to YOLO format

### System Requirements
  - Ubuntu 20.04
  - python 3.7
  - python packages: requirements.txt

### 사용방법
  - 디렉토리 구조는 data -> 상위폴더(000002_000054) -> 하위폴더(n000002) -> jpg,json 순으로 되어있을때 사용가능합니다.
  - 결과값은 data/LABELS ,data/IMAGES 에 저장됩니다.
  - consts.py 파일 내 경로를 수정해서 사용합니다.
