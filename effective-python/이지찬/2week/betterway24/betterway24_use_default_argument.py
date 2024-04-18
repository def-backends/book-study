from time import sleep
from datetime import datetime

def log(message, when=datetime.now()):
    """메시지와 타임스탬프를 로그에 남긴다

    Args:
        message: 출력할 메시지
        when: 메시지가 발생한 시각(datetime)
            디폴트 값은 현재 시간
    """
    print(f"{when}: {message}")


log('안녕!')
sleep(0.1)
log('다시 안녕!')

import json
def decode(data, default={}):
    try:
        return json.loads(data)
    except ValueError:
        return default


foo = decode('잘못된 데이터')
foo['stuff'] = 5
bar = decode('또 잘못된 데이터')
bar['meep'] = 1
print('Foo:', foo)
print('Bar:', bar)