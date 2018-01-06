package falcon.falconmobile;

import android.content.Intent;
import android.content.res.Configuration;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.support.v7.widget.Toolbar;
import android.util.Log;
import android.view.Menu;
import android.view.MenuItem;
import android.widget.TextView;
import android.widget.Toast;

import com.github.niqdev.mjpeg.DisplayMode;
import com.github.niqdev.mjpeg.Mjpeg;
import com.github.niqdev.mjpeg.MjpegSurfaceView;
import com.squareup.okhttp.HttpUrl;

import java.util.ArrayList;

import io.github.controlwear.virtual.joystick.android.JoystickView;

public class MainActivity extends AppCompatActivity {

    private static final int TIMEOUT = 5;
    private static String BASE_URL_CAM = "http://192.168.0.2:8080";
    private static String BASE_URL_SERVER = "http://192.168.0.3:5000";
    private static final String URL_STOP = BASE_URL_SERVER + "/stop";
    MjpegSurfaceView mjpegView;
    private TextView mTextViewAngleLeft;
    private TextView mTextViewStrengthLeft;


    private String actualDirection = Direction.STOP.value;
    private int actualSpeed = Speed.FIRST.value;

    /**
     * @param savedInstanceState
     */
    @Override
    protected void onCreate(Bundle savedInstanceState) {

        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        Toolbar toolbar = (Toolbar) findViewById(R.id.toolbar);
        setSupportActionBar(toolbar);

        mTextViewAngleLeft = (TextView) findViewById(R.id.textView_angle_left);
        mTextViewStrengthLeft = (TextView) findViewById(R.id.textView_strength_left);
        mjpegView = (MjpegSurfaceView) findViewById(R.id.mjpegViewDefault);


        JoystickView joystickLeft = (JoystickView) findViewById(R.id.joystickView_left);
        joystickLeft.setOnMoveListener(new JoystickView.OnMoveListener() {
            @Override
            public void onMove(int angle, int strength) {

                if (Direction.getDirection(angle).value != actualDirection || Speed.getSpeed(strength).value != actualSpeed) {

                    actualDirection = Direction.getDirection(angle).value;
                    actualSpeed = Speed.getSpeed(strength).value;

                    HttpUrl.Builder urlBuilder = HttpUrl.parse("http://" + BASE_URL_SERVER + "/" + actualDirection).newBuilder();
                    urlBuilder.addQueryParameter("strength", String.valueOf(actualSpeed));
                    String url_request = urlBuilder.build().toString();

                    (new Client(getApplicationContext())).execute(url_request);


                    mTextViewAngleLeft.setText(angle + "°");
                    mTextViewStrengthLeft.setText(strength + "%");
                }
                if (angle == 0) {
                    (new Client(getApplicationContext())).execute(URL_STOP);
                }
            }
        });
    }

    /**
     * @param menu
     * @return
     */
    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.menu_main, menu);
        return true;
    }

    /**
     * @param item
     * @return
     */
    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        int id = item.getItemId();

        if (id == R.id.action_config) {
            Intent intent = new Intent(MainActivity.this, ConfigureActivity.class);
            startActivityForResult(intent, 1000);
            return true;
        }

        if (id == R.id.action_photo) {

            HttpUrl.Builder urlBuilder = HttpUrl.parse("http://" + BASE_URL_SERVER + "/" + "photo").newBuilder();
            String url_request = urlBuilder.build().toString();
            (new Client(getApplicationContext())).execute(url_request);
            return true;
        }

        return super.onOptionsItemSelected(item);
    }

    /**
     * @param requestCode
     * @param resultCode
     * @param data
     */
    @Override
    public void onActivityResult(int requestCode, int resultCode, Intent data) {

        super.onActivityResult(requestCode, resultCode, data);

        if (requestCode == 1000 && resultCode == RESULT_OK) {
            try {
                ArrayList<String> config = (ArrayList<String>) data.getSerializableExtra("config");
                BASE_URL_CAM = config.get(0).toString();
                BASE_URL_SERVER = config.get(1).toString();
                //this.loadIpCam();
            } catch (Exception e) {
                Toast.makeText(MainActivity.this, "Erreur lors de la configuration", Toast.LENGTH_SHORT).show();
            }
        }
    }


    /**
     * @return
     */
    private DisplayMode calculateDisplayMode() {
        int orientation = getResources().getConfiguration().orientation;
        return orientation == Configuration.ORIENTATION_LANDSCAPE ?
                DisplayMode.FULLSCREEN : DisplayMode.BEST_FIT;
    }

    /**
     *
     */
    private void loadIpCam() {

        Mjpeg.newInstance()
                .credential("falcon", "falcon")
                //.credential(getPreference(""), getPreference(""))
                //.open("http://10.3.141.1:8080/html/cam_pic_new.php", TIMEOUT)
                .open("http://" + BASE_URL_CAM + "/html/cam_pic_new.php", TIMEOUT)
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


    /**
     *
     */
    @Override
    protected void onResume() {
        super.onResume();
    }
}