package com.example.mqtt_ex

import android.content.Intent
import android.content.res.ColorStateList
import android.graphics.Color
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.util.Log
import android.widget.SeekBar
import com.example.mylib.Notification
import com.example.mylib.net.Mqtt
import com.example.mylib.openapi.piapi.PiApi
import kotlinx.android.synthetic.main.activity_main.*
import org.eclipse.paho.client.mqttv3.MqttMessage
import java.lang.Exception

const val SUB_TOPIC = "iot/monitor/#"
const val PUB_TOPIC = "iot/led"
const val SERVER_URI = "tcp://192.168.0.10:1883"

class MainActivity : AppCompatActivity() {
    companion object{
        const val CHANNEL_ID = "com.example.mqtt_ex"
        const val CHANNE_NAME = "Pi Camera"
        const val CHANNEL_DESCRIPTION = "Camera를 실행하려면 터치해주세요"
        const val NOTIFICATION_REQUEST = 0
        const val NOTIFICATION_ID = 100
    }
    val TAG = "MqttActivity"

    lateinit var mqttClient: Mqtt

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        mqttClient = Mqtt(this, SERVER_URI)
        try{
//            mqttClient.setCallback{ topic, message ->  }
            mqttClient.setCallback(::onReceived)
            mqttClient.connect(arrayOf<String>(SUB_TOPIC))
        } catch (e: Exception) {
            e.printStackTrace()
        }

        btnCamera.setOnClickListener {

            val i = Intent(this, DetectiveActivity::class.java)
            startActivityForResult(i, NOTIFICATION_REQUEST)

        }
        ledSwitch.setOnCheckedChangeListener { buttonView, isChecked ->
            val value = if(isChecked) "on" else "off"
            mqttClient.publish("iot/control/led", value)
            if (isChecked) {
                PiApi.controlLed("1","on"){
                imgLight.imageTintList = ColorStateList.valueOf(Color.YELLOW)
                }
            } else {
                PiApi.controlLed("1","off"){
                imgLight.imageTintList = ColorStateList.valueOf(Color.DKGRAY)
                }
            }
        }

        seekAngle.setOnSeekBarChangeListener(object: SeekBar.OnSeekBarChangeListener{
            override fun onProgressChanged(seekBar: SeekBar?, progress: Int, fromUser: Boolean) {
                val value = progress.toString()
                mqttClient.publish("iot/control/servo", value)
                PiApi.controlServo("1",progress){}
                txtServo.text = "Servo Motor: $value"
                }

            override fun onStartTrackingTouch(seekBar: SeekBar?) {
            }

            override fun onStopTrackingTouch(seekBar: SeekBar?) {
            }
        })
    }

    fun onReceived(topic: String, message: MqttMessage) {
        // 토픽 수신 처리
        val msg = String(message.payload)
        Log.i(TAG, "$topic : $msg")

        // onReceieved가 어느 Thread에서 실행되는지 확인하는 작업
        txtWeatherInfo.text = "$topic : $msg"
        if (msg == "motion_on"){
        notification(msg)
        }
    }
    fun notification(msg: String){
        val noti = Notification(this)
        noti.createNotificationChannel(CHANNEL_ID, CHANNE_NAME, CHANNEL_DESCRIPTION)
        val pendingIntent = noti.getPendingIntent(
                DetectiveActivity::class.java,      // this.javaClass
                NOTIFICATION_REQUEST)
        noti.notifyBasic(CHANNEL_ID, NOTIFICATION_ID, "Alarm", "움직임 감지 $msg",
                R.drawable.ic_launcher_foreground, pendingIntent)
    }

    fun publish() {
        mqttClient.publish(PUB_TOPIC, "1")
    }
}