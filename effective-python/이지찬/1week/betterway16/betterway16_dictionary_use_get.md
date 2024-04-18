## in을 사용하고 딕셔너리 키가 없을때 KeyError를 처리하기보다는 get을 사용하라
```bash
1. 딕셔너리의 키가 존재하는지 확인할 때 in을 사용하면 KeyError를 방지할 수 있다.
2. get 메서드를 사용하면 키가 존재하지 않을 때 기본값을 반환할 수 있다.
3. setdefault 메서드를 사용하면 키가 존재하지 않을 때 기본값을 설정할 수 있다.
4. 카운터와 같은 딕셔너리를 사용할 때 get을 사용하면 코드가 간결해진다.
```
## 실제 사용 예제
```python
# new_market AK몰 모델 클래스중 고시구분 ID를 반환하는 메서드
@property
def notice_class_id(self):
    """
    고시 구분 ID(request > reqInfo > notice_class_id)
    """

    mid_category = self.market_product_data.category_full_kor_name.split("/")[1]

    notice_code_mapping = {
        "의류": "1",
        "슈즈": "2",
        "가방": "3",
        "액세서리": "4",
    }
    
    #before 
    return notice_code_mapping[mid_category]
    # after
    return notice_code_mapping.get("mid_category")


# 다른 클래스 메서드에서 notice_class_id를 사용시
# before
notice_class_id = self.notice_class_id

# after
if not (notice_class_id := self.notice_class_id):
    raise ValueError("매핑된 고시정보 ID(notice_class_id)값이 존재하지 않습니다.")
```
## 느낀점
```bash
get을 사용하면 KeyError을 방지 할 수 있다.
왈러스 연산자를 통해 변수에 값을 할당 및 존재 여부를 동시에 할 수 있다.
keyerror을 발생시키는 것보단 ValueError를 발생시키는 것이 더 좋은 방법같다..
왜냐하면, key에러는 예측하지 못한 에러이고 ValueError는 명시적으로 작성하고 발생시키는 에러이기 때문이다.
```