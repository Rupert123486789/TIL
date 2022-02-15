* Bootstrap
  * form overview : 로그인 화면
  * modal : button 누르면 modal 창이 열림, target = # modal 과 id ="modal"일치 시켜야됨 / 토글 → 스위치 / 제대로 된 위치에 집어넣기
  * position fixed (normal flow 벗어남) / position sticky (normal flow 지킴)
  * card : style width 있으면 카드 겹침 / gutter 넣으면 공백생김
  * carousel : 이미지 슬라이드 / container로 크기 맞춰줌
  * alters  / badge / buttons / close button / off canvas






* Tip
  * ,가 아닌 띄어쓰기로 구분
  * 크롬 개발자 도구(Ctrl+Shift+i / F12 / 우클릭+검사 / ... + 관리자 도구)
  * 태그 열고 닫은다음 바로바로 테스트!!
  * `<!-- --> `: 주석
  * `.` 시작 -> class 선택자 / `#` 시작 -> id 선택자
  * Lorem Ipsum -> Lorem 300 : 글시를 채워넣을때 사용
  * 한글 입숨도 있으나 이상함
  * style 태그는 웬만하면 쓰지 않는게 좋음 : 우선순위가 높아 꼬일 가능성 있음
  * 움직일 수 있는 공간 파악이 중요 : 부모에서 공간을 설정하면 자식도 영향 받음
  * 구글폰트 : 폰트 선택 → selectr this style → @import 누르고 복사해서 쓰기
  * snippet generator




* 단축키
  * a(다른 태그도 가능) + tab : tag 자동 생성
  * Alt + Shift + 방향키 : tag 복사
  * Alt + B
  * ! + tab : 기본틀 자동 완성
  * ul > li*3 처럼 단축문으로 형식을 불러올 수 있음
  * Alt 누른 상태에서 각각을 클릭해서 한번에 변경 가능
  * Ctrl + d : 같은 단어 수정 가능(VS code)
  * Ctrl + alt + 방향키(위아래) / Alt+클릭 : multiline selector



* 실력 향상
  * clone coding(여러 사이트를 그대로 만들어 보자)
  * CSS + 키워드 + mdn 검색 
  * 구글에 답이 있다(💥구글링)
  * 관리자 도구 이용하기
  * bootstrap
  * ✨flexbox froggy : flexbox 연습 사이트
  * d2 flex
  * flukeout
  * 마이 리얼트립 최적화
  * animate.css



* 관통
  * CSS 작성 순서 : 구글은 알파벳 순 / NHN은 관련성 순
  * Bootstrap 활용 : 문서상에서 비슷한것을 찾기 / 개발자 도구 활용
    * cdn 우선 넣기
    * nav bar : 이름변경, link active, fixed top (normal flow 벗어나서 이미지 잘림), sticky top (margin 안 줘도 됨 / 주로 사용)
    * carousel
    * grid system
      * container → row → col
    * modal 
      * data-bs-toggle="modal"
      * data-bs-target="# ~~~"
      * id="~~~"
        * target과 id 일치 / # : 아이디 선택자 / toggle 바꾸지 X
        * card 안으로 modal 넣으면 안됨(body 태그 안에 넣기)
        * HTML top level에 넣기 : 다른 요소에 영향을 안 받기 위해서
    * flex glow 설정
    * cheat sheet : bootstrap에서 보고 싶은거 다 있음

​		
