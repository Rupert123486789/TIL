# CSS Layout

* **CSS layout techniques**

  * Display, Position, Float(CSS1, 1996), 💥Flexbox(2012), Grid(2017)

  * 기타 : Responsive Web Design(2010), Media Queries(2012)

    

---



### 1.  float

* **CSS 원칙 I**

  * ![image-20220212143039621](css_layout(web2).assets/image-20220212143039621.png)
  * 모든 요소는 ✨네모(박스모델)이고, 위에서부터 아래로, 왼쪽에서 오른쪽으로 쌓인다.(✨좌측 상단에 배치)
  * 어떤 요소를 깜싸는 형태로의 배치는? 혹은 좌/우측에 배치는?
    * ![image-20220212143225050](css_layout(web2).assets/image-20220212143225050.png)

* **Float**

  * 박스를 왼쪽혹은 오른쪽으로 이동시켜 텍스트를 포함 인라인 요소들이 주변을 wrapping 하도록 함 (block 주변을 감쌈).
  * 요소가 Normal flow를 벗어나도록 함.(Positioning- absolute: static이 아닌 부모 / fixed : 브라우저 (viewpoint))
  * ![image-20220212151924158](css_layout(web2).assets/image-20220212151924158.png)
  * none : 기본값
  * left : 요소를 왼쪽으로 띄움
  * right : 요소를 오른쪽으로 띄움
    * ![image-20220212143515242](css_layout(web2).assets/image-20220212143515242.png)

* **Clearing Float**

  * ![image-20220212144127241](css_layout(web2).assets/image-20220212144127241.png)
  * ![image-20220212152000167](css_layout(web2).assets/image-20220212152000167.png)
  * Float는 Normal Flow에서 벗어나 부동 상태(떠 있음)
  * 따라서, 이후 요소에 대하여 Float 속성이 적용되지 않도록 Clearing이 필수적임.
    * ::after : 선택한 요소의 맨 마지막 자식으로 가상 요소를 하나 생성(✨가상 의사 선택자)
      * 보통 content 속성과 함께 짝지어, 요소에 장식용 콘텐츠를 추가할 때 사용
    * clear 속성 부여
    * ![image-20220212144117798](css_layout(web2).assets/image-20220212144117798.png)

* **Float 정리**

  * Float는 레이아웃을 구성하기 위해 필수적으로 활용 되었으며, 최근엔 Flexbox, Grid 등장과 함께 사용도가 낮아짐

  * Float 활용 전략 : Normal Flow에서 벗어난 레이아웃 구성
    * 원하는 요소들을 Float로 지정하여 배치
    * ✨부모 요소에 반드시 clearing Float를 하여 이후 요소부터 Normal Flow를 가지도혹 규정



---



### 2. Flexbox

* **💥CSS Flexible Box Layout**
  * 행과 열 형태로 아이템들을 배치하는 💥1차원 레이아웃 모델 → main axis
  * 축 : 💥가로 세로로 외우지말고 개념을 외우자
    * main axis(메인 축) : 정렬을 하는 기본 방향 축
    * cross axis(교차 축) : 정렬을 하는 방향의 수직 축
  * 구성 요소
    * Flex Container(부모 요소)
    * Flex Item(자식 요소)
  * ![image-20220212144639171](css_layout(web2).assets/image-20220212144639171.png)
  * Flexbox 축
    * ![image-20220212144742812](css_layout(web2).assets/image-20220212144742812.png)
  * Flexbox 구성 요소
    * Flex Container(부모 요소)
      * flexbox 레이아웃을 형성하는 가장 기본적인 모델
      * Flex Item들이 놓여있는 영역
      * ✨display 속성을 flex 혹은 inline-flex로 지정
    * Flex Item(자식 요소)
      * 컨테이너에 속해 있는 컨텐츠(박스)
    *  ![image-20220212145018757](css_layout(web2).assets/image-20220212145018757.png)
  * 왜 Flexbox를 사용해야 할까?
    * 이전까지 Normal Flow를 벗어나는 수단은 Float 혹은 Position 이었음
    * 그러나, (수동 값 부여 없이) 1. 수직 정렬, 2. 아이템의 너비와 높이 혹은 간격을 동일하게 배치하기 어려움.
    * ![image-20220212145206860](css_layout(web2).assets/image-20220212145206860.png)
  
* **Flex 속성**
  * 배치 설정
    * flex-direction
    * flex-wrap
  * 공간 나누기
    * justify-content (main axis)
    * align-content (cross axis) : 자주 쓰이지는 않음
  * 정렬
    * align-items (모든 아이템을 cross axis 기준으로)
    * aligh-self (개별 아이템)

* **배치 설정(flex-direction & flex-wrap)**
  * flex-direction
    * Main axis 기준 방향 설정
    * 역방향의 경우 HTML 태그 선언 순서와 시각적으로 다르니 유의 (웹 접근성에 영향)
    * ![image-20220212145611650](css_layout(web2).assets/image-20220212145611650.png)
  * flex-wrap
    * 아이템이 컨테이너를 벗어나는 경우 해당 영역 내에 배치되도록 설정
    * 즉, 기본적으로 컨테이너 영역을 벗어나지 않도록 함
    * ![image-20220212145644616](css_layout(web2).assets/image-20220212145644616.png)
  * flex-direction : Main axis의 방향을 설정
  * flex-wrap : 요소들이 강제로 한 줄에 배치 되게 할 것인지 여부 설정
    * nowrap (기본 값) : 한 줄에 배치
    * wrap : 넘치면 그 다음 줄로 배치
  * flex-flow
    * flex-direction 과 flex-wrap 의 shorthand
    * flex-direction과 flex-wrap에 대한 설정 값을 차례로 작성
  * Ex.  flex-flow : row nowrap;
  
* **공간 나누기(justify-content & align-content)**
  * justify-content
    * Main axis를 기준으로 공간 배분
    * ![image-20220212152113388](css_layout(web2).assets/image-20220212152113388.png)
    
  * align-content
    * Cross axis를 기준으로 공간 배분 (아이템이 한 줄로 배치되는 경우 확인할수 없음)
    
      
    
    * ![image-20220212150217565](css_layout(web2).assets/image-20220212150217565.png)
    
  * 공간 배분
    * flex-start (기본값) : 아이템들을 axis 시작점으로
    * flex-end : 아이템들을 axis 끝 쪽으로
    * center : 아이템들을 axis 중앙으로
    * space-between : 아이템사이의 간격을 균일하게 분배
    * space-around : 아이템을 둘러싼 영역을 균일하게 분배 (가질 수 있는 영역을 반으로 나눠서 양쪽에)
    * space-evenly : 전체 영역에서 아이템 간 간격을 균일하게 분배
  
* **정렬(align-items)**
  * align-items
    * 모든 아이템을 Cross axis를 기준으로 정렬
    * ![image-20220212150508428](css_layout(web2).assets/image-20220212150508428.png)
  * align-self
    * 개별 아이템을 Cross axis 기준으로 정렬
      * ✨주의! 해당 속성은 컨테이너에 적용하는 것이 아니라 개별 아이템에 적용
    * ![image-20220212150553597](css_layout(web2).assets/image-20220212150553597.png)
  * align-items & align-self
    * Cross axis를 중심으로
      * stretch (기본 값) : 컨테이너를 가득 채움
      * flex-start : 위
      * flex-end : 아래
      * center : 가운데
      * baseline : 텍스트 baseline에 기준선을 맞춤
  
* **Flex에 적용하는 속성**
  * 기타 속성
    * flex-grow : 남은 영역을 아이템에 분배
    * order : 배치 순서
    * ![image-20220212150858830](css_layout(web2).assets/image-20220212150858830.png)
    * flex-shirink : 영역이 부족할때 축소를 할지 
    * flex-basis : item의 기본 크기를 결정
  
* **활용 레이아웃**
  * 수직 수평 가운데 정렬
    * ![image-20220212150950838](css_layout(web2).assets/image-20220212150950838.png)
  * 카드 배치
    * ![image-20220212151005113](css_layout(web2).assets/image-20220212151005113.png)

---



* **정리**
  * float → flex(페러다임)
  * block / inline → axis(main, cross) / container : 정렬을 쉽게
