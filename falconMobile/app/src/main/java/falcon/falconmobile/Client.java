package falcon.falconmobile;

import android.content.Context;
import android.os.AsyncTask;
import android.widget.Toast;

import com.squareup.okhttp.Callback;
import com.squareup.okhttp.OkHttpClient;
import com.squareup.okhttp.Request;
import com.squareup.okhttp.Response;

import org.json.JSONException;
import org.json.JSONObject;

import java.io.IOException;

/**
 * Created by loubia on 23/12/17.
 */
class Client extends AsyncTask<String, Void, String> {

    static String responseMessage = "";
    private static Context ctx;
    private OkHttpClient internal_client;

    public Client(Context context) {
        internal_client = new OkHttpClient();
        ctx = context;
    }

    @Override
    protected void onPreExecute() {
        super.onPreExecute();
    }

    @Override
    protected String doInBackground(String... urls) {

        Request request = new Request.Builder().url(urls[0]).build();

        internal_client.newCall(request).enqueue(new Callback() {
            @Override
            public void onFailure(Request request, IOException e) {
            }

            @Override
            public void onResponse(Response response) throws IOException {
                String tmp_response_msg = response.body().string();
                try {
                    JSONObject obj = new JSONObject(tmp_response_msg);
                    if (tmp_response_msg.contains("TF : "))
                        responseMessage = obj.getString("results");
                } catch (Exception e) {
                    responseMessage = "COMMAND FAIL";
                }
            }
        });

        return responseMessage.length() != 0 ? responseMessage : "";
    }

    @Override
    protected void onPostExecute(String result) {
        // j'affiche uniquement si y a une erreur
        if (result.length() != 0) {
            Toast.makeText(ctx, result, Toast.LENGTH_LONG).show();
        }
    }
}
