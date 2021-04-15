package com.example.parttimejob;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.widget.Button;
import android.widget.EditText;

public class user_register extends AppCompatActivity {
    EditText e1,e2,e3,e4,e5,e6,e7,e8;
    Button b1;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_user_register);
        e1 = (EditText)findViewById(R.id.editTextTextPersonName2);
        e2 = (EditText)findViewById(R.id.editTextTextPersonName3);
        e3 = (EditText)findViewById(R.id.editTextTextEmailAddress);
        e4 = (EditText)findViewById(R.id.editTextTextPassword2);
        e5 = (EditText)findViewById(R.id.editTextTextPersonName5);
        e6 = (EditText)findViewById(R.id.editTextTextPersonName6);
        e7 = (EditText)findViewById(R.id.editTextNumber);
        e8 = (EditText)findViewById(R.id.editTextPhone);
        b1 = (Button)findViewById(R.id.button);


    }
}