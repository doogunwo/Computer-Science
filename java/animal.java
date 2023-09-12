abstract class animal {
    String name;
    abstract void move();
}

class tiger extends animal {
    int age;
    void move(){
        System.out.println("move move move");
    }
}

class eagle extends animal{
    String home;
    void move(){
        System.out.println("move move move move fly");
    }
}

