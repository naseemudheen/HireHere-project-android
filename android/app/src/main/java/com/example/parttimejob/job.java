package com.example.parttimejob;

public class job {
    String company_name,salary,place,job_name;
    String job_id,contact_no;
   public job(String job_id,String company_name,String salary,String place,String contact_no,String job_name) {
        this.job_id = job_id;
        this.company_name = company_name;
        this.salary = salary;
        this.place = place;
        this.contact_no = contact_no;
        this.job_name = job_name;
    }


    public job(String company_name, String job_name) {
       this.company_name = company_name;
       this.job_name = job_name;
    }
}
