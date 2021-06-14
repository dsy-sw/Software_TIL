package com.example.mqttex

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import com.example.mylib.net.Mqtt
import android.util.Log
import kotlinx.android.synthetic.main.activity_main.*
import org.eclipse.paho.client.mqttv3.MqttMessage

const val SUB_TOPIC = "iot/monitor/#"
const val PUB_TOPIC = "iot/led"
const val SERVER_URI = "tcp://192.168.0.10:1883"

// 192....
class MainActivity : AppCompatActivity() {
    val TAG = "MqttActivity"
    lateinit var mqttClient: Mqtt

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        mqttClient = Mqtt(this, SERVER_URI)
        try{
            mqttClient.setCallback(::onReceived)
            mqttClient.connect(arrayOf(SUB_TOPIC))
        } catch (e: Exception){
            e.printStackTrace()
        }
        ledSwitch.setOnCheckedChangeListener{ buttonView, isChecked ->
            val value = if(isChecked) "on" else "off"
            mqttClient.publish("iot/control/led", value)
        }
    }

    fun onReceived(topic: String, message: MqttMessage) {
        // 토픽 수신 처리
        val msg = String(message.payload)
        Log.i(TAG, "$topic : $msg")
        txtWeatherInfo.text = "$topic : $msg"
    }

    fun publish() {
        mqttClient.publish(PUB_TOPIC, "1")
    }
}