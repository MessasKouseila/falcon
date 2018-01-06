package falcon.falconmobile;

import android.content.Intent;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import java.util.ArrayList;


public class ConfigureActivity extends AppCompatActivity {

    private EditText configCam;
    private EditText configServer;
    private Button btn;

    @Override
    protected void onCreate(Bundle savedInstanceState) {

        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_configure);

        configCam = (EditText) findViewById(R.id.config_cam);
        configServer = (EditText) findViewById(R.id.config_server);
        btn = (Button) findViewById(R.id.btn_validate);

        btn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if (!configCam.getText().toString().isEmpty() && !configServer.getText().toString().isEmpty()) {
                    Intent intent = new Intent();
                    final ArrayList<String> config = new ArrayList<String>();
                    config.add(configCam.getText().toString());
                    config.add(configServer.getText().toString());
                    intent.putExtra("config", config);

                    setResult(RESULT_OK, intent);
                    finish();
                } else {
                    Toast.makeText(getApplicationContext(), "Veuillez remplir le formulaire", Toast.LENGTH_LONG).show();
                }
            }
        });
    }
}
