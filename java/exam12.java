interface ianimal {
    abstract void eat();
}

public class exam12 {
    public static void main(String args[]){
        iCat cat = new iCat();
        cat.eat();

        iTiger tiger = new iTiger();
        tiger.move();
        tiger.eat();

    }

    static class iCat implements ianimal{
        public void eat(){
            System.out.println("eat fish");
        }
    }
    static class iTiger extends animal implements ianimal{
        void move(){
            System.out.println("4val move");
        }
        public void eat(){
            System.out.println("eat mat fig");
        }
    }
}
