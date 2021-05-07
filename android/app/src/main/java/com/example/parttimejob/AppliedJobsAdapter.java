package com.example.parttimejob;

import android.content.Context;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ArrayAdapter;
import android.widget.ImageButton;
import android.widget.TextView;

import androidx.annotation.NonNull;

import java.util.ArrayList;


class AppliedJobsAdapter extends ArrayAdapter<job> {


    public AppliedJobsAdapter(@NonNull Context context, @NonNull ArrayList<job> objects) {
        super(context, 0, objects);
    }

    @Override
    public View getView(int position, View convertView, ViewGroup parent){
        job jb=getItem(position);

        if(convertView == null) {
            convertView = LayoutInflater.from(getContext()).inflate(R.layout.applied_job_list, parent, false);
        }
        TextView company_name = (TextView)convertView.findViewById(R.id.textView2);
        TextView job_name = (TextView)convertView.findViewById(R.id.textView15);
        ImageButton delete =(ImageButton)convertView.findViewById(R.id.imageButton);
        company_name.setText(jb.company_name);
        job_name.setText(jb.job_name);
        return convertView;
    }
}

