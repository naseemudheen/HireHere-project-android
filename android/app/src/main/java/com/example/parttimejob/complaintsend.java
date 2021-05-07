package com.example.parttimejob;

import android.content.Intent;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.view.Window;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;

import com.android.volley.AuthFailureError;
import com.android.volley.RequestQueue;
import com.android.volley.toolbox.StringRequest;
import com.android.volley.toolbox.Volley;

import java.util.HashMap;
import java.util.Map;

public class complaintsend extends AppCompatActivity {
    EditText e1;
    Button b1;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        requestWindowFeature(Window.FEATURE_NO_TITLE);
        setContentView(R.layout.activity_complaintsend);

        e1 = findViewById(R.id.editTextTextMultiLine3);
        b1 = (Button) findViewById(R.id.button12);





        Intent intent = getIntent();
        String uid = intent.getStringExtra("uid");
        b1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                String message =e1.getText().toString();
                if(message.isEmpty()){
                    Toast.makeText(getApplicationContext(), "Something went wrong,Check your input", Toast.LENGTH_LONG).show();
                }
                else {
                    RequestQueue requestQueue = Volley.newRequestQueue(getApplicationContext());
                    StringRequest stringRequest = new StringRequest(com.android.volley.Request.Method.POST, URLs.URL_SENDCOMP,
                            response -> {
                                Log.d("Responce from server :" , response);

                                try {
                                    if (response.equals("success")) {
                                        Toast.makeText(getApplicationContext(), "Complaint Send.", Toast.LENGTH_LONG).show();
                                    } else {
                                        Toast.makeText(getApplicationContext(), "Something went wrong", Toast.LENGTH_LONG).show();

                                    }
                                } catch (Exception e) {
                                    e.printStackTrace();
                                }


                            }, error -> Log.d("LOGIN : ", error.getMessage())) {
                        @Override
                        protected Map<String, String> getParams() throws AuthFailureError {
                            Map<String, String> params = new HashMap<>();
                            params.put("uid", uid);
                            params.put("msg", message);
                            return params;
                        }

                    };
                    requestQueue.add(stringRequest);
                }
            }
        });
    }
}