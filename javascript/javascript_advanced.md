## ![펭귄](javascript_basic.assets/펭귄.png)

<br>

## Java Script Advanced

<br>

### 1. History of JavaScript

<br>

* **핵심 키워드**
  * 핵심 인물
  * JavaScript의 탄생
  * 브라우저 전쟁
  * 파편화와 표준화
  * JavaScript ES6+

<br>

* **핵심 인물**
  * 팀 버너스리(Tim Berners-Lee)
    * WWW, URL, HTTP, HTML 최초 설계자
    * 웹의 아버지
  * 브랜던 아이크(Brendan Eich)
    * JavaScript 최초 설계자
    * 모질라 재단 공동 설립자
    * 코드네임 피닉스 프로젝트 진행
      * 파이어폭스의 전신

<br>

* **JavaScript의 탄생**
  * 1994년 당시 넷스케이프 커뮤니케이션스사의 Netscape Navigator(NN) 브라우저가 전 세계 점유율을 80% 이상 독점하며 브라우저의 표준 역할을 함
  * 당시 넷스케이프에 재직 중이던 브랜던 아이크가 HTML을 동적으로 동작하기 위한 회사 내부 프로젝트를 진행 중 JS를 개발
  * JavaScript 이름 변천사
    * Moche -> LiveScript -> JavaScript(1995)
  * 그러나 1995년 경쟁사 마이크로소프트에서 이를 채택하여 커스터마이징한 Jscript를 만듦
  * 이를, IE 1.0에 탑재 -> 1차 브라우저 전쟁의 시작

<br>

* **제1차 브라우저 전쟁**
  * 넷스케이프 vs 마이크로소프트(이하 MS)
  * 빌 게이츠 주도하에 MS는 1997년 IE 4를 발표하면서 시장을 장악하기 시작
    * 당시 윈도우 OS의 시장 점유율은 90%
    * 글로벌 기업 MS의 공격적인 마케팅
  * MS의 승리로 끝나며 2001년부터 IE의 점유율은 90%를 상회
  * 1998년 넷스케이프에서 나온 브랜던 아이크 외 후계자들은 모질라 재단을 설립
    * 파이어폭스를 통해 IE에 대항하며 꾸준히 점유율을 올려 나감
  * MS의 폭발적 성장, IE3에서 자체적인 JScript를 지원, 호환성 문제로 크로스 브라우징 등의 이슈 발생
  * 이후 넷스케이프 후계자들은 모질라 재단 기반의 파이어폭스를 개발
    * ![image-20220501162411997](javascript_advanced.assets/image-20220501162411997.png)

<br>

* **제2차 브라우저 전쟁**
  * MS vs Google
  * 2008년 Google의 Chrome(이하 크롬) 브라우저 발표
  * 2011년 3년 만에 파이어폭스의 점유율을 돌파 후 2012년부터 전 세계 점유율 1위 등록
  * 크롬의 승리 요인
    * 압도적인 속도
    * 강력한 개발자 도구 제공
    * 웹 표준

<br>

* **파편화와 표준화**
  * 제1차 브라우저 전쟁 이후 수많은 브라우저에서 자체 자바스크립트 언어를 사용하게 됨
  * 결국 서로 다른 자바스크립트가 만들어지면서 크로스 브라우징 이슈가 발생하여 웹 표준의 필요성이 제기
  * 크로스 브라우징(Cross Browsing)
    * W3C에서 채택된 표준 웹 기술을 채용하여 각각의 브라우저마다 다르게 구현되는 기술을 비슷하게 만들되, 어느 한쪽에 치우치지 않도록 웹 페이지를 제작하는 방법론(동일성이 아닌 동등성)
    * 브라우저마다 렌더링에 사용하는 엔진이 다르기 때문
  * 1996년부터 넷스케이프는 표준 제정의 필요성을 주장
    * ECMA 인터내셔널(정보와 통신 시스템을 위한 국제적 표준화 기구)에 표준 제정 요청
  * 1997년 ECMAScript 1(ES1) 탄생
  * 제1차 브라우저 전쟁 이후 제기된 언어의 파편화를 해결하기 위해 각 브라우저 회사와 재단은 표준화에 더욱 적극적으로 힘을 모으기 시작

<br>

* **JavaScript ES6+**
  * 2015년 ES2015(ES6) 탄생
    * "Next-gen of JS"
    * JavaScript의 고질적인 문제들을 해결
    * JavaScript의 다음 시대라고 불릴 정도로 많은 혁신과 변화를 맞이한 버전
    * 이때부터 버전 순서가 아닌 출시 연도를 붙이는 것이 공식 명칭이나 통상적으로  ES6라 부름
    * 현재는 표준 대부분이 ES6+로 넘어옴

<br>

* **Vanilla JavaScript**
  * 크로스 브라우징, 간편한 활용 등을 위해 많은 라이브러리 등장(jQuery 등)
  * ES6 이후, 다양한 도구의 등장으로 순수 자바스크립트 활용의 증대

<br>

* **정리**
  * History of JavaScript & Browser
    * 브라우저 전쟁
    * 파편화와 표준화의 투쟁
  * 브라우저 전쟁의 여파
    * Cross Browsing Issue
    * 표준화(통합)를 위한 노력
    * Vanilla JavaScript

<br>

---

<br>

### 2. DOM 조작

<br>

* **DOM 조작 - 개념**(✨문서 조작 - string을 조작하는게 아니고, 그것이 해석된 객체를 조정)
  * Document는 문서 한 장(HTML)에 해당하고 이를 조작
  * DOM 조작 순서
    1. 선택(Select)
    2. 변경(Manipulation)

<br>

* **DOM 조작 - Document 위치**
  * ![image-20220501163315386](javascript_advanced.assets/image-20220501163315386.png)

<br>

* **DOM 관련 객체의 상속 구조**
  * EventTarget
    * Event Listener를 가질 수 있는 객체가 구현하는 DOM 인터페이스
  * Node
    * 여러가지 DOM 타입들이 상속하는 인터페이스
  * ![image-20220501163406972](javascript_advanced.assets/image-20220501163406972.png)
  * Element
    * Document 안의 모든 객체가 상속하는 가장 범용적인 인터페이스
    * 부모인 Node와 그 부모인 EventTarget의 속성을 상속
  * Document
    * 브라우저가 불러온 웹 페이지를 나타냄
    * DOM 트리의 진입점(entry point) 역할을 수행
  * HTMLElement
    * 모든 종류의 HTML 요소
    * 부모 element의 속성 상속
  * ![image-20220501163538596](javascript_advanced.assets/image-20220501163538596.png)

<br>

- **DOM 선택 - 선택 관련 메서드**
  - 💥**document.querySelector(selector)**
    - 제공한 선택자와 일치하는 element 하나 선택
    - 제공한 CSS selector를 만족하는 첫 번째 element 객체를 반환(없다면 null)
  - ✨**document.querySelectorAll(selector)**
    - 제공한 선택자와 일치하는 여러 element를 선택
    - 매칭 할 하나 이상의 셀렉터를 포함하는 유효한 CSS selector를 인자(문자열)로 받음
    - 지정된 셀렉터에 일치하는 NodeList를 반환
  - getElementById(id)
  - getElementByTagName(name)
  - getElementByClassName(names)
  - querySelector(), querySelectorAll()을 사용하는 이유
    - id, class 그리고 tag 선택자 등을 모두 사용 가능하므로, 더 구체적이고, 유연하게 선택 가능
    - ex. document.querySelector('#id'), document.querySelectorAll('.class')

<br>

* **DOM 선택 - 선택 메서드별 반환 타입**
  1. 단일 element
     * getElementById()
     * querySelector()
  2. HTMLCollection
     * getElementsByTagName()
     * getElementsByClassName()
  3. NodeList
     * querySelectorAll()

<br>

* **DOM 선택 - HTMLCollection & NodeList**
  * 둘 다 배열과 같이 각 항목에 접근하기 위한 index를 제공(유사 배열)
  * HTMLCollection
    * name, id, index 속성으로 각 항목에 접근 가능
  * NodeList
    * index로만 각 항목에 접근 가능
    * 단, HTMLCollection과 달리 배열에서 사용하는 forEach 메서드 및 다양한 메서드 사용 가능
  * 둘 다 Live Collection으로 DOM의 변경사항을 실시간으로 반영하지만, querySelectorAll()에 의해 반환되는 NodeList는 Static Collection으로 실시간으로 반영되지 않음

<br>

* **DOM 선택 - Collection**
  * Live Collection
    * 문서가 바뀔 때 실시간으로 업데이트 됨
    * DOM의 변경사항을 실시간으로 collection에 반영
    * ex. HTMLCollection, NodeList
  * Static Collection(non-live)
    * DOM이 변경되어도 collection 내용에는 영향을 주지 않음
    * querySelectorAll()의 반환 NodeList만 static collection

<br>

* **DOM 선택 실습**
  * BEM
  * copy -> copy JS path

<br>

* **DOM 변경 - 변경 관련 메서드(Creation)**
  * **✨document.createElement()**
    * 작성한 태그 명의 HTML 요소를 생성하여 반환

<br>

* **DOM 변경 - 변경 관련 메서드(append DOM)**
  * ✨**Element.append()**
    * 특정 부모 Node의 자식 NodeList 중 마지막 자식 다음에 Node 객체나 DOMString을 삽입
    * 여려 개의 Node 객체, DOMString을 추가 할 수 있음
    * 반환 값이 없음
  * ✨**Node.appendChild()**
    * 한 Node를 특정 부모 Node의 자식 NodeList 중 마지막 자식으로 삽입(Node만 추가 가능)
    * 한번에 오직 하나의 Node만 추가할 수 있음
    * 만약 주어진 Node가 이미 문서에 존재하는 다른 Node를 참조한다면 새로운 위치로 이동

<br>

* **DOM 변경 실습**
  * Element.append()
  * Node.appendChild()

<br>

* **ParentNode.append() vs Node.appendChild()**
  * append()를 사용하면 DOMString 객체를 추가할 수도 있지만, .appendChild()는 Node 객체만 허용
  * append()는 반환 값이 없지만, appendChild()는 추가된  Node 객체를 반환
  * ✨append()는 여러 Node 객체와 문자열을 추가할 수 있지만, .appendChild()는 하나의 Node 객체만 추가할 수 있음

<br>

* **DOM 변경 - 변경 관련 속성(property)**
  * **💥Node.innerText**
    * Node 객체와 그 자손의 텍스트 컨텐츠(DOMString)를 표현 (해당 요소 내부의 raw text / 사람이 읽을 수 있는 요소만 남김)
    * 즉, 줄 바꿈을 인식하고 숨겨진 내용을 무시하는 등 최종적으로 스타일링이 적용된 모습으로 표현
  * **✨Element.innerHTML**
    * 요소(element) 내에 포함된 HTML 마크업을 반환
    * [참고] XSS 공격에 취약하므로 사용 시 주의 (✨사용자가 입력으로 스크립트 코드를 넣을 수 있음)

<br>

* **DOM 변경 실습**
  * innerText vs innerHTML

<br>

* **XSS(Cross-site Scripting)**
  * 공격자가 입력요소를 사용하여(`<input>`) 웹 사이트 클라이언트 측 코드에 악성 스크립트를 삽입해 공격하는 방법
  * 피해자(사용자)의 브라우저가 악성 스크립트를 실행하며 공격자가 엑세스 제어를 우회하고 사용자를 가장 할 수 있도록 함
  * 게시판이나 메일 등 악성 자바스크립트 코드를 삽입해 민감한 정보를 탈취할 수 있음

<br>

* **DOM 삭제 - 삭제 관련 메서드**
  * ChildNode.remove()
    * Node가 속한 트리에서 해당 Node를 제거
  * Node.removeChild()
    * DOM에서 자식 Node를 제거하고 제거된 Node를 반환
    * Node는 인자로 들어가는 자식 Node의 부모 Node

<br>

* **DOM 삭제 실습**
  * ChildNode.remove()
  * Node.removeChild()

<br>

* **DOM 속성 - 속성 관련 메서드**
  * Element.setAttribute(name, value)
    * 지정된 요소의 값을 설정
    * 속성이 이미 존재하면 값을 갱신, 존재하지 않으면 지정된 이름과 값으로 새 속성을 추가
  * Element.getAttribute(attributeName)
    * 해당 요소의 지정된 값(문자열)을 반환
    * 인자(attributeName)는 값을 얻고자 하는 속성의 이름

<br>

* **DOM 속성 실습**
  * Element.setAttribute(name, value)
  * Element.getAttribute(attributeName)

<br>

* **DOM 조작 - 정리**
  1. 💥**선택한다.**
     * querySelector(), querySelectorAll() ...
  2. 💥**변경(조작) 한다.**
     * innerText, innerHTML, element.style.color, setAttribute(), getAttribute(), createElement(), appendChild() ...

<br>

---

<br>

### 3. Event

<br>

* **Event(이벤트) 개념**
  * 네트워크 활동이나 사용자와의 상호작용 같은 사건의 발생을 알리기 위한 객체
  * 이벤트 발생
    * 마우스를 클릭하거나 키보드를 누르는 등 사용자 행동으로 발생할 수 도 있음
    * 특정 메서드를 호출(Element.click())하여 프로그래밍적으로도 만들어 낼 수 있음

<br>

* **Event 기반 인터페이스**
  * AnimationEvent, ClipboardEvent, DragEvent 등
  * UIEvent
    * 간단한 사용자 인터페이스 이벤트
    * Event의 상속을 받음
    * MouseEvent, KeyboardEvent, InputEvent, FocusEvent 등의 부모 객체 역할을 함
    * ![image-20220501170643724](javascript_advanced.assets/image-20220501170643724.png)

<br>

* **Event는 왜 필요할까?**
  * ![image-20220501170705355](javascript_advanced.assets/image-20220501170705355.png)

<br>

* **Event의 역할**
  * "~하면 ~한다."
  * "클릭하면, 경고창을 띄운다."
  * "특정 이벤트가 발생하면, **💥할 일을 등록한다.**"

<br>

* **Event handler - addEventListener()**
  * **💥EventTarget.addEventListener()**
    * 지정한 이벤트가 대상에 전달될 때마다 호출할 함수를 설정
    * 이벤트를 지원하는 모든 객체(Element, Document, Window 등)를 대상으로 지정 가능
  * **💥target.addEventListener(type, listener[, options])**
    * type
      * 반응 할 이벤트 유형(대소문자 구분 문자열)
    * listener
      * 지정된 타입의 이벤트가 발생했을 때 알림을 받는 객체
      * EventListener 인터페이스 혹은 JS function 객체(콜백 함수)여야 함

<br>

* **DOM 관련 객체의 상속 구조 복습**
  * EventTarget
    * Event Listener를 가질 수 있는 객체가 구현하는 DOM 인터페이스
    * ![image-20220501171148380](javascript_advanced.assets/image-20220501171148380.png)

<br>

* **Event handler - addEventListener()**
  * 3가지 필요(대상/이벤트 명세/할일)
  * "**대상**에 **특정 이벤트**가 발생하면, **할 일**을 등록하자"
  * **EventTarget**.addEventListener(**type**, **listener**)

<br>

* **addEventListener 예시**
  * ![image-20220501171407395](javascript_advanced.assets/image-20220501171407395.png)

<br>

* **addEventListener 실습**
  * 71-3-1 : 함수 주소를 넘기는 것 / 함수의 리턴 값을 넘기는 것
  * 73-8 : 함수의 이름을 지정해도 되고 안해도 됨
  * 74-3 : blue 4번 실행 중 4번 다 시행할 필요없는 것은 밖으로 빼줌

<br>

* **Event 취소**
  * **💥event.preventDefault()**
  * 현재 이벤트의 기본 동작을 중단
  * HTML 요소의 기본 동작을 작동하지 않게 막음
    * ex. a 태그의 기본 동작은 클릭 시 링크로 이동 / form 태그의 기본 동작은 form 데이터 전송
  * 이벤트를 취소할 수 있는 경우, 이벤트의 전파를 막지 않고 그 이벤트를 취소

<br>

* **Event 취소 실습**
  * submit
  * 77-3 : 어떤 방식 제출을 하든 다 막음
  * 취소 할 수 없는 이벤트도 존재
    * 이벤트의 취소 가능 여부는 event.cancelable을 사용해 확인할 수 있음

<br>

* **Event 추가 학습**
  * 다양한 이벤트 유형 참고
  * https://developer.mozilla.org/en-US/docs/Web/Events

<br>

* **Event 종합 실습**
  * CREATE, READ 기능을 충족하는 todo app 만들기
    * button은 form 안에 있어야 제출의 기능을 가짐
    * input -> submit
