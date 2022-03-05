## ![펭귄](0117_control_statement.assets/펭귄.png)

## 제어문 (Cotrol Statement)



### 1. 제어문 (Control Statement) : 위에서 아래로, 좌측할당 <- 우측결과

* **제어문 **
  * 파이썬은 기본적으로 위에서부터 아래로 순차적으로 명령을 수행
  * 특정 상황에 따라 코드를 선택적으로 실행 (분기/조건)하거나 계속하여 실행 (반복)하는 제어가 필요함
  * 제어문은 순서도 (flow chart)로 표현이 가능



---



### 2. 조건문 (Conditional Statement)

* **if 조건문**
  * 조건문은 참/거짓을 판단(연산자) 할 수 있는 조건식과 함께 사용
  * 조건이 참이면` :` 이후를 수행, 거짓이면 `else:` 이후를 수행
  * 여러 `elif`가 있을 수 있고, `else`는 선택적으로 사용
* **elif 복수 조건**
  * 2개 이상의 조건을 활용하는 경우 사용


* **중첩 조건문(Nested Conditional Statement)**

  *  조건문은 다른 조건문에 중첩 가능함

* **조건 표현식(Conditional Expression)** 

  * 조건에 따라 값을 정할 때 활용
  
  * 삼항 연산자(Ternary Operator)라고 부르기도 함
  
  * 중첩해서 사용 가능 하지만, 가독성이 좋지 않으므로 적당히만 사용
  
  * ```python
    true_value if <조건식> else false_value
    ```



---



### 3. 반복문(Loop Statement)

* **while 반복문**

  * 조건식이 참(True)인 경우 반복적으로 코드를 실행

  * 조건식 뒤에 `:`이 반드시 필요하고, 무조건 **종료조건을 설정해야 함**

  * ```python
    while <조건식>:
        <코드 블럭>
    ```

* **for문**

  * 시퀀스(string, tuple, list, range)를 포함한 순회가능한 객체(iterable)의 요소들을 순회함

  * ```python
    for <임시변수> in <순회가능한데이터(iterable)>:
        <코드 블럭>
    ```

* **문자열(String) 순회**

  * range()와 순회할 string의 길이를 활용(len)하여 index를 조작 가능함

* **딕셔너리 순회(반복문 활용)**

  * 딕셔너리의 key에 접근할 수 있으면, 이를 통해 value에도 접근할 수 있음

  * 딕셔너리에서 for를 활용하는 4가지 방법

  * ```python
    # 0. dictionary 순회 (key 활용)
    for key in dict:
        print(key)
        print(dict[key])
    
    # 1. `.keys()` 활용
    for key in dict.keys():
        print(key)
        print(dict[key])
        
    # 2. `.values()` 활용
    # 이 경우 key는 출력할 수 없음
    for val in dict.values():
        print(val)
        
    # 3. `.items()` 활용
    for key, val in dict.items():
        print(key, val)

* **enumerate()**
  * 인덱스(index)와 값(value)을 함께 활용 가능함
    * enumerate()를 활용하면, 추가적인 변수를 활용할 수 있음
  * enumerate(iterable, start=0)
    * 튜플로 돌려줌

* **List Comprehension**

  * 표현식과 제어문을 통해 리스트를 생성

  * 여러 줄의 코드를 한 줄로 줄일 수 있음

  * ```python
    [expression for 변수 in iterable]
    
    list(expression for 변수 in iterable)
    ```

* **Dictionary Comprehension**

  * 딕셔너리도 comprehension을 활용할 수 있음

  * `iterable`에서 `dict`를 생성할 수 있음

    ```python
    {키: 값 for 요소 in iterable}
    
    dict({키: 값 for 요소 in iterable})
    ```

* **반복제어(break, continue, for-else)**

  * break
    * 반복문을 종료
    * for 나 while문을 빠져나감
  * continue
    * continue 이후의 코드를 수행하지 않고, 다음 요소부터 계속(continue)하여 반복을 수행함

  * pass
    * 아무것도 하지 않음, 자리 채우는 용도
  * else
    * 끝까지 반복문을 실행한 이후에 실행
    * 반복문이 break 문으로 종료될 때는 실행되지 않음
