# 마크다운(Markdown)

* 문서의 구조를 잡기위해 사용
* md 파일명으로 축약
* 일반 텍스트 기반의 경량 마크업(Markup) 언어 -> Mark(글의 역할을 지정하는 표시)로 둘러싸인 언어, 직관적이고 쉬움
* https://d2.naver.com/news/3435170  (개발툴 -> 레벨2 스스로 학습, **문서화**가 특히 중요함!)



## 마크다운 문법 알아보기

### 1. 제목(Heading)

* h1 - h6 에 해당하는 제목을 표현가능

* `# 을 사용`
* 예시(프로그램마다 차이가 있을 수 있음)

```markdown
# 제목1
## 제목2
### 제목3
#### 제목4
##### 제목5
###### 제목6
```



# 제목1
## 제목2
### 제목3
#### 제목4
##### 제목5
###### 제목6



---

### 2.목록(List)

* 순서가 없는 목록(불렛으로 사용되는 목록)과 순서가 있는 목록을 표현할 수 있음

+ 순서가 없는 목록은 `- * + `를 사용하고 한칸 띄우기
+ 순서가 있는 목록은 `1. 2. 3. (숫자, 형태)`

1. 순서가 있는 목록을 표현
   + tab 키를 이용해서 들여쓰기 가능
2. `shift + tab` 키를 이용해서 내어쓰기 가능

+ 예시

``` markdown
- 순서가 없는 목록
	+ 서브 목록
	* 서브 목록
 
1. 순서가 있는 목록
	1. 서브 목록
	2. 서브 목록

- 순서가 없는 목록
	1. 서브 목록으로 순서가 있는 리스트
	2. 서브 목록으로 순서가 있는 리스트

1. 순서가 있는 목록
	* 서브 목록으로 순서가 없는 리스트
	* 서브 목록으로 순서가 없는 리스트
```

- 순서가 없는 목록
	+ 서브 목록
	
	* 서브 목록
	
	

1. 순서가 있는 목록
	1. 서브 목록
	2. 서브 목록
	
	

- 순서가 없는 목록
	1. 서브 목록으로 순서가 있는 리스트
	2. 서브 목록으로 순서가 있는 리스트
	
	

1. 순서가 있는 목록
	* 서브 목록으로 순서가 없는 리스트
	* 서브 목록으로 순서가 없는 리스트



---



### 3. 강조

* 글자의 스타일링을 표현(마우스 우클릭으로도 가능)
* **굵게** : `**글자**` 혹은 `__글자__`
* *기울이기* : `*글자*` 혹은 `_글자_`
* ~~취소~~ : `~~글자~~`



---



### 4. 코드 표현

* 한 줄 코드 표현 (inline 코드,) : `print("Hello world")`, 백틱(`)으로 감싸서 표현
* 여러 줄 코드 표현(block 코드) : 백틱 3개를 연달아 작성, 언어까지 넣어야 가독성 좋아짐

```python
print('Hello world')
```



---



### 5. 링크(link)

* 클릭했을 때 해당 주소로 이동할 수 있는 링크를 표현
* `[표시할 글자](이곳에 이동할 주소 ex. url)`
* 예시

```markdown
[google](https://google.com) 을 누르면 구글로 이동합니다.
```

[google](https://google.com) 을 누르면 구글로 이동합니다.

잘 안되면 ctrl 누르고 클릭



---



### 6. 이미지

* `![이미지가 없을때 나오는 텍스트](이미지 위치한 경로)`

* 예시

  > 아래는 링크에 대한 예시 입니다.

  ```
  ![펭수](https://upload.wikimedia.org/wikipedia/ko/thumb/d/d4/%ED%8E%AD%EC%88%98.jpg/300px-%ED%8E%AD%EC%88%98.jpg)
  ```

  ![펭수](https://upload.wikimedia.org/wikipedia/ko/thumb/d/d4/%ED%8E%AD%EC%88%98.jpg/300px-%ED%8E%AD%EC%88%98.jpg)

  

---



### 7. 인용문

* 주석이나 인용 문구 표현
* `>`를 사용

```markdown
> 인용문을 작성합니다.
>> 중첩 인용 1
>>> 중첩 인용 2
```

> 인용문을 작성합니다.
> > 중첩 인용 1
> >
> > > 중첩 인용 2



---



### 8. 테이블(Ctrl + T)

* 파이프(`|`)와 하이픈(`-`)을 이용해서 행과 열을 구분

* 하이픈으로 칼럼명과 행을 구분할 때는 3개 이상으로 작성해야 한다.

  > 다음은 테이블 작성 예시와 결과 입니다.

``` markdown
| 동물 | 종류 | 다리개수 |
|-----|-----|---------|
|호랑이|포유류|4개|
|닭|조류|2개|
```

| 동물   | 종류   | 다리개수 |
| ------ | ------ | -------- |
| 호랑이 | 포유류 | 4개      |
| 닭     | 조류   | 2개      |

* but, Ctrl + T를 눌러서 편하게 사용하자!!



---



### 9. 수평선

* 구분선
* `-, *, _`를 3개 이상 연속으로 작성(3개 중 취향껏 사용)

----



### 참고 사이트

* https://www.markdownguide.org/cheat-sheet/
* https://support.typora.io/Markdown-Reference/