public class car{
    String color;
    int speed = 0;
    static int carCount =0;
    final static int maxspeed = 200;
    final static int minspeed = 200;

    static int cueentcarcount(){
        return carCount;
    }


    car(String color, int speed){
        this.color = color;
        this.speed = speed;
        carCount = carCount +1;
    }

    car(int speed) {
        this.speed = speed;
    }

    car(){

    }
    
    int getSpeed(){
        return speed;
    }

    void upSpeed(int value){
        if(speed + value >=200){
            speed =200;
        }
        else{
            speed = speed + value;
        }
    }

    void downSpeed(int value){
        if(speed - value<=0){
            speed = 0;
        }
        else{
            speed = speed+ value;
        }

    }

    String getColor(){
        return color;
    }
}