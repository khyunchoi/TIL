package hellojpa;

import javax.persistence.*;

public class MemberProduct {

    @Id @GeneratedValue
    private Long id;

    @ManyToOne
    @JoinColumn(name = "Member_ID")
    private Member member;

    @OneToMany
    @JoinColumn(name = "PRODUCT_ID")
    private Product product;
}
