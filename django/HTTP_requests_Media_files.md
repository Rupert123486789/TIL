## ![펭귄](template_view_routing.assets/펭귄.png)

<br>

## Handling HTTP requests & Media files

<br>

### 1.  Handling HTTP requests

<br>

* **Handling HTTP request**
  * Django에서 HTTP 요청을 처리하는 방법
    1. Django shortcut functions
    2. View decorators

<br>

* **1. Django shortcuts functions**
  * django.shortcust 패키지는 개발에 도움 될 수 잇는 여러 함수와 클래스를 제공
  * shortcuts function 종류
    * render()
    * redirect()
    * get_object_or_404()
      * ✨단일 객체를 조회하는것은 get과 똑같지만 예외가 발생했을대 다르게 return 해줌(500 -> 404)
    * get_list_or_404()

<br>

* **get_object_or_404()**
  * 모델 manager인 objects에서 get()을 호출하지만, 해당 객체가 없을 경우 DoesNotExist 예외 대신 Http 404를 raise
  * get()에 경우 조건에 맞는 데이터가 없을 경우에 예외를 발생 시킴
    * 코드 실행 단계에서 발생한 예외 및 에러에 대해서 브라우저는 http status code 500으로 인식함
  * ✨**상황에 따라 적절한 예외 처리**를 하고, 클라이언트에게 **✨올바른 에러 상황을 전달하는 것** 또한 개발의 중요한 요소 중 하나
  * index 페이지에서는 사용하면 안됨
    * 게시판이 비어 있으면 404를 줘서 적절하지 않은 사용 / 첫번째 글이 없으면 메인 페이지가 안 뜸
  * API로 서버를 쓸 때 사용 
    * ex. TMDB : 영화목록 조회 - JSON - 목록 없으면 404

<br>

* **2. Django View decorators**
  * Django는 다양한 HTTP 기능을 지원하기 위해 view 함수에 적용할 수 있는 여러 데코레이터를 제공
  * [참고] Decorator(데코레이터)
    * 어떤 함수에 기능을 추가하고 싶을 대, 해당 함수를 수정하지 않고 기능을 연장 해주는 함수
    * 즉, 원본 함수를 수정하지 않으면서 추가 기능만을 구현할 때 사용
  * Allowed HTTP methods
    * 요청 메서드에 따라 view 함수에 대한 엑세스를 제한
    * 요청이 조건을 충족시키지 못하면 HttpResponseNotAllowed을 return (405 Method Not Allowed)
    * require_http_method(), require_POST(), require_safe(), require_GET()
      1. require_http_method()
         * view 함수가 특정한 method 요청에 대해서만 허용하도록 하는 데코레이터
      2. require_POST() => delete
         * view 함수가 POST method 요청만 승인하도록 하는 데코레이터
      3. require_safe() => GET => index, detail
         * view 함수가 GET 및 HEAD method만 허용하도록 요구하는 데코레이터
         * django는 require_GET 대신 require_safe를 사용하는 것을 권장	
  * View decorator 작성
  * delete view 함수 코드 변경
    * 불필요해진 코드 삭제
  * URL로 delete 요청 후 405 http status code 확인

<br>

* **결론**
  * HTTP 요청에 따라 적절한 예외처리 혹은 데코레이터를 사용해 서버를 보호하고 클라이언트에게 정확한 상황을 제공하는 것의 중요성

<br>

---

<br>

### 2. Media files

<br><br><br><br><br><br><br><br>
