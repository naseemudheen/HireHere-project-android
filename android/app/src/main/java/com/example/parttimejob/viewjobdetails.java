package com.example.parttimejob;

import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.preference.PreferenceManager;
import android.view.View;
import android.view.Window;
import android.widget.Button;
import android.widget.TextView;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;

import com.android.volley.AuthFailureError;
import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.StringRequest;
import com.android.volley.toolbox.Volley;

import java.util.HashMap;
import java.util.Map;

public class viewjobdetails extends AppCompatActivity {
    Button b1;
    String job_id;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        requestWindowFeature(Window.FEATURE_NO_TITLE);
        setContentView(R.layout.activity_viewjobdetails);
        b1 = (Button)findViewById(R.id.button8);

        TextView companyview = (TextView)findViewById(R.id.textView6);
        TextView jobview = (TextView)findViewById(R.id.textView7);
        TextView salaryview = (TextView)findViewById(R.id.textView9);
        TextView placeview = (TextView)findViewById(R.id.textView11);
        TextView contactview = (TextView)findViewById(R.id.textView13);


        Intent intent =getIntent();

        companyview.setText(intent.getStringExtra("company_name"));
        jobview.setText(intent.getStringExtra("job_name"));
        salaryview.setText(intent.getStringExtra("salary"));
        placeview.setText(intent.getStringExtra("place"));
        contactview.setText(intent.getStringExtra("contact_no"));

        job_id= intent.getStringExtra("job_id");






    }
    public void jobApply(View v){
        RequestQueue requestQueue = Volley.newRequestQueue(getApplicationContext());
        SharedPreferences sh = PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
        String uid = sh.getString("KEY_ID","");
            StringRequest stringRequest = new StringRequest(Request.Method.POST, URLs.URL_JOBAPPPLY,
                    new Response.Listener<String>() {
                        @Override
                        public void onResponse(String response) {
                            if(response.toString().equals("success")){
                                Toast.makeText(getApplicationContext(), "Job Applied successfully.", Toast.LENGTH_LONG).show();
                            }
                            else{
                                Toast.makeText(getApplicationContext(), "You have Already applied for this job.", Toast.LENGTH_LONG).show();
                            }
                        }
                    }, new Response.ErrorListener() {
                @Override
                public void onErrorResponse(VolleyError error) {
                }
            })
            {
                @Override
                protected Map<String,String> getParams() throws AuthFailureError{
                    Map<String,String> params = new HashMap<>();
                    params.put("user_id",uid);
                    params.put("job_id",job_id);
                    return params;
                }
            };
            requestQueue.add(stringRequest);


    }
}