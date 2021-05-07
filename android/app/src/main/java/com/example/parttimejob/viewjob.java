package com.example.parttimejob;

import android.content.Intent;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.view.Window;
import android.widget.AdapterView;
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

public class viewjob extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        requestWindowFeature(Window.FEATURE_NO_TITLE);
        setContentView(R.layout.activity_viewjob);


        ArrayList<job> list = new ArrayList<job>();
        ListView listView = (ListView)findViewById(R.id.listView) ;
        

        OkHttpClient client = new OkHttpClient();
        final Request request = new Request.Builder()
                .url(URLs.URL_VIEWJOB)
                .build();
        client.newCall(request).enqueue(new Callback() {
            @Override
            public void onFailure(Call call, IOException e) {
                Log.d("VIEW JOB",e.getMessage());
            }

            @Override
            public void onResponse(Call call, Response response) throws IOException {
                String responseText = response.body().string();
                try {
                    JSONArray array = new JSONArray(responseText);
                    for (int i = 0; i < array.length(); i++) {
                        JSONObject jsonObject = array.optJSONObject(i);
                        String job_id = jsonObject.optString("id");
                        String company_name = jsonObject.optString("company");
                        String salary = jsonObject.optString("salary");
                        String place = jsonObject.optString("place");
                        String contact_no = jsonObject.optString("contact");
                        String job_name = jsonObject.optString("job");
                        list.add(new job(job_id, company_name, salary, place, contact_no, job_name));


                    }
                }
                    catch (JSONException e) {
                    e.printStackTrace();
                }


            }
        });


        NewAdapter adapter =new NewAdapter(this,list);

        listView.setAdapter(adapter);
        listView.setOnItemClickListener(new AdapterView.OnItemClickListener() {

            @Override
            public void onItemClick(AdapterView<?> parent, View view, int position, long id) {
                Intent intent=new Intent(getApplicationContext(),viewjobdetails.class);

                intent.putExtra("company_name", list.get(position).company_name);
                intent.putExtra("salary", list.get(position).salary);
                intent.putExtra("place",list.get(position). place);
                intent.putExtra("contact_no", list.get(position).contact_no);
                intent.putExtra("job_name", list.get(position).job_name);
                intent.putExtra("job_id", list.get(position).job_id);
                startActivity(intent);
            }
        });


    }
}
