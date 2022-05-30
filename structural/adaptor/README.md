client가 특정 interface를 필요로 하는 경우에 interface가 다른 object를 적용해야 할 때

객체를 wrapper로 감싸는 형태(decorator 패턴도 이 방식을 이용한다.) => 원래 객체의 field나 method 외에 새로운 interface를 추가해야 할 경우.

객체를 wrapper로 감싸는 경우

- 기능 추가(decorator)
- interface 단순화(facade)
- 특정 interface로 맞춰야 할 때(adaptor)

대형 타겟 인터페이스를 구현해야하는 경우.. 효율적인가?
- 복잡하긴 하나 클라이언트 코드를 수정하는 것 보단 간단하다.

adapter는 하나의 클래쓰만 감싸야 하는가
- 원칙적으로는 하나의 adaptee 클래스를 감싸나 상황에 따라 두개 이상의 adaptee를 감싸야 할 수도
- Facade 패턴과 관련

다중 어댑터(Two Way adapter)
- 여러 인터페이스를 적용해야 하는 경우

패턴 구성
- adapter는 adaptee를 composition(객체 구성)을 사용하여 감싼다.
- adaptee의 subclass도 adapter에서 사용할 수 있다.
- client는 adapter interface와 연결시킴
- 인터페이스를 기준으로 코딩하여 확장성있게 사용

class adapter
- adapter가 target과 adaptee를 다중상속한 구조

객체 adapter / class adapter
- Java는 단일상속이므로 객체 adaper만 사용할 수 있음
- class adapter가 상속으로 구현된다면 객체 adapter는 composition을 사용

