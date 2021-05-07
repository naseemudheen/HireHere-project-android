package com.example.parttimejob;

import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.preference.PreferenceManager;
import android.view.View;
import android.view.Window;
import android.widget.Button;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;

public class Userhome extends AppCompatActivity {
    Button jobview,appliedjob,sendcomp,sendfeed,logout;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        requestWindowFeature(Window.FEATURE_NO_TITLE);
        setContentView(R.layout.activity_userhome);
        jobview = (Button)findViewById(R.id.button2);
        appliedjob = (Button)findViewById(R.id.button3);
        sendcomp = (Button)findViewById(R.id.button4);
        sendfeed = (Button)findViewById(R.id.button5);
        logout = (Button)findViewById(R.id.button6);

        TextView user =(TextView)findViewById(R.id.textView16);

        SharedPreferences sh = PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
        final String fullname = sh.getString("KEY_FULLNAME","");
        final String uid = sh.getString("KEY_ID","");

        user.setText("Hi ,"+ fullname);
        jobview.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent = new Intent(getApplicationContext(),viewjob.class);
                startActivity(intent);
            }
        });

        appliedjob.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent = new Intent(getApplicationContext(),Appliedjob.class);
                startActivity(intent);

            }
        });

        sendcomp.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent = new Intent(getApplicationContext(),complaintsend.class);
                intent.putExtra("uid",uid);
                startActivity(intent);

            }
        });

        sendfeed.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent = new Intent(getApplicationContext(),feedbacksend.class);
                intent.putExtra("uid",uid);
                startActivity(intent);

            }
        });

    }

        public void logOut(View v) {
            SharedPreferences sharedPreferences= PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
            SharedPreferences.Editor editor =sharedPreferences.edit();
            editor.clear();
            editor.apply();
            Intent intent = new Intent(getApplicationContext(),MainActivity.class);
            startActivity(intent);

        }

}