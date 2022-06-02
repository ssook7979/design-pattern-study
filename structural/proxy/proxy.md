# Proxy Pattern
```plantuml
@startuml
    class Client {
        -car: ConcreteCar
    }
    node DrivingSystem {
        interface Car {
            +drive()
        }
        class ConcreteCar {
            -driver: Driver
            --
            +drive()
        }

        class Driver {
            -name
            -age
        }
        Car <|.. ConcreteCar
        Client::car -r-> ConcreteCar
        ConcreteCar -r-> Driver
    }
@enduml
```
```plantuml
@startuml
    class Client {
        -car: ProxyCar
    }
    node ProxiedDrivingSystem {
        interface Car {
            +drive()
        }
        class ConcreteCar {
            -driver: Driver
            --
            +drive()
        }
        class ProxyCar #aliceblue {
            -car: ConcreteCar
            --
            +drive()
        }
        class ConcreteCar {
            -driver: Driver
            --
            +drive()
        }
        class Driver {
            -name
            -age
        }
        note "if (driver.age >= 20) {\n\t car.drive() \n}" as note_proxy_drive

        Car <|.. ConcreteCar
        Car <|.. ProxyCar
        Client::car -r-> ProxyCar
        ProxyCar::drive <-d- note_proxy_drive
        ConcreteCar -d-> Driver
        ProxyCar::car -> ConcreteCar
    }
@enduml
```

## Proxy vs. Decorator
- Proxy는 원래 class와 같은 interface; Decorator는 feature added interface
- Decorator는 원래 class의 instance를 member변수로 가지고 있다.(injected when constructor is called)
- Proxy는 원래의 class를 refrence하고 있을 수도 있고 아닐 수도 있음(다른 방식으로 call을 전달할 수도 있다.)