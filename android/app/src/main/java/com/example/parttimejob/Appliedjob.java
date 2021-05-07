package com.example.parttimejob;

import android.os.Bundle;
import android.util.Log;
import android.view.Window;
import android.widget.ListView;

import androidx.appcompat.app.AppCompatActivity;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import java.io.IOException;
import java.util.ArrayList;

import okhttp3.Call;
import okhttp3.Callback;
import okhttp3.OkHttpClient;
import okhttp3.Request;
import okhttp3.Response;

public class Appliedjob extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        requestWindowFeature(Window.FEATURE_NO_TITLE);
        setContentView(R.layout.activity_appliedjob);

        ArrayList<job> appliedList = new ArrayList<job>();
        ListView listView = (ListView)findViewById(R.id.listView) ;

        OkHttpClient client = new OkHttpClient();
        final Request request = new Request.Builder()
                .url(URLs.URL_VIEWJOB)
                .build();
        client.newCall(request).enqueue(new Callback() {
            @Override
            public void onFailure(Call call, IOException e) {
                Log.d("VIEW APPLIED JOB",e.getMessage());
            }

            @Override
            public void onResponse(Call call, Response response) throws IOException {
                String responseText = response.body().string();
                        try {

                            JSONArray array = new JSONArray(responseText);
                            for (int i = 0; i < array.length(); i++) {
                                JSONObject jsonObject = array.optJSONObject(i);
                                String company_name = jsonObject.optString("company");
                                String job_name = jsonObject.optString("job");

                                appliedList.add(new job(company_name,job_name));


                            }
                        }
                        catch (JSONException e) {
                            e.printStackTrace();
                        }


            }
        });


        AppliedJobsAdapter adapter =new AppliedJobsAdapter(this,appliedList);
        listView.setAdapter(adapter);
    }
}