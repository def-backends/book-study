## 여러 이터레이터에 대해 나란히 루프를 수행하려면 zip을 사용하라
```bash
1. zip 내장 함수는 여러 이터레이터를 병렬로 순회할 수 있게 해준다.
2. zip은 각 이터레이터로부터 다음 값을 가져와 튜플로 묶어 반환한다.
3. zip은 이터레이터 중 가장 짧은 이터레이터가 끝날 때까지만 값을 생산한다.
4. 두개의 이터레이터의 길이가 다를경우 zip_longest를 사용하면 된다.
```