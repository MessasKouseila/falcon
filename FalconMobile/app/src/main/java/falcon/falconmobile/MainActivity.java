package falcon.falconmobile;

import android.content.res.Configuration;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.util.Log;
import android.widget.TextView;
import android.widget.Toast;

import com.github.niqdev.mjpeg.DisplayMode;
import com.github.niqdev.mjpeg.Mjpeg;
import com.github.niqdev.mjpeg.MjpegSurfaceView;
import com.squareup.okhttp.HttpUrl;

import io.github.controlwear.virtual.joystick.android.JoystickView;


public class MainActivity extends AppCompatActivity {

    private static final int TIMEOUT = 5;
    private static final String BASE_URL = "http://192.168.0.16:5000/";
    private static final String URL_STOP = BASE_URL + "stop";

    MjpegSurfaceView mjpegView;
    private TextView mTextViewAngleLeft;
    private TextView mTextViewStrengthLeft;


    private String actualDirection = "stop";

    @Override
    protected void onCreate(Bundle savedInstanceState) {

        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        mTextViewAngleLeft = (TextView) findViewById(R.id.textView_angle_left);
        mTextViewStrengthLeft = (TextView) findViewById(R.id.textView_strength_left);
        mjpegView = (MjpegSurfaceView) findViewById(R.id.mjpegViewDefault);


        JoystickView joystickLeft = (JoystickView) findViewById(R.id.joystickView_left);
        joystickLeft.setOnMoveListener(new JoystickView.OnMoveListener() {
            @Override
            public void onMove(int angle, int strength) {

                if (Direction.getDirection(angle).value != actualDirection) {

                    actualDirection = Direction.getDirection(angle).value;

                    HttpUrl.Builder urlBuilder = HttpUrl.parse(BASE_URL + actualDirection).newBuilder();
                    urlBuilder.addQueryParameter("strength", String.valueOf(strength));
                    String url_request = urlBuilder.build().toString();

                    (new Client(getApplicationContext())).execute(url_request);


                    mTextViewAngleLeft.setText(angle + "°");
                    mTextViewStrengthLeft.setText(strength + "%");

                    if (angle == 0) {
                        (new Client(getApplicationContext())).execute(URL_STOP);
                    }
                }

            }
        });
    }

    private DisplayMode calculateDisplayMode() {
        int orientation = getResources().getConfiguration().orientation;
        return orientation == Configuration.ORIENTATION_LANDSCAPE ?
                DisplayMode.FULLSCREEN : DisplayMode.BEST_FIT;
    }

    private void loadIpCam() {

        Mjpeg.newInstance()
                .credential("falcon", "falcon")
                //.credential(getPreference(""), getPreference(""))
                //.open("http://10.3.141.1:8080/html/cam_pic_new.php", TIMEOUT)
                .open("http://10.188.54.168:8080/html/cam_pic_new.php", TIMEOUT)
                .subscribe(
                        inputStream -> {
                            mjpegView.setSource(inputStream);
                            mjpegView.setDisplayMode(calculateDisplayMode());
                            mjpegView.showFps(true);
                        },
                        throwable -> {
                            Log.e(getClass().getSimpleName(), "mjpeg error", throwable);
                            Toast.makeText(this, "Error", Toast.LENGTH_LONG).show();
                        });
    }


    /*
        updateWeather = new Update();
        updateWeather.execute(MainActivity.listCity);
    */
    @Override
    protected void onResume() {
        super.onResume();
        //loadIpCam();
    }
}