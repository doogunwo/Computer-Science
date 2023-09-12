public class Automobile extends car{
    int seatnum;

    int getseatnum(){
        return seatnum;
    }
    void upSpeed(int value){
        if(speed+ value>=300){
            speed = 300;
        }
        else{
            speed = speed + (int)value;
        }
    }
}
