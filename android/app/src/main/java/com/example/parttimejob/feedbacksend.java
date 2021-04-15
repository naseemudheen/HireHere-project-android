package com.example.parttimejob;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.widget.Button;
import android.widget.EditText;

public class feedbacksend extends AppCompatActivity {
    EditText e1;
    Button b1;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_feedbacksend);
        e1 = (EditText)findViewById(R.id.editTextTextMultiLine3);
        b1 = (Button)findViewById(R.id.button12);
    }
}