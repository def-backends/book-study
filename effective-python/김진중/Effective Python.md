# Chapter 01. 파이썬답게 생각하기

## Better Way 1. 사용 중인 파이썬의 버전을 알아두라

Python 2는 2020년부터 더 이상 공식적으로 지원되지 않는다.

### Python 2와 Python 3의 대표적 차이점

- 유니코드 지원
    - Python 2에서는 `str`과 `unicode` 타입이 별도로 존재하며, `str`은 바이트 문자열, `unicode`는 유니코드
      문자열을 나타낸다.
        - Python 2: `u"Hello, World!"`
        - Python 3: `"Hello, World!"`
- `print` 함수
    - Python 2: `print "Hello, World!"`
    - Python 3: `print("Hello, World!")`
- `integer` 나눗셈
    - Python 2: `5 / 2 == 2`
    - Python 3: `5 / 2 == 2.5`
- `xrange` 함수
    - Python 2: `xrange`는 `range`와 비슷하지만, `xrange`는 이터레이터를 반환한다.
    - Python 3: `xrange`가 없어지고, `range`가 `xrange`의 역할을 대신한다.

### Python 2와 Python 3의 호환성

- 공식적으로 백포팅이 지원되지는 않는다.
- `2to3` 라이브러리를 사용하여 Python 2 코드를 Python 3 코드로 변환할 수 있다.

## Better Way 2. PEP 8 스타일 가이드를 따르라

PEP 8은 파이썬 코드를 어떻게 구성할지에 대한 스타일 가이드이다. PEP 8을 반드시 지켜야 하는 것은 아니지만, 대부분의 잘 작성된 파이썬 코드는 PEP 8을 따른다.

### PEP 8의 주요 내용
자세한 내용은 [PEP 8](https://peps.python.org/pep-0008/)을 참고한다.
#### [들여쓰기](https://peps.python.org/pep-0008/#indentation)
- [탭 대신 공백을 사용한다.](https://peps.python.org/pep-0008/#tabs-or-spaces)
- 공백 4개를 사용한다.
- 긴 식을 여러 줄로 나누어 작성하는 경우, 추가 들여쓰기를 사용해야 한다.
- 첫 번째 줄에 인수가 없어야 한다.
- `if` 문의 조건식이 길어질 경우, 조건식을 괄호로 둘러 싸고, 여러 줄로 나누어 작성한다.
	- 이 경우 상세한 방침은 사용자의 판단에 달려 있다.
#### 줄 바꿈
- [한 줄은 최대 79자까지만 작성한다.](https://peps.python.org/pep-0008/#maximum-line-length)
- [연산자 앞에서 줄 바꿈을 **권장**한다.](https://peps.python.org/pep-0008/#should-a-line-break-before-or-after-a-binary-operator)
#### [빈 줄](https://peps.python.org/pep-0008/#blank-lines)
- 함수 정의와 클래스 정의 사이에는 두 줄을 둔다.
- 클래스 내의 메서드 정의 사이에는 한 줄을 둔다.
#### [인코딩](https://peps.python.org/pep-0008/#source-file-encoding)
- 소스 파일의 인코딩은 UTF-8을 사용한다.
#### [임포트](https://peps.python.org/pep-0008/#imports)
- 모듈을 임포트할 때는 항상 모듈의 절대 이름을 사용한다.
#### [모듈 레벨 던더 메서드](https://peps.python.org/pep-0008/#module-level-dunder-names)
- 참고: 던더 메서드란, `__`로 시작하고 끝나는 메서드를 말한다.
- `__all__`, `__author__`, `__version__` 등의 모듈 레벨 던더 메서드는 모듈의 최상단에 위치한다.
#### [문자열 따옴표](https://peps.python.org/pep-0008/#string-quotes)
- 작은 또는 큰 따옴표 중 하나를 선택하여 일관성 있게 사용한다. (단, 문자열 안에 따옴표가 포함되어 있는 경우, 다른 따옴표를 사용한다.)
- [**주석: Python 3.12부터는 일관성 있는 `f-string` 을 사용하여 문자열을 포매팅 할 수 있다.**](https://docs.python.org/3.12/whatsnew/3.12.html#pep-701-syntactic-formalization-of-f-strings)
	- [PEP-701](https://peps.python.org/pep-0701/) 참고
#### [식과 문의 공백](https://peps.python.org/pep-0008/#whitespace-in-expressions-and-statements)
- [불필요한 공백을 피하라.](https://peps.python.org/pep-0008/#whitespace-in-expressions-and-statements)
- [기타 권장 사항](https://peps.python.org/pep-0008/#other-recommendations)
	- **후행 공백을 절대로 사용하지 않는다.**
	- 할당, 증강 할당, 비교, 논리 연산자 주변에는 공백을 사용한다.
		- 우선 순위가 다른 연산자를 사용하는 경우, 우선 순위가 가장 낮은 연산자 주변에만 공백을 사용한다.
			- **가독성은 좋지만, 현실적으로 지키기 어려운 경우가 많다.**
			- 올바른 예시
				```python
				# Correct:
				i = i + 1
				submitted += 1
				x = x*2 - 1
				hypot2 = x*x + y*y
				c = (a+b) * (a-b)
				```
			- 잘못된 예시
				```python 
				# Wrong:
				i=i+1
				submitted +=1
				x = x * 2 - 1
				hypot2 = x * x + y * y
				c = (a + b) * (a - b)
				```
	- 함수 어노테이션은 반드시 콜론 사용 규칙을 따라야 하며, `->` 화살표 주변에는 반드시 공백이 있어야 한다.
		- 올바른 예시
			```python
			def munge(input: AnyStr): ...
			def munge() -> AnyStr: ...
			def munge(input: AnyStr) -> AnyStr: ...
			```
		- 잘못된 예시
			```python
			def munge(input:AnyStr): ...
			def munge()->PosInt: ...
			def munge(input: AnyStr)->PosInt: ...
			```
	- 키워드 파라미터 또는 기본 인수 값의 `=` 주변에는 공백을 사용하지 않는다.
		- 올바른 예시
			```python
			def complex(real, imag=0.0): ...
			def munge(sep: AnyStr = None): ...
			```
		- 잘못된 예시
			```python
			def complex(real, imag = 0.0): ...
			def munge(sep: AnyStr=None): ...
			```
	- 기본 값을 사용하는 키워드 인수의 경우, `=` 주변에 공백을 사용한다.
		- 올바른 예시
			```python
			def munge(input: AnyStr = None): ...
			def munge(input: AnyStr, sep: AnyStr = None, limit=1000): ...
			```
		- 잘못된 예시
			```python
			def munge(input: AnyStr=None): ...
			def munge(input: AnyStr, limit = 1000): ...
			``` 
	- 복합문을 사용하지 않는다.
		- 올바른 예시
			```python
			if foo == 'blah':
				do_blah_thing()
			do_one()
			do_two()
			do_three()
			```
		- 잘못된 예시
			```python
			if foo == 'blah': do_blah_thing()
			do_one(); do_two(); do_three()
			```
	- 여러 절이 사용되는 경우, `if`/`for`/`while` 문을 한 줄에 작성하지 않는다.			```
		- 가급적 하지 마세요
			```python
			if foo == 'blah': do_blah_thing()
			for x in lst: total += x
			while t < 10: t = delay()
			```
		- 절대 하지 마세요
			```python
			if foo == 'blah': do_blah_thing()
			else: do_non_blah_thing()
			
			try: something()
			finally: cleanup()
			
			do_one(); do_two(); do_three(long, argument,
			list, like, this)
			
			if foo == 'blah': one(); two(); three()
			```
#### [후행 쉼표를 사용해야 하는 경우](https://peps.python.org/pep-0008/#when-to-use-trailing-commas)
- **튜플 사용 시에는 필수이다.**
	- 올바른 예시
		 ```python
		FILES = ('setup.cfg',)
		```
	- 잘못된 예시
	```python
	FILES = ('setup.cfg')
	```
    - 여러 줄로 나누어 작성하는 경우, 마지막 요소 뒤에 쉼표를 사용한다. (**단, 한 줄로 작성하는 경우에는 쉼표를 사용하지 않는다.**)
        - 올바른 예시
			```python
			FILES = [
				'setup.cfg',
				'tox.ini',
				]
			initialize(FILES,
					   error=True,
					   )
			```
        - 잘못된 예시
	        ```python
			FILES = ['setup.cfg', 'tox.ini']
			initialize(FILES, error=True)
			```
#### [주석](https://peps.python.org/pep-0008/#comments)
- 반드시 항상 코드와 일치하는 주석을 작성해야 한다.
- 완전한 문장으로 작성해야 한다.
#### [docstring](https://peps.python.org/pep-0008/#documentation-strings)
- 독스트링 작성 규칙은 [PEP-0257](https://peps.python.org/pep-0257/) 에서 상세하게 제시하고 있다.
#### [명명 규칙](https://peps.python.org/pep-0008/#naming-conventions)
##### [클래스 명](https://peps.python.org/pep-0008/#class-names)
- 클래스 이름은 `CapWords` 규칙을 사용해야 한다.
- `Callable` 로 사용되는 경우 함수 이름을 사용할 수 있다.
##### [메서드 및 인스턴스 변수명](https://peps.python.org/pep-0008/#function-and-method-arguments)
- `snake_case`로 함수 이름을 사용해야 한다.
- 비공개 메서드, 인스턴스 변수는 밑줄 하나만 사용한다.
##### [예외 이름](https://peps.python.org/pep-0008/#exception-names)
- 예외 이름은 `Error` 접미사로 끝나야 한다.
##### [상수](https://peps.python.org/pep-0008/#constants)
- 상수는 대문자와 언더바를 사용하여 모듈 레벨에서 작성한다.

#### [프로그래밍 권장 사항](https://peps.python.org/pep-0008/#programming-recommendations)
- **`None`(null) 값을 확인 시 `if` 또는 `if not` 을 사용하지 말라.**
- 람다 식을 변수에 할당하지 말고, 함수를 정의하라.
	- [Ruff E731](https://docs.astral.sh/ruff/rules/lambda-assignment/) 참고.
- **예외 연쇄를 적절히 사용하라.**
	- [주석: `raise from` 사용법](https://stackoverflow.com/questions/24752395/python-raise-from-usage) 참고.
- 반환(`return`) 문에 일관성을 가져라.
	- return 문이 반드시 있어야 하면, 모든 함수에 return 을 명시하고, 그렇지 않은 경우 모두 생략해야 한다.
- 접두사 / 접미사를 확인 시 `str.startswith` 또는 `str.endswith` 메서드를 사용하라.
- **객체 타입 비교는 타입을 비교하지 말고, `isinstance` 함수를 사용하라.**
	- [Ruff E721](https://docs.astral.sh/ruff/rules/type-comparison/) 참고.
- **시퀀스의 경우 빈 시퀀스가 `bool` 취급 시 `False` 인 점을 이용하라.** 
- **후행 공백을 사용하지 말라.**
- eq 연산자(`==`) 를 사용하여 `bool` 값과 비교하지 말라. 

#### [함수 주석](https://peps.python.org/pep-0484/)
- 함수 주석은 [https://peps.python.org/pep-0484/](https://peps.python.org/pep-0484/)를 따라야 한다.
- 타입 검사기는 선택사항이다.
#### [변수 주석](https://peps.python.org/pep-0008/#variable-annotations)
- 모듈 수준 변수, 클래스 및 인스턴스 변수, 로컬 변수에 대한 주석은 콜론 뒤에 공백이 하나 있어야 한다.
- 콜론 앞에 공백이 없어야 한다.
- 대입에 오른쪽이 있는 경우 등호에는 양쪽에 정확히 한 칸씩 공백이 있어야 한다.

## Better Way 3. `bytes`와  `str`의 차이를 알아두라
### 요약
- `bytes`  값에는 8비트 값의 시퀀스가 들어있고, `str`는 유니코드 코드 포인트가 들어있다.
- `bytes` 는 텍스트 인코딩이 없고, `str`는 이진 인코딩이 없다.
- 프로그램의 핵심 부분은 유니코드 데이터가 들어있는 `str`을 사용해야 한다.
	- 입력 데이터는 여러 인코딩을 허용하고, 출력 텍스트 인코딩은 `UTF-8` 등으로 제한할 수 있다.
- 각각의 타입 내 연산은 잘 지원되나, `bytes`와 `str` 간 연산 시 제대로 처리되지 않는다.
- 파일 핸들과 관련된 연산 시 유니코드 문자열을 기본 값으로 사용한다.
	- `mode` 를 `wb`, `rb` 등을 사용하거나 인코딩 값을 바꾸어주어야 한다.

## Better Way 4. C 스타일 형식 문자열을 `str.format`과 쓰기보다는 `f-string`을 통한 인터폴레이션을 사용하라
### 요약
- 과거의 파이썬은 `%` 문자열을 사용하는 형식화 연산자를 기반으로 문자열 포매팅을 하였다.
	- 이는 `C언어`의 `printf` 함수에서 비롯되었다.
- 과거 방식 사용 시, 순서에 따라서 포매팅 위치가 결정되므로 관리하기가 어렵다.
- 딕셔너리를 사용하는 방법이 추가되어 포매팅 시 위치에 영향을 받지 않게 되었으나, 문자열이 난잡해지고, 반복되는 내용이 많아진다.
- `f-string` 사용 시 가독성이 향상되고, 변수 등을 통한 동적인 파라미터 등의 행위가 간단해진다.
### 문제점
- `f-string`은 문자열을 "먼저" 생성하므로, 성능이 중요하거나, 문자열이 많이 생성되는 환경에서는 `f-string`을 사용해서는 안된다.
	- `logging` 시에는 `extra` 등으로 사후 평가 처리가 필요하다.
### Linter
- [UP032](https://docs.astral.sh/ruff/rules/f-string/) 사용 시 자동으로 `str.format` 함수는 수정된다. 모든 상황에서 지원되지는 않는다.
- [G004](https://docs.astral.sh/ruff/rules/logging-f-string/) 사용 시 `logging` 사용 시 `f-string`을 사용하는지 체크할 수 있다.

## Better Way 5. 복잡한 식을 쓰는 대신 도우미 함수를 작성하라
### 요약
- Python 언어 사용 시, 복잡하고 읽기 어려운 "원 라인 코드"를 작성하기 쉽다.
- 복잡한 식을 재사용할 수 있는 도우미 함수로 옮기고, 기존 코드가 해당 도우미 함수를 사용하게 하라.
### 팁
- Pycharm IDE 기능을 사용하면 좋다.
	- [중복 코드 탐지](https://www.jetbrains.com/help/pycharm/analyzing-duplicates.html) 등의 링크 참고.

## Better Way 6. 인덱스를 사용하는 대신 대입을 사용해 데이터를 언패킹하라

### 요약
- 복잡한 데이터 구조에 시퀀스에 인덱스를 사용하면 가독성이 떨어지고 사용하기가 복잡하다.
- 한 문장안에서 여러 값을 대입하는 언패킹 문법을 사용 시 가독성, 명확성이 개선된다.
- 모든 이터러블에 언패킹을 적용할 수 있다.
### 팁
- 상당히 복잡한 데이터 구조라면, 언패킹 이전에 데이터 클래스를 정의하는 것이 좋다.
	- 데이터 구조상 편리한 방법은 [NamedTuple](https://docs.python.org/3/library/collections.html#collections.namedtuple), [dataclasses](https://docs.python.org/ko/3/library/dataclasses.html) 를 사용하는 것이다.
	- [TypedDict](https://docs.python.org/3/library/collections.html#collections.namedtuple) 도 사용할 수 있지만, 키 값 사용 시 다소 타 방법에 비해 불편하고 이점이 적다.
		- 딕셔너리 형식을 유지하는 클래스 정의 시, [UserDict](https://docs.python.org/3/library/collections.html#collections.UserDict) 등을 사용해야 한다.

## Better Way 7. `range` 보다는 `enumerate` 를 사용하라
### 요약
- `enumerate` 를 사용하면 이터레이터에서 인덱스와 원소 값을 동시에 얻을 수 있다.
- `range` 를 사용하는 것보다 가독성이 좋고 코드가 간결해진다.
- `enumerate`의 두 번째 파라미터로 인덱스 시작 값을 지정할 수 있다. 기본 값은 0이다.

## Better Way 8. 여러 이터레이터에 대해 나란히 루프를 수행하려면 `zip`을 사용하라.
### 요약
- 여러 개의 이터레이터를 이터레이션 하는 경우 코드가 번잡하고 이해하기 어려워진다.
- `zip` 함수를 사용하면 여러 개의 이터레이터를 간편하게 이터레이션 할 수 있다.
- `zip` 함수는 제너레이터를 생성하므로, 메모리에 대한 걱정 없이 사용할 수 있다.
- `zip` 함수는 가장 짧은 이터레이터가 멈추는 순간, 나머지 원소들을 무시한다.
- 길이 제한을 원하지 않는 경우, `itertools` 함수의 `zip_longest` 함수를 사용하라.
### 팁
- Python 3.10 부터는 [PEP-618](https://peps.python.org/pep-0618/) 이 적용됨에 따라서, `strict` 파라미터를 사용할 수 있다.
	- 이 파라미터를 `False` 값으로 사용 시 이터레이터들의 길이가 다르게 소진되는 경우, `ValueError` 가 발생한다.
	- 가급적 `strict` 를 `True` 로 사용하여, 의도하지 않은 동작이 발생하지 않도록 사전에 방지하는 것이 바람직하다.
		- 에러는 조기에 버그나 변경 사항을 추적하는 데 큰 도움이 된다.
### Linter
- [B905](https://docs.astral.sh/ruff/rules/zip-without-explicit-strict/) 사용 시 `strict` 를 지정하지 않고 사용하는 경우 오류 발생.
## Better Way 9. `for` 나 `while` 뒤에 `else` 블록을 사용하지 말라
- `for`, `while` 문 뒤에 `else` 문을 사용 시 루프가 `break` 문이 실행되지 않은 경우에 해당 블록이 실행된다.
- 동작이 직관적이지 않으므로, 사용해서는 안된다.

### Linter
- [PLW0120](https://docs.astral.sh/ruff/rules/useless-else-on-loop/) 사용 시 for/else 문을 단순 for 문으로 바꾸어준다. 일부 직접 수정 가능.

## Better Way 10. 대입식을 사용해 반복을 피하라
### 요약
- 대입식에서 왈러스 연산자 (`:=`)를 사용하여 식 내에서 변수에 값 대입이 가능하다.
- `switch/case` 또는 `do/while` 문과 같은 python 언어에 없는 기능들과 유사한 문법을 흉내낼 수 있다.
### Linter
- [RUF018](https://docs.astral.sh/ruff/rules/assignment-in-assert/) 이 있긴 하지만 그다지 유용성은 없다.
### Formatter
- [Ruff 와 Black 의 포매팅 차이가 있다.](https://docs.astral.sh/ruff/formatter/black/#walruses-in-slice-expressions)

# Chapter 02

## Better Way 11. 시퀀스를 슬라이싱하는 방법을 익혀라
### 요약
- 슬라이싱의 기본 형태는 `[시작:끝]` 이다.
- 맨 앞부터 슬라이싱 시 0을 생략해야 한다.
- 맨 뒤까지 슬라이싱 시 끝 인덱스를 생략해야 한다.
- 리스트의 인덱스 범위를 넘어가는 인덱스는 조용히 무시된다.
### 팁
- [Python3.12 부터 `slice` 객체는 `hashable` 객체이다.](https://docs.python.org/3/library/functions.html#slice)
	- **`dict`, `frozenset` 등에 사용할 수 있다는 뜻이다.**
		- 이를 응용하면, 최근 쿼리 등에 사용된 페이징 조건 등을 간편하게 저장할 수도 있다.
- **값 할당/삭제를 위해서라면 `slicing` 자체가 권장되지 않는다.**
	- **가독성/명시성이 떨어지기 때문이다.**
	- 리스트의 얕은 복사본을 생성하기 위해서라면, `list[:]` 문법보다는 `list.copy()` 메서드를 사용하는 것이 좋다.
### Linter
- [FURB131](https://docs.astral.sh/ruff/rules/delete-full-slice/) 은 `del` 문을 사용하여 list/dict 내 요소를 제거하는 경우 에러를 발생시킨다. 현재 `unstable` 상태.
- [FURB145](https://docs.astral.sh/ruff/rules/slice-copy/) 는 list slicing 방식의 shallow copy (`list[:]`)를 `list.copy`로 바꾸어준다. 현재 `unstable` 상태.

## Better Way 12. 스트라이드와 슬라이스를 한 식에 함께 사용하지 말라
### 요약
- 스트라이드(`간격`)는 일정 간격을 두고 슬라이싱을 할 수 있도록 하는 특별한 구문을 의미한다.
	- `[start:end:step(stride)]` 문법
- 슬라이스에 `step` 값까지 지정하면 코드가 너무 밀도가 높아 이해하기 어렵다.
- `bytes` 데이터를 `-1` step 을 사용하여 스트라이딩을 적용한 경우, 의도치 않은 에러가 발생할 수 있다.
- 음수 값을 스트라이드에 사용하는 것은 피해야 한다.
- 한 슬라이스에서 `start`, `end`, `step` 을 모두 사용해야 한다면 단계를 나누거나, `itertoos.islice` 함수를 사용하라.
### 의문점
- 예제 코드에서는 다음과 같은 코드를 제시한다.
	- 
		```python
		>>> w = "寿司"
		>>> x = w.encode("utf-8")
		>>> y = x[::-1]
		>>> z = y.decode("utf-8")
		
		Traceback (most recent call last):
		  File "<input>", line 4, in <module>
		UnicodeDecodeError: 'utf-8' codec can't decode byte 0xb8 in position 0: invalid start byte

		```
	- 이 코드는 그다지 적절한 예시로서 사용되지 않은 것이, 애초에 `bytes` 데이터에서 역순으로 바꾼 데이터를 `utf-8` 데이터로 파싱하면 에러가 나는 것이 당연하다.
		- **프로그램 `bytes` 데이터를 역순으로 바꾸어서 프로그램이 작동하지 않으면 그건 사용자 책임이다.**
	- `utf-8` 문자열 내에서 역순으로 처리하는 경우 당연히 정상적으로 작동한다.
		- 
			```python
		>>> 	w = "寿司"
		>>> 	print(w[::-1])
			
			司寿
			```

## Better Way 13. 슬라이싱보다는 나머지를 모두 잡아내는 언패킹을 사용하라
### Before & After

```python
car_ages = [0, 9, 4, 8, 7, 20, 19, 1, 6, 15]
car_ages_descending = sorted(car_ages, reverse=True)

# before
oldest = car_ages+descending[0]
second_oldest = car_ages_descending[1]
others = car_ages_descending[2:]

# after
oldest, second_oldest, *others = car_ages_descending
oldest, *others, youngest = car_ages_descending
*others, second_youngest, youngest = car_ages_descending
```
### 요약
- 언패킹 대입에 `starred-expression` 을 사용하면 대입되지 않는 모든 부분을 리스트에 잡을 수 있다.
- `starred-expression`은 어떤 위치에든 놓을 수 있으나, `starred-expression`만 단독으로 사용할 수는 없다.
- `starred-expression` 위치의 변수에는 항상 리스트가 들어가며, 0개 이상의 원소가 포함되어 있다.
- 슬라이싱, 인덱스보다 `starred-expression`이 실수 여지가 줄어든다.

### Linter
- [F622](https://docs.astral.sh/ruff/rules/multiple-starred-expressions/#multiple-starred-expressions-f622) 는 다중 `starred-expression` 을 검사한다.

## Better Way 14. 복잡한 기준을 사용해 정렬할 때는 key 파라미터를 사용하라

### 요약
- `list` 자료에서 sort 메서드를 사용 시 `key` 파라미터를 사용하여 원하는 방식으로 원소 정렬이 가능하다.
- 원소 타입에서 특별 메서드 (`__eq__`, `__ne__`, `__lt__`, `__le__`, `__gt__`, `__ge__`) 가 정의되어 있지 않으면 `sort` 메서드를 사용할 수 없다.
- `key` 파라미터를 사용하여 임의의 함수 규칙대로 정렬하도록 기능 제공이 가능하다.
- `-` 연산자 등을 사용하여 역순으로 자료를 정렬할 수 있다.
	- `-` 연산자 등을 사용할 수 없는 경우, 여러 번의 정렬 과정을 거쳐야 한다.

### 팁
- 일반적으로 `lambda` 함수 사용이 안티 패턴으로 취급되는 경향이 강한데, 특히 함수형 프로그래밍과 병행하는 경우 더욱 그렇다.
	- **가능하다면 매직 메서드를 구현하는 것이 일반적으로 옳다.**
	- 매직 메서드를 구현할 수 없다면, 내부 함수 등으로 함수를 정의하는 것이 좋다.
	- 정말 원라인 코드로 간결하게 요약되지 않는다면, 함수를 분리해야 마땅하다. 

## Better Way 15. 딕셔너리 삽입 순서에 의존할 때는 조심하라
### 요약
- Python 3.7 부터는 `dict` 인스턴스에 들어 있는 내용이 삽입 순서를 따른다는 점에 의존할 수 있다.
- Python 언어는 `duck typing` 등을 지원하므로, 유사 dict 의 경우 키 삽입 순서를 반드시 믿을 수 없다.

### 의문점
- 작성자가 제시하는 `MutableMapping` 을 상속한 클래스는 `dict` 의 기준을 따르지 않는다.
	- **즉, 애초에 딕셔너리가 아니라 `MutableMapping` 의 하위 타입이다.**
	- `__iter__` 매직 메서드에서 완전히 커스텀한 로직을 작성한 후 이것이 `dict` 에 부합하지 않는다는 이야기를 펼치는데, **애초에 `dict` 를 내부에 감쌌을 뿐 `dict`가 아니다.**
		- **`MutableMapping` 의 조건을 만족한 것이지, 원본 `dict` 의 조건을 만족한 게 아니다.**
			- [원본 `dict` 에서는 삽입 순서를 보장하기 위해 별도의 `bit vector` 를 사용하고 있다.](https://github.com/python/cpython/blob/main/Include/internal/pycore_dict.h#L259-L275)
			- 자세한 히스토리는 [링크 1](https://morepypy.blogspot.com/2015/01/faster-more-memory-efficient-and-more.html) 와 [PHP Hashtable 구현](https://www.npopov.com/2014/12/22/PHPs-new-hashtable-implementation.html) 을 참고.
		- **`Duck Typing` 은 "명목상 하위 유형" (`Nominal Subtyping`)에 속하며, 리스코프 치환적인 개념이 아니다.**
			- 자세한 내용은 [PEP-544](https://peps.python.org/pep-0544/#changes-in-the-typing-module) 를 참고.
- 정말 `dict` 를 리스코프 치환하여 대체하고 싶다면, `dict` 또는 [UserDict](https://docs.python.org/3/library/collections.html#userdict-objects) 등을 상속해야 한다.

## Better Way 16. in 을 사용하고 딕셔너리 키가 없을 때 KeyError를 처리하기보다는 get을 사용하라
### 요약
- 딕셔너리 키가 없는 경우, 처리할 수 있는 대표적인 방법들은 다음과 같다.
	1. `in` 으로 사전 검증
	2. `KeyError` 예외 사용 (직접 조회 등)
	3. `get` 메서드 사용
	4. `setdefault` 메서드 사용
- 대부분의 경우 `get` 메서드를 사용하는 것이 적절하다.
- 값을 설정해야 하는 경우, `setdefault` 로 기본 값을 설정하여 해결할 수 있지만, `defaultdict` 를 사용하는 것이 더 편할 수 있다.

### 팁
- 코드의 중요도에 따라 다르지만, 코드가 보통 빠르게 개발되고 유지보수가 크게 필요 없는 경우, collection 을 default 값으로 사용하는 chaining 을 사용하면 용이하다.
	- **단, 스키마는 고정적이어야 한다.**
	- 예를 들어, 복잡한 `JSON` 스키마 데이터를 파싱해야 하는 경우, 다음과 같이 default 값을 사용하여 체이닝을 하면 편리하다.
		```python
		json_res: JSON_ro = ...
		assert json_res.get("...", []).get(..., {}).get(..., HTTPStatus.NOT_FOUND) == HTTPStatus.OK
		```
## Better Way 17. 내부 상태에서 원소가 없는 경우를 처리할 때는 setdefault보다 defaultdict 를 사용하라
### 요약
- 키 값이 없는 경우 `setdefault` 로 기본 값을 생성하는 것보다, `defaultdict` 자료형을 사용하는 것이 더 편리하다.

## Better Way 18. `__missing__` 을 사용해 키에 따라 다른 디폴트 값을 생성하는 방법을 알아두라

### 요약
- `setdefault`, `defaultdict` 로도 모두 적절하게 처리하기 어려운 경우, `__missing__` 을 사용하여 키 값에 대응되는 값을 설정해야 한다.
	- `defaultdict` 는 파라미터를 허용하지 않는다.
	- `defaultdict` 는 동적으로 키 값을 생성할 수 없기 때문에 파라미터 값 또는 주어진 키 값에 의존적인 동적인 처리를 위해서는 `__missing__` 메서드가 필요하다.

### 팁
- `dict` 자체를 상속하는 것보다, [`defaultdict` 를 상속하여 `__missing__` 메서드만 오버라이딩을 하는 최대로 날로 먹는 방법이 있다.](https://stackoverflow.com/a/2912455)
	- 타입 체커 등을 만족하는 훌륭한 예시도 해당 링크에 포함되어 있다.
		 ```python
		from typing import Callable, TypeVar
		
		K = TypeVar("K")
		V = TypeVar("V")
		
		class keydefaultdict(dict[K, V]):
		    def __init__(self, default_factory: Callable[[K], V]):
		        super().__init__()
		        self.default_factory = default_factory
		
		    def __missing__(self, key: K) -> V:
		        if self.default_factory is None:
		            raise KeyError(key)
		        else:
		            ret = self[key] = self.default_factory(key)
		            return ret
		```

# Chapter 03
## Better Way 19. 함수가 여러 값을 반환하는 경우 절대로 네 값 이상을 언패킹하지 말라

### 요약
- 함수가 여러 값을 반환하는 경우 튜플 형식으로 반환이 가능하고, 호출하는 쪽에서 언패킹하여 사용할 수 있다.
- 언패킹하여 사용 시 위치 기반으로 사용해야 하므로 실수의 가능성이 높아지고, 변경에 취약해진다.
- 언패킹 구문에 변수가 4개 이상 나오면 실수하기가 쉽다.
- 대안으로 `NamedTuple` 또는 DTO 등을 사용하라.

## Better Way 20. `None` 을 반환하기보다는 예외를 발생시켜라
### 요약
- 특별한 의미를 표시하는 `None` (임의로 정한 값)을 반환하는 함수를 사용하면 조건문에 사용 시 `False`로 취급되어 실수할 가능성이 높아진다.
- `None`을 반환하는 대신 예외를 발생시켜라.
	- 예외 정보를 문서화한다.
- 타입 어노테이션으로 `return type` 을 명시하여 `None`이 반환되지 않는다는 점을 명시화 할 수 있다.

### 예외는 반드시 발생시켜야 하는가
하지만 "적절한" 예외 처리 또한 필요하다.
- [자바스크립트는 왜 그 모양일까?](https://product.kyobobook.co.kr/detail/S000001033091) 책에는 에러와 관련하여 [다음과 같은 내용들](https://rinae.dev/posts/how-javascript-works-summary/)이 있다.
	- "잘 작성된 자바스크립트 프로그램에서는 예외 객체가 전혀 필요하지 않다."
	- "예외 처리를 잘못 쓰는 가장 흔한 경우는 정상적인 결과를 처리할 때도 쓰는 것이다. 예외 처리는 예상하지 못한 문제를 처리할 때만 사용해야 한다."
- [이펙티브 자바](https://www.yes24.com/Product/Goods/65551284) 에도 비슷한 내용이 있다.
	- "아이템 69. 예외는 진짜 예외 상황에만 사용하라"

## Better Way 21. 변수 영역과 클로저의 상호작용 방식을 이해하라

### 요약
- 파이썬은 클로저를 지원한다.
	- 클로저란, 내부 함수가 외부 함수의 컨텍스트에 접근할 수 있는 것을 의미한다.
		- [What is a 'Closure'? - Stackoverflow](https://stackoverflow.com/questions/36636/what-is-a-closure)참고.
- 파이썬 인터프리터는 참조를 해결하기 위해 다음 순서로 영역을 뒤진다.
	- [잘 설명된 Stackoverflow 글 참고](https://stackoverflow.com/a/75051033)
	1. 현재 함수의 영역
	2. 현재 함수를 둘러싼 영역(지역 영역(local scope))
		```python
		foo = 0 # <- ✖
		def outer():
		    foo = 5 # <- ✖
		    def middle():
		        foo = 10 # <- 〇
		        def inner():
		            nonlocal foo # Here
		            foo += 1
		            print(foo) # 11
		        inner()
		    middle()
		outer()
		```
	3. 현재 코드가 들어 있는 모듈의 영역(전역 영역(global scope)
		```python
		foo = 0 # <- 〇
		def outer():
		    foo = 5 # <- ✖
		    def middle():
		        foo = 10 # <- ✖
		        def inner():
		            global foo # Here
		            foo += 1
		            print(foo) # 1
		        inner()
		    middle()
		outer()
		```
	4. 내장 영역 (built-in scope)
- 한 컨텍스트 내부에서 사용한 대입문은 외부 컨텍스트를 변경하지 않는다.
- 외부 컨텍스트를 수정하고 싶다면, `nonlocal` 과 `global` 문을 사용하여 외부 컨텍스트를 수정할 수 있도록 지정해야 한다.
- 가독성과 코드 품질 등을 고려하였을 때, 불가피한 경우가 아니라면 `nonlocal`과 `global` 문을 사용하지 않는 것이 낫다.

## Better Way 22. 변수 위치 인자를 사용해 시각적인 잡음을 줄여라
### 요약
- `def` 문에서 `*args` 를 사용하면 함수가 가변 위치 기반 인자를 받을 수 있다.
- `*` 연산자를 사용하면 가변 인자를 받는 함수에게 시퀀스 내의 원소들을 전달할 수 있다.
- `*args` 를 받는 함수에 새로운 위치 기반 인자를 넣으면 감지하기 힘든 버그가 생길 수 있다.
	- 기존 함수를 확장해야 한다면, `*args` 앞에 위치 파라미터를 추가하지 않고 키워드 파라미터를 추가해야 한다.
### 그 외
- 제네레이터는 사용하는 지점 외에서는 반드시 이터레이션이 되지 않도록 해야 한다.
## Better Way 23. 키워드 인자로 선택적인 기능을 제공하라.
### 요약
- 키워드 인자와 디폴트 값을 함께 사용하면 기본 호출 코드를 마이그레이션 하지 않고도 함수에 새로운 기능을 쉽게 추가할 수 있다.
- 선택적 키워드 인자는 항상 키워드를 사용해 전달돼야 한다.
### 그 외
- `Better Way 24`, `Better Way 25` 와 병행해야 한다.
## Better Way 24. `None` 과 docstring 을 사용해 동적인 디폴트 인자를 지정하라
### 요약
- 디폴트 파라미터 값을 사용 시 함수 실행 시 마다 값이 생성되기를 원하지만, 기본 값에 값을 바로 지정 시 함수 생성 시점에 정의되며 아무리 호출을 하더라도 재생성되지 않는다.
	- 예시: `sleep` 을 하였음에도 `datetime.now()` 값이 동일하다.
	```python
	from time import sleep  
	from datetime import datetime  
	  
	  
	def log(message, when=datetime.now()):  
	    print(f"{when}: {message}")  


	log("안녕!")  
	sleep(0.1)  
	log("다시 안녕!")

	# 2024-04-18 07:27:43.886986: 안녕!
	# 2024-04-18 07:27:43.886986: 다시 안녕!
	```
	- 파라미터가 가변적인 컬렉션인 경우 함수를 사용하는 곳에서 모두 같은 컬렉션을 공유하게 된다.
- 기본 값에 `None`을 사용하여 `None` 이 지정된 경우, 함수 내부에서 값을 새로 생성해야 한다.
- docstring과 타입 어노테이션을 사용하여 파라미터의 기본값을 명시화 할 수 있다.

## Better Way 25. 위치로만 인자를 지정하게 하거나 키워드로만 인자를 지정하게 해서 함수 호출을 명확하게 만들라
### 요약
- 파이썬에서 함수 파라미터를 사용 시, 위치 기반과 키워드 기반 인자로 모두 사용 가능하다.
- 파라미터에 `*` 를 적용하여 키워드 용도로만 파라미터를 사용할 수 있도록 강제할 수 있다.
- Python 3.8 이상부터는 `/` 를 적용하여, 이 앞에 있는 파라미터들에게 위치 기반을 강제할 수 있다.
	- 자세한 내용은 [PEP-570](https://peps.python.org/pep-0570/) 참고.
	- `/` 사용 시 `*` 가 있는 경우, `/` 가 `*` 앞에 위치해야 한다.
	- 둘 사이에 있는 파라미터는 양 쪽 방향으로 모두 호출 가능하다.
- 기본 값을 사용하는 옵션 파라미터는 키워드 기반을 강제하는 것이 좋다.
## Better Way 26. `functools.wraps` 을 사용해 함수 데코레이터를 정의하라
### 요약
- 함수 데코레이터를 사용 시, 래핑된 함수의 정의가 래퍼 함수의 정의로 바뀌게 된다.
	- 인트로스펙션 사용 등의 목적이 있는 경우 원본 함수에 접근해야 할 필요가 있는데, 이 경우 접근이 어려워진다.
	- 따라서 디버깅 등의 목적을 위해서라면 원본 함수로 함수 정의를 교체해줄 필요가 있다.
- [`functools.wraps`를 사용 시 원본 함수의 정의로 내부 속성을 교체해준다.](https://docs.python.org/3/library/functools.html#functools.update_wrapper)
	- `__module__`, `__name__`, `__qualname__`, `__annotations__`, `__doc__` 외 인스턴스 사전인 `__dict__` 를 업데이트 처리한다.

# Chapter 4. 컴프리헨션과 제너레이터
## Better Way 27. `map`과 `filter` 대신 컴프리헨션을 사용하라

### 요약
- `map`과 `filter`를 사용하여 `iterable` 객체에서 특정한 요소를 편하게 추출할 수 있다.
- 하지만 `map`, `filter` 는 `lambda` 문 또는 별도의 함수 정의가 필요하다.
	- 단순한 로직이라면 가독성이 좋지 않아진다.
- 따라서 단순한 로직이라면 `map` 과 `filter` 를 사용하여 요소를 필터링 하는 것보다 컴프리헨션을 사용하여 표기하는 것이 더 낫다.

### 팁
- 성능 상으로도 `map` 은 컴프리헨션에 비해서 성능이 좋지 않다.
	- https://stackoverflow.com/a/1247490 참고.

### Linter
- [unnecessary-map (C417)](https://docs.astral.sh/ruff/rules/unnecessary-map/) 사용 시 불필요한 `map` 사용을 방지할 수 있다.

## Better Way 28. 컴프리헨션 내부에 하위 식을 세 개 이상 사용하지 말라
### 요약
- 컴프리헨션은 간단한 사용처의 경우 가독성과 성능 모두를 얻을 수 있다.
- 하지만 복잡한 상황에 컴프리헨션을 사용하는 경우 가독성이 매우 좋지 않아진다.
- 따라서 하위 식이 세 개 이상인 경우 컴프리헨션을 사용하지 말라.

## Better Way 29. 대입식을 사용해 컴프리헨션 안에서 반복 작업을 피하라
### 요약
- 대입식을 사용해 컴프리헨션이나 제너레이터 식의 조건 부분에서 사용한 값을 같은 컴프리헨션이나 제너레이터의 다른 위치에서 재사용할 수 있다.
	- 이를 통해 가독성과 성능을 향상시킬 수 있다.
- 조건이 아닌 부분에도 대입식을 사용할 수 있지만, 그런 형태의 사용은 피해야 한다.
### [PEP-572](https://peps.python.org/pep-0572)
책에서는 컴프리헨션 등을 주요 예시로 설명하지만, 실제 PEP 제안 문서를 보면 `if`-`elif`-`else` 문이 중첩되어 사용하는 것을 간소화하는 것에 중점을 두고 있다.
#### Python 표준 라이브러리 예시
##### [site.py](https://peps.python.org/pep-0572/#site-py)
###### Before
```python
env_base = os.environ.get("PYTHONUSERBASE", None)
if env_base:
    return env_base
```
###### After
```python
if env_base := os.environ.get("PYTHONUSERBASE", None):
    return env_base
```
##### [_pydecimal.py](https://peps.python.org/pep-0572/#pydecimal-py)

###### Before
```python
if self._is_special:
    ans = self._check_nans(context=context)
    if ans:
        return ans
```
###### After
```python
if self._is_special and (ans := self._check_nans(context=context)):
    return ans
```

##### [copy.py](https://peps.python.org/pep-0572/#copy-py)
###### Before
```python
reductor = dispatch_table.get(cls)
if reductor:
    rv = reductor(x)
else:
    reductor = getattr(x, "__reduce_ex__", None)
    if reductor:
        rv = reductor(4)
    else:
        reductor = getattr(x, "__reduce__", None)
        if reductor:
            rv = reductor()
        else:
            raise Error(
                "un(deep)copyable object of type %s" % cls)
```

###### After
```python
if reductor := dispatch_table.get(cls):
    rv = reductor(x)
elif reductor := getattr(x, "__reduce_ex__", None):
    rv = reductor(4)
elif reductor := getattr(x, "__reduce__", None):
    rv = reductor()
else:
    raise Error("un(deep)copyable object of type %s" % cls)
```

##### [datetime.py](https://peps.python.org/pep-0572/#datetime-py)
###### Before
```python
s = _format_time(self._hour, self._minute,
                 self._second, self._microsecond,
                 timespec)
tz = self._tzstr()
if tz:
    s += tz
return s
```
###### After
```python
s = _format_time(self._hour, self._minute,
                 self._second, self._microsecond,
                 timespec)
if tz := self._tzstr():
    s += tz
return s
```

##### [sysconfig.py](https://peps.python.org/pep-0572/#sysconfig-py)
###### Before
```python
while True:
    line = fp.readline()
    if not line:
        break
    m = define_rx.match(line)
    if m:
        n, v = m.group(1, 2)
        try:
            v = int(v)
        except ValueError:
            pass
        vars[n] = v
    else:
        m = undef_rx.match(line)
        if m:
            vars[m.group(1)] = 0
```
###### After
```python
while line := fp.readline():
    if m := define_rx.match(line):
        n, v = m.group(1, 2)
        try:
            v = int(v)
        except ValueError:
            pass
        vars[n] = v
    elif m := undef_rx.match(line):
        vars[m.group(1)] = 0
```

##### 추가 예시
###### Before
```python
diff = x - x_base
if diff:
    g = gcd(diff, n)
    if g > 1:
        return g
```

###### After
```python
if (diff := x - x_base) and (g := gcd(diff, n)) > 1:
    return g
```
### 주의사항
##### 대입식과 할당 문은 다르다
###### 다중 변수는 직접적으로 지원되지 않는다
```python
x = y = z = 0  # Equivalent: (z := (y := (x := 0)))
```
###### 변수 외의 할당은 지원되지 않는다
```python
# No equivalent
a[i] = x
self.rest = []
```
###### 컴마 관련 우선순위 작동 방식이 다르다
```python
x = 1, 2  # Sets x to (1, 2)
(x := 1, 2)  # Sets x to 1
```
###### `Iterable`  패킹/언패킹은 지원되지 않는다
```python
# Equivalent needs extra parentheses
loc = x, y  # Use (loc := (x, y))
info = name, phone, *rest  # Use (info := (name, phone, *rest))

# No equivalent
px, py, pz = position
name, phone, email, *other_info = contact
```
###### 인라인 타입 어노테이션은 지원되지 않는다
```python
# Closest equivalent is "p: Optional[int]" as a separate declaration
p: Optional[int] = None
```
###### `Augmented Assignment` (증강 할당문, `+=`)는 지원되지 않는다
```python
total += tax  # Equivalent: (total := total + tax)
```

## Better Way 32. 긴 리스트 컴프리헨션보다는 제너레이터 식을 사용하라
### 요약
- 입력이 크면 메모리를 너무 많이 사용하기 때문에 리스트 컴프리헨션은 문제를 일으킬 수 있다.
- 제너레이터 식은 이터레이터처럼 한 번에 원소를 하나씩 출력하기 때문에 메모리 문제를 피할 수 있다.
- 제너레이터 식이 반환한 이터레이터르 다른 제너레이터 식의 하위 식으로 사용함으로써 제너레이터 식을 서로 합성할 수 있다.
- 서로 연결된 제너레이터 식은 매우 빠르게 실행되며 메모리도 효율적으로 사용한다.
### [PEP-255](https://peps.python.org/pep-0255)
#### [명세](https://peps.python.org/pep-0255/#specification-yield)
`yield` 의 명세를 보면 다음과 같은 내용이 있다.

> The `yield` statement may only be used inside functions. A function that contains a `yield` statement is called a generator function. A generator function is an ordinary function object in all respects, but has the new `CO_GENERATOR` flag set in the code object’s co_flags member.
> `반환` 문은 함수 내에서만 사용할 수 있습니다. `반환` 문을 포함하는 함수를 제너레이터 함수라고 합니다. 제너레이터 함수는 모든 면에서 일반 함수 객체이지만 코드 객체의 co_flags 멤버에 새로운`CO_GENERATOR` 플래그가 설정되어 있습니다.
> 
> When a generator function is called, the actual arguments are bound to function-local formal argument names in the usual way, but no code in the body of the function is executed. Instead a generator-iterator object is returned; this conforms to the [iterator protocol](https://peps.python.org/pep-0234/ "PEP 234 – Iterators"), so in particular can be used in for-loops in a natural way. Note that when the intent is clear from context, the unqualified name “generator” may be used to refer either to a generator-function or a generator-iterator.
> 제너레이터 함수가 호출되면 실제 인수는 일반적인 방식으로 함수 로컬 형식 인자 이름에 바인딩되지만 함수 본문에 있는 코드는 실행되지 않습니다. 대신 제너레이터-이터레이터 객체가 반환되며, 이는 [이터레이터 프로토콜을](https://peps.python.org/pep-0234/ "PEP 234 – Iterators") 준수하므로 특히 for-루프에서 자연스럽게 사용할 수 있습니다. 문맥에서 의도가 분명한 경우, 한정되지 않은 이름 "generator"를 사용하여 제너레이터 함수 또는 제너레이터 이터레이터를 지칭할 수 있습니다.
>
> Each time the `.next()` method of a generator-iterator is invoked, the code in the body of the generator-function is executed until a `yield` or `return` statement (see below) is encountered, or until the end of the body is reached.
>제너레이터-이터레이터의 `.next()` 메서드가 호출될 때마다 `제너레이터-함수` 본문의 코드는`반환문` 또는`반환문` (아래 참조)이 발생하거나 본문의 끝에 도달할 때까지 실행됩니다.
>
I If a `yield` statement is encountered, the state of the function is frozen, and the value of _expression_list_ is returned to `.next()`’s caller. By “frozen” we mean that all local state is retained, including the current bindings of local variables, the instruction pointer, and the internal evaluation stack: enough information is saved so that the next time `.next()` is invoked, the function can proceed exactly as if the `yield` statement were just another external call.
> **`yield` 문이 발생하면 함수 상태가 고정되고 `.next()`의 호출자에게 _expression_list_ 값이 반환됩니다.** "고정"이란 로컬 변수의 현재 바인딩, 명령 포인터, 내부 평가 스택을 포함한 모든 로컬 상태가 유지된다는 의미로, 다음에`.next()` 가 호출될 때 `함수가`마치 다른 외부 호출인 것처럼 정확하게 진행될 수 있도록 충분한 정보가 저장되어 있습니다.

즉, `yield` 의 목적은 다음과 같다.
1. **발생 시점의 함수 상태 고정**
2. `for` 루프에서 편리하게 생성되는 값을 사용 가능

왜 이런 기능이 필요한지는 [Motivation](https://peps.python.org/pep-0255/#motivation) 문단을 참고하면 찾아볼 수 있다. 이 문단에서는 **함수가 생성된 값 사이의 상태를 유지해야 하는 경우**에 대해 설명하고 있다. 특히 장점에 대해서는 다음과 같이 잘 요약하고 있다.

>As in the thread approach, this allows both sides to be coded in the most natural ways; but unlike the thread approach, this can be done efficiently and on all platforms. Indeed, resuming a generator should be no more expensive than a function call.
>스레드 접근 방식과 마찬가지로 양쪽을 가장 자연스러운 방식으로 코딩할 수 있지만, **스레드 접근 방식과 달리 모든 플랫폼에서 효율적으로 수행할 수 있습니다. 실제로 제너레이터를 다시 시작하는 데 함수 호출보다 더 많은 비용이 들지 않습니다.**

## Better Way 30. 리스트를 반환하기보다는 제너레이터를 사용하라
### 요약
- 제너레이터를 사용하면 결과를 리스트에 합쳐서 반환하는 것보다 더 깔끔하다.
- 제너레이터가 반환하는 이터레이터는 제너레이터 함수의 본문에서 `yield`가 반환하는 값들로 이뤄진 집합을 만들어낸다.
- 제너레이터를 사용하면 작업 메모리에 모든 입력과 출력을 저장할 필요가 없으므로 입력이 아주 커도 출력 시퀀스를 만들 수 있다.

## Better Way 31. 인자에 대해 이터레이션할 때는 방어적이 돼라
### 요약
- 입력 인자를 여러 번 이터레이션 하는 함수나 메서드를 조심하라. 입력받은 인자가 이터레이터면 함수가 이상하게 작동하거나 결과가 없을 수 있다.
- 파이썬의 이터레이터 프로토콜은 컨테이너와 이터레이터가 `iter`, `next` 내장 함수나 `for` 루프 등의 관련 식과 상호작용하는 절차를 정의한다.
- `__iter__` 메서드를 제너레이터로 정의하면 쉽게 이터러블 컨테이너 타입을 정의할 수 있다.
- 어떤 값이 (컨테이너가 아닌) 이터레이터인지 감지하려면, 이 값을 `iter` 내장 함수에 넘겨서 반환되는 값이 원래 값과 같은지 확인하면 된다. 다른 방법으로 `collections.abc.Iterator` 클래스를 `isinstance` 함수와 함께 사용할 수도 있다.

### 주의사항
- 예시에서 제공하는 `방어적 복사` 예시는 항상 가능한 것은 아니다.
	- 라이브러리, 프레임워크 등에서 다음에 `iterator` 를 새로 만드는 경우 이전의 `iterator` 와 다른 데이터가 반환되는 경우도 많다.
		- **해당 코드의 문제로 볼 수 있지만, 불가피하게 의존이 필요한 경우에는 문제를 온전히 끊어낼 수는 없다.**
		- 따라서 온전한 방어적 복사를 하기 위해서는 컬렉션 등에 `Iterable` 의 데이터를 담아서 처리해야 하는 경우도 있다.
	- 제너레이터와 같은 "일회용 이터레이터"도 많기 때문에, 적절히 사용해야 한다.
		- 제너레이터는 **"상태 유지"** 기능이 있기 때문.
### 레퍼런스
- https://stackoverflow.com/a/31245371

## Better Way 33. `yield from`을 사용해 여러 제너레이터를 합성하라
###  요약
- `yield from` 식을 사용하면 여러 내장 제너레이터를 모아서 제너레이터 하나로 합성할 수 있다.
- 직접 내포된 제너레이터를 이터레이션하면서 각 제너레이터의 출력을 내보내는 것보다 `yield from` 을 사용하는 것이 성능 면에서 더 좋다.
### [PEP-380](https://peps.python.org/pep-0380/)
실제로 `yield from` 이 해주는 기능은 생각보다 많다. 특히, [Formal Semantics](https://peps.python.org/pep-0380/#formal-semantics) 부분을 살펴보면 아예 간략한 정의가 있다.
```python
_i = iter(EXPR)
try:
    _y = next(_i)
except StopIteration as _e:
    _r = _e.value
else:
    while 1:
        try:
            _s = yield _y
        except GeneratorExit as _e:
            try:
                _m = _i.close
            except AttributeError:
                pass
            else:
                _m()
            raise _e
        except BaseException as _e:
            _x = sys.exc_info()
            try:
                _m = _i.throw
            except AttributeError:
                raise _e
            else:
                try:
                    _y = _m(*_x)
                except StopIteration as _e:
                    _r = _e.value
                    break
        else:
            try:
                if _s is None:
                    _y = next(_i)
                else:
                    _y = _i.send(_s)
            except StopIteration as _e:
                _r = _e.value
                break
RESULT = _r
```

기능은 해당 PEP 문서에도 잘 요약되어 있다.

> - Any values that the iterator yields are passed directly to the caller.
> - 반복자가 산출하는 모든 값은 호출자에게 직접 전달됩니다.
> 
> - Any values sent to the delegating generator using `send()` are passed directly to the iterator. If the sent value is None, the iterator’s `__next__()` method is called. If the sent value is not None, the iterator’s `send()` method is called. If the call raises StopIteration, the delegating generator is resumed. Any other exception is propagated to the delegating generator.
> - `send()`를 사용하여 위임 생성기로 전송된 모든 값은 이터레이터에 직접 전달됩니다. 전송된 값이 `None`이면 이터레이터의 `__next__()` 메서드가 호출됩니다. 전송된 값이 `None`이 아닌 경우 이터레이터의 `send()` 메서드가 호출됩니다. 호출에서 `StopIteration`이 발생하면 위임 제너레이터가 재개됩니다. 다른 예외는 위임 제너레이터로 전파됩니다.
> 
> - Exceptions other than GeneratorExit thrown into the delegating generator are passed to the `throw()` method of the iterator. If the call raises StopIteration, the delegating generator is resumed. Any other exception is propagated to the delegating generator.
> - 위임 제너레이터에 던져진 `GeneratorExit` 이외의 예외는 이터레이터의 `throw()` 메서드로 전달됩니다. 호출이 `StopIteration` 을 발생시키면 위임 제너레이터가 다시 시작됩니다. 다른 모든 예외는 위임 제너레이터로 전파됩니다.
> 
> - If a GeneratorExit exception is thrown into the delegating generator, or the `close()` method of the delegating generator is called, then the `close()` method of the iterator is called if it has one. If this call results in an exception, it is propagated to the delegating generator. Otherwise, GeneratorExit is raised in the delegating generator.
> - 위임 제너레이터에 GeneratorExit 예외가 발생하거나 위임 제너레이터의 `close()` 메서드가 호출되면 이터레이터의 `close()` 메서드가 있는 경우 호출됩니다. 이 호출로 인해 예외가 발생하면 위임 제너레이터로 전파됩니다. 그렇지 않으면 위임 제너레이터에서 `GeneratorExit`가 발생합니다.
> 
> - The value of the `yield from` expression is the first argument to the `StopIteration` exception raised by the iterator when it terminates.
> - `yield from` 표현식 값은 이터레이터가 종료될 때 발생하는 `StopIteration` 예외의 첫 번째 인자입니다.
> 
> - `return expr` in a generator causes `StopIteration(expr)` to be raised upon exit from the generator.
> - 제너레이터에서 `expr` 을 반환하면 제너레이터가 종료될 때 `StopIteration(expr)` 이 발생하게 됩니다.

즉, 단순히 제너레이터를 모아주는 것 외에도 예외 처리 등의 기능이 포함되어 있으므로 이를 사용하는 것이 바람직하다.


## Better Way 34. `send`로 제너레이터에 데이터를 주입하지 말라
### 요약
- `send` 메서드를 사용해 데이터를 제너레이터에 주입할 수 있다. 제너레이터는 `send` 로 주입된 값을 `yield` 식이 반환하는 값을 통해 받으며, 이 값을 변수에 저장해 활용할 수 있다.
- `send`와 `yield from` 식을 함께 사용하면 제너레이터의 출력에 `None`이 불쑥 타나타나는 의외의 결과를 얻을 수도 있다.
- 합성할 제너레이터들의 입력으로 이터레이터를 전달하는 방식이 `send`를 사용하는 방식보다 더 낫다. `send`는 가급적 사용하지 말라.
### [PEP-342](https://peps.python.org/pep-0342)
**사실 `send` 메서드는 코루틴을 구현하기 위한 방법이다.** 이는 [Motivation](https://peps.python.org/pep-0342/#motivation) 항목을 보면 특히 자세히 설명된다. 해당 PEP 문서에 관련된 히스토리들이 자세하게 적혀있으므로 읽는 것을 추천한다.

> Coroutines are a natural way of expressing many algorithms, such as simulations, games, asynchronous I/O, and other forms of event-driven programming or co-operative multitasking. Python’s generator functions are almost coroutines – but not quite – in that they allow pausing execution to produce a value, but do not provide for values or exceptions to be passed in when execution resumes. They also do not allow execution to be paused within the `try` portion of `try/finally` blocks, and therefore make it difficult for an aborted coroutine to clean up after itself.
> 코루틴은 시뮬레이션, 게임, 비동기 입출력, 기타 형태의 이벤트 중심 프로그래밍 또는 협동 멀티태스킹 등 많은 알고리즘을 표현하는 자연스러운 방법입니다. 파이썬의 제너레이터 함수는 실행을 일시 중지하여 값을 생성할 수 있지만 실행이 재개될 때 전달할 값이나 예외를 제공하지 않는다는 점에서 거의 코루틴에 가깝지만 완전히 그런 것은 아닙니다. 또한 `try/finally` 블록의 `try` 부분 내에서 실행을 일시 중지할 수 없으므로 중단된 코루틴을 스스로 정리하기가 어렵습니다.

> Also, generators cannot yield control while other functions are executing, unless those functions are themselves expressed as generators, and the outer generator is written to yield in response to values yielded by the inner generator. This complicates the implementation of even relatively simple use cases like asynchronous communications, because calling any functions either requires the generator to _block_ (i.e. be unable to yield control), or else a lot of boilerplate looping code must be added around every needed function call.
> 또한 제너레이터는 다른 함수가 실행되는 동안에는 제어권을 양보할 수 없으며, 그 함수 자체가 제너레이터로 표현되고 외부 제너레이터가 내부 제너레이터가 산출한 값에 대한 응답으로 양보하도록 작성되지 않는 한, 다른 함수가 실행되는 동안에는 제어권을 양보할 수 없습니다. 이는 비동기 통신과 같이 비교적 간단한 사용 사례의 구현도 복잡하게 만드는데, 함수를 호출하려면 제너레이터가 _차단_ (즉, 제어권을 반환할 수 없음)되거나 필요한 함수 호출마다 많은 상용구 루핑 코드를 추가해야 하기 때문입니다.

하지만 이와는 별개로, 현재의 python은 `asyncio`와 `Coroutine` 객체가 있으므로 예전의 이해하기도 사용하기도 어려운 방법을 고수할 필요는 없다.

## Better Way 35. 제너레이터 안에서 `throw`로 상태를 변화시키지 말라
### 요약
- `throw` 메서드를 사용하면 제너레이터가 마지막으로 실행한 `yield` 식의 위치에서 예외를 다시 발생시킬 수 있다.
- `throw`를 사용하면 가독성이 나빠진다. 예외를 잡아내고 다시 발생시키는 데 준비 코드가 필요하며 내포 단계가 깊어지기 때문이다.
- 제너레이터에서 예외적인 동작을 제공하는 더 나은 방법은 `__iter__` 메서드를 구현하는 클래스를 사용하면서 예외적인 경우에 상태를 전이시키는 것이다.

## Better Way 36. 이터레이터나 제너레이터를 다룰 때는 `itertools`를 사용하라
### 요약
- 이터레이터나 제너레이터를 다루는 `itertools` 함수는 세 가지 범주로 나눌 수 있다.
	- 연결
		- `chain` 
		- `repeat`
		- `cycle`
		- `tee`
		- `zip_longest`
	- 필터
		- `islice
		- `takewhile`
		- `dropwhile`
		- `filterfalse`
	- 조합
		- `accumulate`
		- `product
		- `permutations`
		- `combinations`
		- `combinations_with_replacement`
### 핵심 기능
- `chain`, `cycle`
	- 제너레이터 사용 시 빈번히 사용
- `product`, `permutations`, `combinations`
	- 알고리즘 문제를 풀 때 용이함
### 요약 (참고: https://docs.python.org/ko/3/library/itertools.html)
#### 무한 이터레이터
| 이터레이터                                                                                                 | 인자              | 결과                                 | 예                                     |
| ----------------------------------------------------------------------------------------------------- | --------------- | ---------------------------------- | ------------------------------------- |
| [`count()`](https://docs.python.org/ko/3/library/itertools.html#itertools.count "itertools.count")    | [start[, step]] | start, start+step, start+2*step, … | `count(10) → 10 11 12 13 14 ...`      |
| [`cycle()`](https://docs.python.org/ko/3/library/itertools.html#itertools.cycle "itertools.cycle")    | p               | p0, p1, … plast, p0, p1, …         | `cycle('ABCD') → A B C D A B C D ...` |
| [`repeat()`](https://docs.python.org/ko/3/library/itertools.html#itertools.repeat "itertools.repeat") | elem [,n]       | elem, elem, elem, … 끝없이 또는 최대 n 번  | `repeat(10, 3) → 10 10 10`            |
#### 가장 짧은 입력 시퀀스에서 종료되는 이터레이터
|이터레이터|인자|결과|예|
|---|---|---|---|
|[`accumulate()`](https://docs.python.org/ko/3/library/itertools.html#itertools.accumulate "itertools.accumulate")|p [,func]|p0, p0+p1, p0+p1+p2, …|`accumulate([1,2,3,4,5]) → 1 3 6 10 15`|
|[`batched()`](https://docs.python.org/ko/3/library/itertools.html#itertools.batched "itertools.batched")|p, n|(p0, p1, …, p_n-1), …|`batched('ABCDEFG', n=3) → ABC DEF G`|
|[`chain()`](https://docs.python.org/ko/3/library/itertools.html#itertools.chain "itertools.chain")|p, q, …|p0, p1, … plast, q0, q1, …|`chain('ABC', 'DEF') → A B C D E F`|
|[`chain.from_iterable()`](https://docs.python.org/ko/3/library/itertools.html#itertools.chain.from_iterable "itertools.chain.from_iterable")|iterable|p0, p1, … plast, q0, q1, …|`chain.from_iterable(['ABC', 'DEF']) → A B C D E F`|
|[`compress()`](https://docs.python.org/ko/3/library/itertools.html#itertools.compress "itertools.compress")|data, selectors|(d[0] if s[0]), (d[1] if s[1]), …|`compress('ABCDEF', [1,0,1,0,1,1]) → A C E F`|
|[`dropwhile()`](https://docs.python.org/ko/3/library/itertools.html#itertools.dropwhile "itertools.dropwhile")|predicate, seq|seq[n], seq[n+1], starting when predicate fails|`dropwhile(lambda x: x<5, [1,4,6,4,1]) → 6 4 1`|
|[`filterfalse()`](https://docs.python.org/ko/3/library/itertools.html#itertools.filterfalse "itertools.filterfalse")|predicate, seq|elements of seq where predicate(elem) fails|`filterfalse(lambda x: x%2, range(10)) → 0 2 4 6 8`|
|[`groupby()`](https://docs.python.org/ko/3/library/itertools.html#itertools.groupby "itertools.groupby")|iterable[, key]|key(v)의 값으로 그룹화된 서브 이터레이터들||
|[`islice()`](https://docs.python.org/ko/3/library/itertools.html#itertools.islice "itertools.islice")|seq, [start,] stop [, step]|seq[start:stop:step]의 요소들|`islice('ABCDEFG', 2, None) → C D E F G`|
|[`pairwise()`](https://docs.python.org/ko/3/library/itertools.html#itertools.pairwise "itertools.pairwise")|iterable|(p[0], p[1]), (p[1], p[2])|`pairwise('ABCDEFG') → AB BC CD DE EF FG`|
|[`starmap()`](https://docs.python.org/ko/3/library/itertools.html#itertools.starmap "itertools.starmap")|func, seq|func(*seq[0]), func(*seq[1]), …|`starmap(pow, [(2,5), (3,2), (10,3)]) → 32 9 1000`|
|[`takewhile()`](https://docs.python.org/ko/3/library/itertools.html#itertools.takewhile "itertools.takewhile")|predicate, seq|seq[0], seq[1], until predicate fails|`takewhile(lambda x: x<5, [1,4,6,4,1]) → 1 4`|
|[`tee()`](https://docs.python.org/ko/3/library/itertools.html#itertools.tee "itertools.tee")|it, n|it1, it2, … itn 하나의 이터레이터를 n개의 이터레이터로 나눕니다||
|[`zip_longest()`](https://docs.python.org/ko/3/library/itertools.html#itertools.zip_longest "itertools.zip_longest")|p, q, …|(p[0], q[0]), (p[1], q[1]), …|`zip_longest('ABCD', 'xy', fillvalue='-') → Ax By C- D-`|
#### 조합형 이터레이터

| 이터레이터                                                                                                                                                                      | 인자                 | 결과                                           |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ | -------------------------------------------- |
| [`product()`](https://docs.python.org/ko/3/library/itertools.html#itertools.product "itertools.product")                                                                   | p, q, … [repeat=1] | 데카르트 곱(cartesian product), 중첩된 for 루프와 동등합니다 |
| [`permutations()`](https://docs.python.org/ko/3/library/itertools.html#itertools.permutations "itertools.permutations")                                                    | p[, r]             | r-길이 튜플들, 모든 가능한 순서, 반복되는 요소 없음              |
| [`combinations()`](https://docs.python.org/ko/3/library/itertools.html#itertools.combinations "itertools.combinations")                                                    | p, r               | r-길이 튜플들, 정렬된 순서, 반복되는 요소 없음                 |
| [`combinations_with_replacement()`](https://docs.python.org/ko/3/library/itertools.html#itertools.combinations_with_replacement "itertools.combinations_with_replacement") | p, r               | r-길이 튜플들, 정렬된 순서, 반복되는 요소 있음                 |

## Better Way 37. 내장 타입을 여러 단계로 내포시키기보다는 클래스를 합성하라
### 요약
- 내장 타입에 의존하여 코드 작성 시 이해하거나 읽기 어려운 코드가 작성될 수 있다.
- 내장 타입이 여러 단계로 내포되는 경우 관리가 어려워지므로, 내장 타입이 중첩되어 사용되는 경우 클래스로 분리하라.
- `namedtuple`, `dataclasses` 모듈들을 사용하여 간단한 클래스를 정의하여 빠르게 적용할 수 있다.
- 내장 타입을 클래스 내부에 은닉하고, 클래스의 메서드를 사용하여 명확하고 읽기 좋은 코드를 작성할 수 있다.

## Better Way 38. 간단한 인터페이스의 경우 클래스 대신 함수를 받아라 
### 요약
- 파이썬의 여러 컴포넌트 사이에 간단한 인터페이스가 필요할 때는 클래스를 정의하고 인스턴스화 하는 대신 간단히 함수를 사용할 수 있다.
- 파이썬 함수나 메서드는 일급 시민이다. 따라서 (다른 타입의 값과 마찬가지로) 함수나 함수 참조를 식에 사용할 수 있다.
- `__call__` 특별 메서드를 사용하면 클래스의 인스턴스인 객체를 일반 파이썬 함수처럼 호출할 수 있다.
- 상태를 유지하기 위한 함수가 필요한 경우에는 상태가 있는 클로저를 정의하는 대신 `__call__` 메서드가 있는 클래스를 정의할 지 고려해보라.
### 프로토콜
이전에도 언급된 [PEP-544](https://peps.python.org/pep-0544) 를 참고하면 특히나 도움이 된다.
- `Protocol` 을 상속하는 클래스를 정의하여 사용하면 타입 힌트와 타입 체커를 모두 만족시킬 수 있다.
## Better Way 39. 객체를 제너릭하게 구성하려면 `@classmethod`를 통한 다형성을 활용하라
### 요약
- 파이썬의 클래스에는 생성자가 `__init__` 메서드 뿐이다.
- `@classmethod`를 사용하면 클래스에 다른 생성자를 정의할 수 있다.
- 클래스 메서드 다형성을 활용하면 여러 구체적인 하위 클래스들의 객체를 만들고 연결하는 제너릭한 방법을 제공할 수 있다.
### 디자인 패턴
사실상 생성형 디자인 패턴 관련 내용이다. 아래 두 패턴 참고.
- [팩토리 메서드 패턴](https://refactoring.guru/ko/design-patterns/factory-method)
- [추상 팩토리 패턴](https://refactoring.guru/ko/design-patterns/abstract-factory)

## Better Way 40. `super` 로 부모 클래스를 초기화하라

### 요약
- 파이썬은 표준 메서드 결정 순서 (`MRO`)를 활용해 상위 클래스 초기화 순서와 다이아몬드 상속 문제를 해결한다.
- 부모 클래스를 초기화할 때는 `super` 내장 함수를 아무 인자 없이 호출하라.
	- `super`를 아무 인자 없이 호출하면 파이썬 컴파일러가 자동으로 올바른 파라미터를 넣어준다.

### 레퍼런스
- [PEP-3135](https://peps.python.org/pep-3135/) 참고.

## Better Way 41. 기능을 합성할 때는 믹스인 클래스를 사용하라\
### 요약
- 믹스인을 사용해 구현할 수 있는 기능을 인스턴스 애트리뷰트와 `__init__`을 사용하는 다중 상속을 통해 구현하지 말라.
- 믹스인 클래스가 클래스별로 특화된 기능을 필요로 한다면 인스턴스 수준에서 끼워 넣을 수 있는 기능(정해진 메서드를 통해 해당 기능을 인스턴스가 제공하게 만듦)을 활용하라.
- 믹스인에는 필요에 따라 인스턴스 메서드는 물론 클래스 메서드도 포함될 수 있다.

### 실제 사용 사례
#### 장고

장고에서 API 뷰를 작성 시 특히나 믹스인을 많이 사용하고 있다.

```python
"""  
Basic building blocks for generic class based views.  
  
We don't bind behaviour to http method handlers yet,  
which allows mixin classes to be composed in interesting ways.  
"""  
from rest_framework import status  
from rest_framework.response import Response  
from rest_framework.settings import api_settings  
  
  
class CreateModelMixin:  
    """  
    Create a model instance.    """    def create(self, request, *args, **kwargs):  
        serializer = self.get_serializer(data=request.data)  
        serializer.is_valid(raise_exception=True)  
        self.perform_create(serializer)  
        headers = self.get_success_headers(serializer.data)  
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)  
  
    def perform_create(self, serializer):  
        serializer.save()  
  
    def get_success_headers(self, data):  
        try:  
            return {'Location': str(data[api_settings.URL_FIELD_NAME])}  
        except (TypeError, KeyError):  
            return {}  
  
  
class ListModelMixin:  
    """  
    List a queryset.    """    def list(self, request, *args, **kwargs):  
        queryset = self.filter_queryset(self.get_queryset())  
  
        page = self.paginate_queryset(queryset)  
        if page is not None:  
            serializer = self.get_serializer(page, many=True)  
            return self.get_paginated_response(serializer.data)  
  
        serializer = self.get_serializer(queryset, many=True)  
        return Response(serializer.data)  
  
  
class RetrieveModelMixin:  
    """  
    Retrieve a model instance.    """    def retrieve(self, request, *args, **kwargs):  
        instance = self.get_object()  
        serializer = self.get_serializer(instance)  
        return Response(serializer.data)  
  
  
class UpdateModelMixin:  
    """  
    Update a model instance.    """    def update(self, request, *args, **kwargs):  
        partial = kwargs.pop('partial', False)  
        instance = self.get_object()  
        serializer = self.get_serializer(instance, data=request.data, partial=partial)  
        serializer.is_valid(raise_exception=True)  
        self.perform_update(serializer)  
  
        if getattr(instance, '_prefetched_objects_cache', None):  
            # If 'prefetch_related' has been applied to a queryset, we need to  
            # forcibly invalidate the prefetch cache on the instance.            instance._prefetched_objects_cache = {}  
  
        return Response(serializer.data)  
  
    def perform_update(self, serializer):  
        serializer.save()  
  
    def partial_update(self, request, *args, **kwargs):  
        kwargs['partial'] = True  
        return self.update(request, *args, **kwargs)  
  
  
class DestroyModelMixin:  
    """  
    Destroy a model instance.    """    def destroy(self, request, *args, **kwargs):  
        instance = self.get_object()  
        self.perform_destroy(instance)  
        return Response(status=status.HTTP_204_NO_CONTENT)  
  
    def perform_destroy(self, instance):  
        instance.delete()
```

위 믹스인을 `ViewSet` 클래스들에 사용하는 공식 코드는 다음과 같다.

```python
class ViewSet(ViewSetMixin, views.APIView):  
    """  
    The base ViewSet class does not provide any actions by default.    """    pass  
  
  
class GenericViewSet(ViewSetMixin, generics.GenericAPIView):  
    """  
    The GenericViewSet class does not provide any actions by default,    but does include the base set of generic view behavior, such as    the `get_object` and `get_queryset` methods.    """    pass  
  
  
class ReadOnlyModelViewSet(mixins.RetrieveModelMixin,  
                           mixins.ListModelMixin,  
                           GenericViewSet):  
    """  
    A viewset that provides default `list()` and `retrieve()` actions.    """    pass  
  
  
class ModelViewSet(mixins.CreateModelMixin,  
                   mixins.RetrieveModelMixin,  
                   mixins.UpdateModelMixin,  
                   mixins.DestroyModelMixin,  
                   mixins.ListModelMixin,  
                   GenericViewSet):  
    """  
    A viewset that provides default `create()`, `retrieve()`, `update()`,    `partial_update()`, `destroy()` and `list()` actions.    """    pass
```

## Better Way 42. 비공개 애트리뷰트보다는 공개 애트리뷰트를 사용하라

### 요약
- 파이썬 컴파일러는 비공개 애트리뷰트를 자식 클래스나 클래스 외부에서 사용하지 못하도록 엄격히 금지하지 않는다.
- 내부 API에 있는 클래스의 하위 클래스를 정의하는 사람들이 여러분이 제공하는 클래스의 애트리뷰트를 사용하지 못하도록 막기보다는 애트리뷰트를 사용해 더 많은 일을 할 수 있게 허용하라.
- 비공개 애트리뷰트로 (외부나 하위 클래스의) 접근을 막으려고 시도하기보다는 보호된 필드를 사용하면서 문서에 적절한 가이드를 남겨라.

### 린터
- [SLF001](https://docs.astral.sh/ruff/rules/private-member-access/) 참고.

### 개인적인 의견
- 그럼에도 불구하고, 경우에 따라서 외부에 노출하거나 상속을 허용하는 것이 아무런 이득이 없는 경우에는 언더바를 사용하는 것이 개인적으로는 더 좋다고 생각한다. 개인적인 근거는:
	- 파이썬의 네이밍 규칙을 이해하고 있다면, 클래스나 메서드, 필드 근처에 있는 docstring 을 읽는 것보다 훨씬 이해하기 쉽다
		- 누가 봐도 "건들면 문제 생길 법한 필드" 지 않는가

## Better Way 43. 커스텀 컨테이너 타입은 collections.abc를 상속하라
### 요약
- 간편하게 사용할 경우에는 파이썬 컨테이너 타입(리스트나 딕셔너리 등)을 직접 상속하라.
- 커스텀 컨테이너를 제대로 구현하려면 수많은 메서드를 구현해야 한다는 점에 주의하라.
- 커스텀 컨테이너 타입이 `collections.abc` 에 정의된 인터페이스를 상속하면 커스텀 컨테이너 타입이 정상적으로 작동하기 위해 필요한 인터페이스와 기능을 제대로 구현하도록 보장할 수 있다.

파이썬은 워낙 이미 구현되어 있는 클래스들이 많아서 굳이 맨 땅에서 시작해야 하나 싶긴 함.

## Better Way 44. 세터와 게터 메서드 대신 평범한 애트리뷰트를 사용하라

### 요약
- 새로운 클래스 인터페이스를 정의할 때는 간단한 공개 애트리뷰트에서 시작하고, 세터나 게터 메서드를 가급적 사용하지 말라.
- 객체에 있는 애트리뷰트에 접근할 때 특별한 동작이 필요하면 @property로 이를 구현할 수 있다.
- `@property` 메서드를 만들 때는 최소 놀람의 법칙을 따르고 이상한 부작용을 만들어내지 말라.
- `@property` 메서드가 빠르게 실행되도록 유지하라. 느리거나 복잡한 작업의 경우 (특히 I/O를 수행하는 등의 부수 효과가 있는 경우)에는 프로퍼티 대신 일반적인 메서드를 사용하라.

### 잡기술

보통 `Mixin` 패턴과 혼용하면 유용하게 사용할 수 있다.

```python
from typing import TypeVar, Protocol

class HasName(Protocol):
    first_name: str
    last_name: str

class NameMixin:
    @property
    def full_name(self: HasName) -> str:
        return f"{self.first_name} {self.last_name}"

class Person(NameMixin):
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name

person = Person("John", "Doe")
print(person.full_name)

```

## Better Way 45. 애트리뷰트를 리팩터링하는 대신 `@property` 를 사용하라

### 요약
- `@property`를 사용해 기존 인스턴스 애트리뷰트에 새로운 기능을 제공할 수 있다.
- `@property`를 사용해 데이터 모델을 점진적으로 개선하라.
- `@property` 메서드를 너무 과하게 쓰고 있다면, 클래스와 클래스를 사용하는 모든 코드를 리팩토링하는 것을 고려하라.

같은 내용 반복적이라 생략함.

## Better Way 46. 재사용 가능한 `@property` 메서드를 만들려면 디스크립터를 사용하라

### 요약
- @property 메서드의 동작과 검증 기능을 재사용하고 싶다면 디스크립터 클래스를 만들라.
- 디스크립터 클래스를 만들 때는 메모리 누수를 방지하기 위해 `WeakKeyDictionary`를 사용하라.
- `__getattribute__` 가 디스크립터 프로토콜을 사용해 애트리뷰트 값을 읽거나 설정하는 방식을 정확히 이해하라.

### 개인적인 의견
- 굳이 디스크립터 객체를 만들어서 협업을 힘들게 할 이유가 있을까? 그것도 약한 참조까지 써가면서...
	- 평범한 비동기 코드조차 진입 장벽이 있는 판에 굳이 이렇게 작성해야 하는지는 좀 의문

## Better Way 47. 지연 계산 애트리뷰트가 필요하면 `__getattr__`, `__getattribute__`, `__setattr__` 을 사용하라
### 요약
- `__getattr__`과 `__setattr__` 을 사용해 객체의 애트리뷰트를 지연해 가져오거나 저장할 수 있다.
- `__getattr__`은 애트리뷰트가 존재하지 않을 때만 호출되지만, `__getattribute__` 는 애트리뷰트를 읽을 때마다 항상 호출된다는 점을 이해하라.
- `__getattribute__`와 `__setattr__` 에서 무한 재귀를 피하려면 `super()` 에 있는 (즉, object 클래스에 있는) 메서드를 사용해 인스턴스 애트리뷰트에 접근하라.

### 조금 풀어서 쓴 설명
- [stackoverflow 글](https://stackoverflow.com/questions/3278077/difference-between-getattr-and-getattribute) 참고.
	- 객체의 어트리뷰트 접근 시 `__getattr__` 또는 `__getattribute__` 사용하여 값을 찾음
	- `__getattribute__`, `__setattr__` 는 어트리뷰트 값 접근 / 수정 시 무조건 호출
	- `__getattr__`  호출 시 객체 내부에 있는 `__dict__` 에서 값을 찾음 (캐싱 개념)
		- `__getattribute__` 와는 다르게 `__dict__` 를 먼저 찾아봄
		- 있으면 꺼내서 바로 반환
		- 없으면 내부 로직 수행함

## Better Way 48, 49, 50, 51
- 생략, 이 부분들은 오히려 안티 패턴으로 취급해야 한다고 생각함
## Better Way 52. 자식 프로세스를 관리하기 위해 `subprocess`를 사용하라
### 요약
- 파이썬은 `GIL` 구조로 인해 하나의 CPU 코어에 묶여있지만, 하위 프로세스를 사용하면 여러 CPU를 동시에 조작할 수 있다.
- `subprocess` 모듈을 사용해 자식 프로세스를 실행하고 입력과 출력 스트림을 관리할 수 있다.
- 간단하게 자식 프로세스를 실행하고 싶은 경우에는 `run` 편의 함수를 사용하라. 유닉스 스타일의 파이프라인이 필요하면 `Popen` 클래스를 사용하라.
- `communicate` 메서드에 `timeout` 파라미터를 지정하여 자식 프로세스가 멈추거나 교착 상태가 발생하는 상황을 방지할 수 있다.

### 참고 사항
- `asyncio` 등을 사용한 "동시성" 프로그래밍 환경에서는 서브 프로세스 방식이 대부분 블로킹 방식으로 처리되므로, 이벤트 루프를 차단할 수 있다.
	- [create-subprocess-in-async-function (ASYNC220) - Ruff (astral.sh)](https://docs.astral.sh/ruff/rules/create-subprocess-in-async-function/#create-subprocess-in-async-function-async220) 참고.
- 동시성과 병렬성은 상당히 다른 개념이며, 네트워크 IO 최적화가 필요한 상황이라면 멀티 프로세싱보다는 `asyncio` 기반의 동시성으로 처리하는 것이 좋다.
	- 동시성과 병렬성의 차이에 대해 이해하기 어렵다면 [language agnostic - What is the difference between concurrency and parallelism? - Stack Overflow](https://stackoverflow.com/questions/1050222/what-is-the-difference-between-concurrency-and-parallelism) 링크 참고.

## Better Way 53. 블로킹 I/O의 경우 스레드를 사용하고 병렬성을 피하라.
### 요약
- `CPython` 은 전역 인터프리터 락(`Global Interpreter Lock, GIL`)이라는 방법을 사용하여 상태 일관성을 강제로 유지한다.
	- `GIL`은 상호 배제 락 (뮤텍스(`mutex`))이며, 스레드 인터럽트가 함부로 발생하는 것을 방지하여 인터프리터 상태가 제대로 유지되도록 한다.
	- `GIL`은 멀티 스레드를 지원하나 `GIL` 로 인해 하나의 스레드만 실행될 수 있다. 따라서 멀티 스레딩을 사용시 병렬 처리가 제대로 수행되지 않는다.
- 블로킹 I/O 처리 시 멀티 스레딩을 사용하더라도 CPU 바운드 I/O 가 아닌 네트워크 바운드 I/O 이므로 성능 개선이 가능하다.

## Better Way 54. 스레드에서 데이터 경합을 위해 `Lock`을 사용하라
### 요약
- `GIL`은 경합 조건을 방지해주지 않는다.
- `GIL`은 시분할 방식으로 작동하므로, 언제 프로그램이 인터럽트 될 지 알 수 없다.
- 간단한 단일 명령어로 보이는 작업도 실제로는 여러 단계의 명령어로 나뉠 수 있다.
- 따라서 프로그램 내에서 불변 조건을 유지해야 하는 중요 로직이라면 `Lock`을 사용하여 경합 조건을 방지해야 한다.

### 더 나아가서
- `Lock` 사용 시 상당히 번거롭다.
	- 잠금 대기 관련 로직을 직접 제어해야 한다.
	- `RLock` 객체 사용 시, 타 언어에서 사용하는 `ReentrantLock`을 그대로 사용할 수 있다.
		- `synchronized`를 `ReentrantLock` 으로 대체하려는 시도가 자바에서 많다. 
			- [pgjdbc issue#1951]([Loom compatible - replace synchronized block with for example j.u.c.ReentrantLock · Issue #1951 · pgjdbc/pgjdbc · GitHub](https://github.com/pgjdbc/pgjdbc/issues/1951)) 참고.
	- `Condition` 객체 사용 시 `Lock`의 기능을 그대로 사용하면서도, 여러 클래스의 Producer / Consumer 로직을 단순화 할 수 있다.
		- [Condition 객체]([threading — Thread-based parallelism — Python 3.12.4 documentation](https://docs.python.org/3/library/threading.html#condition-objects)) 참고.
- `Semaphore` 사용 또한 병행되어야 한다.
	- 단순 `Lock` 클래스만으로는 동시성 / 병행성을 세밀하게 제어할 수 없다.
## Better Way 55. `Queue`를 사용해 스레드 사이의 작업을 조율하라
### 요약
- 순차적인 작업을 동시에 여러 파이썬 스레드에서 실행되도록 조직하고 싶을 때, 특히 I/O 위주의 프로그램인 경우라면 파이프라인이 매우 유용하다.
- 동시성 파이프라인을 만들 때 발생할 수 있는 여러가지 문제(바쁜 대기, 작업자에게 종료를 알리는 방법, 잠재적인 메모리 사용량 폭발 등)를 잘 알아두라.
- Queue 클래스는 튼튼한 파이프라인을 구축할 때 필요한 기능인 블로킹 연산, 버퍼 크기 지정, join을 통한 완료 대기를 모두 제공한다.

### 더 나아가서
- 프로그램이 고도화 되어야 하면 Producer / Consumer 구조 적용은 필수적이다.
	- 다른 패턴들이 있더라도 이 패턴만큼 보편적이거나 구현하기는 쉽지 않다.
	- 비동기 환경이라고 해도 이는 필수적이다.
		- 비동기 환경에서 특정한 작업(Task)를 예약하는 작업 자체가 `asyncio`의 `Task`, `Future`에 의존해야 하는데, 이 객체들은 상당히 관리하기가 까다롭다.
		- 어느 정도 asyncio 기반 생태계가 구성 되어야 수월하게 개발할 수 있다. 또는 생태계에 대한 이해를 하고 있어야 한다.
		- 코루틴이나 비동기 Task 자체가 Producer/Consumer 패턴에 비해 메모리 비용이 저렴하지는 않다.
			- `asyncio.gather` 또는 `TaskGroup` 등을 사용하면 모든 Task 가 종료될 때까지 메모리를 홀딩하는 문제가 있다. 

## Better Way 56. 언제 동시성이 필요할지 인식하는 방법을 알아두라

### 요약
- 프로그램이 커지면서 범위와 복잡도가 증가함에 따라 동시에 실행되는 여러 실행 흐름이 필요해지는 경우가 많다.
- 동시성을 조율하는 가장 일반적인 방법으로는 팬아웃(새로운 동시성 단위들을 만들어냄)과 팬인(기존 동시성 단위들의 실행이 끝나기를 기다림)이 있다.
- 파이썬은 팬아웃과 팬인을 구현하는 다양한 방법을 제공한다.

### 더 나아가서
- 팬아웃이 가능한 지점이 Bound 작업이라는 점이 중요하다.
- 실제로 중요한 것은 CPU Bound 와 I/O Bound 를 구분하는 것이다.\
	- [잘 정리된 글](https://realpython.com/python-concurrency/)이 있으니 참고.
- CPU Bound 작업의 경우 CPU 코어를 늘리는 방법으로 확장할 수 있다.
	- 자원 효율적인 방법 순으로 정리하면 다음과 같다.
		- Thread
		- Process (or Subprocess)
	- 하지만 Python은 `GIL`로 인해 Thread 를 사용 시 CPU Bound 작업에서는 이점을 얻을 수 없다.
		- 따라서 CPU Bound 처리 시, 멀티 프로세싱이 강요된다.
- I/O Bound 작업의 경우 이점이 명확하다.
	-  `GIL`의 존재에도 불구하고 Thread 를 사용하여 I/O 작업을 팬아웃 할 수 있다.
		- I/O 작업은 CPU 사용량이 많은 작업이 아니기 때문에 이를 Thread 처리하더라도 성능 상의 손실이 적다.
	- 자원 효율적인 방법 순으로 정리하면 다음과 같다.
		- Coroutine
		- Thread
		- Process

## Better Way 57. 요구에 따라 팬아웃을 진행하려면 새로운 스레드를 생성하지 말라
### 요약
- 스레드에는 많은 단점이 있다. 스레드를 시작하고 실행하는 데 비용이 들기 때문에 스레드가 많이 필요하면 상당히 많은 메모리를 사용한다. 그리고 스레드 사이를 조율하기 위해 Lock과 같은 특별한 도구를 사용해야 한다.
- 스레드를 시작하거나 스레드가 종료하기를 기다리는 코드에게 스레드 실행 중에 발생한 예외를 돌려주는 파이썬 내장 기능은 없다. 이로 인해 스레드 디버깅이 더 어려워진다.
### 더 나아가서
- 제발 [concurrent.futures — Launching parallel tasks — Python 3.12.4 문서](https://docs.python.org/ko/3/library/concurrent.futures.html) 를 사용하자.

## Better Way 58. 동시성과 Queue를 사용하기 위해 코드를 어떻게 리팩터링해야 하는지 이해하라
### 요약
- 작업자 스레드 수를 고정하고 Queue와 함께 사용하면 스레드를 사용할 때 팬인과 팬아웃의 규모 확장성을 개선할 수 있다.
- Queue를 사용하도록 기존 코드를 리팩터링하려면 상당히 많은 작업이 필요하다. 특히 다단계로 이뤄진 파이프라인이 필요하면 작업량이 더 늘어난다.
- 다른 파이썬 내장 기능이나 모듈이 제공하는 병렬 I/O를 가능하게 해주는 다른 기능과 비교하면, Queue는 프로그램이 활용할 수 있는 전체 I/O 병렬성의 정도를 제한한다는 단점이 있다.

### 개인적인 의견
- 책에서 나오는 코드 예시 가독성 끔찍하다...
	- 앞에서 나오는 Better Way 들 본인부터 지키는게..
- Producer / Consumer 구조에 가깝게 코드를 유지만 하면 코드 리팩터링에 대한 고민은 별로 없어짐
	- 책에서 제시하는 예시가 별로 와 닿지 않는 건 그냥 dataclass도 안 쓰고, 타입 힌트도 안 쓰고, 구조도 함수로 떡칠했기 때문임
	- 팬아웃 / 팬인 되는 입출구만 잘 관리해도 별 다른 문제는 없다

## Better Way 59. 동시성을 위해 스레드가 필요한 경우에는 `ThreadPoolExecutor`를 사용하라
### 요약
- `ThreadPoolExecutor`를 사용하면 한정된 리팩터링만으로 간단한 I/O 병렬성을 활성화할 수 있고, 동시성을 팬아웃해야 하는 경우에 발생하는 스레드 시작 비용을 쉽게 줄일 수 있다.
- `ThreadPoolExecutor`를 사용하면 스레드를 직접 사용할 때 발생할 수 있는 잠재적인 메모리 낭비 문제를 없애주지만, `max_workers`의 개수를 미리 지정해야 하므로 I/O 병렬성을 제한한다.

## Better Way 60. I/O를 할 때는 코루틴을 사용해 동시성을 높여라
### 요약
- async 키워드로 정의한 함수를 코루틴이라고 부른다. 코루틴을 호출하는 호출자는 await 키워드를 사용해 자신이 의존하는 코루틴의 결과를 받을 수 있다.
- 코루틴은 수만 개의 함수가 동시에 실행되는 것처럼 보이게 만드는 효과적인 방법을 제공한다.
- I/O를 병렬화하면서 스레드로 I/O를 수행할 때 발생할 수 있는 문제를 극복하기 위해 팬인과 팬아웃에 코루틴을 사용할 수 있다.
### 더 나아가서
- [[#[PEP-342](https //peps.python.org/pep-0342)]] 내용 참고.
	- 즉, `asyncio.Coroutine`은 실제로는 제너레이터로 구현되어 있다.
- 코루틴 개념에 대해서는 [코루틴(Coroutine)에 대하여 (gmarket.com)](https://dev.gmarket.com/82)글을 참고하면 도움이 될 듯 하다.
- python `asyncio` 내에서 활용하기 위해서는 [코루틴과 태스크 — Python 3.12.4 문서](https://docs.python.org/ko/3/library/asyncio-task.html#coroutines) 를 참고하는 것이 좋다.
- 아래 PDF도 읽어보는 것을 추천

![[./cheat-sheet-for-python-asyncio.pdf]]