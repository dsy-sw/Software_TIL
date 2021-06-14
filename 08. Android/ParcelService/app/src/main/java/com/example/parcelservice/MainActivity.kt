package com.example.parcelservice

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.webkit.WebViewClient
import com.example.mylib.Notification
import kotlinx.android.synthetic.main.activity_main.*

const val SUB_TOPIC = "iot//#"
const val PUB_TOPIC = "iot/led"
const val SERVER_URI = "tcp://192.168.0.10:1883"

class MainActivity : AppCompatActivity() {
    companion object {
        const val CHANNEL_ID = "com.example.basic_3_toast_noti"
        const val CHANNEL_NAME = "My Channel"
        const val CHANNEL_DESCRIPTION = "Channel Test"
        const val NOTIFICATION_REQUEST = 0
        const val NOTIFICATION_ID = 100
    }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        // 웹뷰 기본 설정
        gateView.apply {
            settings.javaScriptEnabled = true
            webViewClient = WebViewClient()
        }
        gateView.loadUrl("http://www.google.com")

        btnOpen.setOnClickListener{
            val noti = Notification(this)
            noti.createNotificationChannel(CHANNEL_ID, CHANNEL_NAME, CHANNEL_DESCRIPTION)
            val pendingIntent = noti.getPendingIntent(
//                    DetectionActivity::class.java,
                this.javaClass,
                NOTIFICATION_REQUEST)
            noti.notifyBasic(CHANNEL_ID, NOTIFICATION_ID, "Alarm", "침입 발생",
                R.drawable.ic_launcher_foreground, pendingIntent)
        }
    }

    // 백 버튼 처리
    override fun onBackPressed() {
        if (gateView.canGoBack()) {
            gateView.goBack()
        } else {
            super.onBackPressed()
        }
    }
}