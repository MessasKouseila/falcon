package falcon.falconmobile;

import java.io.Serializable;

/**
 * Created by loubia on 02/01/18.
 */

public enum Speed implements Serializable {

    FIRST(25),
    SECOND(50),
    THIRD(75),
    FORTH(100);

    public final int value;

    private Speed(int value) {
        this.value = value;
    }

    public static Speed getSpeed(int strenght) {

        if (strenght < 25) return Speed.FIRST;
        if (strenght >= 25 && strenght < 50) return Speed.SECOND;
        if (strenght >= 50 && strenght < 75) return Speed.THIRD;
        return Speed.FORTH;
    }
}
