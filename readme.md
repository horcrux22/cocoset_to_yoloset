#구조 수정중입니다.
# 설명

```json_to_text.py``` : json파일로 되어있는 coco format 을 yolo format으로 변경후 labels 디렉토리에 txt파일로 저장

```move_jpg.py``` : 폴더내 json파일과 jpg 파일이 있을때 jpg 파일은 images폴더로 이동시키고 json 파일은 삭제

```move_img_label.py``` : move_jpg.py 로 작업완료후 data 하위디렉토리에 images,labels 폴더를 만들어서 jpg파일과 txt파일이름을 변경후 전부 옮김

폴더구조는 data -> 상위폴더(000002_000054) -> 하위폴더(n000002) -> jpg,json 에서

data -> images,labels 으로 변경



# 사용방법

1. >```pip install pillow```

2. json_to_text.py , move_jpg.py 파일을 data폴더에 넣기

3. >```python json_to_text.py```

4. 위 과정을 했을시 jpg,json 파일과 생성된 labels 폴더가 있습니다.

5. jpg 옮기고 json 파일을 삭제하기위해 아래 명령어 실행

6. >```python move_jpg.py```

7. 하위 폴더 내에 images,labels 폴더가 생성

8. >```python move_img_label.py```

9. 하위 폴더 내에 images,labels 폴더내에 있는 파일들을 이름을 하위폴더 이름에 파일이름을 추가하여 (하위폴더이름_파일이름) 변경 

10. data 하위 디렉토리에 images,labes를 생성후 그 파일들을 전부 이동시킵니다.
