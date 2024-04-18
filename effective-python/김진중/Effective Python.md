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
