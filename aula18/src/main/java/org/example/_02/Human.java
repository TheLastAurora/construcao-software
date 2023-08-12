package org.example._02;

class Human {
    private String name;
    private Address address;
    private String age;

    public String getAddress() {
        return this.address.getFullAddress();
    }
}
