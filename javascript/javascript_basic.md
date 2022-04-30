## ![펭귄](javascript_basic.assets/펭귄.png)

<br>

## Java Script Basic

<br>

### 1. Intro

<br>

* **동작 방식**
  * ![image-20220430213908417](javascript_basic.assets/image-20220430213908417.png)

<br>

* **브라우저(browser)**
  * URL로 웹(WWW)을 탐색하며 서버와 통신하고, HTML 문서나 파일을 출력하는 GUI 기반의 소프트웨어
  * 인터넷의 컨텐츠를 검색  및 열람하도록 함
  * "웹 브라우저"라고도 함
  * 주요 브라우저
    * Google Chrome, Mozilla Firefox, Microsoft Edge, Opera, Safan

<br>

* **JavaScript의 필요성**
  * 브라우저 화면을 '동적'으로 만들기 위함
  * 브라우저를 조작할 수 있는 **💥유일한 언어**
    * ![image-20220430214155547](javascript_basic.assets/image-20220430214155547.png)
    * SQL : DB를 조작할 수 있는 유일한 언어(ORM으로 번역해서 쓰기는 하지만)

<br>

* **Most Populat Programming Language in 2021 survey**
  * ![image-20220430214356537](javascript_basic.assets/image-20220430214356537.png)
    * Jetbrain : 파이참을 만든 회사

<br>

---

<br>

### 2. Browser

<br>

* **브라우저에서 할 수 있는 일**
  * DOM(Document Object Model) 조작
    * 문서(HTML) 조작
  * BOM(Brower Object Model) 조작
    * navigator, screen, location, frames, history, XHR
  * JavaScript Core(ECMAScript)
    * Data Structure(Object, Array), Conditional Expression, Iteration

<br>

* **DOM 이란?**
  * HTML, XML과 같은 문서를 다루기 위한 프로그래밍 인터페이스
  * 문서를 구조화하고, 구조화된 구성 요소를 하나의 객체로 취급하여 다루는 논리적 트리 모델
  * 문서가 객체(object)로 구조화되어 있으며 key로 접근 가능
  * 단순한 속성 접근, 메서드 활용뿐만 아니라 프로그래밍 언어적 특성을 활용한 조작 가능
  * 주요 객체
    * window : DOM을 표현하는 창(브라우저 탭), 최상위 객체(작성 시 생략 가능)
    * document : 페이지 컨텐츠의 Entry Point 역할을 하며, `<head>`, `<body>` 등과 같은 수많은 다른 요소들을 포함
    * navigator, location, history, screen
  * ✨한 줄 요약 : 문서(HTML)를 프로그램으로 조작할 수 있다.

<br>

* **DOM**
  * ![image-20220430215028498](javascript_basic.assets/image-20220430215028498.png)
    * 구조화

<br>

* **DOM - 해석**
  * 파싱 (Parsing)
    * 구문 분석, 해석
    * 브라우저가 문자열을 해석하여 DOM Tree로 만드는 과정
    * ![image-20220430215120819](javascript_basic.assets/image-20220430215120819.png)

<br>

* **DOM - 조작**
  * ![image-20220430215149047](javascript_basic.assets/image-20220430215149047.png)

<br>

* **BOM 이란?**
  * Browser Object Model
  * 자바스크립트가 브라우저와 소통하기 위한 모델
  * 브라우저의 창이나 프레임을 추상화해서 프로그래밍적으로 제어할 수 있도록 제공하는 수단
    * 버튼, URL 입력창, 타이틀 바 등 브라우저 윈도우 및 웹 페이지 일부분을 제어 가능
  * window 객체는 모든 브라우저로부터 지원받으며 브라우저의 창(window)를 지칭
  * ✨브라우저에 대한 제어권도 프로그래밍 언어로 접근 가능

<br>

* **BOM 조작**
  * ![image-20220430215330096](javascript_basic.assets/image-20220430215330096.png)

<br>

* **JavaScript Core**
  * 브라우저(BOM & DOM)을 조작하기 위한 명령어 약속(언어)
    * ![image-20220430215435667](javascript_basic.assets/image-20220430215435667.png)

<br>

* **정리**
  * ![image-20220430215624875](javascript_basic.assets/image-20220430215624875.png)
  * 브라우저(BOM)과 그 내부의 문서(DOM)를 조작하기 위해 ECMAScript(JS)를 학습

<br>

---

<br>

### 3. Introduction

<br>

* **ECMA**
  * ECMA(ECMA International)
    * 정보 통신에 대한 **✨표준을 제정하는 비영리 표준화 기구**
  * ECMAScript는 ECMA에서 ECMA-262 규격에 따라 정의한 언어
    * ECMA-262 : 범용적인 목적의 프로그래밍 언어에 대한 명세
  * ✨**ECMAScript6는 ECMA에서 제안하는 6번째 표준 명세를 말함**
    * (참고) ECMAScript6의 발표 연도에 따라 ECMAScript2015라고도 불림
  * JS와 ECMAScript가 혼용됨
    * ✨ECMAScript는 여러버전이 있고, 현재는 6(6이전과 이후의 차이가 큼)

<br>

- **세미콜론(semicolon)**
  - 자바스크립트는 ✨**세미콜론을 선택적으로 사용가능**
  - 세미콜론이 없으면 **✨ASI**에 의해 자동으로 세미콜론이 삽입됨
    - ASI : 자동 세미콜론 삽입 규칙(Automatic Semicolon Insertion)
  - 본 수업에서는 자바스크립의 문법 및 개념적 측면에 집중하기 위해 세미콜론을 사용하지 않고 진행
  - 세미콜론(semicolon) 예시
    - ![image-20220430220226154](javascript_basic.assets/image-20220430220226154.png)

<br>

* **코딩 스타일 가이드**
  * 코딩 스타일의 핵심은 합의된 원칙과 일관성
    * 절대적인 하나의 정답은 없으며, 상황에 맞게 원칙을 정하고 일관성 있게 사용하는 것이 중요
  * 코딩 스타일은 코드의 품질에 직결되는 중요한 요소
    * 코드의 가독성, 유지보수 또는 팀원과의 커뮤니케이션 등 개발 과정 전체에 영향을 끼침
  * (참고) 다양한 자바스크립트 코딩 스타일 가이드
    * ✨Airbnb Javascript Style Guide
    * Google Javascript Style Guide
    * standardjs
  * 코딩 스타일 가이드 예시
    * 본 수업에서는 Airbnb Style Guide를 중심으로 진행할 예정
      * 단, 가이드의 일부 항목은 문법 및 개념적 측면에 집중하기 위해 변형해서 사용
      * ![image-20220430220502042](javascript_basic.assets/image-20220430220502042.png)

<br>

---

<br>

### 4. 변수와 식별자

<br>

* **식별자 정의와 특징**
  * 식별자(identifier)는 변수를 구분할 수 있는 변수명을 말함
  * 식별자는 반드시 문자, **✨달러($) 또는 밑줄(_)로 시작**
  * 대소문자를 구분하며, 클래스명 외에는 모두 소문자로 시작
  * 예약어 사용 불가능
    * 예약어 예시 : for, if, function 등

<br>

* **식별자 작성 스타일**(✨JS에서는 주로 camelCase를 사용)
  * 카멜 케이스(camelCase, lower-camel-case)
    * 변수, 객체, 함수에 사용
  * 파스칼 케이스(PascalCase, upper-camel-case)
    * 클래스, 생성자에 사용
  * 대문자 스네이크 케이스(SNAKE_CASE)
    * 상수(constants)에 사용
      * 상수의 정의 : 개발자의 의도와 상관없이 변경될 가능성이 없는 값을 의미
  * ![image-20220430220834394](javascript_basic.assets/image-20220430220834394.png)
  * ![image-20220430220846128](javascript_basic.assets/image-20220430220846128.png)
  * ![image-20220430220909111](javascript_basic.assets/image-20220430220909111.png)

<br>

* **변수 선언 키워드(let, const)**
  * ![image-20220430221018628](javascript_basic.assets/image-20220430221018628.png)

<br>

* **(참고) 선언, 할당, 초기화**(✨파이썬은 불가능하지만, JS에서는 선언과 할당을 따로 할 수 있음)
  * ![image-20220430221149651](javascript_basic.assets/image-20220430221149651.png)
  * 선언(Declaration)
    * **변수를 생성**하는 행위 또는 시점
  * 할당(Assignment)
    * **선언된 변수에 값을 저장**하는 행위 또는 시점
  * 초기화(Initialization)
    * **선언된 변수에 처음으로 값을 저장**하는 행위 또는 시점

<br>

* **변수 선언 키워드(let, const) 예시 - 재할당 / 재선언**
  * ![image-20220430221258737](javascript_basic.assets/image-20220430221258737.png)
    * 재할당과 값을 바꿈은 같은게 아님
    * 다른 값을 넣는게 아니고, 기존에 가지고 있는 값에서 조작하는 것이 가능
  * ![image-20220430221317931](javascript_basic.assets/image-20220430221317931.png)

<br>

* **변수 선언 키워드(let, const)**
  * 블록 스코프(block scope)
    * if, for, 함수 등의 **✨중괄호 내부**를 가리킴
    * 블록 스코프를 가지는 변수는 **💥블록 바깥에서 접근 불가능**
    * ![image-20220430221612083](javascript_basic.assets/image-20220430221612083.png)
  * 파이썬 스코프는 LEGB
    * 파이썬은 조건문 안에서 선언된 변수를 외부에서 사용가능
    * JS는 중괄호 기준으로 움직임

<br>

* **변수 선언 키워드 - var**
  * var(✨사용 지양)
    * var로 선언한 변수는 재선언 및 재할당 모두 가능
    * ES6 이전에 변수를 선언할 때 사용되는 키워드
    * 호이스팅되는 특성으로 인해 예기치 못한 문제 발생 가능
      * 따라서 ES6 이후부터는 var 대신 const와 let을 사용하는 것을 권장
    * 함수 스코프
  * ![image-20220430221854102](javascript_basic.assets/image-20220430221854102.png)
  * 함수 스코프(function scope)
    * ✨**함수의 중괄호 내부**를 가리킴
    * 함수 스코프를 가지는 변수는 **💥함수 바깥에서 접근 불가능**
    * if, for 안에서 쓰면 밖에서 접근 가능(파이썬 같이)
    * ![image-20220430222020050](javascript_basic.assets/image-20220430222020050.png)
  * 호이스팅(hoisting) - ✨var의 가장 큰 문제점 / 디버깅을 어렵게 함
    * 변수를 선언 이전에 참조할 수 있는 현상
    * 변수 선언 이전의 위치에서 접근시 undefined를 반환
    * ![image-20220430222108265](javascript_basic.assets/image-20220430222108265.png)

<br>

* **let, const, var 비교**
  * ![image-20220430222314084](javascript_basic.assets/image-20220430222314084.png)
    * 블록 스코프 : {}

<br>

---

<br>

### 5. 데이터 타입

<br>

* **데이터 타입 종류**
  * 자바스크립트의 모든 값은 특정한 데이터 타입을 가짐
  * 크게 원시 타입(Primitive type)과 참조 타입(Reference type)으로 분류됨
    * ![image-20220430222453696](javascript_basic.assets/image-20220430222453696.png)

<br>

* **(참고) 원시 타입과 참조 타입 비교**
  * 원시 타입(Primitive type)
    * 객체(object)가 아닌 기본 타입
    * 변수에 해당 타입의 값을 담김
    * 다른 변수에 복사할 때 실제 값이 복사됨
    * ![image-20220430222552945](javascript_basic.assets/image-20220430222552945.png)
  * 참조 타입(Reference type)
    * 객체(object) 타입의 자료형
    * 변수에 해당 객체의 참조 값이 담김
    * 다른 변수에 복사할 때 참조 값이 복사됨
    * ![image-20220430222650318](javascript_basic.assets/image-20220430222650318.png)

<br>

* **원시 타입(Primitive type)**
  * 숫자(Number) 타입
    * 정수, 실수 구분 없는 하나의 숫자 타입
    * 부동소수점 형식을 따름
    * (참고) NaN(Not-A-Number)
      * 계산 불가능한 경우 반환되는 값
        * ex. 'Angel' / 1004 => NaN(✨숫자가 아닌것을 나타내는 숫자형(?))
    * ![image-20220430222923456](javascript_basic.assets/image-20220430222923456.png)
    * 파이썬은 float(INF)로 무한대를 나타냄
  * 문자열(String) 타입
    * 텍스트 데이터를 나타내는 타입
    * 16비트 유니코드 문자의 집합
    * 작은따옴표 또는 큰따옴표 모두 가능
    * 템플릿 리터럴(Template Literal)
      * ES6부터 지원
      * 따옴표 대신 backtick(``)으로 표현
      * ${expression} 형태로 표현식 삽입 가능
      * ![image-20220430223134717](javascript_basic.assets/image-20220430223134717.png)
  * undefined
    * 변수의 값이 없음을 나타내는 데이터 타입
    * 변수 선언 이후 직접 값을 할당하지 않으면, 자동으로 undefined가 할당됨
    * ![image-20220430223208014](javascript_basic.assets/image-20220430223208014.png)
  * null
    * 변수의 값이 없음을 의도적으로 표현할 때 사용하는 타입
    * (참고) null 타입과 typeof 연산자
      * typeof 연산자 : 자료형 평가를 위한 연산자
      * null 타입은 ECMA 명세의 원시 타입의 정의에 따라 원시 타입에 속하지만, typeof 연산자의 결과는 객체(object)로 표현됨
    * ![image-20220430223340430](javascript_basic.assets/image-20220430223340430.png)

<br>

* **(참고) undefined 타입과 null 타입 비교** => 설계 미스(그래도 나누자면...)
  * undefined(✨개발자의 의도가 안 들어가 있음)
    * 빈 값을 표현하기 위한 데이터 타입
    * 변수 선언 시 아무 값도 할당하지 않으면, 자바스크립트가 자동으로 할당
    * typeof 연산자의 결과는 undefined
    * ![image-20220430223442813](javascript_basic.assets/image-20220430223442813.png)
  * null(✨의도적으로 표현 해줘야함 / null을 안 써주면 null 안나옴)
    * 빈 값을 표현하기 위한 데이터 타입
    * 개발자가 의도적으로 필요한 경우 할당
    * typeof 연산자의 결과는 object
    * ![image-20220430223514256](javascript_basic.assets/image-20220430223514256.png)

<br>

* **원시 타입(Primitive type)**
  * Boolean 타입
    * 논리적 참 또는 거짓을 나타내는 타입
    * true 또는 false로 표현(✨대문자가 아님)
    * 조건문 또는 반복문에서 유용하게 사용
      * (참고) 조건문 또는 반복문에서 boolean이 아닌 데이터 타입은 자동 형변환 규칙에 따라 true 또는 false로 변환됨
    * ![image-20220430223753615](javascript_basic.assets/image-20220430223753615.png)

<br>

* **(참고) ToBoolean Conversions(자동 형변환) 정리**
  * ![image-20220430223848840](javascript_basic.assets/image-20220430223848840.png)
  * if ([]) : 파이썬은 False / JS는 true

<br>

* **참조 타입(Reference type)**
  * 자세한 내용은 해당 타입의 챕터 참고
  * 타입 별 챕터 링크 목록
    * 함수(Functions)
    * 배열(Arrays)
    * 객체(Objects)

<br>

---

<br>

### 6. 연산자

<br>

* **할당 연산자**
  * 오른쪽에 있는 피연산자의 평가 결과를 왼쪽 피연산자에 할당하는 연산자
  * 다양한 연산에 대한 단축 연산자 지원
  * (참고) Increment 및 Decrement 연산자 (✨while문 등에서 n += 1과 같은 작업이 많아서 생김)
    * Increment(++) : 피연산자의 값을 1 증가시키는 연산자
    * Decrement(--) : 피연산자의 값을 1 감소시키는 연산자
    * Airbnb Style Guide에서는 '+=' 또는 '-='와 같이 더 분명한 표현으로 적을 것을 권장
    * ![image-20220430224316046](javascript_basic.assets/image-20220430224316046.png)

<br>

* **비교 연산자**
  * 피연산자들(숫자, 문자, Boolean 등)을 비교하고 결과값을 boolean으로 반환하는 연산자
  * 문자열은 **✨유니코드 값을 사용(할당된 숫자로 비교)**하며 표준 사전 순서를 기반으로 비교
    * ex. 알파벳끼리 비교할 경우
      * 알파벳 순서상 후순위가 더 크다
      * 소문자가 대문자보다 더 크다
  * ![image-20220430224506742](javascript_basic.assets/image-20220430224506742.png)

<br>

* **동등 비교 연산자(==)**
  * 두 피연산자가 같은 값으로 평가되는지 비교 후 boolean 값을 반환
  * 비교할 때 **✨암묵적 타입변환**을 통해 타입을 일치시킨 후 같은 값인지 비교
  * 두 피연산자가 모두 객체일 경우 메모리의 같은 객체를 바라보는지 판별
  * 💥**예상치 못한 결과가 발생할 수 있으므로 특별한 경우를 제외하고 사용하지 않음**
  * ![image-20220430224713013](javascript_basic.assets/image-20220430224713013.png)

<br>

* **일치 비교 연산자(===)**
  * 두 피연산자가 같은 값으로 평가되는지 비교 후 boolean 값을 반환
  * **✨엄격한 비교**가 이뤄지며 암묵적 타입 변환이 발생하지 않음
    * 엄격한 비교 : 두 비교 대상의 타입과 값 모두 같은지 비교하는 방식
  * 두 피연산자가 모두 객체일 경우 메모리의 같은 객체를 바라보는지 판별
  * ![image-20220430224847603](javascript_basic.assets/image-20220430224847603.png)

<br>

* **논리 연산자**
  * 세 가지 논리 연산자로 구성
    * and 연산은 '&&' 연산자를 이용
    * or 연산은 '||' 연산자를 이용
    * not 연산은 '!' 연산자를 이용
  * 단축 평가 지원
    * ex. false && ture => false
    * ex. true || false => true
  * ![image-20220430225011665](javascript_basic.assets/image-20220430225011665.png)

<br>

* **삼항 연산자(Ternary Operator)**
  * 세 개의 피연산자를 사용하여 조건에 따라 값을 반환하는 연산자
  * 가장 왼쪽 조건식이 참이면 콜론(:) 앞의 값을 사용하고 그렇지 않으면 콜론(:) 뒤의 값을 사용
  * 삼항 연산자의 결과 **✨값(하나의 결과)**이기 때문에 변수에 할당 가능
  * (참고) 한 줄에 표기하는 것을 권장
  * ![image-20220430225220987](javascript_basic.assets/image-20220430225220987.png)
  * 항이 3개 / 💥항이 몇개든 결국 평가되어 **하나의 값**이 됨

<br>

---

<br>

### 7. 조건문

<br>

* **조건문의 종류와 특징**
  * 'if' statement
    * 조건 표현식의 결과값을 Boolean 타입으로 변환 후 참/거짓을 판단
  * 'switch' statement
    * 조건 표현식의 결과값이 어느 값(case)에 해당하는지 판별
    * (참고) 주로 특정 변수의 값에 따라 조건을 분기할 때 활용
      * 조건이 많아질 경우 if문보다 가독성이 나을 수 있음

<br>

* **if statement**
  * if, else if, else
    * 조건은 소괄호(condition) 안에 작성
    * 실행할 코드는 중괄호{} 안에 작성
    * 블록 스코프 생성
    * ![image-20220430225607378](javascript_basic.assets/image-20220430225607378.png)

<br>

* **if statement 예시**
  * ![image-20220430225636273](javascript_basic.assets/image-20220430225636273.png)
    * elif 아님 => else if
    * ✨괄호 / 중괄호 뒤에 else if 와 else임 (주의 !!!)

<br>

* **switch statement**
  * switch
    * 표현식(expression)의 결과값을 이용한 조건문
    * 표현식의 결과값과 case문의 오른쪽 값을 비교
    * break 및 default문은 [선택적]으로 사용 가능
    * break문이 없는 경우 break문을 만나거나 default문을 실행할 때까지 다음 조건문 실행
    * 블록 스코프 생성
    * ![image-20220430225838743](javascript_basic.assets/image-20220430225838743.png)

<br>

* **switch 예시**
  * break가 있는 경우
    * ![image-20220430225935471](javascript_basic.assets/image-20220430225935471.png)
  * break가 없는 경우
    * ![image-20220430225959053](javascript_basic.assets/image-20220430225959053.png)

<br>

* **if vs. switch**
  * ![image-20220430230029083](javascript_basic.assets/image-20220430230029083.png)
    * 조건이 조금이라도 복합적이면 switch 못씀

<br>

---

<br>

### 8.  반복문

<br><br><br><br><br><br>

---

<br>

### 9. 

<br><br><br><br><br><br>

---

<br>

### 10. 

<br><br><br><br><br><br>

---

<br>

### 11.

<br><br><br><br><br><br>



