package com.example.basic_1_edittext

import android.content.Intent
import android.graphics.Color
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.text.Editable
import android.view.View
import android.widget.EditText
import android.widget.TextView
import androidx.core.widget.addTextChangedListener
import kotlinx.android.synthetic.main.activity_main.*
import android.text.TextWatcher

// 인터페이스의 추상 메서드가 1개인 경우
class MyClickListener : View.OnClickListener{
    override fun onClick(v: View?) {
    }
}

fun onClick(v: View?){
//    val name
//    (v as TextView).text = name
}

class MainActivity : AppCompatActivity() {
    companion object{       // 어떤 호출인지 상수로 정의
        val REQUEST = 0
        val ID = "ID"
        val PASSWD = "PASSWD"
        val RESULT = "RESULT"
    }
    var name = "Test"
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        val myClickListener = MyClickListener()
//        edtName.setOnClickListener(myClickListener)
//        edtName.setOnClickListener(::onClick)

        edtName.setOnClickListener {
            (it as TextView).text = name
        }

        edtName.setOnFocusChangeListener() { v, hasFocus ->
            val edt = v as EditText
            val color = if (hasFocus){
                Color.TRANSPARENT       // 투명처리
            } else {
                Color.LTGRAY
            }
            edt.setBackgroundColor(color)
        }
        edtPassWD.addTextChangedListener(object:TextWatcher {
            override fun afterTextChanged(s: Editable?) {
            }

            override fun beforeTextChanged(s: CharSequence?, start: Int, count: Int, after: Int) {
            }

            override fun onTextChanged(s: CharSequence?, start: Int, before: Int, count: Int) {
                txtMessage.text = s
            }
        })

        btnLogin.setOnClickListener {
            val i = Intent(this, ResultActivity::class.java)
            i.putExtra(ID, edtName.text.toString())     // edtID -> edtName으로 변경
            i.putExtra(PASSWD, edtPassWD.text.toString())

            startActivityForResult(i, REQUEST)
        }
    }       // end of onCreate()

    override fun onActivityResult(requestCode: Int, resultCode: Int, data: Intent?) {
        if(requestCode != REQUEST) return

        data?.getStringExtra(RESULT).let{
            txtMessage.text = it
        }
        super.onActivityResult(requestCode, resultCode, data)
    }
}