# HTML

<br>

* **Hyper Text Markup Language**

### 1. HTML 기본구조

* **현재의 웹 표준**

  * W3C	HTML5
  * WHATWG   HTML Living Standard     Apple, Google, Microsoft, Mozilla
  * 2019년 WHATWG가 주도권 싸음웨서 승리하면서 표준이 됨

* **Can I use?** -> strong, flex

  * 빨강 : 지원 X / 갈색 : 일부 지원 / 초록 : 지원 / 회색 : 잘 모름

* **HTML : Hyper Text Markup Language**

  * info.cern.ch : 최초의 웹 사이트
  * Hyper Text : 참조(하이퍼 링크)를 통해 사용자가 한 문서에서 다른 문서로 즉시 접근할 수 있는 텍스트
  * ![image-20220206005059864](html.assets/image-20220206005059864.png)
  * Markup Language : 태그 등을 이용하여 문서나 데이터의 구조를 명시하는 언어
    * HTML, Markdown
  * 웹 페이지를 작성(구조화)하기 위한 언어


<br>

* **HTML 기본 구조(Web의 뼈대를 만들기 위한 언어)**

  * html : 문서의 최상위(root) 요소, 쌍으로 존재('`<html></html>`) / 언어 기본값은 en

  * head : 문서 메타데이터 요소(ex. 카메라 사진 데이터 속 GPS, 조리개값, 노출, 일자, 기종....)

    * 문서 제목, 인코딩, 스타일, 외부 파일 로딩 등(html 정보)
    * 일반적으로 브라우저에 나타나지 않는 내용

  * body : 문서 본문 요소

    * 실제 화면 구성과 관련된 내용
    * `<!DOCTYPE html>` 왠만하면 넣어주자 : 해당 문서가 html5로 구성되어있음 / IE 환경의 user를 생각해서

  * ![image-20220206005357343](html.assets/image-20220206005357343.png)

  * head 예시

    * `<title>` : 브라우저 상단 타이틀
    * `<meta>` : 문서 레벨 메타데이터 요소, html 문서의 ✨**정보를 담당**
    * `<link>` : **✨외부** 리소스 연결 요소 (CSS 파일, favicon 등)
    * `<script>` : ✨**스크립트 요소** (JavaScript 파일/코드), body tag에 들어갈 수도 있음
    * `<style>` : CSS 직접 작성, ✨**html을 꾸며줌**
    * ![image-20220207005305348](html.assets/image-20220207005305348.png)
    * Open Graph Protocol : 메타 데이터를 표현하는 새로운 규약
      * HTML 문서의 메타 데이터를 통해 문서의 정보를 전달(미리보기, 프리뷰)
      * 메타정보에 해당하는 제목, 설명 등을 쓸 수 있도록 정의

  * 💥DOM(Document Object Model) 트리

    * 텍스트 파일인 HTML 문서를 브라우저에서 렌더링 하기 위한 구조
      * HTML 문서에 대한 모델을 구성함
      * HTML 문서 내의 각 요소에 접근 / 수정에 필요한 프로퍼티와 메서드를 제공함
      * ![image-20220206010221613](html.assets/image-20220206010221613.png)
      * ![image-20220206010256580](html.assets/image-20220206010256580.png)
      * Markup Language여서 들여쓰기를 안해도 되지만 가독성을 좋게하여 유지보수가 쉬워짐

  * 요소(element) : 여는태그 / 닫는 태그 + 내용

  * ![image-20220206010458470](html.assets/image-20220206010458470.png)

    * HTML 요소는 시작 태그와 종료 태그 그리고 태그 사이에 위치한 내용으로 구성
      * 태그(Element, 요소)는 컨텐츠(내용)를 감싸는 것으로 그 정보의 성격과 의미를 정의
    * 💥내용이 없는 태그들(`<single tag> `존재)
      * br, hr, img, input, link, meta
    * 요소는 중접(nested)될 수 있음
      * 요소의 중첩을 통해 하나의 문서를 구조화
      * 여는 태그와 닫는 태그의 쌍을 잘 확인 해야함
        * 오류를 반환하는 것이 아닌 그냥 레이아웃이 깨진 상태로 출력되어 디버깅이 힘들어 질 수 있음 (✨바로 바로 테스트해보는게 좋음 / 나중에 찾으려면 눈으로 직접해야함)

  * 속성(attribute)

    * ![image-20220206010913653](html.assets/image-20220206010913653.png)

    * 속성명 / 속성값 : key / value 느낌
    * ![image-20220206011013217](html.assets/image-20220206011013217.png)
    * 홑따옴표도 가능은 하지만 쌍따옴표 권장!
    * 속성을 통해 태그의 부가적인 정보를 설정할 수 있음(Tag별로 사용가능한 속성이 다르다)
    * 요소는 속성을 가질 수 있으며, 경로나 크기와 같은 추가적인 정보를 제공
    * 요소의 시작 태그에 작성하며 보통 이름과 값이 하나의 쌍으로 존재(속성명="속성값")
    * 태그와 상관없이 사용 가능한 속성(HTML Globla Attribute)들도 있음

  * HTML Global Attribute

    * 모든 HTML 요소가 공통으로 사용할 수 있는 대표적인 속성 (몇몇 요소에는 아무 효과가 없을 수 있음)
      * id : 문서 전체에서 유일한 고유 식별자 지정
      * 💥class : 공백으로 구분된 해당 요소의 클래스의 목록 (CSS, JS에서 요소를 선택하거나 접근)
        * id 와 class는 식별자
      * data-* : 페이지에 개인 사용자 정의 데이터를 저장하기 위해 사용
      * style : inline 스타일, 해당 요소를 꾸밀때 사용
      * title : 요소에 대한 추가 정보 지정
      * tabindex : 요소의 탭 순서
      * ![image-20220206011429731](html.assets/image-20220206011429731.png)
      * ![image-20220206011456700](html.assets/image-20220206011456700.png)

  * 시맨틱 태그

    * HTML5에서 의미론적 요소를 담은 태그의 등장
      * 기존 영역을 의미하는 div 태그(공간 분리)를 대체하여 사용

    * 대표적인 태그 목록
      * header : 문서 전체나 섹션의 헤더(머리말 부분)

      * nav : 내비게이션

      * aside : 사이드에 위치한 공간, 메인 콘텐츠와 관련성이 적은 콘텐츠

      * section :  문서의 일반적인 구분, 컨텐츠의 그룹을 표현

      * article : 문서, 페이지, 사이트 안에서 독립적으로 구분되는 영역

      * footer : 문서 전체나 섹션의 푸터(마지막 부분)

      * ![image-20220206011856600](html.assets/image-20220206011856600.png)

      * Non semantic 요소는 div, span 등이 있으며, h1, table 태그들도 시맨틱 태그로 볼  수 있음

      * 개발자 및 사용자 뿐만 아니라 검색엔진 등에 의미 있는 정보의 그룹을 태그로 표현

      * 단순히 구역을 나누는 것 뿐만 아니라 '의미'를 가지는 태그들을 활용하기 위한 노력

      * 요소의 의미가 명확해지기 때문에(구조화/ 명시적 표현 가능) 코드의 가독성을 높이고 유지보수를 쉽게 함

      * 검색엔진최적화(SEO)를 위해서 메타태그, 시맨틱 태그 등을 통한 마크업을 효과적으로 활용 해야함

        

---



# 2. HTML 문서 구조화

* **인라인 / 블록 요소**
* **텍스트 요소**(inlien요소 - 한 줄 일부 차지)
  * ![image-20220206231049864](html.assets/image-20220206231049864.png)
  * b / strong, i / em(시맨틱 태그) 표현의 차이는 없음, 의미론적 차이(✨**강조!**)
  * ![image-20220206231159436](html.assets/image-20220206231159436.png)
* **그룹 컨텐츠**(block요소 - 한 줄 전체 차지)
  * ![image-20220206231255022](html.assets/image-20220206231255022.png)
  * ![image-20220206231318874](html.assets/image-20220206231318874.png)
* **table**
  * table의 각 영역을 명시하기 위해 `<thead> <tbody> <tfoot>` 요소를 활용
  * ![image-20220206231423131](html.assets/image-20220206231423131.png)
  * `<tr>`으로 가로줄을 구성하고 내부에는 `<th>`혹은 `<td>`로 셀을 구성
  * ![image-20220206231541470](html.assets/image-20220206231541470.png)
  * colspan(열을 병합), rowspan(행을 병합) 속성을 활용하여 셀 병합
  * ![image-20220206231603098](html.assets/image-20220206231603098.png)
  * `<caption>`을 통해 표 설명 도는 제목을 나타냄
  * table 태그 기본 구성
    * thead
      * tr > th

    * tbody
      * tr > td

    * tfoot
      * tr > td

    * caption

  * ![image-20220206231753629](html.assets/image-20220206231753629.png)
* 💥**form**(Django에서 굉장히 자주 사용)
  * `<form>`은 정보(데이터)를 서버에 제출하기 위한 영역
  * `<form>` 기본 속성
    * 💥action : form을 처리할 서버의 URL
    * method : form을 제출할 때 사용할 HTTP 메서드 (GEF 혹은 POST)
    * enctype : method가 post인 경우 데이터의 유형
      * application/x-www-form-urlencoded : 기본값
      * mutipart/form-data : 파일 전송시 (input type이 file인 경우, 이미지/비디오/파일)
      * text/plain : HTML5 디버깅용(잘 사용되지 않음)

  * ![image-20220206232120757](html.assets/image-20220206232120757.png)
* **input**
  * 다양한 타입을 가지는 입력 데이터 유형과 위젯이 제공됨
  * `<input>` 대표적인 속성
    * name : form control에 적용되는 이름(이름/값 페어로 전송됨)
    * value : form control에 적용되는 값(이름/값 페어로 전송됨)
    * required, readonly, autofocus, autocomplete, disabled 등
  * ![image-20220206232221074](html.assets/image-20220206232221074.png)
* **input label**
  * label을 클릭하여 input 자체의 초점을 맞추거나 활성화 시킬 수 있음
    * 사용자는 선택할 수 있는 영역이 늘어나 웹 / 모바일(터치) 환경에서 편하게 사용할 수 있음
    * label과 input 입력의 관계가 시각적 뿐만 아니라 화면 리더기에서도 label을 읽어 쉽게 내용을 확인 할 수 있도록 함

  * `<input>`에 id 속성을, `<label>`에는 for 속성을 활용하여 상호 연관을 시킴
  * ![image-20220206232410147](html.assets/image-20220206232410147.png)
* **input 유형 - 일반**
  * 일반적으로 입력을 받기 위하여 제공되며 타입별로 HTML 기본 검증 혹은 추가 속성을 활용할 수 있음
    * text : 일반 텍스트 입력
    * password : 입력 시 값이 보이지 않고 문자를 특수기호(*)로 표현
    * email : 이메일 형식이 아닌 경우 form 제출 불가
    * number : min, max, step 속성을 활용하여 숫자 범위 설정 가능
    * file : accept 속성을 활용하여 파일 타입 지정 가능
    * ![image-20220206232648256](html.assets/image-20220206232648256.png)
* **input 유형 - 항목 중 선택**
  * 일반적으로 label을 사용하여 내용을 작성하며 항목 중 선택할 수 있는 input을 제공
  * 동일 항목에 대하여는 name을 지정하고 선택된 항목에 대해 value를 지정해야 함
    * checkbox : 다중 선택
    * radio : 단일 선택

  * ![image-20220206232801609](html.assets/image-20220206232801609.png)
* **input 유형 - 기타**
  * 다양한 종류의 input을 위한 picker를 제공
    * color : color picker
    * date : date picker

  * hidden input을 활용하여 사용자 입력을 받지 않고 서버에 전송되어야 하는 값을 설정
    * hidden : 사용자에게 보이지 않는 input

  * ![image-20220206232903729](html.assets/image-20220206232903729.png)

<br>

* **input 유형 - 종합**
  * `<input>` 요소의 동작은 type에 따라 달라지므로, 각각의 내용을 숙지할 것
