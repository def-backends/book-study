## 변수 영역과 클로저의 상호작용 방식을 이해하라
```bash
전역 변수를 사용하는것은 안티패턴이다.
클로저 함수는 리턴되는 inner 함수이다.
inner 함수는 자신이 속한 Outer 함수의 변수를 참조 할 수 있다.
클로저 함수가 자신을 감싸는 outer 함수의 변수를 변경한다는 사실을 표시할때 nonlocal을 사용해야 한다.
그리고 가금쩍 nonlocaldmf tkdydgkwl akfrh __call__ 이라는 특별한 메서드를 사용 하자

-리뷰
- https://stackoverflow.com/questions/36636/what-is-a-closure
```
