## ![펭귄](template_view_routing.assets/펭귄.png)

<br>

## Django Review

<br>

* 4 : 각각 model을 하나의 데이터 베이스 테이블에 매핑
* 5 : model로 레이아웃을 짜고, 그 레이아웃 기반으로 DB 생성
* 12 : 생산성 때문에 사용
* 14-1 : 상속, 이미  만들어진 (Model) 사용
* 14-2 : id는 장고가 알아서 생성
* 24-1, 2 : 이미 처음부터 존재하는 앱들
* 28-1 : 출력 표현을 바꾸는 것 뿐이라 DB에 영향을 주지는 않음 (makemigrations 해도 변경 없음)
  * 변경 사항에 따라 다름 헷갈리면 그냥 makemigrations 하자
* 31 : objects는 고정
* 43 : 유일한 값 조회
* 44 : 없으면 그냥 빈 쿼리셋을 줌 / 오류 X
* 49 : 삭제한 값 재사용 X, auto increment 설정
* 49-5 : 추가할 때마다 전부 찾아서 수정 할 수 없으므로 url 태그 사용
* 49-6 : app_name : name

* 49-7 : 유효성 검사를 위해 create() 말고 다른 방식 사용
* 49-8, 9 : input의 name 값에서 왔음
* 49-10 : 수정
* 49-13 : 요청이 2개
* 49-14 : 글을 쓰고 detail page 보고싶어 / redirect : 새로운 요청이 가는것(요청을 해야 응답을 하기 때문에)
