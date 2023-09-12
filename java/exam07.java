

public class exam07 {
    public static void main(String args[]){
        car myCar1 = new car("red",0);
        car myCar2 = new car("blue",0);
        car myCar3 = new car("green",0);
       

        myCar1.upSpeed(50);
        System.out.println(myCar1.getColor()+ myCar1.getSpeed());
        myCar2.downSpeed(10);
        myCar3.upSpeed(10);

    }
}