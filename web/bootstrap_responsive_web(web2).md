# Bootstrap

### 1. Bootstrap

* ![image-20220212152404091](bootstrap_responsive_web(web2).assets/image-20220212152404091.png)The world most popular fron-end open source (rank 9)
* Bootstrap으로 만든 사이트 : 넷플릭스
* ![image-20220212152423326](bootstrap_responsive_web(web2).assets/image-20220212152423326.png)
* ![image-20220212152431364](bootstrap_responsive_web(web2).assets/image-20220212152431364.png)
* **CDN**
  * Content Delivery (Distribution) Network
  * 컨텐츠 (CSS, JS, Image, Text 등)을 효율적으로 전달하기 위해 여러 노드에 가진 네트워크에 데이터를 제공하는 시스템
  * 개별 end-user의 가까운 서버를 통해 빠르게 전달 가능 (지리적 이점), 외부 서버를 활용함으로써 본인 서버의 부하가 적어짐
  * 💥bootstrap을 쓰려면 CDN을 가져오자
* **spacing**
  * mt-1
    * ![image-20220212152929538](bootstrap_responsive_web(web2).assets/image-20220212152929538.png)
  * 브라우저 `<html>`의 root 글꼴 크기는 16px
  * ![image-20220212152837294](bootstrap_responsive_web(web2).assets/image-20220212152837294.png)
  * mx-0
    * ![image-20220212152946185](bootstrap_responsive_web(web2).assets/image-20220212152946185.png)
  * mx-auto : 수평 중앙 정렬
    * ![image-20220212152958503](bootstrap_responsive_web(web2).assets/image-20220212152958503.png)
  * py-0
    * ![image-20220212153026259](bootstrap_responsive_web(web2).assets/image-20220212153026259.png)
  * 💥spacing 종합
    * ![image-20220212153102103](bootstrap_responsive_web(web2).assets/image-20220212153102103.png)
* **Color**
  * ![image-20220212153138564](bootstrap_responsive_web(web2).assets/image-20220212153138564.png)
* **Responsive Web Design**
  * 다양한 화면 크기를 가진 디바이스들이 등장함에 따라 responsive web design 개념이 등장
  * 반응형 웹은 별도의 기술 이름이 아닌 웹 디자인에 대한 접근 방식, 반응형 레이아웃 작성에 도움이 되는 사례들의 모음 등을 기술하는데 사용되는 용어
  * 예시
    * Media Queries, Flexbox, Bootstrap Grid System, The viewport meta tag

### 	

---

### 2. Grid system (web design)

* **Grid system**
  * 요소들의 디자인과 배치에 도움을 주는 시스템
  * 기본 요소
    * Column : 실제 컨텐츠를 포함하는 부분
    * Gutter : 컬럼과 컬럼 사이의 공간 (사이 간격)
    * Container : Column들을 담고 있는 공산
    * ![image-20220212153552458](bootstrap_responsive_web(web2).assets/image-20220212153552458.png)
  * Bootstrap Grid system은 flexbox로 제작됨
  * container, rows, column으로 컨텐츠를 배치하고 정렬
  * 💥반드시 기억해야 할 2가지!
    1. 12개의 column(row를 넣어줘야 12개로 됨)
    2. 6개의 grid breakpoints
* **Grid system breakpoints**
  * ![image-20220212153836463](bootstrap_responsive_web(web2).assets/image-20220212153836463.png)
  * ![image-20220212153900811](bootstrap_responsive_web(web2).assets/image-20220212153900811.png)
  * ![image-20220212154635846](bootstrap_responsive_web(web2).assets/image-20220212154635846.png)
  * **💥breakpoint, nesting, offset💥**

---

### 마무리

* 각각의 기술은 저마다 용도가 있고, 장단점이 있으며, 어떤 기술도 독립적인 용도를 갖추도록 설계 되지는 않았음.
* 특정 상황에 어떤 기술이 가장 적합한 도구가 될 것인지 파악하는 데에는 많은 경험이 뒷받침 되어야함.

