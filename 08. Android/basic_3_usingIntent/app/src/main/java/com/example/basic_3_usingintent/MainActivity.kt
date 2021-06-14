package com.example.basic_3_usingintent

import android.content.Intent
import android.net.Uri
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import kotlinx.android.synthetic.main.activity_main.*

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        setUpUI()
    }

    private fun setUpUI() {
        // 암묵적 인텐트 호출 <-> 명시적 인텐트 호출
        btnSMS.setOnClickListener {
            // SMS 보내기
            val uri = Uri.parse("smsto:"+"01086863058")
            val intent = Intent(Intent.ACTION_SENDTO, uri)
            intent.putExtra("sms_body", "여기 문자!")
            startActivity(intent)
        }
        btnInternet.setOnClickListener {
//            val intent = Intent(Intent.ACTION_DIAL, Uri.parse("tel:" + 114))
            val uri = Uri.parse("http://naver.com/")
            val intent = Intent(Intent.ACTION_VIEW, uri)
            startActivity(intent)
        }

        btnMap.setOnClickListener {
            val uri = Uri.parse("geo: 37.488950397916376, 126.88631694704904")
            val intent = Intent(Intent.ACTION_VIEW, uri)
            startActivity(intent)
        }
        btnMarket.setOnClickListener {
            val uri = Uri.parse("\"market://details?id=com.psw.moringcall")
            val intent = Intent(Intent.ACTION_VIEW, uri)
            startActivity(intent)
        }
    }
}