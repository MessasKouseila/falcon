package falcon.falconmobile;

import android.content.Context;
import android.os.AsyncTask;
import android.widget.Toast;

import com.squareup.okhttp.HttpUrl;
import com.squareup.okhttp.OkHttpClient;
import com.squareup.okhttp.Request;
import com.squareup.okhttp.Response;

import java.io.IOException;

/**
 * Created by loubia on 23/12/17.
 */
class Client extends AsyncTask<String, Void, String> {

    private OkHttpClient internal_client;
    private Context ctx;

    public Client(Context context) {
        internal_client = new OkHttpClient();
        this.ctx = context;
    }

    @Override
    protected void onPreExecute() {
        super.onPreExecute();
    }

    @Override
    protected String doInBackground(String... urls) {

        try {
            Request request = new Request.Builder().url(urls[0]).build();
            Response response = null;
            response = internal_client.newCall(request).execute();

            if (response.isSuccessful()) {
                return response.body().string();
            }

        } catch (IOException e) {
            e.printStackTrace();
        }
        return "command failed";
    }

    @Override
    protected void onPostExecute(String result) {
        Toast.makeText(this.ctx, "result", Toast.LENGTH_SHORT).show();
    }
}
