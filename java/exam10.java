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



public class exam10 {
    public static void main(String args[]){
        tiger t1 = new tiger();
        eagle e1 = new eagle();

        t1.move();
        e1.move();
    }
}
