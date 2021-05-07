package com.example.parttimejob;

import android.os.Bundle;
import android.view.View;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;

import org.json.JSONException;
import org.json.JSONObject;

import java.io.IOException;

import okhttp3.Call;
import okhttp3.Callback;
import okhttp3.MediaType;
import okhttp3.OkHttpClient;
import okhttp3.Request;
import okhttp3.RequestBody;
import okhttp3.Response;

public class user_register extends AppCompatActivity {


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        this.getSupportActionBar().hide();
        setContentView(R.layout.activity_user_register);

      }

        public void register(View v){

           EditText first_nameview = (EditText)findViewById(R.id.editTextTextPersonName2);
           EditText last_nameview = (EditText)findViewById(R.id.editTextTextPersonName3);
           EditText emailview = (EditText)findViewById(R.id.editTextTextEmailAddress);
           EditText passview = (EditText)findViewById(R.id.editTextTextPassword2);
           EditText placeview = (EditText)findViewById(R.id.editTextTextPersonName5);
           EditText postview = (EditText)findViewById(R.id.editTextTextPersonName6);
           EditText pinview = (EditText)findViewById(R.id.editTextNumber);
           EditText phoneview = (EditText)findViewById(R.id.editTextPhone);
           EditText usernameview = (EditText)findViewById(R.id.editTextTextPersonName7);


            String  firstname = first_nameview.getText().toString().trim();
            String  lastname = last_nameview.getText().toString().trim();
            String  email = emailview.getText().toString().trim();
            String  pass = passview.getText().toString().trim();
            String  place = placeview.getText().toString().trim();
            String  post = postview.getText().toString().trim();
            String  pin = pinview.getText().toString().trim();
            String  phone = phoneview.getText().toString().trim();
            String  username = usernameview.getText().toString().trim();

            if(firstname.length() == 0 || lastname.length() == 0 || username.length() == 0 || pass.length() == 0)
            {
                Toast.makeText(getApplicationContext(),"Something Went wrong,Please check your inputs",Toast.LENGTH_LONG).show();

            }
            else
            {
                JSONObject registrationform = new JSONObject();
                try{
                    registrationform.put("firstname",firstname);
                    registrationform.put("lastname",lastname);
                    registrationform.put("username",username);
                    registrationform.put("email",email);
                    registrationform.put("password",pass);
                    registrationform.put("place",place);
                    registrationform.put("pin",pin);
                    registrationform.put("post",post);
                    registrationform.put("phone",phone);

                } catch (JSONException e) {
                    e.printStackTrace();
                }
                RequestBody body = RequestBody.create(MediaType.parse("application/json;charset=utf-8"),registrationform.toString());
                postRequest(URLs.URL_REGISTER,body);
                
            }
    }

    private void postRequest(String postUrl, RequestBody body) {
        OkHttpClient client = new OkHttpClient();
        final Request request = new Request.Builder()
                .url(postUrl)
                .post(body)
                .header("Accept", "application/json")
                .header("Content-Type", "application/json")
                .build();
        client.newCall(request).enqueue(new Callback() {
            @Override
            public void onFailure(Call call, IOException e) {
                runOnUiThread(new Runnable() {
                    @Override
                    public void run() {
                        TextView responseText = (TextView)findViewById(R.id.textViewResponse);
                        responseText.setText("Failed to connect to server,try again later!");
                    }
                });

            }

            @Override
            public void onResponse(Call call, Response response) throws IOException {
                final TextView responseText = (TextView)findViewById(R.id.textViewResponse);
                try{
                    final String responseString = response.body().string().trim();
                    runOnUiThread(new Runnable() {
                        @Override
                        public void run() {
                            if(responseString.equals("success")){
                                Toast.makeText(getApplicationContext(),"Registration Completed Succesfully",Toast.LENGTH_LONG);
                            }
                            else if(responseString.equals("username")){
                                responseText.setText("Username already exists.Please try another username.");
                            }
                            else
                                responseText.setText("Something went Wrong!");
                        }
                    });
                } catch (IOException e) {
                    e.printStackTrace();
                }

            }
        });
    }


}