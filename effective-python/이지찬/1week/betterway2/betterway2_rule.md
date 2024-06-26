## PEP8 Style Guide
PEP8 파이썬 코드 스타일 가이드: https://peps.python.org/pep-0008/
### 공백
```bash
1. tab 대신 스페이스 사용하여 들여쓰기
2. 들여쓰기는 4칸 스페이스
3. 라인길이는 79개 문자 이하
4. 긴 문장 이후 다음 이어쓰기는 들여쓰기보다 4개의 스페이스를 더 넣어야 한다.
5. 함수, 클래스 사이에는 2줄 공백
6. 딕셔너리에서 키와 콜론(:)사이에는 공백을 넣지 않는다. 같은 줄에 키와 값을 같이 넣는 경우 콜론다음에 스페이스 하나씩만 넣는다.
7. 변수 대입 전후에는 스페이스를 하나씩만 넣는다.
   e.g) a = "text"
8. 타입표기를 덧붙이는 경우 변수 이름과 콜론 사이에 고백을 넣지 않도록 한다. 콜론과 타입 정보 사이에는 스페이스를 하나만 넣는다.
   e.g) x: int = 5
```

### 명명 규약
```bash
1. 함수, 변수, 어트리뷰트는 소문자와 밑줄을 사용해야 한다.
2. 보호돼야 하는 인스턴스 어트리뷰트는 이름 규칙을 밑줄로 시작한다.
   e.g) 판매처 market_account의 copy 대신 auth 정보를 초기화 시킨후 _를 붙여서 사용 하는것?
3. 한 클래스 안에서만 쓰이고 다른곳에서 쓰이면 안되는 경우(private) 인스턴스, 어트리뷰트의 경우 밑줄 두개로 시작한다.
4. 클래스는 여러 단어를 붙이되 첫글자는 대문자로 만든다.
5. 모듈 수준의 상수는 모든 글자를 대문자로 하고 단어와 단어 사이를 밑줄로 연결한다.
6. 클래스에 들어있는 인스턴스 메서드는 첫번째 인자로 반드시 self를 사용 해야한다.
7. 클래스 메서드는 첫번째 인자로 반드시 cls를 사용해야 한다.
   e.g) factory method -> factory_method_example.py
```

### 식과 문
```bash
1. 긍정적인 식을 부정하지 말고 부정을 내부에 넣어라.
   e.g) if a is not b: pass
2. 빈 컨테이너나 시퀀스를 검사할때 길이를 0과 비교하지 말아라
   e.g) betterway2_rule_expression.py   
3. 비어있지 않은 컨테이너나 시퀀스를 검사할때 길이를 0과 비교하지 말아라
4. 한줄짜리 if문, for, while, except문을 사용하지 말고 줄을 나누어 명시적으로 표현 하라.
5. 식을 한줄안에 다 쓸수 없을 경우 식을 괄호로 둘러싸고 줄바꿈을 하여 여러줄로 나눠라
6. 여러줄에 걸쳐 식을 쓸때는 \를 사용하기 보다는 괄호를 사용하라.
      
```

### 임포트(import)
pylint: https://www.pylint.org/
```bash
1. import문은 항상 파일 맨 앞에 위치 시켜라
2. 모듈을 임포트할때 절대적인 이름을 사용해야하며 모듈의 상대적인 이름을 사용하면 안된다.
   e.g) import foo (X) -> from bar import foo (O)
3. 상대적인 경로로 임포트 해야 할경우 명시적인 구문을 사용 하라
    e.g) from . import foo
4. 임포트는 다음 순서로 해야한다.
   1) 표준 라이브러리 모듈
   2) 서드파티 모듈
   3) 자신이 만든 모듈
   각 그룹안에서는 알파벳 순서로 임포트 해야한다.
```