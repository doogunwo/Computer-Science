interface clickLisn {
    public void print();
}


public class exam13 {
    public static void main(String args[]){
        
        clickLisn lisn = (new clickLisn (){
            public void print() {
                System.out.println("클릭리스너입니다.");
            }
        });

        lisn.print();
    }
}
