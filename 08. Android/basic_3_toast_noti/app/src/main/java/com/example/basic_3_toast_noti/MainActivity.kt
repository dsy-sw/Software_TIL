package com.example.basic_3_toast_noti

import android.content.Context
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.view.Gravity
import android.view.LayoutInflater
import android.widget.Toast
import com.example.mylib.Notification
import kotlinx.android.synthetic.main.activity_main.*
import kotlinx.android.synthetic.main.custom_toast.view.*

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
        setContentView(R.layout.activity_main)      //inflate 작업

        btnNoti.setOnClickListener {
            val noti = Notification(this)
            noti.createNotificationChannel(CHANNEL_ID, CHANNEL_NAME, CHANNEL_DESCRIPTION)
            val pendingIntent = noti.getPendingIntent(
//                    DetectionActivity::class.java,
                    this.javaClass,
                    NOTIFICATION_REQUEST)
            noti.notifyBasic(CHANNEL_ID, NOTIFICATION_ID, "Alarm", "침입 발생",
            R.drawable.ic_launcher_foreground, pendingIntent)
        }

        btnToast.setOnClickListener {
            Toast.makeText(application, "안녕하세요", Toast.LENGTH_SHORT).show()
        }

        btnToast2.setOnClickListener {
            showCustom("안녕하세요!")
        }
    }

    private fun showCustom(s:String){
        val layouInflater = getSystemService(
            Context.LAYOUT_INFLATER_SERVICE) as LayoutInflater
        val layout = layoutInflater.inflate(R.layout.custom_toast, null)

        // layout 안의 txtMessage
        layout.txtMessage.text = s

        val toast = Toast(applicationContext)
        toast.setGravity(Gravity.CENTER,0,0)
        toast.duration = Toast.LENGTH_SHORT
        toast.view = layout
        toast.show()
    }
}