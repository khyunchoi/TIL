## 스프링 시큐리티란?

스프링 시큐리티는 스프링 기반의 애플리케이션의 **보안**(인증과 권한, 인가 등)을 담당하는 스프링 하위 프레임워크이다. 주로 서블릿 필터와 이들로 구성된 **필터체인**으로의 위임모델을 사용한다. 그리고 보안과 관련해서 체계적으로 많은 옵션을 제공해주기 때문에 개발자 입장에서는 일일이 보안관련 로직을 작성하지 않아도 된다는 장점이 있다.

## 보안 용어

- 접근 주체(Principal) : 보호된 리소스에 접근하는 대상
- 인증(Authentication) : 보호된 리소스에 접근한 대상에 대해 이 유저가 누구인지, 애플리케이션의 작업을 수행해도 되는 주체인지 확인하는 과정(ex. Form 기반 Login)
- 인가(Authorize) : 해당 리소스에 대해 접근 가능한 권한을 가지고 있는지 확인하는 과정(After Authentication, 인증 이후)
- 권한 : 어떠한 리소스에 대한 접근 제한, 모든 리소스는 접근 제어 권한이 걸려있다. 즉, 인가 과정에서 해당 리소스에 대한 제한된 최소한의 권한을 가졌는지 확인.