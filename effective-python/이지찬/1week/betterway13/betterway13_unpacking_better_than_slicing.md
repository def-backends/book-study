## 슬라이싱보다는 나머지를 모두 잡아내는 언패킹을 사용하라
```bash
1. 언패킹 대입에 별표식을 사용하면 패턴에 대입되지 않은 부분을 모두 잡아 낼 수있다.
2. 별표식은 언패킹 패턴의 어느 위치에든 놓을수 있다.
3. 별표 식에 대입된 결과는 항상 리스트로 반환 된다.
4. 별표 식이 받은 값은 0개 또는 그 이상이 될 수 있다.
5. 리스트를 여러 조각으로 나눌 경우 슬라이싱과 인덱싱을 하기 보다는 언패킹을 사용 하자.
```