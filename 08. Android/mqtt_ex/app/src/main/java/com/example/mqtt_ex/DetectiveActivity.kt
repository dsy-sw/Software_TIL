package com.example.mqtt_ex

import android.content.Intent
import android.os.Bundle
import android.view.inputmethod.EditorInfo
import android.webkit.WebViewClient
import androidx.appcompat.app.AppCompatActivity
import kotlinx.android.synthetic.main.activity_camera.*


class DetectiveActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_camera)

        // 웹뷰 기본 설정
        webView.apply {
            settings.javaScriptEnabled = true
            webViewClient = WebViewClient()
        }
        webView.loadUrl("http://192.168.0.8:8000/mjpeg/stream")    // picamera ip address
//        webView.loadUrl("http://www.google.com")    // picamera ip address
//        urlEditText.setOnEditorActionListener { _, actionId, _ ->
//            if (actionId == EditorInfo.IME_ACTION_SEARCH) {
//                var url = urlEditText.text.toString()
//                if (!url.startsWith("http://") && !url.startsWith("https://")) {
//                    url = "http://$url"
//                }
//                webView.loadUrl(url)
//                true
//            } else {
//                false
//            }
//        }
        // 백 버튼 처리
    }
        override fun onBackPressed() {
            if (webView.canGoBack()) {
                webView.goBack()
            } else {
                super.onBackPressed()
            }
        }
}