package falcon.falconmobile;

import java.io.Serializable;

/**
 * Created by loubia on 25/12/17.
 */

public enum Direction implements Serializable {
    STOP("stop"),
    UP("up"),
    DOWN("down"),
    RIGHT("right"),
    LEFT("left"),
    UP_RIGHT("up_right"),
    DOWN_RIGHT("down_right"),
    UP_LEFT("up_left"),
    DOWN_LEFT("down_left");


    public final String value;

    private Direction(String value) {
        this.value = value;
    }

    public static Direction getDirection(float degree) {

        if (degree >= 0) {
            if (degree <= 30 || degree >= 330) return Direction.RIGHT;
            if (degree > 30 && degree < 60) return Direction.UP_RIGHT;
            if (degree >= 60 && degree <= 120) return Direction.UP;
            if (degree > 120 && degree < 150) return Direction.UP_LEFT;
            if (degree >= 150 && degree <= 210) return Direction.LEFT;
            if (degree > 210 && degree < 240) return Direction.DOWN_LEFT;
            if (degree >= 240 && degree <= 300) return Direction.DOWN;
            if (degree > 300 && degree < 330) return Direction.DOWN_RIGHT;
        }
        return Direction.STOP;
    }
}

