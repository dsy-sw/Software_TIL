package com.example.mywebbrowser

import android.content.Context
import android.content.Intent
import android.net.Uri
import android.os.Bundle
import android.view.ContextMenu
import com.google.android.material.floatingactionbutton.FloatingActionButton
import com.google.android.material.snackbar.Snackbar
import androidx.appcompat.app.AppCompatActivity
import android.view.Menu
import android.view.MenuItem
import android.view.View
import android.view.inputmethod.EditorInfo
import android.webkit.WebViewClient
import kotlinx.android.synthetic.main.content_main.*
import org.jetbrains.anko.browse
import org.jetbrains.anko.email
import org.jetbrains.anko.sendSMS
import org.jetbrains.anko.share

class MainActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        // 컨텍스트 메뉴 등록
        registerForContextMenu(webview)
        setSupportActionBar(findViewById(R.id.toolbar))     // 메뉴 처리 툴바

        // 웹뷰 기본 설정
        webview.apply {
            settings.javaScriptEnabled = true
            webViewClient = WebViewClient()
        }
        webview.loadUrl("http://www.google.com")

        urlEditText.setOnEditorActionListener { _, actionId, _ ->
            if (actionId == EditorInfo.IME_ACTION_SEARCH) {
                var url = urlEditText.text.toString()
                if (!url.startsWith("http://") && !url.startsWith("https://")) {
                    url = "http://$url"
                }
                webview.loadUrl(url)
                true
            } else {
                false
            }
        }
    }

    // 백 버튼 처리
    override fun onBackPressed() {
        if (webview.canGoBack()) {
            webview.goBack()
        } else {
            super.onBackPressed()
        }
    }

    override fun onContextItemSelected(item: MenuItem): Boolean {
        return when (item?.itemId) {
            R.id.action_share -> {
                webview.url?.let { share(it) }
                true
            }
            R.id.action_browser -> {
                webview.url?.let {
                    browse(it)
                }
                true
            }
            else -> super.onContextItemSelected(item)
        }
    }
    override fun onCreateOptionsMenu(menu: Menu): Boolean {
        // Inflate the menu; this adds items to the action bar if it is present.
        menuInflater.inflate(R.menu.menu_main, menu)
        return true
    }

    override fun onOptionsItemSelected(item: MenuItem): Boolean {
        // Handle action bar item clicks here. The action bar will
        // automatically handle clicks on the Home/Up button, so long
        // as you specify a parent activity in AndroidManifest.xml.
        return when (item.itemId) {
            R.id.action_google, R.id.action_home -> {
                webview.loadUrl("http://www.google.com")
                return true
            }
            R.id.action_naver -> {
                webview.loadUrl("http://www.naver.com")
                return true
            }
            R.id.action_daum -> {
                webview.loadUrl("http://www.daum.com")
                return true
            }
            R.id.action_call -> {
                val intent = Intent(Intent.ACTION_DIAL)
                intent.data = Uri.parse("tel:010-0000-0000")
                if (intent.resolveActivity(packageManager) != null) {
                    startActivity(intent)
                }
                return true
            }
            R.id.action_send_text -> {
                webview.url?.let {
                    sendSMS("010-0000-0000", it)
                }
                return true
            }
            R.id.action_email -> {
                webview.url?.let {
                    email(
                        "test@example.com",
                        "좋은 사이트",
                        webview.url!!       // it으로 대체 가능
                    )      // !! : null이 아님을 개발자가 보장하니 그냥 처리
                }
                return true
            }
            else -> super.onOptionsItemSelected(item)
        }
    }

    override fun onCreateContextMenu(
        menu: ContextMenu?,
        v: View?,
        menuInfo: ContextMenu.ContextMenuInfo?
    ) {
        super.onCreateContextMenu(menu, v, menuInfo)
        menuInflater.inflate(R.menu.menu_context, menu)
    }
}